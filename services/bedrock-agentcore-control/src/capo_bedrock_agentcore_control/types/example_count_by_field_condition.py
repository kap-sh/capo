"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExampleCountByFieldCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.example_field_list


class ExampleCountByFieldCondition(TypedDict, closed=True):
    any_of: NotRequired[
        "capo_bedrock_agentcore_control.types.example_field_list.ExampleFieldList"
    ]
    """<p> The fields to count. An example counts if it has at least one of these fields. Required. </p>"""
    min: NotRequired["int"]
    """<p> The minimum count, inclusive. </p>"""
    max: NotRequired["int"]
    """<p> The maximum count, inclusive. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExampleCountByFieldCondition) -> dict:
    out: dict = {}
    if "any_of" in value:
        import capo_bedrock_agentcore_control.types.example_field_list

        out["anyOf"] = (
            capo_bedrock_agentcore_control.types.example_field_list.serialize_json(
                value["any_of"]
            )
        )
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> ExampleCountByFieldCondition:
    out: ExampleCountByFieldCondition = {}  # type: ignore[typeddict-item]
    if data.get("anyOf") is not None:
        import capo_bedrock_agentcore_control.types.example_field_list

        out["any_of"] = (
            capo_bedrock_agentcore_control.types.example_field_list.deserialize_json(
                data["anyOf"]
            )
        )
    if data.get("min") is not None:
        out["min"] = data["min"]
    if data.get("max") is not None:
        out["max"] = data["max"]
    return out
