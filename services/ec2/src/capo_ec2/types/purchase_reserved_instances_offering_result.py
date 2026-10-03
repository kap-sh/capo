"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseReservedInstancesOfferingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class PurchaseReservedInstancesOfferingResult(TypedDict, closed=True):
    reserved_instances_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The IDs of the purchased Reserved Instances. If your purchase crosses into a discounted pricing tier, the final Reserved Instances IDs might change. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-reserved-instances-application.html#crossing-pricing-tiers">Crossing pricing tiers</a> in the <i>Amazon EC2 User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseReservedInstancesOfferingResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{key_prefix}ReservedInstancesId", str(value["reserved_instances_id"]))
        )


def deserialize_ec2_query(el: Element) -> PurchaseReservedInstancesOfferingResult:
    out: PurchaseReservedInstancesOfferingResult = {}  # type: ignore[typeddict-item]
    child_reserved_instances_id = el.find("reservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    return out
