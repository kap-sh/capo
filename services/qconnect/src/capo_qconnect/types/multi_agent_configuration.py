"""Generated from Smithy shape ``com.amazonaws.qconnect#MultiAgentConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.delegate_agent_configuration
    import capo_qconnect.types.handoff_agent_configuration


class _MultiAgentConfiguration_delegateAgentConfiguration(TypedDict, closed=True):
    delegateAgentConfiguration: (
        "capo_qconnect.types.delegate_agent_configuration.DelegateAgentConfiguration"
    )


class _MultiAgentConfiguration_handoffAgentConfiguration(TypedDict, closed=True):
    handoffAgentConfiguration: (
        "capo_qconnect.types.handoff_agent_configuration.HandoffAgentConfiguration"
    )


MultiAgentConfiguration: TypeAlias = (
    _MultiAgentConfiguration_delegateAgentConfiguration
    | _MultiAgentConfiguration_handoffAgentConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: MultiAgentConfiguration) -> dict:
    if "delegateAgentConfiguration" in value:
        import capo_qconnect.types.delegate_agent_configuration

        return {
            "delegateAgentConfiguration": capo_qconnect.types.delegate_agent_configuration.serialize_json(
                value["delegateAgentConfiguration"]
            )
        }
    elif "handoffAgentConfiguration" in value:
        import capo_qconnect.types.handoff_agent_configuration

        return {
            "handoffAgentConfiguration": capo_qconnect.types.handoff_agent_configuration.serialize_json(
                value["handoffAgentConfiguration"]
            )
        }
    else:
        raise SerializationError("MultiAgentConfiguration: no variant present")


def deserialize_json(data: dict) -> MultiAgentConfiguration:
    if data.get("delegateAgentConfiguration") is not None:
        import capo_qconnect.types.delegate_agent_configuration

        return {
            "delegateAgentConfiguration": capo_qconnect.types.delegate_agent_configuration.deserialize_json(
                data["delegateAgentConfiguration"]
            )
        }
    elif data.get("handoffAgentConfiguration") is not None:
        import capo_qconnect.types.handoff_agent_configuration

        return {
            "handoffAgentConfiguration": capo_qconnect.types.handoff_agent_configuration.deserialize_json(
                data["handoffAgentConfiguration"]
            )
        }
    else:
        raise DeserializationError("MultiAgentConfiguration: no recognized variant key")


def redact_sensitive(value: MultiAgentConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "delegateAgentConfiguration" in value:
        import capo_qconnect.types.delegate_agent_configuration

        out["delegateAgentConfiguration"] = (
            capo_qconnect.types.delegate_agent_configuration.redact_sensitive(
                value["delegateAgentConfiguration"]
            )
        )
    if "handoffAgentConfiguration" in value:
        import capo_qconnect.types.handoff_agent_configuration

        out["handoffAgentConfiguration"] = (
            capo_qconnect.types.handoff_agent_configuration.redact_sensitive(
                value["handoffAgentConfiguration"]
            )
        )
    return out
