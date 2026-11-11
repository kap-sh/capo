"""Generated from Smithy shape ``com.amazonaws.qconnect#RegisterAssistantReplicaKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.assistant_data


class RegisterAssistantReplicaKeyResponse(TypedDict, closed=True):
    assistant: "capo_qconnect.types.assistant_data.AssistantData"


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAssistantReplicaKeyResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.assistant_data

    out["assistant"] = capo_qconnect.types.assistant_data.serialize_json(
        value["assistant"]
    )
    return out


def deserialize_json(data: dict) -> RegisterAssistantReplicaKeyResponse:
    out: RegisterAssistantReplicaKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("assistant") is not None:
        import capo_qconnect.types.assistant_data

        out["assistant"] = capo_qconnect.types.assistant_data.deserialize_json(
            data["assistant"]
        )
    else:
        raise DeserializationError(
            "RegisterAssistantReplicaKeyResponse.assistant required"
        )
    return out
