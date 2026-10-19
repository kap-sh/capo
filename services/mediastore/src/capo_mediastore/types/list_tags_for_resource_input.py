"""Generated from Smithy shape ``com.amazonaws.mediastore#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediastore.types.container_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource: "capo_mediastore.types.container_arn.ContainerARN"
    """<p>The Amazon Resource Name (ARN) for the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["Resource"] = value["resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Resource") is not None:
        out["resource"] = data["Resource"]
    else:
        out["resource"] = ""
    return out
