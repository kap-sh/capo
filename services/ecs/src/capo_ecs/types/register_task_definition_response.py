"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.tags
    import capo_ecs.types.task_definition


class RegisterTaskDefinitionResponse(TypedDict, closed=True):
    task_definition: NotRequired["capo_ecs.types.task_definition.TaskDefinition"]
    """<p>The full description of the registered task definition.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The list of tags associated with the task definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "task_definition" in value:
        import capo_ecs.types.task_definition

        out["taskDefinition"] = capo_ecs.types.task_definition.serialize_aws_json_1_1(
            value["task_definition"]
        )
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterTaskDefinitionResponse:
    out: RegisterTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("taskDefinition") is not None:
        import capo_ecs.types.task_definition

        out["task_definition"] = (
            capo_ecs.types.task_definition.deserialize_aws_json_1_1(
                data["taskDefinition"]
            )
        )
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out


def redact_sensitive(value: RegisterTaskDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "task_definition" in value:
        import capo_ecs.types.task_definition

        out["task_definition"] = capo_ecs.types.task_definition.redact_sensitive(
            value["task_definition"]
        )
    return out
