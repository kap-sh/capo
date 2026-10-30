"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerSupportabilityScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.string
    import capo_ec2.types.supportability_score


class CapacityManagerSupportabilityScore(TypedDict, closed=True):
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p> The instance type. </p>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p> The ID of the Availability Zone. </p>"""
    score: NotRequired["capo_ec2.types.supportability_score.SupportabilityScore"]
    """<p> How well the combination can support the requested capacity right now. <code>high</code> means that the combination holds several times the requested amount. <code>medium</code> means that it can cover the request with little to spare. <code>low</code> means that it holds less than the requested amount. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerSupportabilityScore, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "score" in value:
        import capo_ec2.types.supportability_score

        capo_ec2.types.supportability_score.serialize_ec2_query(
            value["score"], pairs, f"{key_prefix}Score"
        )


def deserialize_ec2_query(el: Element) -> CapacityManagerSupportabilityScore:
    out: CapacityManagerSupportabilityScore = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_score = el.find("score")
    if child_score is not None:
        import capo_ec2.types.supportability_score

        out["score"] = capo_ec2.types.supportability_score.deserialize_ec2_query(
            child_score
        )
    return out
