"""Generated from Smithy shape ``com.amazonaws.qconnect#RegisterKnowledgeBaseReplicaKeyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.knowledge_base_data


class RegisterKnowledgeBaseReplicaKeyResponse(TypedDict, closed=True):
    knowledge_base: "capo_qconnect.types.knowledge_base_data.KnowledgeBaseData"


# --- restJson1 ser/de ---
def serialize_json(value: RegisterKnowledgeBaseReplicaKeyResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.knowledge_base_data

    out["knowledgeBase"] = capo_qconnect.types.knowledge_base_data.serialize_json(
        value["knowledge_base"]
    )
    return out


def deserialize_json(data: dict) -> RegisterKnowledgeBaseReplicaKeyResponse:
    out: RegisterKnowledgeBaseReplicaKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBase") is not None:
        import capo_qconnect.types.knowledge_base_data

        out["knowledge_base"] = (
            capo_qconnect.types.knowledge_base_data.deserialize_json(
                data["knowledgeBase"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterKnowledgeBaseReplicaKeyResponse.knowledge_base required"
        )
    return out


def redact_sensitive(value: RegisterKnowledgeBaseReplicaKeyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base" in value:
        import capo_qconnect.types.knowledge_base_data

        out["knowledge_base"] = (
            capo_qconnect.types.knowledge_base_data.redact_sensitive(
                value["knowledge_base"]
            )
        )
    return out
