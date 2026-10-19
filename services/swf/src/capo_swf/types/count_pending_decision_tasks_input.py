"""Generated from Smithy shape ``com.amazonaws.swf#CountPendingDecisionTasksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.domain_name
    import capo_swf.types.task_list


class CountPendingDecisionTasksInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain that contains the task list.</p>"""
    task_list: "capo_swf.types.task_list.TaskList"
    """<p>The name of the task list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountPendingDecisionTasksInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import capo_swf.types.task_list

    out["taskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CountPendingDecisionTasksInput:
    out: CountPendingDecisionTasksInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("taskList") is not None:
        import capo_swf.types.task_list

        out["task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError("CountPendingDecisionTasksInput.task_list required")
    return out
