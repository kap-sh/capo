"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CutoverTarget``."""

from typing import Literal, TypeAlias, cast

"""<p>The cluster to cut over to in a cloned blue/green upgrade.</p>"""
CutoverTarget: TypeAlias = Literal[
    "ClonedCluster",
    "PrimaryCluster",
]


# --- restJson1 ser/de ---
def serialize_json(value: CutoverTarget) -> str:
    return value


def deserialize_json(data: str) -> CutoverTarget:
    return cast(CutoverTarget, data)
