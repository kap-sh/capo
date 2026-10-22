"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBCapacityReservationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_capacity_reservation_identifier
    import capo_rds.types.filter_list
    import capo_rds.types.max_records
    import capo_rds.types.string


class DescribeDBCapacityReservationsRequest(TypedDict, closed=True):
    db_capacity_reservation_identifier: NotRequired[
        "capo_rds.types.db_capacity_reservation_identifier.DBCapacityReservationIdentifier"
    ]
    """<p>The identifier or the name of the DB capacity reservation to describe. You can specify the identifier, which has the prefix <code>dbcr-</code>, or the reservation name.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBCapacityReservations</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["capo_rds.types.max_records.MaxRecords"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints:</p> <ul> <li> <p>Must be a minimum of 20.</p> </li> <li> <p>Can't exceed 100.</p> </li> </ul>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies which DB capacity reservations to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-capacity-reservation-name</code> - Accepts DB capacity reservation names. The response includes only the reservations that these names identify. Use this filter to describe several reservations by name in one request.</p> </li> <li> <p> <code>state</code> - Accepts reservation states. The response includes only the reservations in these states.</p> </li> <li> <p> <code>engine</code> - Accepts database engine names. The response includes only the reservations that reserve capacity for these engines.</p> </li> <li> <p> <code>db-instance-class</code> - Accepts DB instance classes. The response includes only the reservations that reserve capacity for these DB instance classes.</p> </li> <li> <p> <code>availability-zone</code> - Accepts Availability Zone names. The response includes only the reservations that cover these Availability Zones.</p> </li> </ul> <p>When you specify more than one value for a filter, the response includes the reservations that match any of those values. When you specify more than one filter, the response includes only the reservations that match every filter.</p> <p>Amazon RDS rejects the request when a filter name isn't in this list, or when a filter specifies no values.</p> <note> <p>The <code>state</code> filter doesn't accept <code>expired</code>. To find an expired reservation, compare <code>EndDate</code> against the current date and time.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBCapacityReservationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_capacity_reservation_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBCapacityReservationIdentifier",
                str(value["db_capacity_reservation_identifier"]),
            )
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )


def deserialize_query(el: Element) -> DescribeDBCapacityReservationsRequest:
    out: DescribeDBCapacityReservationsRequest = {}  # type: ignore[typeddict-item]
    child_db_capacity_reservation_identifier = el.find(
        "DBCapacityReservationIdentifier"
    )
    if child_db_capacity_reservation_identifier is not None:
        out["db_capacity_reservation_identifier"] = str(
            child_db_capacity_reservation_identifier.text or ""
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    return out
