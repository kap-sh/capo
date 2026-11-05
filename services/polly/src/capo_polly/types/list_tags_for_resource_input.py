"""Generated from Smithy shape ``com.amazonaws.polly#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_polly.types.amazon_resource_name


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "capo_polly.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the only supported resource is an Amazon Polly lexicon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
