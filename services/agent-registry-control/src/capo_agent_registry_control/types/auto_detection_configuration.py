"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AutoDetectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.auto_detection_scope


class AutoDetectionConfiguration(TypedDict, closed=True):
    scope: "capo_agent_registry_control.types.auto_detection_scope.AutoDetectionScope"
    """<p>The source from which resources are detected. For example, <code>ORGANIZATION</code> sources resources from all member accounts of an Amazon Web Services organization.</p>"""
    enabled: "bool"
    """<p>Specifies whether auto-detection is requested for the registry. Setting this to <code>true</code> is necessary but not sufficient for auto-detection to become active; the preconditions of the configured scope must also be met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoDetectionConfiguration) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.auto_detection_scope

    out["scope"] = (
        capo_agent_registry_control.types.auto_detection_scope.serialize_json(
            value["scope"]
        )
    )
    out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> AutoDetectionConfiguration:
    out: AutoDetectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scope") is not None:
        import capo_agent_registry_control.types.auto_detection_scope

        out["scope"] = (
            capo_agent_registry_control.types.auto_detection_scope.deserialize_json(
                data["scope"]
            )
        )
    else:
        raise DeserializationError("AutoDetectionConfiguration.scope required")
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("AutoDetectionConfiguration.enabled required")
    return out
