"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#UnifiedConversationalSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError, SerializationError
from capo_opensearchmemory.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_opensearchmemory.types.unified_conversational_object


class UnifiedConversationalSourceObjectMember(TypedDict, closed=True):
    object: "capo_opensearchmemory.types.unified_conversational_object.UnifiedConversationalObject"


UnifiedConversationalSource: TypeAlias = (
    UnifiedConversationalSourceObjectMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnifiedConversationalSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UnifiedConversationalSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "object" in value:
        import capo_opensearchmemory.types.unified_conversational_object

        return {
            "object": capo_opensearchmemory.types.unified_conversational_object.serialize_aws_json_1_0(
                value["object"]
            )
        }
    else:
        raise SerializationError("UnifiedConversationalSource: no variant present")


def deserialize_aws_json_1_0(data: dict) -> UnifiedConversationalSource:
    if data.get("object") is not None:
        import capo_opensearchmemory.types.unified_conversational_object

        return {
            "object": capo_opensearchmemory.types.unified_conversational_object.deserialize_aws_json_1_0(
                data["object"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "UnifiedConversationalSource: no recognized variant key"
        )


def redact_sensitive(value: UnifiedConversationalSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "object" in value:
        import capo_opensearchmemory.types.unified_conversational_object

        out["object"] = (
            capo_opensearchmemory.types.unified_conversational_object.redact_sensitive(
                value["object"]
            )
        )
    return out
