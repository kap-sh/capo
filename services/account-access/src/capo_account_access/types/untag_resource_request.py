"""Generated from Smithy shape ``com.amazonaws.accountaccess#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_account_access.types.application_arn
    import capo_account_access.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the resource to remove tags from.</p>"""
    tag_keys: "capo_account_access.types.tag_keys.TagKeys"
    """<p>Specifies the tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
