"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessReasoningContentBlockDelta``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.body


class HarnessReasoningContentBlockDeltaTextMember(TypedDict, closed=True):
    text: "str"


class HarnessReasoningContentBlockDeltaRedactedContentMember(TypedDict, closed=True):
    redactedContent: "capo_bedrock_agentcore.types.body.Body"


class HarnessReasoningContentBlockDeltaSignatureMember(TypedDict, closed=True):
    signature: "str"


HarnessReasoningContentBlockDelta: TypeAlias = (
    HarnessReasoningContentBlockDeltaTextMember
    | HarnessReasoningContentBlockDeltaRedactedContentMember
    | HarnessReasoningContentBlockDeltaSignatureMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessReasoningContentBlockDelta) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessReasoningContentBlockDelta: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "redactedContent" in value:
        import capo_bedrock_agentcore.types.body

        return {
            "redactedContent": capo_bedrock_agentcore.types.body.serialize_json(
                value["redactedContent"]
            )
        }
    elif "signature" in value:
        return {"signature": value["signature"]}
    else:
        raise SerializationError(
            "HarnessReasoningContentBlockDelta: no variant present"
        )


def deserialize_json(data: dict) -> HarnessReasoningContentBlockDelta:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("redactedContent") is not None:
        import capo_bedrock_agentcore.types.body

        return {
            "redactedContent": capo_bedrock_agentcore.types.body.deserialize_json(
                data["redactedContent"]
            )
        }
    elif data.get("signature") is not None:
        return {"signature": data["signature"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "HarnessReasoningContentBlockDelta: no recognized variant key"
        )
