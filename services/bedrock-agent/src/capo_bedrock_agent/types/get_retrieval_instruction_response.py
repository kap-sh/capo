"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetRetrievalInstructionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.retrieval_instruction_arn
    import capo_bedrock_agent.types.retrieval_instruction_content
    import capo_bedrock_agent.types.retrieval_instruction_description
    import capo_bedrock_agent.types.retrieval_instruction_failure_reasons
    import capo_bedrock_agent.types.retrieval_instruction_id
    import capo_bedrock_agent.types.retrieval_instruction_last_transition_status
    import capo_bedrock_agent.types.retrieval_instruction_name
    import capo_bedrock_agent.types.retrieval_instruction_numerical_version
    import capo_bedrock_agent.types.retrieval_instruction_status
    import capo_bedrock_agent.types.retrieval_instruction_version_selector


class GetRetrievalInstructionResponse(TypedDict, closed=True):
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
    """<p>Specifies whether you can use the instruction. You can resolve only an ACTIVE instruction at retrieval time. Monotone: INACTIVE to ACTIVE once, never back. Numbered versions are always ACTIVE.</p>"""
    last_transition_status: "capo_bedrock_agent.types.retrieval_instruction_last_transition_status.RetrievalInstructionLastTransitionStatus"
    """<p>The outcome or in-progress state of the most recent create or update. CREATING or UPDATING means the operation is still running. Independent of status. Always has a value from the create 202 onward. On a numbered version this is always CREATE_SUCCESSFUL: a version is created once, from reviewed content, and is immutable.</p>"""
    instruction: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_content.RetrievalInstructionContent"
    ]
    """<p>The reviewed content this instruction serves — what AgenticRetrieveStream resolves while status is ACTIVE. Absent until the first create review passes. Always present on a numbered version.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When the retrieval instruction was created. On a numbered version, when that version was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When the retrieval instruction was last updated. Equal to createdAt on a numbered version, which is immutable.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
    ]
    """<p>A description of the retrieval instruction. On a numbered version, the description of that version.</p>"""
    customer_encryption_key_arn: NotRequired[
        "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The ARN of the customer managed KMS key protecting this content, when one was supplied at create.</p>"""
    last_transition_status_reasons: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_failure_reasons.RetrievalInstructionFailureReasons"
    ]
    """<p>Why the most recent create or update was rejected. One entry for each rejected field, or a single entry when the review itself failed. Each entry has a machine-readable code and a message, and names the field when it applies to one. The service includes this field only when lastTransitionStatus is CREATE_FAILED or UPDATE_FAILED. Never present on a numbered version.</p>"""
    version: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_version_selector.RetrievalInstructionVersionSelector"
    ]
    """<p>The version this response describes: a version number, or DRAFT.</p>"""
    latest_version: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_numerical_version.RetrievalInstructionNumericalVersion"
    ]
    """<p>The largest version number that currently exists for this retrieval instruction, that is, the newest version you can retrieve. Present only on a DRAFT read, and only when at least one version exists. Because version numbers are never reused, deleting versions can leave gaps: this is the newest existing version, not a count and not the highest number ever created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetrievalInstructionResponse) -> dict:
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
    if "instruction" in value:
        import capo_bedrock_agent.types.retrieval_instruction_content

        out["instruction"] = (
            capo_bedrock_agent.types.retrieval_instruction_content.serialize_json(
                value["instruction"]
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
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    if "last_transition_status_reasons" in value:
        import capo_bedrock_agent.types.retrieval_instruction_failure_reasons

        out["lastTransitionStatusReasons"] = (
            capo_bedrock_agent.types.retrieval_instruction_failure_reasons.serialize_json(
                value["last_transition_status_reasons"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    if "latest_version" in value:
        out["latestVersion"] = value["latest_version"]
    return out


def deserialize_json(data: dict) -> GetRetrievalInstructionResponse:
    out: GetRetrievalInstructionResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("instruction") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_content

        out["instruction"] = (
            capo_bedrock_agent.types.retrieval_instruction_content.deserialize_json(
                data["instruction"]
            )
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
    if data.get("customerEncryptionKeyArn") is not None:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if data.get("lastTransitionStatusReasons") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_failure_reasons

        out["last_transition_status_reasons"] = (
            capo_bedrock_agent.types.retrieval_instruction_failure_reasons.deserialize_json(
                data["lastTransitionStatusReasons"]
            )
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("latestVersion") is not None:
        out["latest_version"] = data["latestVersion"]
    return out


def redact_sensitive(value: GetRetrievalInstructionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
