"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string2048


class HubContentStepMetadata(TypedDict, closed=True):
    hub_arn: NotRequired["capo_sagemaker.types.string2048.String2048"]
    """<p>The Amazon Resource Name (ARN) of the hub that the step imported the content into.</p>"""
    hub_content_arn: NotRequired["capo_sagemaker.types.string2048.String2048"]
    """<p>The Amazon Resource Name (ARN) of the hub content that was imported by this step execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentStepMetadata) -> dict:
    out: dict = {}
    if "hub_arn" in value:
        out["HubArn"] = value["hub_arn"]
    if "hub_content_arn" in value:
        out["HubContentArn"] = value["hub_content_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HubContentStepMetadata:
    out: HubContentStepMetadata = {}  # type: ignore[typeddict-item]
    if data.get("HubArn") is not None:
        out["hub_arn"] = data["HubArn"]
    if data.get("HubContentArn") is not None:
        out["hub_content_arn"] = data["HubContentArn"]
    return out
