"""Generated from Smithy shape ``com.amazonaws.ec2#SpotMaintenanceStrategies``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_capacity_rebalance


class SpotMaintenanceStrategies(TypedDict, closed=True):
    capacity_rebalance: NotRequired[
        "capo_ec2.types.spot_capacity_rebalance.SpotCapacityRebalance"
    ]
    """<p>The Spot Instance replacement strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-capacity-rebalance.html">Capacity rebalancing</a> in the <i>Amazon EC2 User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotMaintenanceStrategies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_rebalance" in value:
        import capo_ec2.types.spot_capacity_rebalance

        capo_ec2.types.spot_capacity_rebalance.serialize_ec2_query(
            value["capacity_rebalance"], pairs, f"{key_prefix}CapacityRebalance"
        )


def deserialize_ec2_query(el: Element) -> SpotMaintenanceStrategies:
    out: SpotMaintenanceStrategies = {}  # type: ignore[typeddict-item]
    child_capacity_rebalance = el.find("capacityRebalance")
    if child_capacity_rebalance is not None:
        import capo_ec2.types.spot_capacity_rebalance

        out["capacity_rebalance"] = (
            capo_ec2.types.spot_capacity_rebalance.deserialize_ec2_query(
                child_capacity_rebalance
            )
        )
    return out
