"""Generated from Smithy shape ``com.amazonaws.deadline#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.string


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_deadline.types.string.String"
    """The resource ARN to list tags for."""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
