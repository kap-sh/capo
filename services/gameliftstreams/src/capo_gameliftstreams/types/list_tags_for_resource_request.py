"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_gameliftstreams.types.arn.Arn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> that you want to retrieve tags for. To get an Amazon GameLift Streams resource ARN, call a List or Get operation for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
