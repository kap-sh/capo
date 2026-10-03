"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionPlacementConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.task_definition_placement_constraint_type


class TaskDefinitionPlacementConstraint(TypedDict, closed=True):
    type: NotRequired[
        "capo_ecs.types.task_definition_placement_constraint_type.TaskDefinitionPlacementConstraintType"
    ]
    """<p>The type of constraint. The <code>MemberOf</code> constraint restricts selection to be from a group of valid candidates.</p>"""
    expression: NotRequired["capo_ecs.types.string.String"]
    """<p>A cluster query language expression to apply to the constraint. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster query language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskDefinitionPlacementConstraint) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_ecs.types.task_definition_placement_constraint_type

        out["type"] = (
            capo_ecs.types.task_definition_placement_constraint_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskDefinitionPlacementConstraint:
    out: TaskDefinitionPlacementConstraint = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_ecs.types.task_definition_placement_constraint_type

        out["type"] = (
            capo_ecs.types.task_definition_placement_constraint_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    return out
