export enum WoodType {
    Wooden = "Wooden",
    Oak = "oak",
    Teak = "teak",
    Mahogany = "mahogany",
    Camphor = "camphor",
    Ironwood = "ironwood",
    Rosewood = "rosewood"
}

export enum MetalType {
    Bronze = "bronze",
    Iron = "iron",
    Steel = "steel",
    Mithril = "mithril",
    Adamant = "adamant",
    Rune = "rune",
    Cupronickel = "cupronickel",
    Lead = "lead",
    Dragon = "dragon"
}

export enum FabricType {
    Linen = "linen",
    Canvas = "canvas",
    Cotton = "cotton"
}

export type MaterialCategory =
| "Nail"
| "Log"
| "Plank"
| "Bar"
| "Metal sheet"
| "Hull part"
| "Keel part"
| "Fabric"
| "Tar"
| "Rope"
| "special";

interface BaseMaterial {
    category : MaterialCategory,
    amount : number
}

interface WoodMaterial extends BaseMaterial {
    category : "Log" | "Plank" | "Hull part";
    woodType : WoodType;
    metalType? : never;
    fabricType? : never;
}

interface MetalMaterial extends BaseMaterial {
    category : "Bar" | "Metal sheet" | "Keel part" | "Nail";
    metalType : MetalType;
    woodType? : never;
    fabricType? : never;
}

interface FabricMaterial extends BaseMaterial {
    category : "Fabric";
    fabricType : FabricType;
    woodType? : never;
    metalType? : never;
}

interface GenericMaterial extends BaseMaterial {
    category : "Tar" | "Rope";
    name : string;
    woodType? : never;
    metalType? : never;
    fabricType? : never;
}

interface SpecialMaterial extends BaseMaterial {
    category : "special";
    name : string;
    woodType? : never;
    metalType? : never;
    fabricType? : never;
}

export type Material = WoodMaterial | MetalMaterial | FabricMaterial | GenericMaterial | SpecialMaterial;


export interface BuildableComponent {
    id : number,
    name : string,
    type : FacilityType,
    boatType : BoatType,
    sailingReq : number,
    constructionReq : number,
    materials : Material[]
}

enum FacilityType {
    CargoHold = "cargo-hold",
    Cannon = "cannon",
    SalvagingHook = "salvaging-hook",
    TrawlingNet = "trawling-net",
    MastAndSail = "mast-and-sail",
    Keel = "keel",
    Hull = "hull",
    Helm = "helm",
    Station = "station",
    Wind = "wind",
    Misc = "misc"
}

enum BoatType {
    Raft = "raft",
    Skiff = "skiff",
    Sloop = "sloop"
}