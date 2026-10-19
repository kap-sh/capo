"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.non_blank_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.non_blank_string.NonBlankString"
    """<p>The name of the field.</p>"""
    message: "capo_bedrock_agent.types.non_blank_string.NonBlankString"
    """<p>A message describing why this field failed validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
