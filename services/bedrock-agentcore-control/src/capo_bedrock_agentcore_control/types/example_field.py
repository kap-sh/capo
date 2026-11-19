"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExampleField``."""

from typing import Literal, TypeAlias, cast

"""<p> A field that a dataset example can have. </p>"""
ExampleField: TypeAlias = Literal[
    "TURNS",
    "INPUT",
    "ACTOR_PROFILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExampleField) -> str:
    return value


def deserialize_json(data: str) -> ExampleField:
    return cast(ExampleField, data)
