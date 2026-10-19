"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.flow_alias_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_status
    import capo_bedrock_agent_runtime.types.flow_identifier
    import capo_bedrock_agent_runtime.types.version


class FlowExecutionSummary(TypedDict, closed=True):
    execution_arn: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the flow execution.</p>"""
    flow_alias_identifier: (
        "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the flow alias used for the execution.</p>"""
    flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow.</p>"""
    flow_version: "capo_bedrock_agent_runtime.types.version.Version"
    """<p>The version of the flow used for the execution.</p>"""
    status: "capo_bedrock_agent_runtime.types.flow_execution_status.FlowExecutionStatus"
    """<p>The current status of the flow execution.</p> <p>Flow executions time out after 24 hours.</p>"""
    created_at: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the flow execution was created.</p>"""
    ended_at: NotRequired[
        "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the flow execution ended. This field is only populated when the execution has completed, failed, timed out, or been aborted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionSummary) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    out["flowAliasIdentifier"] = value["flow_alias_identifier"]
    out["flowIdentifier"] = value["flow_identifier"]
    out["flowVersion"] = value["flow_version"]
    import capo_bedrock_agent_runtime.types.flow_execution_status

    out["status"] = (
        capo_bedrock_agent_runtime.types.flow_execution_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "ended_at" in value:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["endedAt"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["ended_at"]
        )
    return out


def deserialize_json(data: dict) -> FlowExecutionSummary:
    out: FlowExecutionSummary = {}  # type: ignore[typeddict-item]
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    else:
        out["execution_arn"] = ""
    if data.get("flowAliasIdentifier") is not None:
        out["flow_alias_identifier"] = data["flowAliasIdentifier"]
    else:
        out["flow_alias_identifier"] = ""
    if data.get("flowIdentifier") is not None:
        out["flow_identifier"] = data["flowIdentifier"]
    else:
        out["flow_identifier"] = ""
    if data.get("flowVersion") is not None:
        out["flow_version"] = data["flowVersion"]
    else:
        out["flow_version"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agent_runtime.types.flow_execution_status

        out["status"] = (
            capo_bedrock_agent_runtime.types.flow_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent_runtime.types.flow_execution_status.FlowExecutionStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endedAt") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["ended_at"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["endedAt"]
            )
        )
    return out
