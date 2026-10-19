"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.kinesis_analytics_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_kinesis_analytics.types.kinesis_analytics_arn.KinesisAnalyticsARN"
    )
    """<p>The ARN of the application for which to retrieve tags.</p>"""


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
