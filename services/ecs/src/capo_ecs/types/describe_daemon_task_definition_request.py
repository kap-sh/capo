"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class DescribeDaemonTaskDefinitionRequest(TypedDict, closed=True):
    daemon_task_definition: "capo_ecs.types.string.String"
    """<p>The <code>family</code> for the latest <code>ACTIVE</code> revision, <code>family</code> and <code>revision</code> (<code>family:revision</code>) for a specific revision in the family, or full Amazon Resource Name (ARN) of the daemon task definition to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonTaskDefinitionRequest) -> dict:
    out: dict = {}
    out["daemonTaskDefinition"] = value["daemon_task_definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonTaskDefinitionRequest:
    out: DescribeDaemonTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("daemonTaskDefinition") is not None:
        out["daemon_task_definition"] = data["daemonTaskDefinition"]
    else:
        out["daemon_task_definition"] = ""
    return out
