"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJobMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.extraction_job_messages
    import capo_bedrock_agentcore.types.extraction_job_status


class ExtractionJobMetadata(TypedDict, closed=True):
    job_id: "str"
    """<p>The unique identifier for the extraction job.</p>"""
    messages: (
        "capo_bedrock_agentcore.types.extraction_job_messages.ExtractionJobMessages"
    )
    """<p>The messages associated with the extraction job.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore.types.extraction_job_status.ExtractionJobStatus"
    ]
    """<p>The current status of the extraction job.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The cause of failure, if the job did not complete successfully.</p>"""
    strategy_id: NotRequired["str"]
    """<p>The identifier of the memory strategy for this extraction job.</p>"""
    session_id: NotRequired["str"]
    """<p>The identifier of the session for this extraction job.</p>"""
    actor_id: NotRequired["str"]
    """<p>The identifier of the actor for this extraction job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJobMetadata) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    import capo_bedrock_agentcore.types.extraction_job_messages

    out["messages"] = (
        capo_bedrock_agentcore.types.extraction_job_messages.serialize_json(
            value["messages"]
        )
    )
    if "status" in value:
        import capo_bedrock_agentcore.types.extraction_job_status

        out["status"] = (
            capo_bedrock_agentcore.types.extraction_job_status.serialize_json(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "strategy_id" in value:
        out["strategyId"] = value["strategy_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    return out


def deserialize_json(data: dict) -> ExtractionJobMetadata:
    out: ExtractionJobMetadata = {}  # type: ignore[typeddict-item]
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    else:
        out["job_id"] = ""
    if data.get("messages") is not None:
        import capo_bedrock_agentcore.types.extraction_job_messages

        out["messages"] = (
            capo_bedrock_agentcore.types.extraction_job_messages.deserialize_json(
                data["messages"]
            )
        )
    else:
        out["messages"] = {"$unknown": {"name": ""}}
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.extraction_job_status

        out["status"] = (
            capo_bedrock_agentcore.types.extraction_job_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("strategyId") is not None:
        out["strategy_id"] = data["strategyId"]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    return out
