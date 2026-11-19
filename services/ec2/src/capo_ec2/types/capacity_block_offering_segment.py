"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockOfferingSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class CapacityBlockOfferingSegment(TypedDict, closed=True):
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type of the Capacity Block offering segment.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone of the Capacity Block offering segment.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone for the Capacity Block offering segment.</p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances in the Capacity Block offering segment.</p>"""
    start_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The start date of the Capacity Block offering segment.</p>"""
    end_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The end date of the Capacity Block offering segment.</p>"""
    capacity_block_duration_hours: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of hours for the duration of the Capacity Block offering segment.</p>"""
    capacity_block_duration_minutes: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of minutes for the duration of the Capacity Block offering segment.</p>"""
    upfront_fee: NotRequired["capo_ec2.types.string.String"]
    """<p>The total price to be paid up front for the Capacity Block offering segment.</p>"""
    currency_code: NotRequired["capo_ec2.types.string.String"]
    """<p>The currency of the payment for the Capacity Block offering segment.</p>"""
    zone_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of zone where the Capacity Block offering segment is available.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockOfferingSegment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )
    if "capacity_block_duration_hours" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityBlockDurationHours",
                str(value["capacity_block_duration_hours"]),
            )
        )
    if "capacity_block_duration_minutes" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityBlockDurationMinutes",
                str(value["capacity_block_duration_minutes"]),
            )
        )
    if "upfront_fee" in value:
        pairs.append((f"{key_prefix}UpfrontFee", str(value["upfront_fee"])))
    if "currency_code" in value:
        pairs.append((f"{key_prefix}CurrencyCode", str(value["currency_code"])))
    if "zone_type" in value:
        pairs.append((f"{key_prefix}ZoneType", str(value["zone_type"])))


def deserialize_ec2_query(el: Element) -> CapacityBlockOfferingSegment:
    out: CapacityBlockOfferingSegment = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_instance_count = el.find("instanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_start_date = el.find("startDate")
    if child_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_date
        )
    child_end_date = el.find("endDate")
    if child_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_date
        )
    child_capacity_block_duration_hours = el.find("capacityBlockDurationHours")
    if child_capacity_block_duration_hours is not None:
        out["capacity_block_duration_hours"] = int(
            child_capacity_block_duration_hours.text or ""
        )
    child_capacity_block_duration_minutes = el.find("capacityBlockDurationMinutes")
    if child_capacity_block_duration_minutes is not None:
        out["capacity_block_duration_minutes"] = int(
            child_capacity_block_duration_minutes.text or ""
        )
    child_upfront_fee = el.find("upfrontFee")
    if child_upfront_fee is not None:
        out["upfront_fee"] = str(child_upfront_fee.text or "")
    child_currency_code = el.find("currencyCode")
    if child_currency_code is not None:
        out["currency_code"] = str(child_currency_code.text or "")
    child_zone_type = el.find("zoneType")
    if child_zone_type is not None:
        out["zone_type"] = str(child_zone_type.text or "")
    return out
