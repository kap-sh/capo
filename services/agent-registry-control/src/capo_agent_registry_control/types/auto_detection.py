"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AutoDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.auto_detection_configuration
    import capo_agent_registry_control.types.auto_detection_status


class AutoDetection(TypedDict, closed=True):
    configuration: "capo_agent_registry_control.types.auto_detection_configuration.AutoDetectionConfiguration"
    """<p>The auto-detection settings that control how resources are discovered for the registry.</p>"""
    status: (
        "capo_agent_registry_control.types.auto_detection_status.AutoDetectionStatus"
    )
    """<p>The current auto-detection status. <code>ACTIVE</code> indicates that the registry is actively being populated with detected resources. <code>INACTIVE</code> indicates that the preconditions required at the configured scope are not currently met.</p>"""
    status_reason: NotRequired["str"]
    """<p>A human-readable explanation of the current auto-detection status. Typically populated when the status requires additional context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoDetection) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.auto_detection_configuration

    out["configuration"] = (
        capo_agent_registry_control.types.auto_detection_configuration.serialize_json(
            value["configuration"]
        )
    )
    import capo_agent_registry_control.types.auto_detection_status

    out["status"] = (
        capo_agent_registry_control.types.auto_detection_status.serialize_json(
            value["status"]
        )
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> AutoDetection:
    out: AutoDetection = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        import capo_agent_registry_control.types.auto_detection_configuration

        out["configuration"] = (
            capo_agent_registry_control.types.auto_detection_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("AutoDetection.configuration required")
    if data.get("status") is not None:
        import capo_agent_registry_control.types.auto_detection_status

        out["status"] = (
            capo_agent_registry_control.types.auto_detection_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AutoDetection.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
