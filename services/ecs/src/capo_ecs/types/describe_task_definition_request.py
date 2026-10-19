"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.task_definition_field_list


class DescribeTaskDefinitionRequest(TypedDict, closed=True):
    task_definition: "capo_ecs.types.string.String"
    """<p>The <code>family</code> for the latest <code>ACTIVE</code> revision, <code>family</code> and <code>revision</code> (<code>family:revision</code>) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe.</p>"""
    include: NotRequired[
        "capo_ecs.types.task_definition_field_list.TaskDefinitionFieldList"
    ]
    """<p>Determines whether to see the resource tags for the task definition. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskDefinitionRequest) -> dict:
    out: dict = {}
    out["taskDefinition"] = value["task_definition"]
    if "include" in value:
        import capo_ecs.types.task_definition_field_list

        out["include"] = (
            capo_ecs.types.task_definition_field_list.serialize_aws_json_1_1(
                value["include"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskDefinitionRequest:
    out: DescribeTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("taskDefinition") is not None:
        out["task_definition"] = data["taskDefinition"]
    else:
        out["task_definition"] = ""
    if data.get("include") is not None:
        import capo_ecs.types.task_definition_field_list

        out["include"] = (
            capo_ecs.types.task_definition_field_list.deserialize_aws_json_1_1(
                data["include"]
            )
        )
    return out
