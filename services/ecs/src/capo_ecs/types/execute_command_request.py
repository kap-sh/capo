"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.string


class ExecuteCommandRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) or short name of the cluster the task is running in. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the container to execute the command on. A container name only needs to be specified for tasks containing multiple containers.</p>"""
    command: "capo_ecs.types.string.String"
    """<p>The command to run on the container.</p>"""
    interactive: "capo_ecs.types.boolean.Boolean"
    """<p>Use this flag to run your command in interactive mode.</p>"""
    task: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) or ID of the task the container is part of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteCommandRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "container" in value:
        out["container"] = value["container"]
    out["command"] = value["command"]
    out["interactive"] = value["interactive"]
    out["task"] = value["task"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteCommandRequest:
    out: ExecuteCommandRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("container") is not None:
        out["container"] = data["container"]
    if data.get("command") is not None:
        out["command"] = data["command"]
    else:
        out["command"] = ""
    if data.get("interactive") is not None:
        out["interactive"] = data["interactive"]
    else:
        out["interactive"] = False
    if data.get("task") is not None:
        out["task"] = data["task"]
    else:
        out["task"] = ""
    return out
