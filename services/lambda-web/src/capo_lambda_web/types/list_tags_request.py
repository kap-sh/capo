"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ListTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.resource_arn


class ListTagsRequest(TypedDict, closed=True):
    resource: "capo_lambda_web.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    return out
