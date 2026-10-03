"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageModelCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_card_content
    import capo_sagemaker.types.model_card_status


class ModelPackageModelCard(TypedDict, closed=True):
    model_card_content: NotRequired[
        "capo_sagemaker.types.model_card_content.ModelCardContent"
    ]
    """<p>The content of the model card. The content must follow the schema described in <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema">Model Package Model Card Schema</a>.</p>"""
    model_card_status: NotRequired[
        "capo_sagemaker.types.model_card_status.ModelCardStatus"
    ]
    """<p>The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.</p> <ul> <li> <p> <code>Draft</code>: The model card is a work in progress.</p> </li> <li> <p> <code>PendingReview</code>: The model card is pending review.</p> </li> <li> <p> <code>Approved</code>: The model card is approved.</p> </li> <li> <p> <code>Archived</code>: The model card is archived. No more updates can be made to the model card content. If you try to update the model card content, you will receive the message <code>Model Card is in Archived state</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageModelCard) -> dict:
    out: dict = {}
    if "model_card_content" in value:
        out["ModelCardContent"] = value["model_card_content"]
    if "model_card_status" in value:
        import capo_sagemaker.types.model_card_status

        out["ModelCardStatus"] = (
            capo_sagemaker.types.model_card_status.serialize_aws_json_1_1(
                value["model_card_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageModelCard:
    out: ModelPackageModelCard = {}  # type: ignore[typeddict-item]
    if data.get("ModelCardContent") is not None:
        out["model_card_content"] = data["ModelCardContent"]
    if data.get("ModelCardStatus") is not None:
        import capo_sagemaker.types.model_card_status

        out["model_card_status"] = (
            capo_sagemaker.types.model_card_status.deserialize_aws_json_1_1(
                data["ModelCardStatus"]
            )
        )
    return out
