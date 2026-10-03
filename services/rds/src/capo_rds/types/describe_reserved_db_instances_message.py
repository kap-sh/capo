"""Generated from Smithy shape ``com.amazonaws.rds#DescribeReservedDBInstancesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.filter_list
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class DescribeReservedDBInstancesMessage(TypedDict, closed=True):
    reserved_db_instance_id: NotRequired["capo_rds.types.string.String"]
    """<p>The reserved DB instance identifier filter value. Specify this parameter to show only the reservation that matches the specified reservation ID.</p>"""
    reserved_db_instances_offering_id: NotRequired["capo_rds.types.string.String"]
    """<p>The offering identifier filter value. Specify this parameter to show only purchased reservations matching the specified offering identifier.</p>"""
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The DB instance class filter value. Specify this parameter to show only those reservations matching the specified DB instances class.</p>"""
    duration: NotRequired["capo_rds.types.string.String"]
    """<p>The duration filter value, specified in years or seconds. Specify this parameter to show only reservations for this duration.</p> <p>Valid Values: <code>1 | 3 | 31536000 | 94608000</code> </p>"""
    product_description: NotRequired["capo_rds.types.string.String"]
    """<p>The product description filter value. Specify this parameter to show only those reservations matching the specified product description.</p>"""
    offering_type: NotRequired["capo_rds.types.string.String"]
    """<p>The offering type filter value. Specify this parameter to show only the available offerings matching the specified offering type.</p> <p>Valid Values: <code>"Partial Upfront" | "All Upfront" | "No Upfront" </code> </p>"""
    multi_az: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to show only those reservations that support Multi-AZ.</p>"""
    lease_id: NotRequired["capo_rds.types.string.String"]
    """<p>The lease identifier filter value. Specify this parameter to show only the reservation that matches the specified lease ID.</p> <note> <p>Amazon Web Services Support might request the lease ID for an issue related to a reserved DB instance.</p> </note>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>This parameter isn't currently supported.</p>"""
    max_records: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more than the <code>MaxRecords</code> value is available, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeReservedDBInstancesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_db_instance_id" in value:
        pairs.append(
            (f"{key_prefix}ReservedDBInstanceId", str(value["reserved_db_instance_id"]))
        )
    if "reserved_db_instances_offering_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedDBInstancesOfferingId",
                str(value["reserved_db_instances_offering_id"]),
            )
        )
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "duration" in value:
        pairs.append((f"{key_prefix}Duration", str(value["duration"])))
    if "product_description" in value:
        pairs.append(
            (f"{key_prefix}ProductDescription", str(value["product_description"]))
        )
    if "offering_type" in value:
        pairs.append((f"{key_prefix}OfferingType", str(value["offering_type"])))
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "lease_id" in value:
        pairs.append((f"{key_prefix}LeaseId", str(value["lease_id"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeReservedDBInstancesMessage:
    out: DescribeReservedDBInstancesMessage = {}  # type: ignore[typeddict-item]
    child_reserved_db_instance_id = el.find("ReservedDBInstanceId")
    if child_reserved_db_instance_id is not None:
        out["reserved_db_instance_id"] = str(child_reserved_db_instance_id.text or "")
    child_reserved_db_instances_offering_id = el.find("ReservedDBInstancesOfferingId")
    if child_reserved_db_instances_offering_id is not None:
        out["reserved_db_instances_offering_id"] = str(
            child_reserved_db_instances_offering_id.text or ""
        )
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = str(child_duration.text or "")
    child_product_description = el.find("ProductDescription")
    if child_product_description is not None:
        out["product_description"] = str(child_product_description.text or "")
    child_offering_type = el.find("OfferingType")
    if child_offering_type is not None:
        out["offering_type"] = str(child_offering_type.text or "")
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_lease_id = el.find("LeaseId")
    if child_lease_id is not None:
        out["lease_id"] = str(child_lease_id.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
