"""Generated from Smithy shape ``com.amazonaws.rds#BacktrackDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class BacktrackDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB cluster identifier of the DB cluster to be backtracked. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster1</code> </p>"""
    backtrack_to: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The timestamp of the time to backtrack the DB cluster to, specified in ISO 8601 format. For more information about ISO 8601, see the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <note> <p>If the specified time isn't a consistent time for the DB cluster, Aurora automatically chooses the nearest possible consistent time for the DB cluster.</p> </note> <p>Constraints:</p> <ul> <li> <p>Must contain a valid ISO 8601 timestamp.</p> </li> <li> <p>Can't contain a timestamp set in the future.</p> </li> </ul> <p>Example: <code>2017-07-08T18:00Z</code> </p>"""
    force: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to force the DB cluster to backtrack when binary logging is enabled. Otherwise, an error occurs when binary logging is enabled.</p>"""
    use_earliest_time_on_point_in_time_unavailable: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to backtrack the DB cluster to the earliest possible backtrack time when <i>BacktrackTo</i> is set to a timestamp earlier than the earliest backtrack time. When this parameter is disabled and <i>BacktrackTo</i> is set to a timestamp earlier than the earliest backtrack time, an error occurs.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BacktrackDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "backtrack_to" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["backtrack_to"], pairs, f"{key_prefix}BacktrackTo"
        )
    if "force" in value:
        pairs.append((f"{key_prefix}Force", "true" if value["force"] else "false"))
    if "use_earliest_time_on_point_in_time_unavailable" in value:
        pairs.append(
            (
                f"{key_prefix}UseEarliestTimeOnPointInTimeUnavailable",
                "true"
                if value["use_earliest_time_on_point_in_time_unavailable"]
                else "false",
            )
        )


def deserialize_query(el: Element) -> BacktrackDBClusterMessage:
    out: BacktrackDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_backtrack_to = el.find("BacktrackTo")
    if child_backtrack_to is not None:
        import capo_rds.types.t_stamp

        out["backtrack_to"] = capo_rds.types.t_stamp.deserialize_query(
            child_backtrack_to
        )
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    child_use_earliest_time_on_point_in_time_unavailable = el.find(
        "UseEarliestTimeOnPointInTimeUnavailable"
    )
    if child_use_earliest_time_on_point_in_time_unavailable is not None:
        out["use_earliest_time_on_point_in_time_unavailable"] = (
            child_use_earliest_time_on_point_in_time_unavailable.text or ""
        ).lower() == "true"
    return out
