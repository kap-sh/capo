"""Generated from Smithy shape ``com.amazonaws.sfn#GetActivityTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.name


class GetActivityTaskInput(TypedDict, closed=True):
    activity_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the activity to retrieve tasks from (assigned when you create the task using <a>CreateActivity</a>.)</p>"""
    worker_name: NotRequired["capo_sfn.types.name.Name"]
    """<p>You can provide an arbitrary name in order to identify the worker that the task is assigned to. This name is used when it is logged in the execution history.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetActivityTaskInput) -> dict:
    out: dict = {}
    out["activityArn"] = value["activity_arn"]
    if "worker_name" in value:
        out["workerName"] = value["worker_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetActivityTaskInput:
    out: GetActivityTaskInput = {}  # type: ignore[typeddict-item]
    if data.get("activityArn") is not None:
        out["activity_arn"] = data["activityArn"]
    else:
        out["activity_arn"] = ""
    if data.get("workerName") is not None:
        out["worker_name"] = data["workerName"]
    return out
