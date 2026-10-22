"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.retrieval_instruction_arn
    import capo_bedrock_agent.types.retrieval_instruction_description
    import capo_bedrock_agent.types.retrieval_instruction_id
    import capo_bedrock_agent.types.retrieval_instruction_last_transition_status
    import capo_bedrock_agent.types.retrieval_instruction_name
    import capo_bedrock_agent.types.retrieval_instruction_status


class RetrievalInstructionSummary(TypedDict, closed=True):
    retrieval_instruction_id: (
        "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId"
    )
    """<p>The identifier of the retrieval instruction.</p>"""
    retrieval_instruction_arn: (
        "capo_bedrock_agent.types.retrieval_instruction_arn.RetrievalInstructionArn"
    )
    """<p>The ARN of the retrieval instruction.</p>"""
    name: "capo_bedrock_agent.types.retrieval_instruction_name.RetrievalInstructionName"
    """<p>The name of the retrieval instruction.</p>"""
    status: "capo_bedrock_agent.types.retrieval_instruction_status.RetrievalInstructionStatus"
    """<p>Whether the instruction can be used. Only ACTIVE is resolvable at retrieval time.</p>"""
    last_transition_status: "capo_bedrock_agent.types.retrieval_instruction_last_transition_status.RetrievalInstructionLastTransitionStatus"
    """<p>The outcome or in-progress state of the most recent create or update of the retrieval instruction.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When you created the retrieval instruction.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When the retrieval instruction was last updated.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
    ]
    """<p>A description of the retrieval instruction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionSummary) -> dict:
    out: dict = {}
    out["retrievalInstructionId"] = value["retrieval_instruction_id"]
    out["retrievalInstructionArn"] = value["retrieval_instruction_arn"]
    out["name"] = value["name"]
    import capo_bedrock_agent.types.retrieval_instruction_status

    out["status"] = (
        capo_bedrock_agent.types.retrieval_instruction_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agent.types.retrieval_instruction_last_transition_status

    out["lastTransitionStatus"] = (
        capo_bedrock_agent.types.retrieval_instruction_last_transition_status.serialize_json(
            value["last_transition_status"]
        )
    )
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> RetrievalInstructionSummary:
    out: RetrievalInstructionSummary = {}  # type: ignore[typeddict-item]
    if data.get("retrievalInstructionId") is not None:
        out["retrieval_instruction_id"] = data["retrievalInstructionId"]
    else:
        out["retrieval_instruction_id"] = ""
    if data.get("retrievalInstructionArn") is not None:
        out["retrieval_instruction_arn"] = data["retrievalInstructionArn"]
    else:
        out["retrieval_instruction_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_status

        out["status"] = (
            capo_bedrock_agent.types.retrieval_instruction_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent.types.retrieval_instruction_status.RetrievalInstructionStatus",
            "",
        )
    if data.get("lastTransitionStatus") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_last_transition_status

        out["last_transition_status"] = (
            capo_bedrock_agent.types.retrieval_instruction_last_transition_status.deserialize_json(
                data["lastTransitionStatus"]
            )
        )
    else:
        import typing

        out["last_transition_status"] = typing.cast(
            "capo_bedrock_agent.types.retrieval_instruction_last_transition_status.RetrievalInstructionLastTransitionStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: RetrievalInstructionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
