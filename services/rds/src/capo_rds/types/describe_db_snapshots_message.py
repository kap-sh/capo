"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBSnapshotsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.filter_list
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class DescribeDBSnapshotsMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The ID of the DB instance to retrieve the list of DB snapshots for. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the identifier of an existing DBInstance.</p> </li> </ul>"""
    db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>A specific DB snapshot identifier to describe. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the identifier of an existing DBSnapshot.</p> </li> <li> <p>If this identifier is for an automated snapshot, the <code>SnapshotType</code> parameter must also be specified.</p> </li> </ul>"""
    snapshot_type: NotRequired["capo_rds.types.string.String"]
    """<p>The type of snapshots to be returned. You can specify one of the following values:</p> <ul> <li> <p> <code>automated</code> - Return all DB snapshots that have been automatically taken by Amazon RDS for my Amazon Web Services account.</p> </li> <li> <p> <code>manual</code> - Return all DB snapshots that have been taken by my Amazon Web Services account.</p> </li> <li> <p> <code>shared</code> - Return all manual DB snapshots that have been shared to my Amazon Web Services account.</p> </li> <li> <p> <code>public</code> - Return all DB snapshots that have been marked as public.</p> </li> <li> <p> <code>awsbackup</code> - Return the DB snapshots managed by the Amazon Web Services Backup service.</p> <p>For information about Amazon Web Services Backup, see the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html"> <i>Amazon Web Services Backup Developer Guide.</i> </a> </p> <p>The <code>awsbackup</code> type does not apply to Aurora.</p> </li> </ul> <p>If you don't specify a <code>SnapshotType</code> value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not included in the returned results by default. You can include shared snapshots with these results by enabling the <code>IncludeShared</code> parameter. You can include public snapshots with these results by enabling the <code>IncludePublic</code> parameter.</p> <p>The <code>IncludeShared</code> and <code>IncludePublic</code> parameters don't apply for <code>SnapshotType</code> values of <code>manual</code> or <code>automated</code>. The <code>IncludePublic</code> parameter doesn't apply when <code>SnapshotType</code> is set to <code>shared</code>. The <code>IncludeShared</code> parameter doesn't apply when <code>SnapshotType</code> is set to <code>public</code>.</p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more DB snapshots to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-instance-id</code> - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs).</p> </li> <li> <p> <code>db-snapshot-id</code> - Accepts DB snapshot identifiers.</p> </li> <li> <p> <code>dbi-resource-id</code> - Accepts identifiers of source DB instances.</p> </li> <li> <p> <code>snapshot-type</code> - Accepts types of DB snapshots.</p> </li> <li> <p> <code>engine</code> - Accepts names of database engines.</p> </li> </ul>"""
    max_records: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBSnapshots</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    include_shared: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether to include shared manual DB cluster snapshots from other Amazon Web Services accounts that this Amazon Web Services account has been given permission to copy or restore. By default, these snapshots are not included.</p> <p>You can give an Amazon Web Services account permission to restore a manual DB snapshot from another Amazon Web Services account by using the <code>ModifyDBSnapshotAttribute</code> API action.</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    include_public: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether to include manual DB cluster snapshots that are public and can be copied or restored by any Amazon Web Services account. By default, the public snapshots are not included.</p> <p>You can share a manual DB snapshot as public by using the <a>ModifyDBSnapshotAttribute</a> API.</p> <p>This setting doesn't apply to RDS Custom.</p>"""
    dbi_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>A specific DB resource ID to describe.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBSnapshotsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )
    if "snapshot_type" in value:
        pairs.append((f"{key_prefix}SnapshotType", str(value["snapshot_type"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "include_shared" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeShared",
                "true" if value["include_shared"] else "false",
            )
        )
    if "include_public" in value:
        pairs.append(
            (
                f"{key_prefix}IncludePublic",
                "true" if value["include_public"] else "false",
            )
        )
    if "dbi_resource_id" in value:
        pairs.append((f"{key_prefix}DbiResourceId", str(value["dbi_resource_id"])))


def deserialize_query(el: Element) -> DescribeDBSnapshotsMessage:
    out: DescribeDBSnapshotsMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
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
    child_include_shared = el.find("IncludeShared")
    if child_include_shared is not None:
        out["include_shared"] = (child_include_shared.text or "").lower() == "true"
    child_include_public = el.find("IncludePublic")
    if child_include_public is not None:
        out["include_public"] = (child_include_public.text or "").lower() == "true"
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    return out
