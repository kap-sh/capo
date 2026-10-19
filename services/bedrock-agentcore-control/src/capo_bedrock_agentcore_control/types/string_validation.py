"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StringValidation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.allowed_string_values_list


class StringValidation(TypedDict, closed=True):
    allowed_values: "capo_bedrock_agentcore_control.types.allowed_string_values_list.AllowedStringValuesList"
    """<p>Allowed values for this STRING field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringValidation) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.allowed_string_values_list

    out["allowedValues"] = (
        capo_bedrock_agentcore_control.types.allowed_string_values_list.serialize_json(
            value["allowed_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> StringValidation:
    out: StringValidation = {}  # type: ignore[typeddict-item]
    if data.get("allowedValues") is not None:
        import capo_bedrock_agentcore_control.types.allowed_string_values_list

        out["allowed_values"] = (
            capo_bedrock_agentcore_control.types.allowed_string_values_list.deserialize_json(
                data["allowedValues"]
            )
        )
    else:
        out["allowed_values"] = []
    return out
