"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateRetrievalInstructionVersionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.retrieval_instruction_arn
    import capo_bedrock_agent.types.retrieval_instruction_description
    import capo_bedrock_agent.types.retrieval_instruction_id
    import capo_bedrock_agent.types.retrieval_instruction_numerical_version


class CreateRetrievalInstructionVersionResponse(TypedDict, closed=True):
    retrieval_instruction_id: (
        "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId"
    )
    """<p>The identifier of the retrieval instruction.</p>"""
    retrieval_instruction_arn: (
        "capo_bedrock_agent.types.retrieval_instruction_arn.RetrievalInstructionArn"
    )
    """<p>The ARN of the retrieval instruction. Versions do not have their own ARN.</p>"""
    version: "capo_bedrock_agent.types.retrieval_instruction_numerical_version.RetrievalInstructionNumericalVersion"
    """<p>The number of the version created. Versions are numbered from 1 and allocated monotonically; a number is never reused, even after the version is deleted.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When this version was created.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
    ]
    """<p>The description of this version, when one was supplied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRetrievalInstructionVersionResponse) -> dict:
    out: dict = {}
    out["retrievalInstructionId"] = value["retrieval_instruction_id"]
    out["retrievalInstructionArn"] = value["retrieval_instruction_arn"]
    out["version"] = value["version"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateRetrievalInstructionVersionResponse:
    out: CreateRetrievalInstructionVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("retrievalInstructionId") is not None:
        out["retrieval_instruction_id"] = data["retrievalInstructionId"]
    else:
        out["retrieval_instruction_id"] = ""
    if data.get("retrievalInstructionArn") is not None:
        out["retrieval_instruction_arn"] = data["retrievalInstructionArn"]
    else:
        out["retrieval_instruction_arn"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(
    value: CreateRetrievalInstructionVersionResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
