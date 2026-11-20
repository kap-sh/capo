"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.space_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_opensearchmemory.types.space_arn.SpaceArn"
    """<p>The Amazon Resource Name (ARN) of the space.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    return out
