"""Generated from Smithy shape ``com.amazonaws.bedrock#VectorSearchBedrockRerankingModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.additional_model_request_fields
    import capo_bedrock.types.bedrock_reranking_model_arn


class VectorSearchBedrockRerankingModelConfiguration(TypedDict, closed=True):
    model_arn: "capo_bedrock.types.bedrock_reranking_model_arn.BedrockRerankingModelArn"
    """<p>The Amazon Resource Name (ARN) of the foundation model to use for reranking. This model processes the query and search results to determine a more relevant ordering.</p>"""
    additional_model_request_fields: NotRequired[
        "capo_bedrock.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p>A list of additional fields to include in the model request during reranking. These fields provide extra context or configuration options specific to the selected foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchBedrockRerankingModelConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "additional_model_request_fields" in value:
        import capo_bedrock.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            capo_bedrock.types.additional_model_request_fields.serialize_json(
                value["additional_model_request_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorSearchBedrockRerankingModelConfiguration:
    out: VectorSearchBedrockRerankingModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("additionalModelRequestFields") is not None:
        import capo_bedrock.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            capo_bedrock.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    return out
