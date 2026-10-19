"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.kinesis_analytics_arn
    import capo_kinesis_analytics.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_kinesis_analytics.types.kinesis_analytics_arn.KinesisAnalyticsARN"
    )
    """<p>The ARN of the application to assign the tags.</p>"""
    tags: "capo_kinesis_analytics.types.tags.Tags"
    """<p>The key-value tags to assign to the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_kinesis_analytics.types.tags

    out["Tags"] = capo_kinesis_analytics.types.tags.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_kinesis_analytics.types.tags

        out["tags"] = capo_kinesis_analytics.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
