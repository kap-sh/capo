"""Generated from Smithy shape ``com.amazonaws.scheduler#PlacementConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.placement_constraint_expression
    import capo_scheduler.types.placement_constraint_type


class PlacementConstraint(TypedDict, closed=True):
    type: NotRequired[
        "capo_scheduler.types.placement_constraint_type.PlacementConstraintType"
    ]
    """<p>The type of constraint. Use <code>distinctInstance</code> to ensure that each task in a particular group is running on a different container instance. Use <code>memberOf</code> to restrict the selection to a group of valid candidates.</p>"""
    expression: NotRequired[
        "capo_scheduler.types.placement_constraint_expression.PlacementConstraintExpression"
    ]
    """<p>A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is <code>distinctInstance</code>. For more information, see <a href="https://docs.aws.amazon.com/latest/developerguide/cluster-query-language.html">Cluster query language</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlacementConstraint) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> PlacementConstraint:
    out: PlacementConstraint = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    return out
