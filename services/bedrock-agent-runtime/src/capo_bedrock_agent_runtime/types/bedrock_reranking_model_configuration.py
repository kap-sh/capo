"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockRerankingModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.additional_model_request_fields
    import capo_bedrock_agent_runtime.types.bedrock_model_arn


class BedrockRerankingModelConfiguration(TypedDict, closed=True):
    model_arn: "capo_bedrock_agent_runtime.types.bedrock_model_arn.BedrockModelArn"
    """<p>The ARN of the reranker model.</p>"""
    additional_model_request_fields: NotRequired[
        "capo_bedrock_agent_runtime.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p>A JSON object whose keys are request fields for the model and whose values are values for those fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockRerankingModelConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "additional_model_request_fields" in value:
        import capo_bedrock_agent_runtime.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            capo_bedrock_agent_runtime.types.additional_model_request_fields.serialize_json(
                value["additional_model_request_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> BedrockRerankingModelConfiguration:
    out: BedrockRerankingModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("additionalModelRequestFields") is not None:
        import capo_bedrock_agent_runtime.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            capo_bedrock_agent_runtime.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    return out
