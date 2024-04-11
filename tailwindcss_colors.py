from dataclasses import dataclass
import typing
from enum import Enum


class tailwind_steps(Enum):
    STEP_0 = 0
    STEP_1 = 1
    STEP_2 = 2
    STEP_3 = 3
    STEP_4 = 4
    STEP_5 = 5
    STEP_6 = 6
    STEP_7 = 7
    STEP_8 = 8
    STEP_9 = 9
    STEP_10 = 10

@dataclass
class Palette:
    name : str
    steps : typing.List[str]
    _min_index : int = 0
    _max_index : int = 11


SLATE = Palette(name = "Slate",steps = [
     "#f8fafc",
     "#f1f5f9",
     "#e2e8f0",
     "#cbd5e1",
     "#94a3b8",
     "#64748b",
     "#475569",
     "#334155",
     "#1e293b",
     "#0f172a"
    ])

GRAY = Palette(
        name = "Gray",steps = [
     "#f9fafb",
     "#f3f4f6",
     "#e5e7eb",
     "#d1d5db",
     "#9ca3af",
     "#6b7280",
     "#4b5563",
     "#374151",
     "#1f2937",
     "#111827"
            ]
        )


ZINC = Palette(
        name = "Zinc",steps = [
     "#fafafa",
     "#f4f4f5",
     "#e4e4e7",
     "#d4d4d8",
     "#a1a1aa",
     "#71717a",
     "#52525b",
     "#3f3f46",
     "#27272a",
     "#18181b"
            ]
        )

NEUTRAL= Palette(
        name = "Neutral",steps = [
         "#fafafa",
         "#f5f5f5",
         "#e5e5e5",
         "#d4d4d4",
         "#a3a3a3",
         "#737373",
         "#525252",
         "#404040",
         "#262626",
         "#171717"
            ]
        )


STONE = Palette(
        name = "Stone",steps = [
         "#fafaf9",
         "#f5f5f4",
         "#e7e5e4",
         "#d6d3d1",
         "#a8a29e",
         "#78716c",
         "#57534e",
         "#44403c",
         "#292524",
         "#1c1917"
            ]
        )

RED= Palette(
        name = "Red",steps = [
             "#fef2f2",
             "#fee2e2",
             "#fecaca",
             "#fca5a5",
             "#f87171",
             "#ef4444",
             "#dc2626",
             "#b91c1c",
             "#991b1b",
             "#7f1d1d"
            ]
        )

ORANGE = Palette(
        name = "Orange",steps = [
             "#fff7ed",
             "#ffedd5",
             "#fed7aa",
             "#fdba74",
             "#fb923c",
             "#f97316",
             "#ea580c",
             "#c2410c",
             "#9a3412",
             "#7c2d12"
            ]
        )


AMBER = Palette(
        name = "Amber",steps = [
             "#fffbeb",
             "#fef3c7",
             "#fde68a",
             "#fcd34d",
             "#fbbf24",
             "#f59e0b",
             "#d97706",
             "#b45309",
             "#92400e",
             "#78350f"
            ]
        )



YELLOW = Palette(
        name = "Yellow",steps = [

     "#fefce8",
     "#fef9c3",
     "#fef08a",
     "#fde047",
     "#facc15",
     "#eab308",
     "#ca8a04",
     "#a16207",
     "#854d0e",
     "#713f12"


            ]
        )

LIME = Palette(
        name = "Lime",steps = [

     "#f7fee7",
     "#ecfccb",
     "#d9f99d",
     "#bef264",
     "#a3e635",
     "#84cc16",
     "#65a30d",
     "#4d7c0f",
     "#3f6212",
     "#365314"


            ]
        )


GREEN = Palette(
        name = "Green",steps = [


     "#f0fdf4",
     "#dcfce7",
     "#bbf7d0",
     "#86efac",
     "#4ade80",
     "#22c55e",
     "#16a34a",
     "#15803d",
     "#166534",
     "#14532d"


            ]
        )

EMERALD = Palette(
        name = "Emerald",steps = [
     "#ecfdf5",
     "#d1fae5",
     "#a7f3d0",
     "#6ee7b7",
     "#34d399",
     "#10b981",
     "#059669",
     "#047857",
     "#065f46",
     "#064e3b"

            ]
        )

TEAL = Palette(
        name = "Teal",steps = [

     "#f0fdfa",
     "#ccfbf1",
     "#99f6e4",
     "#5eead4",
     "#2dd4bf",
     "#14b8a6",
     "#0d9488",
     "#0f766e",
     "#115e59",
     "#134e4a"

            ]
        )


CYAN = Palette(
        name = "Cyan",steps = [
     "#ecfeff",
     "#cffafe",
     "#a5f3fc",
     "#67e8f9",
     "#22d3ee",
     "#06b6d4",
     "#0891b2",
     "#0e7490",
     "#155e75",
     "#164e63"

            ]
        )


SKY= Palette(
        name = "Sky",steps = [

     "#f0f9ff",
     "#e0f2fe",
     "#bae6fd",
     "#7dd3fc",
     "#38bdf8",
     "#0ea5e9",
     "#0284c7",
     "#0369a1",
     "#075985",
     "#0c4a6e"

            ]
        )

BLUE = Palette(
        name = "Blue",steps = [

     "#eff6ff",
     "#dbeafe",
     "#bfdbfe",
     "#93c5fd",
     "#60a5fa",
     "#3b82f6",
     "#2563eb",
     "#1d4ed8",
     "#1e40af",
     "#1e3a8a"

            ]
        )


INDIGO = Palette(
        name = "Indigo",steps = [

     "#eef2ff",
     "#e0e7ff",
     "#c7d2fe",
     "#a5b4fc",
     "#818cf8",
     "#6366f1",
     "#4f46e5",
     "#4338ca",
     "#3730a3",
     "#312e81"


            ]
        )



VIOLET = Palette(
        name = "Violet",steps = [


     "#f5f3ff",
     "#ede9fe",
     "#ddd6fe",
     "#c4b5fd",
     "#a78bfa",
     "#8b5cf6",
     "#7c3aed",
     "#6d28d9",
     "#5b21b6",
     "#4c1d95"


            ]
        )



PURPLE = Palette(
        name = "Purple",steps = [

     "#faf5ff",
     "#f3e8ff",
     "#e9d5ff",
     "#d8b4fe",
     "#c084fc",
     "#a855f7",
     "#9333ea",
     "#7e22ce",
     "#6b21a8",
     "#581c87"


            ]
        )


FUCHSIA = Palette(
        name = "Fuchsia",steps = [

     "#fdf4ff",
     "#fae8ff",
     "#f5d0fe",
     "#f0abfc",
     "#e879f9",
     "#d946ef",
     "#c026d3",
     "#a21caf",
     "#86198f",
     "#701a75"

            ]
        )


PINK = Palette(
        name = "Pink",steps = [

     "#fdf2f8",
     "#fce7f3",
     "#fbcfe8",
     "#f9a8d4",
     "#f472b6",
     "#ec4899",
     "#db2777",
     "#be185d",
     "#9d174d",
     "#831843"


            ]
        )


ROSE = Palette(
        name = "Rose",steps = [
     "#fff1f2",
     "#ffe4e6",
     "#fecdd3",
     "#fda4af",
     "#fb7185",
     "#f43f5e",
     "#e11d48",
     "#be123c",
     "#9f1239",
     "#881337"
            ]
        )
