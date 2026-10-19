"""Generated from Smithy shape ``com.amazonaws.cloud9#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cloud9.types.environment_arn.EnvironmentArn"
    """<p>The Amazon Resource Name (ARN) of the Cloud9 development environment to get the tags for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    return out
