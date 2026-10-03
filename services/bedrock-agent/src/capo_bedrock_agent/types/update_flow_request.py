"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_definition
    import capo_bedrock_agent.types.flow_description
    import capo_bedrock_agent.types.flow_execution_role_arn
    import capo_bedrock_agent.types.flow_identifier
    import capo_bedrock_agent.types.flow_name
    import capo_bedrock_agent.types.kms_key_arn


class UpdateFlowRequest(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.flow_name.FlowName"
    """<p>A name for the flow.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.flow_description.FlowDescription"
    ]
    """<p>A description for the flow.</p>"""
    execution_role_arn: (
        "capo_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>"""
    customer_encryption_key_arn: NotRequired[
        "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.</p>"""
    definition: NotRequired["capo_bedrock_agent.types.flow_definition.FlowDefinition"]
    """<p>A definition of the nodes and the connections between the nodes in the flow.</p>"""
    flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    if "definition" in value:
        import capo_bedrock_agent.types.flow_definition

        out["definition"] = capo_bedrock_agent.types.flow_definition.serialize_json(
            value["definition"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowRequest:
    out: UpdateFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateFlowRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("UpdateFlowRequest.execution_role_arn required")
    if data.get("customerEncryptionKeyArn") is not None:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if data.get("definition") is not None:
        import capo_bedrock_agent.types.flow_definition

        out["definition"] = capo_bedrock_agent.types.flow_definition.deserialize_json(
            data["definition"]
        )
    return out
