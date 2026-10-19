"""Generated from Smithy shape ``com.amazonaws.sqs#ListMessageMoveTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.nullable_integer
    import capo_sqs.types.string


class ListMessageMoveTasksRequest(TypedDict, closed=True):
    source_arn: "capo_sqs.types.string.String"
    """<p>The ARN of the queue whose message movement tasks are to be listed.</p>"""
    max_results: NotRequired["capo_sqs.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of results to include in the response. The default is 1, which provides the most recent message movement task. The upper limit is 10.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMessageMoveTasksRequest) -> dict:
    out: dict = {}
    out["SourceArn"] = value["source_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMessageMoveTasksRequest:
    out: ListMessageMoveTasksRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    else:
        out["source_arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
