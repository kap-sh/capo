"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UntagLogGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.tag_list


class UntagLogGroupRequest(TypedDict, closed=True):
    log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    tags: "capo_cloudwatch_logs.types.tag_list.TagList"
    """<p>The tag keys. The corresponding tags are removed from the log group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagLogGroupRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    import capo_cloudwatch_logs.types.tag_list

    out["tags"] = capo_cloudwatch_logs.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagLogGroupRequest:
    out: UntagLogGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tag_list

        out["tags"] = capo_cloudwatch_logs.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
