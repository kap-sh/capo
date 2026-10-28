"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TriggerConditionInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.message_based_trigger_input
    import capo_bedrock_agentcore_control.types.time_based_trigger_input
    import capo_bedrock_agentcore_control.types.token_based_trigger_input


class TriggerConditionInputMessageBasedTriggerMember(TypedDict, closed=True):
    messageBasedTrigger: "capo_bedrock_agentcore_control.types.message_based_trigger_input.MessageBasedTriggerInput"


class TriggerConditionInputTokenBasedTriggerMember(TypedDict, closed=True):
    tokenBasedTrigger: "capo_bedrock_agentcore_control.types.token_based_trigger_input.TokenBasedTriggerInput"


class TriggerConditionInputTimeBasedTriggerMember(TypedDict, closed=True):
    timeBasedTrigger: "capo_bedrock_agentcore_control.types.time_based_trigger_input.TimeBasedTriggerInput"


TriggerConditionInput: TypeAlias = (
    TriggerConditionInputMessageBasedTriggerMember
    | TriggerConditionInputTokenBasedTriggerMember
    | TriggerConditionInputTimeBasedTriggerMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TriggerConditionInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TriggerConditionInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "messageBasedTrigger" in value:
        import capo_bedrock_agentcore_control.types.message_based_trigger_input

        return {
            "messageBasedTrigger": capo_bedrock_agentcore_control.types.message_based_trigger_input.serialize_json(
                value["messageBasedTrigger"]
            )
        }
    elif "tokenBasedTrigger" in value:
        import capo_bedrock_agentcore_control.types.token_based_trigger_input

        return {
            "tokenBasedTrigger": capo_bedrock_agentcore_control.types.token_based_trigger_input.serialize_json(
                value["tokenBasedTrigger"]
            )
        }
    elif "timeBasedTrigger" in value:
        import capo_bedrock_agentcore_control.types.time_based_trigger_input

        return {
            "timeBasedTrigger": capo_bedrock_agentcore_control.types.time_based_trigger_input.serialize_json(
                value["timeBasedTrigger"]
            )
        }
    else:
        raise SerializationError("TriggerConditionInput: no variant present")


def deserialize_json(data: dict) -> TriggerConditionInput:
    if data.get("messageBasedTrigger") is not None:
        import capo_bedrock_agentcore_control.types.message_based_trigger_input

        return {
            "messageBasedTrigger": capo_bedrock_agentcore_control.types.message_based_trigger_input.deserialize_json(
                data["messageBasedTrigger"]
            )
        }
    elif data.get("tokenBasedTrigger") is not None:
        import capo_bedrock_agentcore_control.types.token_based_trigger_input

        return {
            "tokenBasedTrigger": capo_bedrock_agentcore_control.types.token_based_trigger_input.deserialize_json(
                data["tokenBasedTrigger"]
            )
        }
    elif data.get("timeBasedTrigger") is not None:
        import capo_bedrock_agentcore_control.types.time_based_trigger_input

        return {
            "timeBasedTrigger": capo_bedrock_agentcore_control.types.time_based_trigger_input.deserialize_json(
                data["timeBasedTrigger"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TriggerConditionInput: no recognized variant key")
