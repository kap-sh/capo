"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RiskRating``."""

from typing import Literal, TypeAlias, cast

"""<p>The risk rating for automated remediation.</p>"""
RiskRating: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: RiskRating) -> str:
    return value


def deserialize_json(data: str) -> RiskRating:
    return cast(RiskRating, data)
