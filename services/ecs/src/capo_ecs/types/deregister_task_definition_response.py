"""Generated from Smithy shape ``com.amazonaws.ecs#DeregisterTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.task_definition


class DeregisterTaskDefinitionResponse(TypedDict, closed=True):
    task_definition: NotRequired["capo_ecs.types.task_definition.TaskDefinition"]
    """<p>The full description of the deregistered task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "task_definition" in value:
        import capo_ecs.types.task_definition

        out["taskDefinition"] = capo_ecs.types.task_definition.serialize_aws_json_1_1(
            value["task_definition"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterTaskDefinitionResponse:
    out: DeregisterTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("taskDefinition") is not None:
        import capo_ecs.types.task_definition

        out["task_definition"] = (
            capo_ecs.types.task_definition.deserialize_aws_json_1_1(
                data["taskDefinition"]
            )
        )
    return out


def redact_sensitive(value: DeregisterTaskDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "task_definition" in value:
        import capo_ecs.types.task_definition

        out["task_definition"] = capo_ecs.types.task_definition.redact_sensitive(
            value["task_definition"]
        )
    return out
