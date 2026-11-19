"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExampleCountByField``."""

from typing_extensions import TypedDict


class ExampleCountByField(TypedDict, closed=True):
    turns: "int"
    """<p> The number of examples that have <code>turns</code>. </p>"""
    input: "int"
    """<p> The number of examples that have <code>input</code>. </p>"""
    actor_profile: "int"
    """<p> The number of examples that have <code>actor_profile</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExampleCountByField) -> dict:
    out: dict = {}
    out["turns"] = value["turns"]
    out["input"] = value["input"]
    out["actorProfile"] = value["actor_profile"]
    return out


def deserialize_json(data: dict) -> ExampleCountByField:
    out: ExampleCountByField = {}  # type: ignore[typeddict-item]
    if data.get("turns") is not None:
        out["turns"] = data["turns"]
    else:
        out["turns"] = 0
    if data.get("input") is not None:
        out["input"] = data["input"]
    else:
        out["input"] = 0
    if data.get("actorProfile") is not None:
        out["actor_profile"] = data["actorProfile"]
    else:
        out["actor_profile"] = 0
    return out
