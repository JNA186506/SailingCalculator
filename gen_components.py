import json
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "src", "components.json")

components = []
cid = 1

# ─── HELPERS ────────────────────────────────────────────────────────────────

def nail(metal, amount):
    return {"category": "Nail", "metalType": metal, "amount": amount}

def plank(wood, amount):
    return {"category": "Plank", "woodType": wood, "amount": amount}

def log_(wood, amount):
    return {"category": "Log", "woodType": wood, "amount": amount}

def bar(metal, amount):
    return {"category": "Bar", "metalType": metal, "amount": amount}

def sheet(metal, amount):
    return {"category": "Metal sheet", "metalType": metal, "amount": amount}

def hull_part(metal, amount):
    return {"category": "Hull part", "metalType": metal, "amount": amount}

def wood_hull_part(wood, amount):
    return {"category": "Plank", "woodType": wood, "amount": amount}

def fabric(ftype, amount):
    return {"category": "Fabric", "fabricType": ftype, "amount": amount}

def tar(amount):
    return {"category": "Tar", "name": "Swamp tar", "amount": amount}

def rope(amount):
    return {"category": "Rope", "name": "Rope", "amount": amount}

def special(name, amount):
    return {"category": "special", "name": name, "amount": amount}

def add(name, ctype, boat, sail, con, materials):
    global cid
    components.append({
        "id": cid,
        "name": name,
        "type": ctype,
        "boatType": boat,
        "sailingReq": sail,
        "constructionReq": con,
        "materials": materials
    })
    cid += 1

# ─── KEELS ──────────────────────────────────────────────────────────────────

skiff_keel_data = [
    ("Bronze", 15, 1,  [hull_part("bronze", 10)]),
    ("Iron",   22, 17, [hull_part("iron", 10)]),
    ("Steel",  39, 32, [hull_part("steel", 10), bar("lead", 5)]),
    ("Mithril",54, 50, [hull_part("mithril", 10), bar("lead", 5)]),
    ("Adamant",66, 62, [hull_part("adamant", 10), bar("lead", 5)]),
    ("Rune",   85, 78, [hull_part("rune", 10), bar("cupronickel", 5)]),
    ("Dragon", 97, 87, [hull_part("dragon", 10), bar("cupronickel", 5)]),
]
for tier, s, c, mats in skiff_keel_data:
    add(f"{tier} skiff keel", "keel", "skiff", s, c, mats)

sloop_keel_data = [
    ("Bronze", 50, 1,  [hull_part("bronze", 16)]),
    ("Iron",   50, 17, [hull_part("iron", 16)]),
    ("Steel",  50, 32, [hull_part("steel", 16), bar("lead", 5)]),
    ("Mithril",54, 50, [hull_part("mithril", 16), bar("lead", 5)]),
    ("Adamant",66, 62, [hull_part("adamant", 16), bar("lead", 5)]),
    ("Rune",   85, 78, [hull_part("rune", 16), bar("cupronickel", 5)]),
    ("Dragon", 97, 87, [hull_part("dragon", 16), bar("cupronickel", 5)]),
]
for tier, s, c, mats in sloop_keel_data:
    add(f"{tier} sloop keel", "keel", "sloop", s, c, mats)

# ─── HULLS ──────────────────────────────────────────────────────────────────

raft_hull_data = [
    ("Wooden",   1,  1,  [log_("wooden", 10),  rope(6), tar(10)]),
    ("Oak",      20, 8,  [log_("oak", 10),      rope(6), tar(10)]),
    ("Teak",     31, 23, [log_("teak", 10),     rope(6), tar(10), bar("lead", 5)]),
    ("Mahogany", 48, 41, [log_("mahogany", 10), rope(6), tar(10), bar("lead", 5)]),
    ("Camphor",  67, 59, [log_("camphor", 10),  rope(6), tar(10), bar("lead", 5)]),
    ("Ironwood", 81, 75, [log_("ironwood", 10), rope(6), tar(10), bar("cupronickel", 5)]),
    ("Rosewood", 93, 84, [log_("rosewood", 10), rope(6), tar(10), bar("cupronickel", 5)]),
]
for tier, s, c, mats in raft_hull_data:
    add(f"{tier} raft hull", "hull", "raft", s, c, mats)

nail_metal = {
    "wooden": "bronze", "oak": "iron", "teak": "steel",
    "mahogany": "mithril", "camphor": "adamant", "ironwood": "rune", "rosewood": "dragon"
}

skiff_hull_data = [
    ("Wooden",   15, 1,  [wood_hull_part("wooden",   10), nail("bronze",  300), tar(20)]),
    ("Oak",      20, 8,  [wood_hull_part("oak",      10), nail("iron",    300), tar(20)]),
    ("Teak",     31, 23, [wood_hull_part("teak",     10), nail("steel",   300), tar(20), bar("lead", 5)]),
    ("Mahogany", 48, 41, [wood_hull_part("mahogany", 10), nail("mithril", 300), tar(20), bar("lead", 5)]),
    ("Camphor",  67, 59, [wood_hull_part("camphor",  10), nail("adamant", 300), tar(20), bar("lead", 5)]),
    ("Ironwood", 81, 75, [wood_hull_part("ironwood", 10), nail("rune",    300), tar(20), bar("cupronickel", 5)]),
    ("Rosewood", 93, 84, [wood_hull_part("rosewood", 10), nail("dragon",  300), tar(20), bar("cupronickel", 5)]),
]
for tier, s, c, mats in skiff_hull_data:
    add(f"{tier} skiff hull", "hull", "skiff", s, c, mats)

sloop_hull_data = [
    ("Wooden",   50, 1,  [wood_hull_part("wooden",   16), nail("bronze",  600), tar(25)]),
    ("Oak",      50, 8,  [wood_hull_part("oak",      16), nail("iron",    600), tar(25)]),
    ("Teak",     50, 23, [wood_hull_part("teak",     16), nail("steel",   600), tar(25), bar("lead", 5)]),
    ("Mahogany", 50, 41, [wood_hull_part("mahogany", 16), nail("mithril", 600), tar(25), bar("lead", 5)]),
    ("Camphor",  67, 59, [wood_hull_part("camphor",  16), nail("adamant", 600), tar(25), bar("lead", 5)]),
    ("Ironwood", 81, 75, [wood_hull_part("ironwood", 16), nail("rune",    600), tar(25), bar("cupronickel", 5)]),
    ("Rosewood", 93, 84, [wood_hull_part("rosewood", 16), nail("dragon",  600), tar(25), bar("cupronickel", 5)]),
]
for tier, s, c, mats in sloop_hull_data:
    add(f"{tier} sloop hull", "hull", "sloop", s, c, mats)

# ─── MASTS AND SAILS ────────────────────────────────────────────────────────

def mast_fabric(wood):
    if wood in ("wooden", "oak"):               return "linen"
    if wood in ("teak", "mahogany", "camphor"): return "canvas"
    return "cotton"

mast_reqs = [
    ("wooden",   1,  1),
    ("oak",      24, 11),
    ("teak",     36, 26),
    ("mahogany", 52, 45),
    ("camphor",  68, 60),
    ("ironwood", 83, 77),
    ("rosewood", 94, 85),
]
sloop_mast_sail = [50, 50, 50, 52, 68, 83, 94]

for i, (wood, s, c) in enumerate(mast_reqs):
    nm = nail_metal[wood]
    fb = mast_fabric(wood)
    tier_name = wood.capitalize()
    add(f"{tier_name} raft mast and sails",  "mast-and-sail", "raft",  s,                  c, [log_(wood, 5),  nail(nm, 20), fabric(fb, 5)])
    add(f"{tier_name} skiff mast and sails", "mast-and-sail", "skiff", s,                  c, [log_(wood, 10), nail(nm, 40), fabric(fb, 5)])
    add(f"{tier_name} sloop mast and sails", "mast-and-sail", "sloop", sloop_mast_sail[i], c, [log_(wood, 15), nail(nm, 60), fabric(fb, 10)])

# ─── HELMS ──────────────────────────────────────────────────────────────────

helm_data = [
    ("Bronze", 1,  1,  "wooden",   "bronze"),
    ("Iron",   17, 14, "oak",      "iron"),
    ("Steel",  38, 30, "teak",     "steel"),
    ("Mithril",55, 47, "mahogany", "mithril"),
    ("Adamant",72, 59, "camphor",  "adamant"),
    ("Rune",   87, 81, "ironwood", "rune"),
    ("Dragon", 96, 86, "rosewood", "dragon"),
]
for tier, s, c, wood, metal in helm_data:
    for boat, px, bx in [("raft", 2, 4), ("skiff", 3, 6), ("sloop", 4, 8)]:
        metal_mat = sheet(metal, bx) if metal == "dragon" else bar(metal, bx)
        add(f"{tier} {boat} helm", "helm", boat, s, c, [plank(wood, px), metal_mat])

# ─── CARGO HOLDS ────────────────────────────────────────────────────────────

cargo_data = [
    ("Basic",    "wooden",   1,  1,  "bronze",  8, 32, None),
    ("Oak",      "oak",      18, 11, "iron",    8, 32, None),
    ("Teak",     "teak",     29, 21, "steel",   8, 32, ("lead", 3)),
    ("Mahogany", "mahogany", 46, 41, "mithril", 8, 32, ("lead", 3)),
    ("Camphor",  "camphor",  60, 53, "adamant", 8, 32, ("lead", 3)),
    ("Ironwood", "ironwood", 80, 77, "rune",    8, 32, ("cupronickel", 3)),
    ("Rosewood", "rosewood", 89, 84, "dragon",  8, 32, ("cupronickel", 3)),
]
for tier, wood, s, c, metal, pcount, ncount, extra_bar in cargo_data:
    mats = [plank(wood, pcount), nail(metal, ncount)]
    if extra_bar:
        mats.append(bar(extra_bar[0], extra_bar[1]))
    add(f"{tier} cargo hold", "cargo-hold", "raft", s, c, mats)

# ─── CANNONS ────────────────────────────────────────────────────────────────

cannon_data = [
    ("Bronze", 28, 21, "wooden",   "bronze",  4, 16, 8),
    ("Iron",   35, 28, "oak",      "iron",    4, 16, 8),
    ("Steel",  47, 39, "teak",     "steel",   4, 16, 8),
    ("Mithril",57, 50, "mahogany", "mithril", 4, 16, 8),
    ("Adamant",69, 61, "camphor",  "adamant", 4, 16, 8),
    ("Rune",   80, 76, "ironwood", "rune",    4, 16, 8),
    ("Dragon", 92, 84, "rosewood", "dragon",  4, 16, 8),
]
for tier, s, c, wood, metal, pcount, ncount, bcount in cannon_data:
    if metal == "dragon":
        mats = [plank(wood, pcount), nail(metal, ncount), sheet(metal, bcount),
                special("Dragon cannon barrel", 1)]
    else:
        mats = [plank(wood, pcount), nail(metal, ncount), bar(metal, bcount)]
    add(f"{tier} cannon", "cannon", "raft", s, c, mats)

# ─── SALVAGING HOOKS ────────────────────────────────────────────────────────

hook_data = [
    ("Bronze", 15, 1,  "wooden",   "bronze",  4, 16, 6, None,               None),
    ("Iron",   21, 9,  "oak",      "iron",    4, 16, 6, None,               None),
    ("Steel",  27, 18, "teak",     "steel",   4, 16, 6, ("lead", 3),        None),
    ("Mithril",44, 30, "mahogany", "mithril", 4, 16, 6, ("lead", 3),        None),
    ("Adamant",59, 52, "camphor",  "adamant", 4, 16, 6, ("lead", 3),        None),
    ("Rune",   74, 66, "ironwood", "rune",    4, 16, 6, ("lead", 4),        ("cupronickel", 4)),
    ("Dragon", 86, 78, "rosewood", "dragon",  4, 16, 6, ("cupronickel", 4), None),
]
for tier, s, c, wood, metal, pcount, ncount, bcount, extra1, extra2 in hook_data:
    if metal == "dragon":
        mats = [plank(wood, pcount), nail(metal, ncount), sheet(metal, bcount)]
        if extra1: mats.append(bar(extra1[0], extra1[1]))
        mats.append(special("Broken dragon hook", 1))
    else:
        mats = [plank(wood, pcount), nail(metal, ncount), bar(metal, bcount)]
        if extra1: mats.append(bar(extra1[0], extra1[1]))
        if extra2: mats.append(bar(extra2[0], extra2[1]))
    mats.append(rope(1))
    add(f"{tier} salvaging hook", "salvaging-hook", "raft", s, c, mats)

# ─── TRAWLING NETS ──────────────────────────────────────────────────────────

add("Rope trawling net",   "trawling-net", "skiff", 56, 45, [
    rope(7), plank("teak", 4), bar("steel", 4), bar("lead", 2)
])
add("Linen trawling net",  "trawling-net", "skiff", 65, 53, [
    special("Linen yarn", 6), rope(1), plank("mahogany", 4), bar("mithril", 4), bar("lead", 2)
])
add("Hemp trawling net",   "trawling-net", "skiff", 76, 65, [
    special("Hemp yarn", 6), rope(1), plank("camphor", 4), bar("adamant", 4),
    bar("cupronickel", 2), special("Ray barb", 4)
])
add("Cotton trawling net", "trawling-net", "skiff", 84, 73, [
    special("Cotton yarn", 6), rope(1), plank("ironwood", 4), bar("rune", 4),
    bar("cupronickel", 2), special("Ray barb", 8)
])

# ─── STATIONS ───────────────────────────────────────────────────────────────

add("Range",               "station", "raft", 16, 6,  [bar("steel", 4), special("Charcoal", 2), special("Tinderbox", 1)])
add("Keg",                 "station", "raft", 33, 25, [plank("oak", 5), nail("iron", 20), special("Barrel stand", 1)])
add("Salvaging station",   "station", "raft", 42, 34, [plank("teak", 4), nail("steel", 16)])
add("Innoculation station","station", "raft", 40, 37, [plank("teak", 8), nail("steel", 32), special("Relicym's balm(4)", 6)])
add("Chum station",        "station", "raft", 56, 45, [plank("mahogany", 10), nail("mithril", 40), bar("steel", 2), special("Fishing bait", 1000), special("Knife", 1)])
add("Advanced chum station","station","raft", 68, 61, [plank("camphor", 10), nail("adamant", 40), bar("steel", 2), special("Fishing bait", 1000), special("Knife", 1)])
add("Chum spreader",       "station", "raft", 82, 74, [plank("ironwood", 10), nail("rune", 40), bar("cupronickel", 5), special("Fishing bait", 10000), special("Narwhal horn knife", 1)])

# ─── WIND ───────────────────────────────────────────────────────────────────

add("Wind catcher",     "wind", "raft", 53, 47, [plank("teak", 4), nail("steel", 16), bar("steel", 8), bar("lead", 4), special("Air rune", 10000), special("Captured wind mote", 1)])
add("Crystal extractor","wind", "raft", 73, 67, [plank("ironwood", 6), bar("cupronickel", 5), special("Magic stone", 2), special("Heart of Ithell", 1)])
add("Gale catcher",     "wind", "raft", 79, 70, [plank("camphor", 4), nail("adamant", 16), bar("adamant", 8), bar("cupronickel", 4), special("Air rune", 25000), special("Captured wind mote", 1), special("Swift albatross feather", 5)])

# ─── MISC ────────────────────────────────────────────────────────────────────

add("Anchor",               "misc", "raft", 37, 29, [bar("steel", 8), bar("lead", 6), rope(1)])
add("Ballistic attractor",  "misc", "raft", 50, 44, [plank("mahogany", 10), bar("lead", 5), bar("steel", 5), special("Water rune", 5000), special("Law rune", 1000)])
add("Teleport focus",       "misc", "raft", 55, 49, [plank("mahogany", 8), nail("mithril", 32), bar("lead", 4), special("Magic stone", 1)])
add("Fathom stone",         "misc", "raft", 70, 62, [plank("camphor", 10), nail("adamant", 40), bar("cupronickel", 2), special("Molten glass", 4)])
add("Greater teleport focus","misc","raft", 75, 69, [plank("ironwood", 8), nail("rune", 32), bar("cupronickel", 4), special("Magic stone", 2), special("Bottled storm", 1)])
add("Fathom pearl",         "misc", "raft", 91, 83, [plank("rosewood", 10), nail("dragon", 40), sheet("dragon", 2), special("Echo pearl", 1)])

# ─── OUTPUT ──────────────────────────────────────────────────────────────────

print(f"Total components: {len(components)}")
with open(OUTPUT, "w") as f:
    json.dump({"components": components}, f, indent=2)
print(f"Written to {OUTPUT}")
