"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_configuration_map
    import capo_qconnect.types.arn
    import capo_qconnect.types.assistant_capability_configuration
    import capo_qconnect.types.assistant_integration_configuration
    import capo_qconnect.types.assistant_status
    import capo_qconnect.types.assistant_type
    import capo_qconnect.types.description
    import capo_qconnect.types.name
    import capo_qconnect.types.orchestrator_configuration_list
    import capo_qconnect.types.server_side_encryption_configuration
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid


class AssistantData(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    assistant_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name.</p>"""
    type: "capo_qconnect.types.assistant_type.AssistantType"
    """<p>The type of assistant.</p>"""
    status: "capo_qconnect.types.assistant_status.AssistantStatus"
    """<p>The status of the assistant.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect. To use Amazon Q in Connect with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html">Enable Amazon Q in Connect for your instance</a>.</p>"""
    integration_configuration: NotRequired[
        "capo_qconnect.types.assistant_integration_configuration.AssistantIntegrationConfiguration"
    ]
    """<p>The configuration information for the Amazon Q in Connect assistant integration.</p>"""
    capability_configuration: NotRequired[
        "capo_qconnect.types.assistant_capability_configuration.AssistantCapabilityConfiguration"
    ]
    """<p>The configuration information for the Amazon Q in Connect assistant capability. </p>"""
    ai_agent_configuration: NotRequired[
        "capo_qconnect.types.ai_agent_configuration_map.AIAgentConfigurationMap"
    ]
    """<p>The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that is set on the Amazon Q in Connect Assistant.</p>"""
    orchestrator_configuration_list: NotRequired[
        "capo_qconnect.types.orchestrator_configuration_list.OrchestratorConfigurationList"
    ]
    """<p>The list of orchestrator configurations for the assistant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantData) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["status"] = value["status"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    if "server_side_encryption_configuration" in value:
        import capo_qconnect.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            capo_qconnect.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "integration_configuration" in value:
        import capo_qconnect.types.assistant_integration_configuration

        out["integrationConfiguration"] = (
            capo_qconnect.types.assistant_integration_configuration.serialize_json(
                value["integration_configuration"]
            )
        )
    if "capability_configuration" in value:
        import capo_qconnect.types.assistant_capability_configuration

        out["capabilityConfiguration"] = (
            capo_qconnect.types.assistant_capability_configuration.serialize_json(
                value["capability_configuration"]
            )
        )
    if "ai_agent_configuration" in value:
        import capo_qconnect.types.ai_agent_configuration_map

        out["aiAgentConfiguration"] = (
            capo_qconnect.types.ai_agent_configuration_map.serialize_json(
                value["ai_agent_configuration"]
            )
        )
    if "orchestrator_configuration_list" in value:
        import capo_qconnect.types.orchestrator_configuration_list

        out["orchestratorConfigurationList"] = (
            capo_qconnect.types.orchestrator_configuration_list.serialize_json(
                value["orchestrator_configuration_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssistantData:
    out: AssistantData = {}  # type: ignore[typeddict-item]
    if data.get("assistantId") is not None:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AssistantData.assistant_id required")
    if data.get("assistantArn") is not None:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AssistantData.assistant_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssistantData.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AssistantData.type required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("AssistantData.status required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    if data.get("serverSideEncryptionConfiguration") is not None:
        import capo_qconnect.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_qconnect.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if data.get("integrationConfiguration") is not None:
        import capo_qconnect.types.assistant_integration_configuration

        out["integration_configuration"] = (
            capo_qconnect.types.assistant_integration_configuration.deserialize_json(
                data["integrationConfiguration"]
            )
        )
    if data.get("capabilityConfiguration") is not None:
        import capo_qconnect.types.assistant_capability_configuration

        out["capability_configuration"] = (
            capo_qconnect.types.assistant_capability_configuration.deserialize_json(
                data["capabilityConfiguration"]
            )
        )
    if data.get("aiAgentConfiguration") is not None:
        import capo_qconnect.types.ai_agent_configuration_map

        out["ai_agent_configuration"] = (
            capo_qconnect.types.ai_agent_configuration_map.deserialize_json(
                data["aiAgentConfiguration"]
            )
        )
    if data.get("orchestratorConfigurationList") is not None:
        import capo_qconnect.types.orchestrator_configuration_list

        out["orchestrator_configuration_list"] = (
            capo_qconnect.types.orchestrator_configuration_list.deserialize_json(
                data["orchestratorConfigurationList"]
            )
        )
    return out
