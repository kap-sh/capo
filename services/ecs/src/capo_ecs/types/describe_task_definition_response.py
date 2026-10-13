"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.tags
    import capo_ecs.types.task_definition


class DescribeTaskDefinitionResponse(TypedDict, closed=True):
    task_definition: NotRequired["capo_ecs.types.task_definition.TaskDefinition"]
    """<p>The full task definition description.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that's applied to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskDefinitionResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskDefinitionResponse:
    out: DescribeTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: DescribeTaskDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "task_definition" in value:
        import capo_ecs.types.task_definition

        out["task_definition"] = capo_ecs.types.task_definition.redact_sensitive(
            value["task_definition"]
        )
    return out
