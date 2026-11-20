"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#EventPayload``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError, SerializationError
from capo_opensearchmemory.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_opensearchmemory.types.blob_payload
    import capo_opensearchmemory.types.conversational_payload
    import capo_opensearchmemory.types.structured_data_payload


class EventPayloadConversationalMember(TypedDict, closed=True):
    conversational: (
        "capo_opensearchmemory.types.conversational_payload.ConversationalPayload"
    )


class EventPayloadStructuredDataMember(TypedDict, closed=True):
    structuredData: (
        "capo_opensearchmemory.types.structured_data_payload.StructuredDataPayload"
    )


class EventPayloadBlobMember(TypedDict, closed=True):
    blob: "capo_opensearchmemory.types.blob_payload.BlobPayload"


EventPayload: TypeAlias = (
    EventPayloadConversationalMember
    | EventPayloadStructuredDataMember
    | EventPayloadBlobMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventPayload) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EventPayload: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "conversational" in value:
        import capo_opensearchmemory.types.conversational_payload

        return {
            "conversational": capo_opensearchmemory.types.conversational_payload.serialize_aws_json_1_0(
                value["conversational"]
            )
        }
    elif "structuredData" in value:
        import capo_opensearchmemory.types.structured_data_payload

        return {
            "structuredData": capo_opensearchmemory.types.structured_data_payload.serialize_aws_json_1_0(
                value["structuredData"]
            )
        }
    elif "blob" in value:
        import capo_opensearchmemory.types.blob_payload

        return {
            "blob": capo_opensearchmemory.types.blob_payload.serialize_aws_json_1_0(
                value["blob"]
            )
        }
    else:
        raise SerializationError("EventPayload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EventPayload:
    if data.get("conversational") is not None:
        import capo_opensearchmemory.types.conversational_payload

        return {
            "conversational": capo_opensearchmemory.types.conversational_payload.deserialize_aws_json_1_0(
                data["conversational"]
            )
        }
    elif data.get("structuredData") is not None:
        import capo_opensearchmemory.types.structured_data_payload

        return {
            "structuredData": capo_opensearchmemory.types.structured_data_payload.deserialize_aws_json_1_0(
                data["structuredData"]
            )
        }
    elif data.get("blob") is not None:
        import capo_opensearchmemory.types.blob_payload

        return {
            "blob": capo_opensearchmemory.types.blob_payload.deserialize_aws_json_1_0(
                data["blob"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EventPayload: no recognized variant key")


def redact_sensitive(value: EventPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "conversational" in value:
        import capo_opensearchmemory.types.conversational_payload

        out["conversational"] = (
            capo_opensearchmemory.types.conversational_payload.redact_sensitive(
                value["conversational"]
            )
        )
    if "structuredData" in value:
        import capo_opensearchmemory.types.structured_data_payload

        out["structuredData"] = (
            capo_opensearchmemory.types.structured_data_payload.redact_sensitive(
                value["structuredData"]
            )
        )
    if "blob" in value:
        import capo_opensearchmemory.types.blob_payload

        out["blob"] = capo_opensearchmemory.types.blob_payload.redact_sensitive(
            value["blob"]
        )
    return out
