"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetTagSyncTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.tag_sync_task_arn


class GetTagSyncTaskInput(TypedDict, closed=True):
    task_arn: "capo_resource_groups.types.tag_sync_task_arn.TagSyncTaskArn"
    """<p>The Amazon resource name (ARN) of the tag-sync task. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTagSyncTaskInput) -> dict:
    out: dict = {}
    out["TaskArn"] = value["task_arn"]
    return out


def deserialize_json(data: dict) -> GetTagSyncTaskInput:
    out: GetTagSyncTaskInput = {}  # type: ignore[typeddict-item]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    else:
        out["task_arn"] = ""
    return out
