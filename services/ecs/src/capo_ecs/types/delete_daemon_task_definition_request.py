"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemonTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class DeleteDaemonTaskDefinitionRequest(TypedDict, closed=True):
    daemon_task_definition: "capo_ecs.types.string.String"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the daemon task definition to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDaemonTaskDefinitionRequest) -> dict:
    out: dict = {}
    out["daemonTaskDefinition"] = value["daemon_task_definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDaemonTaskDefinitionRequest:
    out: DeleteDaemonTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("daemonTaskDefinition") is not None:
        out["daemon_task_definition"] = data["daemonTaskDefinition"]
    else:
        out["daemon_task_definition"] = ""
    return out
