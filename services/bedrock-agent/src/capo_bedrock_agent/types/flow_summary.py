"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.flow_arn
    import capo_bedrock_agent.types.flow_description
    import capo_bedrock_agent.types.flow_id
    import capo_bedrock_agent.types.flow_name
    import capo_bedrock_agent.types.flow_status


class FlowSummary(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.flow_name.FlowName"
    """<p>The name of the flow.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.flow_description.FlowDescription"
    ]
    """<p>A description of the flow.</p>"""
    id: "capo_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    arn: "capo_bedrock_agent.types.flow_arn.FlowArn"
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    status: "capo_bedrock_agent.types.flow_status.FlowStatus"
    """<p>The status of the flow. The following statuses are possible:</p> <ul> <li> <p>NotPrepared – The flow has been created or updated, but hasn't been prepared. If you just created the flow, you can't test it. If you updated the flow, the <code>DRAFT</code> version won't contain the latest changes for testing. Send a <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PrepareFlow.html">PrepareFlow</a> request to package the latest changes into the <code>DRAFT</code> version.</p> </li> <li> <p>Preparing – The flow is being prepared so that the <code>DRAFT</code> version contains the latest changes for testing.</p> </li> <li> <p>Prepared – The flow is prepared and the <code>DRAFT</code> version contains the latest changes for testing.</p> </li> <li> <p>Failed – The last API operation that you invoked on the flow failed. Send a <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlow.html">GetFlow</a> request and check the error message in the <code>validations</code> field.</p> </li> </ul>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the flow was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the flow was last updated.</p>"""
    version: "capo_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The latest version of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_bedrock_agent.types.flow_status

    out["status"] = capo_bedrock_agent.types.flow_status.serialize_json(value["status"])
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> FlowSummary:
    out: FlowSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FlowSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FlowSummary.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("FlowSummary.arn required")
    if data.get("status") is not None:
        import capo_bedrock_agent.types.flow_status

        out["status"] = capo_bedrock_agent.types.flow_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("FlowSummary.status required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("FlowSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("FlowSummary.updated_at required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("FlowSummary.version required")
    return out
