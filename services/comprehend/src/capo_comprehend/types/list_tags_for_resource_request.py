"""Generated from Smithy shape ``com.amazonaws.comprehend#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_comprehend.types.comprehend_arn.ComprehendArn"
    """<p>The Amazon Resource Name (ARN) of the given Amazon Comprehend resource you are querying. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
