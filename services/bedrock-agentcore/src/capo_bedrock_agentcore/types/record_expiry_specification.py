"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecordExpirySpecification``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.record_expiry_action
    import capo_bedrock_agentcore.types.record_expiry_duration_days


class RecordExpirySpecificationRecordExpiryDurationDaysMember(TypedDict, closed=True):
    recordExpiryDurationDays: "capo_bedrock_agentcore.types.record_expiry_duration_days.RecordExpiryDurationDays"


class RecordExpirySpecificationActionMember(TypedDict, closed=True):
    action: "capo_bedrock_agentcore.types.record_expiry_action.RecordExpiryAction"


RecordExpirySpecification: TypeAlias = (
    RecordExpirySpecificationRecordExpiryDurationDaysMember
    | RecordExpirySpecificationActionMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RecordExpirySpecification) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RecordExpirySpecification: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "recordExpiryDurationDays" in value:
        return {"recordExpiryDurationDays": value["recordExpiryDurationDays"]}
    elif "action" in value:
        import capo_bedrock_agentcore.types.record_expiry_action

        return {
            "action": capo_bedrock_agentcore.types.record_expiry_action.serialize_json(
                value["action"]
            )
        }
    else:
        raise SerializationError("RecordExpirySpecification: no variant present")


def deserialize_json(data: dict) -> RecordExpirySpecification:
    if data.get("recordExpiryDurationDays") is not None:
        return {"recordExpiryDurationDays": data["recordExpiryDurationDays"]}
    elif data.get("action") is not None:
        import capo_bedrock_agentcore.types.record_expiry_action

        return {
            "action": capo_bedrock_agentcore.types.record_expiry_action.deserialize_json(
                data["action"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RecordExpirySpecification: no recognized variant key"
        )
