"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#CreateRegistryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.approval_configuration
    import capo_agent_registry_control.types.auto_detection_configuration
    import capo_agent_registry_control.types.client_token
    import capo_agent_registry_control.types.description
    import capo_agent_registry_control.types.discovery_configuration
    import capo_agent_registry_control.types.encryption_configuration
    import capo_agent_registry_control.types.registry_name
    import capo_agent_registry_control.types.tags_map


class CreateRegistryRequest(TypedDict, closed=True):
    name: "capo_agent_registry_control.types.registry_name.RegistryName"
    """<p>The name of the registry</p>"""
    description: NotRequired[
        "capo_agent_registry_control.types.description.Description"
    ]
    """<p>The description of the registry</p>"""
    encryption_configuration: NotRequired[
        "capo_agent_registry_control.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The optional server-side encryption configuration for the registry. When you provide this field, the specified customer-managed Amazon Web Services KMS key encrypts the registry's content. Omit this field to use an Amazon Web Services-owned encryption key. You cannot change the encryption configuration after registry creation.</p>"""
    discovery_configuration: NotRequired[
        "capo_agent_registry_control.types.discovery_configuration.DiscoveryConfiguration"
    ]
    """<p>Discovery configuration for the registry</p>"""
    client_token: NotRequired[
        "capo_agent_registry_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""
    tags: NotRequired["capo_agent_registry_control.types.tags_map.TagsMap"]
    """<p>Tags to associate with the registry</p>"""
    approval_configuration: NotRequired[
        "capo_agent_registry_control.types.approval_configuration.ApprovalConfiguration"
    ]
    """<p>Approval configuration for registry records</p>"""
    auto_detection_configuration: NotRequired[
        "capo_agent_registry_control.types.auto_detection_configuration.AutoDetectionConfiguration"
    ]
    """<p>The optional auto-detection configuration for the registry. When provided, the registry is automatically populated with resources discovered according to the configuration. Omit this field for registries whose records are managed exclusively through the Agent Registry Control API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_configuration" in value:
        import capo_agent_registry_control.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_agent_registry_control.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "discovery_configuration" in value:
        import capo_agent_registry_control.types.discovery_configuration

        out["discoveryConfiguration"] = (
            capo_agent_registry_control.types.discovery_configuration.serialize_json(
                value["discovery_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_agent_registry_control.types.tags_map

        out["tags"] = capo_agent_registry_control.types.tags_map.serialize_json(
            value["tags"]
        )
    if "approval_configuration" in value:
        import capo_agent_registry_control.types.approval_configuration

        out["approvalConfiguration"] = (
            capo_agent_registry_control.types.approval_configuration.serialize_json(
                value["approval_configuration"]
            )
        )
    if "auto_detection_configuration" in value:
        import capo_agent_registry_control.types.auto_detection_configuration

        out["autoDetectionConfiguration"] = (
            capo_agent_registry_control.types.auto_detection_configuration.serialize_json(
                value["auto_detection_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRegistryRequest:
    out: CreateRegistryRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRegistryRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("encryptionConfiguration") is not None:
        import capo_agent_registry_control.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_agent_registry_control.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("discoveryConfiguration") is not None:
        import capo_agent_registry_control.types.discovery_configuration

        out["discovery_configuration"] = (
            capo_agent_registry_control.types.discovery_configuration.deserialize_json(
                data["discoveryConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_agent_registry_control.types.tags_map

        out["tags"] = capo_agent_registry_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    if data.get("approvalConfiguration") is not None:
        import capo_agent_registry_control.types.approval_configuration

        out["approval_configuration"] = (
            capo_agent_registry_control.types.approval_configuration.deserialize_json(
                data["approvalConfiguration"]
            )
        )
    if data.get("autoDetectionConfiguration") is not None:
        import capo_agent_registry_control.types.auto_detection_configuration

        out["auto_detection_configuration"] = (
            capo_agent_registry_control.types.auto_detection_configuration.deserialize_json(
                data["autoDetectionConfiguration"]
            )
        )
    return out
