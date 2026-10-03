"""Generated from Smithy shape ``com.amazonaws.neptune#DescribeEventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.event_categories_list
    import capo_neptune.types.filter_list
    import capo_neptune.types.integer_optional
    import capo_neptune.types.source_type
    import capo_neptune.types.string
    import capo_neptune.types.t_stamp


class DescribeEventsMessage(TypedDict, closed=True):
    source_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.</p> <p>Constraints:</p> <ul> <li> <p>If SourceIdentifier is supplied, SourceType must also be provided.</p> </li> <li> <p>If the source type is <code>DBInstance</code>, then a <code>DBInstanceIdentifier</code> must be supplied.</p> </li> <li> <p>If the source type is <code>DBSecurityGroup</code>, a <code>DBSecurityGroupName</code> must be supplied.</p> </li> <li> <p>If the source type is <code>DBParameterGroup</code>, a <code>DBParameterGroupName</code> must be supplied.</p> </li> <li> <p>If the source type is <code>DBSnapshot</code>, a <code>DBSnapshotIdentifier</code> must be supplied.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    source_type: NotRequired["capo_neptune.types.source_type.SourceType"]
    """<p>The event source to retrieve events for. If no value is specified, all events are returned.</p>"""
    start_time: NotRequired["capo_neptune.types.t_stamp.TStamp"]
    """<p> The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: 2009-07-08T18:00Z</p>"""
    end_time: NotRequired["capo_neptune.types.t_stamp.TStamp"]
    """<p> The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: 2009-07-08T18:00Z</p>"""
    duration: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>The number of minutes to retrieve events for.</p> <p>Default: 60</p>"""
    event_categories: NotRequired[
        "capo_neptune.types.event_categories_list.EventCategoriesList"
    ]
    """<p>A list of event categories that trigger notifications for a event notification subscription.</p>"""
    filters: NotRequired["capo_neptune.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""
    max_records: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_neptune.types.string.String"]
    """<p> An optional pagination token provided by a previous DescribeEvents request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_identifier" in value:
        pairs.append((f"{key_prefix}SourceIdentifier", str(value["source_identifier"])))
    if "source_type" in value:
        import capo_neptune.types.source_type

        capo_neptune.types.source_type.serialize_query(
            value["source_type"], pairs, f"{key_prefix}SourceType"
        )
    if "start_time" in value:
        import capo_neptune.types.t_stamp

        capo_neptune.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_neptune.types.t_stamp

        capo_neptune.types.t_stamp.serialize_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "duration" in value:
        pairs.append((f"{key_prefix}Duration", str(value["duration"])))
    if "event_categories" in value:
        import capo_neptune.types.event_categories_list

        capo_neptune.types.event_categories_list.serialize_query(
            value["event_categories"], pairs, f"{key_prefix}EventCategories"
        )
    if "filters" in value:
        import capo_neptune.types.filter_list

        capo_neptune.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeEventsMessage:
    out: DescribeEventsMessage = {}  # type: ignore[typeddict-item]
    child_source_identifier = el.find("SourceIdentifier")
    if child_source_identifier is not None:
        out["source_identifier"] = str(child_source_identifier.text or "")
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import capo_neptune.types.source_type

        out["source_type"] = capo_neptune.types.source_type.deserialize_query(
            child_source_type
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_neptune.types.t_stamp

        out["start_time"] = capo_neptune.types.t_stamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_neptune.types.t_stamp

        out["end_time"] = capo_neptune.types.t_stamp.deserialize_query(child_end_time)
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_event_categories = el.find("EventCategories")
    if child_event_categories is not None:
        import capo_neptune.types.event_categories_list

        out["event_categories"] = (
            capo_neptune.types.event_categories_list.deserialize_query(
                child_event_categories
            )
        )
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_neptune.types.filter_list

        out["filters"] = capo_neptune.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
