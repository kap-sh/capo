"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateRegistryRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.descriptor_type
    import capo_bedrock_agentcore_control.types.descriptors
    import capo_bedrock_agentcore_control.types.registry_identifier
    import capo_bedrock_agentcore_control.types.registry_record_name
    import capo_bedrock_agentcore_control.types.registry_record_version
    import capo_bedrock_agentcore_control.types.synchronization_configuration
    import capo_bedrock_agentcore_control.types.synchronization_type


class CreateRegistryRecordRequest(TypedDict, closed=True):
    registry_id: (
        "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry where the record will be created. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>"""
    name: "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
    """<p>The name of the registry record.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>A description of the registry record.</p>"""
    descriptor_type: (
        "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
    )
    """<p>The descriptor type of the registry record.</p> <ul> <li> <p> <code>MCP</code> - Model Context Protocol descriptor for MCP-compatible servers and tools.</p> </li> <li> <p> <code>A2A</code> - Agent-to-Agent protocol descriptor.</p> </li> <li> <p> <code>CUSTOM</code> - Custom descriptor type for resources such as APIs, Lambda functions, or servers not conforming to a standard protocol.</p> </li> <li> <p> <code>AGENT_SKILLS</code> - Agent skills descriptor for defining agent skill definitions.</p> </li> </ul>"""
    descriptors: NotRequired[
        "capo_bedrock_agentcore_control.types.descriptors.Descriptors"
    ]
    """<p>The descriptor-type-specific configuration containing the resource schema and metadata. The structure of this field depends on the <code>descriptorType</code> you specify.</p>"""
    record_version: NotRequired[
        "capo_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
    ]
    """<p>The version of the registry record. Use this to track different versions of the record's content.</p>"""
    synchronization_type: NotRequired[
        "capo_bedrock_agentcore_control.types.synchronization_type.SynchronizationType"
    ]
    """<p>The type of synchronization to use for keeping the record metadata up to date from an external source. Possible values include <code>FROM_URL</code> and <code>NONE</code>.</p>"""
    synchronization_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.synchronization_configuration.SynchronizationConfiguration"
    ]
    """<p>The configuration for synchronizing registry record metadata from an external source, such as a URL-based MCP server.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryRecordRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.descriptor_type

    out["descriptorType"] = (
        capo_bedrock_agentcore_control.types.descriptor_type.serialize_json(
            value["descriptor_type"]
        )
    )
    if "descriptors" in value:
        import capo_bedrock_agentcore_control.types.descriptors

        out["descriptors"] = (
            capo_bedrock_agentcore_control.types.descriptors.serialize_json(
                value["descriptors"]
            )
        )
    if "record_version" in value:
        out["recordVersion"] = value["record_version"]
    if "synchronization_type" in value:
        import capo_bedrock_agentcore_control.types.synchronization_type

        out["synchronizationType"] = (
            capo_bedrock_agentcore_control.types.synchronization_type.serialize_json(
                value["synchronization_type"]
            )
        )
    if "synchronization_configuration" in value:
        import capo_bedrock_agentcore_control.types.synchronization_configuration

        out["synchronizationConfiguration"] = (
            capo_bedrock_agentcore_control.types.synchronization_configuration.serialize_json(
                value["synchronization_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRegistryRecordRequest:
    out: CreateRegistryRecordRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRegistryRecordRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("descriptorType") is not None:
        import capo_bedrock_agentcore_control.types.descriptor_type

        out["descriptor_type"] = (
            capo_bedrock_agentcore_control.types.descriptor_type.deserialize_json(
                data["descriptorType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRegistryRecordRequest.descriptor_type required"
        )
    if data.get("descriptors") is not None:
        import capo_bedrock_agentcore_control.types.descriptors

        out["descriptors"] = (
            capo_bedrock_agentcore_control.types.descriptors.deserialize_json(
                data["descriptors"]
            )
        )
    if data.get("recordVersion") is not None:
        out["record_version"] = data["recordVersion"]
    if data.get("synchronizationType") is not None:
        import capo_bedrock_agentcore_control.types.synchronization_type

        out["synchronization_type"] = (
            capo_bedrock_agentcore_control.types.synchronization_type.deserialize_json(
                data["synchronizationType"]
            )
        )
    if data.get("synchronizationConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.synchronization_configuration

        out["synchronization_configuration"] = (
            capo_bedrock_agentcore_control.types.synchronization_configuration.deserialize_json(
                data["synchronizationConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
