"""Generated from Smithy shape ``com.amazonaws.datasync#ListTaskExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.next_token
    import capo_datasync.types.task_execution_list


class ListTaskExecutionsResponse(TypedDict, closed=True):
    task_executions: NotRequired[
        "capo_datasync.types.task_execution_list.TaskExecutionList"
    ]
    """<p>A list of the task's executions.</p>"""
    next_token: NotRequired["capo_datasync.types.next_token.NextToken"]
    """<p>The opaque string that indicates the position to begin the next list of results in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTaskExecutionsResponse) -> dict:
    out: dict = {}
    if "task_executions" in value:
        import capo_datasync.types.task_execution_list

        out["TaskExecutions"] = (
            capo_datasync.types.task_execution_list.serialize_aws_json_1_1(
                value["task_executions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTaskExecutionsResponse:
    out: ListTaskExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskExecutions") is not None:
        import capo_datasync.types.task_execution_list

        out["task_executions"] = (
            capo_datasync.types.task_execution_list.deserialize_aws_json_1_1(
                data["TaskExecutions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTaskExecutionsResponse) -> dict:
    out: dict = {}
    if "task_executions" in value:
        import capo_datasync.types.task_execution_list

        out["TaskExecutions"] = capo_datasync.types.task_execution_list.serialize_cbor(
            value["task_executions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTaskExecutionsResponse:
    out: ListTaskExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskExecutions") is not None:
        import capo_datasync.types.task_execution_list

        out["task_executions"] = (
            capo_datasync.types.task_execution_list.deserialize_cbor(
                data["TaskExecutions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
