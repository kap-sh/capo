"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExampleFieldCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.example_field_list


class ExampleFieldCondition(TypedDict, closed=True):
    any_of: NotRequired[
        "capo_bedrock_agentcore_control.types.example_field_list.ExampleFieldList"
    ]
    """<p> Matches examples that have at least one of these fields. Required. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExampleFieldCondition) -> dict:
    out: dict = {}
    if "any_of" in value:
        import capo_bedrock_agentcore_control.types.example_field_list

        out["anyOf"] = (
            capo_bedrock_agentcore_control.types.example_field_list.serialize_json(
                value["any_of"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExampleFieldCondition:
    out: ExampleFieldCondition = {}  # type: ignore[typeddict-item]
    if data.get("anyOf") is not None:
        import capo_bedrock_agentcore_control.types.example_field_list

        out["any_of"] = (
            capo_bedrock_agentcore_control.types.example_field_list.deserialize_json(
                data["anyOf"]
            )
        )
    return out
