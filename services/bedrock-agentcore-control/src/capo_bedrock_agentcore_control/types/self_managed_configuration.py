"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SelfManagedConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.invocation_configuration
    import capo_bedrock_agentcore_control.types.trigger_conditions_list


class SelfManagedConfiguration(TypedDict, closed=True):
    trigger_conditions: "capo_bedrock_agentcore_control.types.trigger_conditions_list.TriggerConditionsList"
    """<p>A list of conditions that trigger memory processing.</p>"""
    invocation_configuration: "capo_bedrock_agentcore_control.types.invocation_configuration.InvocationConfiguration"
    """<p>The configuration to use when invoking memory processing.</p>"""
    historical_context_window_size: "int"
    """<p>The number of historical messages to include in processing context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.trigger_conditions_list

    out["triggerConditions"] = (
        capo_bedrock_agentcore_control.types.trigger_conditions_list.serialize_json(
            value["trigger_conditions"]
        )
    )
    import capo_bedrock_agentcore_control.types.invocation_configuration

    out["invocationConfiguration"] = (
        capo_bedrock_agentcore_control.types.invocation_configuration.serialize_json(
            value["invocation_configuration"]
        )
    )
    out["historicalContextWindowSize"] = value["historical_context_window_size"]
    return out


def deserialize_json(data: dict) -> SelfManagedConfiguration:
    out: SelfManagedConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("triggerConditions") is not None:
        import capo_bedrock_agentcore_control.types.trigger_conditions_list

        out["trigger_conditions"] = (
            capo_bedrock_agentcore_control.types.trigger_conditions_list.deserialize_json(
                data["triggerConditions"]
            )
        )
    else:
        out["trigger_conditions"] = []
    if data.get("invocationConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.invocation_configuration

        out["invocation_configuration"] = (
            capo_bedrock_agentcore_control.types.invocation_configuration.deserialize_json(
                data["invocationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SelfManagedConfiguration.invocation_configuration required"
        )
    if data.get("historicalContextWindowSize") is not None:
        out["historical_context_window_size"] = data["historicalContextWindowSize"]
    else:
        out["historical_context_window_size"] = 0
    return out
