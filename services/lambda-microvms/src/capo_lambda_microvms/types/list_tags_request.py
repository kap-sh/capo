"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.taggable_resource


class ListTagsRequest(TypedDict, closed=True):
    resource: "capo_lambda_microvms.types.taggable_resource.TaggableResource"
    """<p>The ARN of the resource to list tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    return out
