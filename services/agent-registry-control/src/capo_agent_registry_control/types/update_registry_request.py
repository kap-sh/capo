"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdateRegistryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_identifier
    import capo_agent_registry_control.types.registry_name
    import capo_agent_registry_control.types.updated_approval_configuration
    import capo_agent_registry_control.types.updated_auto_detection_configuration
    import capo_agent_registry_control.types.updated_description
    import capo_agent_registry_control.types.updated_discovery_configuration


class UpdateRegistryRequest(TypedDict, closed=True):
    registry_id: (
        "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry to update (ARN or ID)</p>"""
    name: NotRequired["capo_agent_registry_control.types.registry_name.RegistryName"]
    """<p>The updated name of the registry</p>"""
    description: NotRequired[
        "capo_agent_registry_control.types.updated_description.UpdatedDescription"
    ]
    """<p>The updated description of the registry</p>"""
    discovery_configuration: NotRequired[
        "capo_agent_registry_control.types.updated_discovery_configuration.UpdatedDiscoveryConfiguration"
    ]
    """<p>The updated discovery configuration. Changing the discovery authorization can break existing consumers that rely on the previous authorization type.</p>"""
    approval_configuration: NotRequired[
        "capo_agent_registry_control.types.updated_approval_configuration.UpdatedApprovalConfiguration"
    ]
    """<p>The updated approval configuration. The change applies only to records that move to PENDING_APPROVAL after the update; records already in PENDING_APPROVAL are unaffected.</p>"""
    auto_detection_configuration: NotRequired[
        "capo_agent_registry_control.types.updated_auto_detection_configuration.UpdatedAutoDetectionConfiguration"
    ]
    """<p>The updated auto-detection configuration for the registry, with PATCH semantics. Omit this field to leave the current configuration unchanged. Supply an empty wrapper to unset it. Supply <code>optionalValue</code> to replace it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        import capo_agent_registry_control.types.updated_description

        out["description"] = (
            capo_agent_registry_control.types.updated_description.serialize_json(
                value["description"]
            )
        )
    if "discovery_configuration" in value:
        import capo_agent_registry_control.types.updated_discovery_configuration

        out["discoveryConfiguration"] = (
            capo_agent_registry_control.types.updated_discovery_configuration.serialize_json(
                value["discovery_configuration"]
            )
        )
    if "approval_configuration" in value:
        import capo_agent_registry_control.types.updated_approval_configuration

        out["approvalConfiguration"] = (
            capo_agent_registry_control.types.updated_approval_configuration.serialize_json(
                value["approval_configuration"]
            )
        )
    if "auto_detection_configuration" in value:
        import capo_agent_registry_control.types.updated_auto_detection_configuration

        out["autoDetectionConfiguration"] = (
            capo_agent_registry_control.types.updated_auto_detection_configuration.serialize_json(
                value["auto_detection_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRegistryRequest:
    out: UpdateRegistryRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        import capo_agent_registry_control.types.updated_description

        out["description"] = (
            capo_agent_registry_control.types.updated_description.deserialize_json(
                data["description"]
            )
        )
    if data.get("discoveryConfiguration") is not None:
        import capo_agent_registry_control.types.updated_discovery_configuration

        out["discovery_configuration"] = (
            capo_agent_registry_control.types.updated_discovery_configuration.deserialize_json(
                data["discoveryConfiguration"]
            )
        )
    if data.get("approvalConfiguration") is not None:
        import capo_agent_registry_control.types.updated_approval_configuration

        out["approval_configuration"] = (
            capo_agent_registry_control.types.updated_approval_configuration.deserialize_json(
                data["approvalConfiguration"]
            )
        )
    if data.get("autoDetectionConfiguration") is not None:
        import capo_agent_registry_control.types.updated_auto_detection_configuration

        out["auto_detection_configuration"] = (
            capo_agent_registry_control.types.updated_auto_detection_configuration.deserialize_json(
                data["autoDetectionConfiguration"]
            )
        )
    return out
