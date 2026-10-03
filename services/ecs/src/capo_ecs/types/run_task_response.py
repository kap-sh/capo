"""Generated from Smithy shape ``com.amazonaws.ecs#RunTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.failures
    import capo_ecs.types.tasks


class RunTaskResponse(TypedDict, closed=True):
    tasks: NotRequired["capo_ecs.types.tasks.Tasks"]
    """<p>A full description of the tasks that were run. The tasks that were successfully placed on your cluster are described here.</p>"""
    failures: NotRequired["capo_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p> <p>For information about how to address failures, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages.html#service-event-messages-list">Service event messages</a> and <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html">API failure reasons</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunTaskResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> RunTaskResponse:
    out: RunTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("tasks") is not None:
        import capo_ecs.types.tasks

        out["tasks"] = capo_ecs.types.tasks.deserialize_aws_json_1_1(data["tasks"])
    if data.get("failures") is not None:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
