import data from './components.json';
import { BuildableComponent, Material } from './types';

const components = data.components as BuildableComponent[];

const sailingLevel = document.getElementById('sailingLevel') as HTMLInputElement;
const constructionLevel = document.getElementById('constructionLevel') as HTMLInputElement;
const calculateButton = document.getElementById('calculate') as HTMLButtonElement;
const resultsGrid = document.getElementById('results-grid') as HTMLElement;
const totalsGrid = document.getElementById('totals-grid') as HTMLElement;

const specialToggle = document.getElementById('special-toggle') as HTMLInputElement;
const specialFacilities = document.getElementById('special-facilities') as HTMLElement;

specialToggle.addEventListener('change', () => {
    specialFacilities.hidden = !specialToggle.checked;
    if (!specialToggle.checked) {
        specialFacilities.querySelectorAll('input[type="checkbox"]')
            .forEach(el => (el as HTMLInputElement).checked = false);
    }
});

calculateButton.addEventListener('click', () => {
    const selectedSailingLevel = Number(sailingLevel.value);
    const selectedConstructionLevel = Number(constructionLevel.value);
    const selectedBoatType = (document.querySelector('input[name="boat-type"]:checked') as HTMLInputElement)?.value;
    const selectedFacilities = [...document.querySelectorAll('#facilities input:checked')]
        .map(el => (el as HTMLInputElement).value);

    const bestComponents = selectedFacilities
        .map(type => getBestComponent(components, type, selectedBoatType, selectedSailingLevel, selectedConstructionLevel))
        .filter((c): c is BuildableComponent => c !== undefined)
        .map(c => excludeDragon.checked && hasDragonMaterial(c)
            ? getBestComponent(components, c.type, selectedBoatType, selectedSailingLevel, selectedConstructionLevel, true)
            : c
        )
        .filter((c): c is BuildableComponent => c !== undefined);

    const totals = getTotalCost(bestComponents);

    renderTotal(totals);
    renderResults(bestComponents);
});

function formatMaterial(material: Material): string {
    const type = material.metalType ?? material.woodType ?? material.fabricType ?? '';
    return `${type} ${material.category} x${material.amount}`;
}

function renderResults(filtered: BuildableComponent[]) {
    resultsGrid.innerHTML = '';
    resultsGrid.removeAttribute('hidden');

    filtered.forEach(c => {
        const card = document.createElement('div');
        card.className = 'component-card';

        const title = document.createElement('h3');
        title.textContent = `${c.name}`;

        const meta = document.createElement('p');
        meta.className = 'meta';
        meta.textContent = `Sailing ${c.sailingReq} · Construction ${c.constructionReq}`;

        const list = document.createElement('ul');
        c.materials.forEach(m => {
            const item = document.createElement('li');
            if ('name' in m) {
                item.textContent = `${m.name} x${m.amount}`;
            } else {
                item.textContent = formatMaterial(m);
            }
            list.appendChild(item);
        });

        card.append(title, meta, list);
        resultsGrid.appendChild(card);
    });
}

function renderTotal(totals : Map<string, { material : Material, total : number}>) {
    totalsGrid.innerHTML = '';

    const byCategory = new Map<string, Array<{material : Material, total : number}>>();
    for (const value of totals.values()) {
        const category = value.material.category;
        if (!byCategory.has(category)) {
            byCategory.set(category, []);
        }
        byCategory.get(category)!.push(value);
    }

    for (const [category, values] of byCategory) {
        const card = document.createElement('div');
        card.className = 'component-card';

        const title = document.createElement('h3');
        title.textContent = category === 'special' ? 'Special items' : `${category}s`;

        const list = document.createElement('ul');
        values.forEach(v => {
            const item = document.createElement('li');
            if ('name' in v.material) {
                item.textContent = `${v.material.name} x${v.total}`;
            } else {
                const type = v.material.metalType ?? v.material.woodType ?? v.material.fabricType ?? '';
                item.textContent = `${type} x${v.total}`;
            }
            list.appendChild(item);
        });

        card.append(title, list);
        totalsGrid.appendChild(card);
    }
}

const boatSpecificTypes = new Set(['keel', 'hull', 'mast-and-sail', 'helm']);

function getTotalCost(components: BuildableComponent[]): Map<string, { material : Material, total : number}>  {
    const mappedTotals = new Map<string, { material : Material, total : number}>();

    components.flatMap(c => c.materials).forEach(m => {
        const key = m.category === 'special'
            ? `special-${m.name}`
            : `${m.category}-${m.metalType ?? m.woodType ?? m.fabricType ?? ''}`;
        const existing = mappedTotals.get(key);
        if (existing) {
            existing.total += m.amount;
        } else {
            mappedTotals.set(key, { material: m, total: m.amount });
        }
    });

    return mappedTotals;
}

const excludeDragon = document.getElementById('exclude') as HTMLInputElement;

function hasDragonMaterial(component: BuildableComponent): boolean {
    return component.materials.some(m =>
        m.metalType === 'dragon' || m.woodType === 'rosewood'
    );
}

function getBestComponent(
    components: BuildableComponent[],
    facilityType: string,
    boatType: string,
    sailingLevel: number,
    constructionLevel: number,
    excludeDragonMaterials: boolean = false
): BuildableComponent | undefined {
    return components
        .filter(c =>
            c.type === facilityType &&
            c.sailingReq <= sailingLevel &&
            c.constructionReq <= constructionLevel &&
            (!boatSpecificTypes.has(facilityType) || c.boatType === boatType) &&
            (!excludeDragonMaterials || !hasDragonMaterial(c))
        )
        .sort((a, b) =>
            b.sailingReq - a.sailingReq || b.constructionReq - a.constructionReq)[0];

}