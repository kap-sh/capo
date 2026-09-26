"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "capo_network_security_manager.types.arn.Arn"
    """<p>The ARN of the resource to list tags for. The ARN must not include a <code>:DRAFT</code> qualifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
