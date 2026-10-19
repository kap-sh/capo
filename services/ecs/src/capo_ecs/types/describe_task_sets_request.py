"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTaskSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.task_set_field_list


class DescribeTaskSetsRequest(TypedDict, closed=True):
    cluster: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>"""
    service: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in.</p>"""
    task_sets: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The ID or full Amazon Resource Name (ARN) of task sets to describe.</p>"""
    include: NotRequired["capo_ecs.types.task_set_field_list.TaskSetFieldList"]
    """<p>Specifies whether to see the resource tags for the task set. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskSetsRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    if "task_sets" in value:
        import capo_ecs.types.string_list

        out["taskSets"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["task_sets"]
        )
    if "include" in value:
        import capo_ecs.types.task_set_field_list

        out["include"] = capo_ecs.types.task_set_field_list.serialize_aws_json_1_1(
            value["include"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskSetsRequest:
    out: DescribeTaskSetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    else:
        out["cluster"] = ""
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        out["service"] = ""
    if data.get("taskSets") is not None:
        import capo_ecs.types.string_list

        out["task_sets"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["taskSets"]
        )
    if data.get("include") is not None:
        import capo_ecs.types.task_set_field_list

        out["include"] = capo_ecs.types.task_set_field_list.deserialize_aws_json_1_1(
            data["include"]
        )
    return out
