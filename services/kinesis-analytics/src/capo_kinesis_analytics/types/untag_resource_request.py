"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.kinesis_analytics_arn
    import capo_kinesis_analytics.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_kinesis_analytics.types.kinesis_analytics_arn.KinesisAnalyticsARN"
    )
    """<p>The ARN of the Kinesis Analytics application from which to remove the tags.</p>"""
    tag_keys: "capo_kinesis_analytics.types.tag_keys.TagKeys"
    """<p>A list of keys of tags to remove from the specified application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_kinesis_analytics.types.tag_keys

    out["TagKeys"] = capo_kinesis_analytics.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_kinesis_analytics.types.tag_keys

        out["tag_keys"] = (
            capo_kinesis_analytics.types.tag_keys.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
