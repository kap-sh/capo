"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeCrossAccountAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string


class DescribeCrossAccountAttachmentRequest(TypedDict, closed=True):
    attachment_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) for the cross-account attachment to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCrossAccountAttachmentRequest) -> dict:
    out: dict = {}
    out["AttachmentArn"] = value["attachment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCrossAccountAttachmentRequest:
    out: DescribeCrossAccountAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AttachmentArn") is not None:
        out["attachment_arn"] = data["AttachmentArn"]
    else:
        out["attachment_arn"] = ""
    return out
