"""Generated from Smithy shape ``com.amazonaws.interconnect#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict, closed=True):
    arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName"
    """<p>The resource ARN for which to list tags. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
