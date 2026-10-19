"""Generated from Smithy shape ``com.amazonaws.swf#PollForActivityTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.domain_name
    import capo_swf.types.identity
    import capo_swf.types.task_list


class PollForActivityTaskInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain that contains the task lists being polled.</p>"""
    task_list: "capo_swf.types.task_list.TaskList"
    r"""<p>Specifies the task list to poll for activity tasks.</p> <p>The specified string must not start or end with whitespace. It must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    identity: NotRequired["capo_swf.types.identity.Identity"]
    """<p>Identity of the worker making the request, recorded in the <code>ActivityTaskStarted</code> event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PollForActivityTaskInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import capo_swf.types.task_list

    out["taskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    if "identity" in value:
        out["identity"] = value["identity"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PollForActivityTaskInput:
    out: PollForActivityTaskInput = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("PollForActivityTaskInput.task_list required")
    if data.get("identity") is not None:
        out["identity"] = data["identity"]
    return out
