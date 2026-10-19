"""Generated from Smithy shape ``com.amazonaws.glue#GetTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glue_resource_arn


class GetTagsRequest(TypedDict, closed=True):
    resource_arn: "capo_glue.types.glue_resource_arn.GlueResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which to retrieve tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagsRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTagsRequest:
    out: GetTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
