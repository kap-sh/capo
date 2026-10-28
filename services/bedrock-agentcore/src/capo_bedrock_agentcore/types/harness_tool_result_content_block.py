"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.sensitive_json
    import capo_bedrock_agentcore.types.sensitive_text


class HarnessToolResultContentBlockTextMember(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.sensitive_text.SensitiveText"


class HarnessToolResultContentBlockJsonMember(TypedDict, closed=True):
    json: "capo_bedrock_agentcore.types.sensitive_json.SensitiveJson"


HarnessToolResultContentBlock: TypeAlias = (
    HarnessToolResultContentBlockTextMember
    | HarnessToolResultContentBlockJsonMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultContentBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessToolResultContentBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("HarnessToolResultContentBlock: no variant present")


def deserialize_json(data: dict) -> HarnessToolResultContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("json") is not None:
        return {"json": data["json"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "HarnessToolResultContentBlock: no recognized variant key"
        )


def redact_sensitive(value: HarnessToolResultContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "json" in value:
        out["json"] = "*** Sensitive Data Redacted ***"
    return out
