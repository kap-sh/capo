"""Generated from Smithy shape ``com.amazonaws.datasync#ListTaskExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.max_results
    import capo_datasync.types.next_token
    import capo_datasync.types.task_arn


class ListTaskExecutionsRequest(TypedDict, closed=True):
    task_arn: NotRequired["capo_datasync.types.task_arn.TaskArn"]
    """<p>Specifies the Amazon Resource Name (ARN) of the task that you want execution information about.</p>"""
    max_results: NotRequired["capo_datasync.types.max_results.MaxResults"]
    """<p>Specifies how many results you want in the response.</p>"""
    next_token: NotRequired["capo_datasync.types.next_token.NextToken"]
    """<p>Specifies an opaque string that indicates the position at which to begin the next list of results in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTaskExecutionsRequest) -> dict:
    out: dict = {}
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTaskExecutionsRequest:
    out: ListTaskExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTaskExecutionsRequest) -> dict:
    out: dict = {}
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTaskExecutionsRequest:
    out: ListTaskExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
