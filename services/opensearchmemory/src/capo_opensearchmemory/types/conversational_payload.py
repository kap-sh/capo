"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ConversationalPayload``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError, SerializationError
from capo_opensearchmemory.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_opensearchmemory.types.unified_conversational


class ConversationalPayloadUnifiedMember(TypedDict, closed=True):
    unified: "capo_opensearchmemory.types.unified_conversational.UnifiedConversational"


ConversationalPayload: TypeAlias = (
    ConversationalPayloadUnifiedMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConversationalPayload) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConversationalPayload: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "unified" in value:
        import capo_opensearchmemory.types.unified_conversational

        return {
            "unified": capo_opensearchmemory.types.unified_conversational.serialize_aws_json_1_0(
                value["unified"]
            )
        }
    else:
        raise SerializationError("ConversationalPayload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ConversationalPayload:
    if data.get("unified") is not None:
        import capo_opensearchmemory.types.unified_conversational

        return {
            "unified": capo_opensearchmemory.types.unified_conversational.deserialize_aws_json_1_0(
                data["unified"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ConversationalPayload: no recognized variant key")


def redact_sensitive(value: ConversationalPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "unified" in value:
        import capo_opensearchmemory.types.unified_conversational

        out["unified"] = (
            capo_opensearchmemory.types.unified_conversational.redact_sensitive(
                value["unified"]
            )
        )
    return out
