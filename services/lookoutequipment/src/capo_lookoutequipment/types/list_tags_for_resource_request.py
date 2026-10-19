"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.amazon_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource (such as the dataset or model) that is the focus of the <code>ListTagsForResource</code> operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
