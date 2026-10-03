"""Generated from Smithy shape ``com.amazonaws.connect#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the resource. All Connect Customer resources (instances, queues, flows, routing profiles, etc) have an ARN. To locate the ARN for an instance, for example, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">Find your Connect Customer instance ID/ARN</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
