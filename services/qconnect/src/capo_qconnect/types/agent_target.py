"""Generated from Smithy shape ``com.amazonaws.qconnect#AgentTarget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string


class _AgentTarget_aiAgentId(TypedDict, closed=True):
    aiAgentId: "capo_qconnect.types.non_empty_string.NonEmptyString"


class _AgentTarget_applicationId(TypedDict, closed=True):
    applicationId: "capo_qconnect.types.non_empty_string.NonEmptyString"


AgentTarget: TypeAlias = (
    _AgentTarget_aiAgentId | _AgentTarget_applicationId | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AgentTarget) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AgentTarget: cannot serialize unknown variant {value.name!r}"
        )
    elif "aiAgentId" in value:
        return {"aiAgentId": value["aiAgentId"]}
    elif "applicationId" in value:
        return {"applicationId": value["applicationId"]}
    else:
        raise SerializationError("AgentTarget: no variant present")


def deserialize_json(data: dict) -> AgentTarget:
    if data.get("aiAgentId") is not None:
        return {"aiAgentId": data["aiAgentId"]}
    elif data.get("applicationId") is not None:
        return {"applicationId": data["applicationId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AgentTarget: no recognized variant key")
