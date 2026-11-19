"""Generated from Smithy shape ``com.amazonaws.datasync#ListTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.next_token
    import capo_datasync.types.task_list


class ListTasksResponse(TypedDict, closed=True):
    tasks: NotRequired["capo_datasync.types.task_list.TaskList"]
    """<p>A list of all the tasks that are returned.</p>"""
    next_token: NotRequired["capo_datasync.types.next_token.NextToken"]
    """<p>An opaque string that indicates the position at which to begin returning the next list of tasks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTasksResponse) -> dict:
    out: dict = {}
    if "tasks" in value:
        import capo_datasync.types.task_list

        out["Tasks"] = capo_datasync.types.task_list.serialize_aws_json_1_1(
            value["tasks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTasksResponse:
    out: ListTasksResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tasks") is not None:
        import capo_datasync.types.task_list

        out["tasks"] = capo_datasync.types.task_list.deserialize_aws_json_1_1(
            data["Tasks"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTasksResponse) -> dict:
    out: dict = {}
    if "tasks" in value:
        import capo_datasync.types.task_list

        out["Tasks"] = capo_datasync.types.task_list.serialize_cbor(value["tasks"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTasksResponse:
    out: ListTasksResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tasks") is not None:
        import capo_datasync.types.task_list

        out["tasks"] = capo_datasync.types.task_list.deserialize_cbor(data["Tasks"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
