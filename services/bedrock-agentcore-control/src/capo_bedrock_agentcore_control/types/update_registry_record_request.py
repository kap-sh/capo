"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateRegistryRecordRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.descriptor_type
    import capo_bedrock_agentcore_control.types.record_identifier
    import capo_bedrock_agentcore_control.types.registry_identifier
    import capo_bedrock_agentcore_control.types.registry_record_name
    import capo_bedrock_agentcore_control.types.registry_record_version
    import capo_bedrock_agentcore_control.types.updated_description
    import capo_bedrock_agentcore_control.types.updated_descriptors
    import capo_bedrock_agentcore_control.types.updated_synchronization_configuration
    import capo_bedrock_agentcore_control.types.updated_synchronization_type


class UpdateRegistryRecordRequest(TypedDict, closed=True):
    registry_id: (
        "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>"""
    record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier"
    """<p>The identifier of the registry record to update. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>"""
    name: NotRequired[
        "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
    ]
    """<p>The updated name for the registry record.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
    ]
    """<p>The updated description for the registry record. To clear the description, include the <code>UpdatedDescription</code> wrapper with <code>optionalValue</code> not specified.</p>"""
    descriptor_type: NotRequired[
        "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
    ]
    """<p>The updated descriptor type for the registry record. Changing the descriptor type may require updating the <code>descriptors</code> field to match the new type's schema requirements.</p>"""
    descriptors: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_descriptors.UpdatedDescriptors"
    ]
    """<p>The updated descriptor-type-specific configuration containing the resource schema and metadata. Uses PATCH semantics where individual descriptor fields can be updated independently.</p>"""
    record_version: NotRequired[
        "capo_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
    ]
    """<p>The version of the registry record for optimistic locking. If provided, it must match the current version of the record. The service automatically increments the version after a successful update.</p>"""
    synchronization_type: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_synchronization_type.UpdatedSynchronizationType"
    ]
    """<p>The updated synchronization type for the registry record.</p>"""
    synchronization_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_synchronization_configuration.UpdatedSynchronizationConfiguration"
    ]
    """<p>The updated synchronization configuration for the registry record.</p>"""
    trigger_synchronization: NotRequired["bool"]
    """<p>Whether to trigger synchronization using the stored or provided configuration. When set to <code>true</code>, the service will synchronize the record metadata from the configured external source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryRecordRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.serialize_json(
                value["description"]
            )
        )
    if "descriptor_type" in value:
        import capo_bedrock_agentcore_control.types.descriptor_type

        out["descriptorType"] = (
            capo_bedrock_agentcore_control.types.descriptor_type.serialize_json(
                value["descriptor_type"]
            )
        )
    if "descriptors" in value:
        import capo_bedrock_agentcore_control.types.updated_descriptors

        out["descriptors"] = (
            capo_bedrock_agentcore_control.types.updated_descriptors.serialize_json(
                value["descriptors"]
            )
        )
    if "record_version" in value:
        out["recordVersion"] = value["record_version"]
    if "synchronization_type" in value:
        import capo_bedrock_agentcore_control.types.updated_synchronization_type

        out["synchronizationType"] = (
            capo_bedrock_agentcore_control.types.updated_synchronization_type.serialize_json(
                value["synchronization_type"]
            )
        )
    if "synchronization_configuration" in value:
        import capo_bedrock_agentcore_control.types.updated_synchronization_configuration

        out["synchronizationConfiguration"] = (
            capo_bedrock_agentcore_control.types.updated_synchronization_configuration.serialize_json(
                value["synchronization_configuration"]
            )
        )
    if "trigger_synchronization" in value:
        out["triggerSynchronization"] = value["trigger_synchronization"]
    return out


def deserialize_json(data: dict) -> UpdateRegistryRecordRequest:
    out: UpdateRegistryRecordRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.deserialize_json(
                data["description"]
            )
        )
    if data.get("descriptorType") is not None:
        import capo_bedrock_agentcore_control.types.descriptor_type

        out["descriptor_type"] = (
            capo_bedrock_agentcore_control.types.descriptor_type.deserialize_json(
                data["descriptorType"]
            )
        )
    if data.get("descriptors") is not None:
        import capo_bedrock_agentcore_control.types.updated_descriptors

        out["descriptors"] = (
            capo_bedrock_agentcore_control.types.updated_descriptors.deserialize_json(
                data["descriptors"]
            )
        )
    if data.get("recordVersion") is not None:
        out["record_version"] = data["recordVersion"]
    if data.get("synchronizationType") is not None:
        import capo_bedrock_agentcore_control.types.updated_synchronization_type

        out["synchronization_type"] = (
            capo_bedrock_agentcore_control.types.updated_synchronization_type.deserialize_json(
                data["synchronizationType"]
            )
        )
    if data.get("synchronizationConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.updated_synchronization_configuration

        out["synchronization_configuration"] = (
            capo_bedrock_agentcore_control.types.updated_synchronization_configuration.deserialize_json(
                data["synchronizationConfiguration"]
            )
        )
    if data.get("triggerSynchronization") is not None:
        out["trigger_synchronization"] = data["triggerSynchronization"]
    return out


def redact_sensitive(value: UpdateRegistryRecordRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.redact_sensitive(
                value["description"]
            )
        )
    return out
