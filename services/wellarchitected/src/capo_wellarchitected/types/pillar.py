"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Pillar``."""

from typing import Literal, TypeAlias, cast

"""<note> <p> <code>OPERATIONAL_EXCELLENCE</code> can appear in recommendation results but cannot be specified as a request parameter. The requestable values are <code>COST_OPTIMIZATION</code>, <code>SECURITY</code>, <code>RESILIENCE</code>, and <code>PERFORMANCE</code>.</p> </note> <p>A pillar of the Amazon Web Services Well-Architected Framework, used to scope recommendation generation.</p>"""
Pillar: TypeAlias = Literal[
    "COST_OPTIMIZATION",
    "SECURITY",
    "RESILIENCE",
    "PERFORMANCE",
    "OPERATIONAL_EXCELLENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Pillar) -> str:
    return value


def deserialize_json(data: str) -> Pillar:
    return cast(Pillar, data)
