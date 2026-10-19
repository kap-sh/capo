"""Generated from Smithy shape ``com.amazonaws.ecs#DeregisterTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class DeregisterTaskDefinitionRequest(TypedDict, closed=True):
    task_definition: "capo_ecs.types.string.String"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a <code>revision</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterTaskDefinitionRequest) -> dict:
    out: dict = {}
    out["taskDefinition"] = value["task_definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterTaskDefinitionRequest:
    out: DeregisterTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("taskDefinition") is not None:
        out["task_definition"] = data["taskDefinition"]
    else:
        out["task_definition"] = ""
    return out
