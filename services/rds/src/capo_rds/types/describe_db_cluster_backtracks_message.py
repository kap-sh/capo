"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBClusterBacktracksMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.filter_list
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class DescribeDBClusterBacktracksMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB cluster identifier of the DB cluster to be described. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster1</code> </p>"""
    backtrack_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>If specified, this value is the backtrack identifier of the backtrack to be described.</p> <p>Constraints:</p> <ul> <li> <p>Must contain a valid universally unique identifier (UUID). For more information about UUIDs, see <a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">Universally unique identifier</a>.</p> </li> </ul> <p>Example: <code>123e4567-e89b-12d3-a456-426655440000</code> </p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more DB clusters to describe. Supported filters include the following:</p> <ul> <li> <p> <code>db-cluster-backtrack-id</code> - Accepts backtrack identifiers. The results list includes information about only the backtracks identified by these identifiers.</p> </li> <li> <p> <code>db-cluster-backtrack-status</code> - Accepts any of the following backtrack status values:</p> <ul> <li> <p> <code>applying</code> </p> </li> <li> <p> <code>completed</code> </p> </li> <li> <p> <code>failed</code> </p> </li> <li> <p> <code>pending</code> </p> </li> </ul> <p>The results list includes information about only the backtracks identified by these values.</p> </li> </ul>"""
    max_records: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBClusterBacktracks</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBClusterBacktracksMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "backtrack_identifier" in value:
        pairs.append(
            (f"{key_prefix}BacktrackIdentifier", str(value["backtrack_identifier"]))
        )
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBClusterBacktracksMessage:
    out: DescribeDBClusterBacktracksMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_backtrack_identifier = el.find("BacktrackIdentifier")
    if child_backtrack_identifier is not None:
        out["backtrack_identifier"] = str(child_backtrack_identifier.text or "")
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
