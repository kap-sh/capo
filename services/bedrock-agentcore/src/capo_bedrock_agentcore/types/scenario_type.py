"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ScenarioType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of scenario a dataset generation produces. Each generation produces one type.</p>"""
ScenarioType: TypeAlias = Literal[
    "FIXED",
    "DYNAMIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScenarioType) -> str:
    return value


def deserialize_json(data: str) -> ScenarioType:
    return cast(ScenarioType, data)
