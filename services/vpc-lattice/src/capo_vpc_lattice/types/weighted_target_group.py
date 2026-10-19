"""Generated from Smithy shape ``com.amazonaws.vpclattice#WeightedTargetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.target_group_identifier
    import capo_vpc_lattice.types.target_group_weight


class WeightedTargetGroup(TypedDict, closed=True):
    target_group_identifier: (
        "capo_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier"
    )
    """<p>The ID or ARN of the target group.</p>"""
    weight: NotRequired["capo_vpc_lattice.types.target_group_weight.TargetGroupWeight"]
    """<p>Only required if you specify multiple target groups for a forward action. The weight determines how requests are distributed to the target group. For example, if you specify two target groups, each with a weight of 10, each target group receives half the requests. If you specify two target groups, one with a weight of 10 and the other with a weight of 20, the target group with a weight of 20 receives twice as many requests as the other target group. If there's only one target group specified, then the default value is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightedTargetGroup) -> dict:
    out: dict = {}
    out["targetGroupIdentifier"] = value["target_group_identifier"]
    if "weight" in value:
        out["weight"] = value["weight"]
    return out


def deserialize_json(data: dict) -> WeightedTargetGroup:
    out: WeightedTargetGroup = {}  # type: ignore[typeddict-item]
    if data.get("targetGroupIdentifier") is not None:
        out["target_group_identifier"] = data["targetGroupIdentifier"]
    else:
        out["target_group_identifier"] = ""
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    return out
