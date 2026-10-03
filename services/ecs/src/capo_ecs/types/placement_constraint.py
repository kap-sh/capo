"""Generated from Smithy shape ``com.amazonaws.ecs#PlacementConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.placement_constraint_type
    import capo_ecs.types.string


class PlacementConstraint(TypedDict, closed=True):
    type: NotRequired[
        "capo_ecs.types.placement_constraint_type.PlacementConstraintType"
    ]
    """<p>The type of constraint. Use <code>distinctInstance</code> to ensure that each task in a particular group is running on a different container instance. Use <code>memberOf</code> to restrict the selection to a group of valid candidates.</p>"""
    expression: NotRequired["capo_ecs.types.string.String"]
    """<p>A cluster query language expression to apply to the constraint. The expression can have a maximum length of 2000 characters. You can't specify an expression if the constraint type is <code>distinctInstance</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster query language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementConstraint) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_ecs.types.placement_constraint_type

        out["type"] = capo_ecs.types.placement_constraint_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacementConstraint:
    out: PlacementConstraint = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_ecs.types.placement_constraint_type

        out["type"] = capo_ecs.types.placement_constraint_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    return out
