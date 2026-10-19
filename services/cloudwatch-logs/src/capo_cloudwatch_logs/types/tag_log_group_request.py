"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TagLogGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.tags


class TagLogGroupRequest(TypedDict, closed=True):
    log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    tags: "capo_cloudwatch_logs.types.tags.Tags"
    """<p>The key-value pairs to use for the tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagLogGroupRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    import capo_cloudwatch_logs.types.tags

    out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagLogGroupRequest:
    out: TagLogGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
