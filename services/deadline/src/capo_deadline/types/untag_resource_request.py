"""Generated from Smithy shape ``com.amazonaws.deadline#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.string
    import capo_deadline.types.string_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_deadline.types.string.String"
    """The ARN of the resource to remove the tag from."""
    tag_keys: "capo_deadline.types.string_list.StringList"
    """They keys of the tag."""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
