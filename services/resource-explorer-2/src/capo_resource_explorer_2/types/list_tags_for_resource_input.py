"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListTagsForResourceInput``."""

from typing_extensions import TypedDict


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view or index that you want to attach tags to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
