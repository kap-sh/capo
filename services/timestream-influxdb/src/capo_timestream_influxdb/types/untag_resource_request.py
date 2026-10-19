"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the tagged resource.</p>"""
    tag_keys: "capo_timestream_influxdb.types.tag_keys.TagKeys"
    """<p>The keys used to identify the tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_timestream_influxdb.types.tag_keys

    out["tagKeys"] = capo_timestream_influxdb.types.tag_keys.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_timestream_influxdb.types.tag_keys

        out["tag_keys"] = (
            capo_timestream_influxdb.types.tag_keys.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
