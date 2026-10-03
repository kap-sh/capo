"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.generic_v2_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_greengrassv2.types.generic_v2_arn.GenericV2ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
