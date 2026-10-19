"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeregisterTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.target_group_identifier
    import capo_vpc_lattice.types.target_list


class DeregisterTargetsRequest(TypedDict, closed=True):
    target_group_identifier: (
        "capo_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier"
    )
    """<p>The ID or ARN of the target group.</p>"""
    targets: "capo_vpc_lattice.types.target_list.TargetList"
    """<p>The targets to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterTargetsRequest) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.target_list

    out["targets"] = capo_vpc_lattice.types.target_list.serialize_json(value["targets"])
    return out


def deserialize_json(data: dict) -> DeregisterTargetsRequest:
    out: DeregisterTargetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("targets") is not None:
        import capo_vpc_lattice.types.target_list

        out["targets"] = capo_vpc_lattice.types.target_list.deserialize_json(
            data["targets"]
        )
    else:
        out["targets"] = []
    return out
