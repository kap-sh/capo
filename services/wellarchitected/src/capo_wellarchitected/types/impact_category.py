"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImpactCategory``."""

from typing import Literal, TypeAlias, cast

"""<p>The severity of a recommendation's impact.</p>"""
ImpactCategory: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImpactCategory) -> str:
    return value


def deserialize_json(data: str) -> ImpactCategory:
    return cast(ImpactCategory, data)
