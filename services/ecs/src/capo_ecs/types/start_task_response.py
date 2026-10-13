"""Generated from Smithy shape ``com.amazonaws.ecs#StartTaskResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.failures
    import capo_ecs.types.tasks


class StartTaskResponse(TypedDict, closed=True):
    tasks: NotRequired["capo_ecs.types.tasks.Tasks"]
    """<p>A full description of the tasks that were started. Each task that was successfully placed on your container instances is described.</p>"""
    failures: NotRequired["capo_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTaskResponse) -> dict:
    out: dict = {}
    if "tasks" in value:
        import capo_ecs.types.tasks

        out["tasks"] = capo_ecs.types.tasks.serialize_aws_json_1_1(value["tasks"])
    if "failures" in value:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTaskResponse:
    out: StartTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("tasks") is not None:
        import capo_ecs.types.tasks

        out["tasks"] = capo_ecs.types.tasks.deserialize_aws_json_1_1(data["tasks"])
    if data.get("failures") is not None:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out


def redact_sensitive(value: StartTaskResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tasks" in value:
        import capo_ecs.types.tasks

        out["tasks"] = capo_ecs.types.tasks.redact_sensitive(value["tasks"])
    return out
