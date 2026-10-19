"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RecordExpirySpecification``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.record_expiry_action
    import capo_bedrock_agentcore_control.types.record_expiry_duration_days


class _RecordExpirySpecification_recordExpiryDurationDays(TypedDict, closed=True):
    recordExpiryDurationDays: "capo_bedrock_agentcore_control.types.record_expiry_duration_days.RecordExpiryDurationDays"


class _RecordExpirySpecification_action(TypedDict, closed=True):
    action: (
        "capo_bedrock_agentcore_control.types.record_expiry_action.RecordExpiryAction"
    )


RecordExpirySpecification: TypeAlias = (
    _RecordExpirySpecification_recordExpiryDurationDays
    | _RecordExpirySpecification_action
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RecordExpirySpecification) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RecordExpirySpecification: cannot serialize unknown variant {value.name!r}"
        )
    elif "recordExpiryDurationDays" in value:
        return {"recordExpiryDurationDays": value["recordExpiryDurationDays"]}
    elif "action" in value:
        import capo_bedrock_agentcore_control.types.record_expiry_action

        return {
            "action": capo_bedrock_agentcore_control.types.record_expiry_action.serialize_json(
                value["action"]
            )
        }
    else:
        raise SerializationError("RecordExpirySpecification: no variant present")


def deserialize_json(data: dict) -> RecordExpirySpecification:
    if data.get("recordExpiryDurationDays") is not None:
        return {"recordExpiryDurationDays": data["recordExpiryDurationDays"]}
    elif data.get("action") is not None:
        import capo_bedrock_agentcore_control.types.record_expiry_action

        return {
            "action": capo_bedrock_agentcore_control.types.record_expiry_action.deserialize_json(
                data["action"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "RecordExpirySpecification: no recognized variant key"
        )
