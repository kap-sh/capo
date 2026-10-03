"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateModelCardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_card_content
    import capo_sagemaker.types.model_card_name_or_arn
    import capo_sagemaker.types.model_card_status


class UpdateModelCardRequest(TypedDict, closed=True):
    model_card_name: NotRequired[
        "capo_sagemaker.types.model_card_name_or_arn.ModelCardNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the model card to update.</p>"""
    content: NotRequired["capo_sagemaker.types.model_card_content.ModelCardContent"]
    """<p>The updated model card content. Content must be in <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema">model card JSON schema</a> and provided as a string.</p> <p>When updating model card content, be sure to include the full content and not just updated content.</p>"""
    model_card_status: NotRequired[
        "capo_sagemaker.types.model_card_status.ModelCardStatus"
    ]
    """<p>The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.</p> <ul> <li> <p> <code>Draft</code>: The model card is a work in progress.</p> </li> <li> <p> <code>PendingReview</code>: The model card is pending review.</p> </li> <li> <p> <code>Approved</code>: The model card is approved.</p> </li> <li> <p> <code>Archived</code>: The model card is archived. No more updates should be made to the model card, but it can still be exported.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateModelCardRequest) -> dict:
    out: dict = {}
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "content" in value:
        out["Content"] = value["content"]
    if "model_card_status" in value:
        import capo_sagemaker.types.model_card_status

        out["ModelCardStatus"] = (
            capo_sagemaker.types.model_card_status.serialize_aws_json_1_1(
                value["model_card_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateModelCardRequest:
    out: UpdateModelCardRequest = {}  # type: ignore[typeddict-item]
    if data.get("ModelCardName") is not None:
        out["model_card_name"] = data["ModelCardName"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("ModelCardStatus") is not None:
        import capo_sagemaker.types.model_card_status

        out["model_card_status"] = (
            capo_sagemaker.types.model_card_status.deserialize_aws_json_1_1(
                data["ModelCardStatus"]
            )
        )
    return out
