"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistrySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.auto_detection
    import capo_agent_registry_control.types.date_timestamp
    import capo_agent_registry_control.types.description
    import capo_agent_registry_control.types.discovery_configuration
    import capo_agent_registry_control.types.registry_arn
    import capo_agent_registry_control.types.registry_id
    import capo_agent_registry_control.types.registry_name
    import capo_agent_registry_control.types.registry_status


class RegistrySummary(TypedDict, closed=True):
    name: "capo_agent_registry_control.types.registry_name.RegistryName"
    """<p>Registry name</p>"""
    description: NotRequired[
        "capo_agent_registry_control.types.description.Description"
    ]
    """<p>Registry description</p>"""
    registry_id: "capo_agent_registry_control.types.registry_id.RegistryId"
    """<p>Unique registry identifier</p>"""
    registry_arn: "capo_agent_registry_control.types.registry_arn.RegistryArn"
    """<p>Registry Amazon Resource Name</p>"""
    discovery_configuration: NotRequired[
        "capo_agent_registry_control.types.discovery_configuration.DiscoveryConfiguration"
    ]
    """<p>Discovery configuration for the registry</p>"""
    status: "capo_agent_registry_control.types.registry_status.RegistryStatus"
    """<p>Current status of the registry</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status. Typically populated when the status indicates a failure state.</p>"""
    auto_detection: NotRequired[
        "capo_agent_registry_control.types.auto_detection.AutoDetection"
    ]
    """<p>The registry's auto-detection properties, including the requested configuration and the current detection status. Present only when auto-detection was configured for the registry.</p>"""
    created_at: "capo_agent_registry_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry was created</p>"""
    updated_at: "capo_agent_registry_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry was last updated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistrySummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["registryId"] = value["registry_id"]
    out["registryArn"] = value["registry_arn"]
    if "discovery_configuration" in value:
        import capo_agent_registry_control.types.discovery_configuration

        out["discoveryConfiguration"] = (
            capo_agent_registry_control.types.discovery_configuration.serialize_json(
                value["discovery_configuration"]
            )
        )
    import capo_agent_registry_control.types.registry_status

    out["status"] = capo_agent_registry_control.types.registry_status.serialize_json(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "auto_detection" in value:
        import capo_agent_registry_control.types.auto_detection

        out["autoDetection"] = (
            capo_agent_registry_control.types.auto_detection.serialize_json(
                value["auto_detection"]
            )
        )
    import capo_agent_registry_control.types.date_timestamp

    out["createdAt"] = capo_agent_registry_control.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_agent_registry_control.types.date_timestamp

    out["updatedAt"] = capo_agent_registry_control.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> RegistrySummary:
    out: RegistrySummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegistrySummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    else:
        raise DeserializationError("RegistrySummary.registry_id required")
    if data.get("registryArn") is not None:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError("RegistrySummary.registry_arn required")
    if data.get("discoveryConfiguration") is not None:
        import capo_agent_registry_control.types.discovery_configuration

        out["discovery_configuration"] = (
            capo_agent_registry_control.types.discovery_configuration.deserialize_json(
                data["discoveryConfiguration"]
            )
        )
    if data.get("status") is not None:
        import capo_agent_registry_control.types.registry_status

        out["status"] = (
            capo_agent_registry_control.types.registry_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("RegistrySummary.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("autoDetection") is not None:
        import capo_agent_registry_control.types.auto_detection

        out["auto_detection"] = (
            capo_agent_registry_control.types.auto_detection.deserialize_json(
                data["autoDetection"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_agent_registry_control.types.date_timestamp

        out["created_at"] = (
            capo_agent_registry_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("RegistrySummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_agent_registry_control.types.date_timestamp

        out["updated_at"] = (
            capo_agent_registry_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("RegistrySummary.updated_at required")
    return out
