"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionFailureReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.retrieval_instruction_failure_reason_code
    import capo_bedrock_agent.types.retrieval_instruction_field_name


class RetrievalInstructionFailureReason(TypedDict, closed=True):
    field_name: NotRequired[
        "capo_bedrock_agent.types.retrieval_instruction_field_name.RetrievalInstructionFieldName"
    ]
    """<p>The instruction field this entry is about. Present on review rejections of a specific field; absent when the failure applies to the whole review, because a client-side execution failure or a service fault has no single field.</p>"""
    code: "capo_bedrock_agent.types.retrieval_instruction_failure_reason_code.RetrievalInstructionFailureReasonCode"
    """<p>Stable, machine-readable classification by fault attribution. Valid values:</p> <ul> <li> <p>CONTENT_REJECTED – The review rejected the named field's content; revise the text and resubmit.</p> </li> <li> <p>CLIENT_ERROR – The review could not run for a customer-side reason, for example the customer managed AWS KMS key could not be used; fix the configuration and resubmit.</p> </li> <li> <p>INTERNAL_ERROR – The review could not complete due to a service fault; retry the create or update.</p> </li> </ul> <p>New values may be added over time; your client should tolerate values it does not recognize and treat them as a failure.</p>"""
    message: "str"
    """<p>Human-readable explanation of the specific cause. Never contains the customer's own text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionFailureReason) -> dict:
    out: dict = {}
    if "field_name" in value:
        import capo_bedrock_agent.types.retrieval_instruction_field_name

        out["fieldName"] = (
            capo_bedrock_agent.types.retrieval_instruction_field_name.serialize_json(
                value["field_name"]
            )
        )
    import capo_bedrock_agent.types.retrieval_instruction_failure_reason_code

    out["code"] = (
        capo_bedrock_agent.types.retrieval_instruction_failure_reason_code.serialize_json(
            value["code"]
        )
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RetrievalInstructionFailureReason:
    out: RetrievalInstructionFailureReason = {}  # type: ignore[typeddict-item]
    if data.get("fieldName") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_field_name

        out["field_name"] = (
            capo_bedrock_agent.types.retrieval_instruction_field_name.deserialize_json(
                data["fieldName"]
            )
        )
    if data.get("code") is not None:
        import capo_bedrock_agent.types.retrieval_instruction_failure_reason_code

        out["code"] = (
            capo_bedrock_agent.types.retrieval_instruction_failure_reason_code.deserialize_json(
                data["code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_bedrock_agent.types.retrieval_instruction_failure_reason_code.RetrievalInstructionFailureReasonCode",
            "",
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
