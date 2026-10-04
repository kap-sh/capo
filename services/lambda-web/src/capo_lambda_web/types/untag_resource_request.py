"""Generated from Smithy shape ``com.amazonaws.lambdaweb#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.resource_arn
    import capo_lambda_web.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource: "capo_lambda_web.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web function.</p>"""
    tag_keys: "capo_lambda_web.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the web function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
