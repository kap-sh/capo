"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateFlowVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.flow_arn
    import capo_bedrock_agent.types.flow_definition
    import capo_bedrock_agent.types.flow_description
    import capo_bedrock_agent.types.flow_execution_role_arn
    import capo_bedrock_agent.types.flow_id
    import capo_bedrock_agent.types.flow_name
    import capo_bedrock_agent.types.flow_status
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.numerical_version


class CreateFlowVersionResponse(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.flow_name.FlowName"
    """<p>The name of the version.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.flow_description.FlowDescription"
    ]
    """<p>The description of the version.</p>"""
    execution_role_arn: (
        "capo_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>"""
    customer_encryption_key_arn: NotRequired[
        "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The KMS key that the flow is encrypted with.</p>"""
    id: "capo_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    arn: "capo_bedrock_agent.types.flow_arn.FlowArn"
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    status: "capo_bedrock_agent.types.flow_status.FlowStatus"
    """<p>The status of the flow.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the flow was created.</p>"""
    version: "capo_bedrock_agent.types.numerical_version.NumericalVersion"
    """<p>The version of the flow that was created. Versions are numbered incrementally, starting from 1.</p>"""
    definition: NotRequired["capo_bedrock_agent.types.flow_definition.FlowDefinition"]
    """<p>A definition of the nodes and connections in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowVersionResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_bedrock_agent.types.flow_status

    out["status"] = capo_bedrock_agent.types.flow_status.serialize_json(value["status"])
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    out["version"] = value["version"]
    if "definition" in value:
        import capo_bedrock_agent.types.flow_definition

        out["definition"] = capo_bedrock_agent.types.flow_definition.serialize_json(
            value["definition"]
        )
    return out


def deserialize_json(data: dict) -> CreateFlowVersionResponse:
    out: CreateFlowVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFlowVersionResponse.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError(
            "CreateFlowVersionResponse.execution_role_arn required"
        )
    if data.get("customerEncryptionKeyArn") is not None:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateFlowVersionResponse.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateFlowVersionResponse.arn required")
    if data.get("status") is not None:
        import capo_bedrock_agent.types.flow_status

        out["status"] = capo_bedrock_agent.types.flow_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateFlowVersionResponse.status required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateFlowVersionResponse.created_at required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreateFlowVersionResponse.version required")
    if data.get("definition") is not None:
        import capo_bedrock_agent.types.flow_definition

        out["definition"] = capo_bedrock_agent.types.flow_definition.deserialize_json(
            data["definition"]
        )
    return out
