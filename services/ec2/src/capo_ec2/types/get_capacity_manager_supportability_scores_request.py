"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerSupportabilityScoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_amount
    import capo_ec2.types.capacity_availability_zone_id_list
    import capo_ec2.types.capacity_unit
    import capo_ec2.types.instance_requirements_with_metadata_request
    import capo_ec2.types.supportability_instance_type_list
    import capo_ec2.types.supportability_market_type


class GetCapacityManagerSupportabilityScoresRequest(TypedDict, closed=True):
    market_type: NotRequired[
        "capo_ec2.types.supportability_market_type.SupportabilityMarketType"
    ]
    """<p> The capacity market to score. </p>"""
    capacity_amount: NotRequired["capo_ec2.types.capacity_amount.CapacityAmount"]
    """<p> The amount of capacity that you need, in the unit that you specify for <code>CapacityUnit</code>. Each score is relative to this amount. </p>"""
    capacity_unit: NotRequired["capo_ec2.types.capacity_unit.CapacityUnit"]
    """<p> The unit for <code>CapacityAmount</code>. </p>"""
    capacity_availability_zone_ids: NotRequired[
        "capo_ec2.types.capacity_availability_zone_id_list.CapacityAvailabilityZoneIdList"
    ]
    """<p> The IDs of the Availability Zones to score, such as <code>use1-az1</code>. You can specify Availability Zones in different Regions. You can specify up to 10 Availability Zones. </p>"""
    instance_types: NotRequired[
        "capo_ec2.types.supportability_instance_type_list.SupportabilityInstanceTypeList"
    ]
    """<p> The instance types to score. You can specify up to 50 instance types. </p> <p> Specify either <code>InstanceTypes</code> or <code>InstanceRequirementsWithMetadata</code>, but not both. </p>"""
    instance_requirements_with_metadata: NotRequired[
        "capo_ec2.types.instance_requirements_with_metadata_request.InstanceRequirementsWithMetadataRequest"
    ]
    """<p> The attributes that the instance types must have, such as vCPU and memory ranges. Capacity Manager resolves the attributes into matching instance types and scores each one. </p> <p> Specify either <code>InstanceTypes</code> or <code>InstanceRequirementsWithMetadata</code>, but not both. </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerSupportabilityScoresRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "market_type" in value:
        import capo_ec2.types.supportability_market_type

        capo_ec2.types.supportability_market_type.serialize_ec2_query(
            value["market_type"], pairs, f"{key_prefix}MarketType"
        )
    if "capacity_amount" in value:
        pairs.append((f"{key_prefix}CapacityAmount", str(value["capacity_amount"])))
    if "capacity_unit" in value:
        import capo_ec2.types.capacity_unit

        capo_ec2.types.capacity_unit.serialize_ec2_query(
            value["capacity_unit"], pairs, f"{key_prefix}CapacityUnit"
        )
    if "capacity_availability_zone_ids" in value:
        import capo_ec2.types.capacity_availability_zone_id_list

        capo_ec2.types.capacity_availability_zone_id_list.serialize_ec2_query(
            value["capacity_availability_zone_ids"],
            pairs,
            f"{key_prefix}CapacityAvailabilityZoneId",
        )
    if "instance_types" in value:
        import capo_ec2.types.supportability_instance_type_list

        capo_ec2.types.supportability_instance_type_list.serialize_ec2_query(
            value["instance_types"], pairs, f"{key_prefix}InstanceType"
        )
    if "instance_requirements_with_metadata" in value:
        import capo_ec2.types.instance_requirements_with_metadata_request

        capo_ec2.types.instance_requirements_with_metadata_request.serialize_ec2_query(
            value["instance_requirements_with_metadata"],
            pairs,
            f"{key_prefix}InstanceRequirementsWithMetadata",
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetCapacityManagerSupportabilityScoresRequest:
    out: GetCapacityManagerSupportabilityScoresRequest = {}  # type: ignore[typeddict-item]
    child_market_type = el.find("MarketType")
    if child_market_type is not None:
        import capo_ec2.types.supportability_market_type

        out["market_type"] = (
            capo_ec2.types.supportability_market_type.deserialize_ec2_query(
                child_market_type
            )
        )
    child_capacity_amount = el.find("CapacityAmount")
    if child_capacity_amount is not None:
        out["capacity_amount"] = int(child_capacity_amount.text or "")
    child_capacity_unit = el.find("CapacityUnit")
    if child_capacity_unit is not None:
        import capo_ec2.types.capacity_unit

        out["capacity_unit"] = capo_ec2.types.capacity_unit.deserialize_ec2_query(
            child_capacity_unit
        )
    child_capacity_availability_zone_ids = el.find("CapacityAvailabilityZoneId")
    if child_capacity_availability_zone_ids is not None:
        import capo_ec2.types.capacity_availability_zone_id_list

        out["capacity_availability_zone_ids"] = (
            capo_ec2.types.capacity_availability_zone_id_list.deserialize_ec2_query(
                child_capacity_availability_zone_ids
            )
        )
    child_instance_types = el.find("InstanceType")
    if child_instance_types is not None:
        import capo_ec2.types.supportability_instance_type_list

        out["instance_types"] = (
            capo_ec2.types.supportability_instance_type_list.deserialize_ec2_query(
                child_instance_types
            )
        )
    child_instance_requirements_with_metadata = el.find(
        "InstanceRequirementsWithMetadata"
    )
    if child_instance_requirements_with_metadata is not None:
        import capo_ec2.types.instance_requirements_with_metadata_request

        out["instance_requirements_with_metadata"] = (
            capo_ec2.types.instance_requirements_with_metadata_request.deserialize_ec2_query(
                child_instance_requirements_with_metadata
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
