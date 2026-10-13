"""Generated from Smithy shape ``com.amazonaws.ecs#StopTaskResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.task


class StopTaskResponse(TypedDict, closed=True):
    task: NotRequired["capo_ecs.types.task.Task"]
    """<p>The task that was stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTaskResponse) -> dict:
    out: dict = {}
    if "task" in value:
        import capo_ecs.types.task

        out["task"] = capo_ecs.types.task.serialize_aws_json_1_1(value["task"])
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTaskResponse:
    out: StopTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("task") is not None:
        import capo_ecs.types.task

        out["task"] = capo_ecs.types.task.deserialize_aws_json_1_1(data["task"])
    return out


def redact_sensitive(value: StopTaskResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "task" in value:
        import capo_ecs.types.task

        out["task"] = capo_ecs.types.task.redact_sensitive(value["task"])
    return out
