"""Generated from Smithy shape ``com.amazonaws.eventbridge#PlacementConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.placement_constraint_expression
    import capo_eventbridge.types.placement_constraint_type


class PlacementConstraint(TypedDict, closed=True):
    type: NotRequired[
        "capo_eventbridge.types.placement_constraint_type.PlacementConstraintType"
    ]
    """<p>The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates. </p>"""
    expression: NotRequired[
        "capo_eventbridge.types.placement_constraint_expression.PlacementConstraintExpression"
    ]
    """<p>A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is <code>distinctInstance</code>. To learn more, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster Query Language</a> in the Amazon Elastic Container Service Developer Guide. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementConstraint) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_eventbridge.types.placement_constraint_type

        out["type"] = (
            capo_eventbridge.types.placement_constraint_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacementConstraint:
    out: PlacementConstraint = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_eventbridge.types.placement_constraint_type

        out["type"] = (
            capo_eventbridge.types.placement_constraint_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    return out
