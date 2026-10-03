"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeClusterSnapshotsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.integer_optional
    import capo_redshift.types.snapshot_sorting_entity_list
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp
    import capo_redshift.types.tag_key_list
    import capo_redshift.types.tag_value_list


class DescribeClusterSnapshotsMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster which generated the requested snapshots.</p>"""
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The snapshot identifier of the snapshot about which to return information.</p>"""
    snapshot_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the snapshot associated with the message to describe cluster snapshots.</p>"""
    snapshot_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.</p> <p>Valid Values: <code>automated</code> | <code>manual</code> </p>"""
    start_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: <code>2012-07-16T18:00:00Z</code> </p>"""
    end_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: <code>2012-07-16T18:00:00Z</code> </p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterSnapshots</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""
    owner_account: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your Amazon Web Services account, or do not specify the parameter.</p>"""
    tag_keys: NotRequired["capo_redshift.types.tag_key_list.TagKeyList"]
    """<p>A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.</p>"""
    tag_values: NotRequired["capo_redshift.types.tag_value_list.TagValueList"]
    """<p>A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.</p>"""
    cluster_exists: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>A value that indicates whether to return snapshots only for an existing cluster. You can perform table-level restore only by using a snapshot of an existing cluster, that is, a cluster that has not been deleted. Values for this parameter work as follows: </p> <ul> <li> <p>If <code>ClusterExists</code> is set to <code>true</code>, <code>ClusterIdentifier</code> is required.</p> </li> <li> <p>If <code>ClusterExists</code> is set to <code>false</code> and <code>ClusterIdentifier</code> isn't specified, all snapshots associated with deleted clusters (orphaned snapshots) are returned. </p> </li> <li> <p>If <code>ClusterExists</code> is set to <code>false</code> and <code>ClusterIdentifier</code> is specified for a deleted cluster, snapshots associated with that cluster are returned.</p> </li> <li> <p>If <code>ClusterExists</code> is set to <code>false</code> and <code>ClusterIdentifier</code> is specified for an existing cluster, no snapshots are returned. </p> </li> </ul>"""
    sorting_entities: NotRequired[
        "capo_redshift.types.snapshot_sorting_entity_list.SnapshotSortingEntityList"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeClusterSnapshotsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}SnapshotIdentifier", str(value["snapshot_identifier"]))
        )
    if "snapshot_arn" in value:
        pairs.append((f"{key_prefix}SnapshotArn", str(value["snapshot_arn"])))
    if "snapshot_type" in value:
        pairs.append((f"{key_prefix}SnapshotType", str(value["snapshot_type"])))
    if "start_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "owner_account" in value:
        pairs.append((f"{key_prefix}OwnerAccount", str(value["owner_account"])))
    if "tag_keys" in value:
        import capo_redshift.types.tag_key_list

        capo_redshift.types.tag_key_list.serialize_query(
            value["tag_keys"], pairs, f"{key_prefix}TagKeys"
        )
    if "tag_values" in value:
        import capo_redshift.types.tag_value_list

        capo_redshift.types.tag_value_list.serialize_query(
            value["tag_values"], pairs, f"{key_prefix}TagValues"
        )
    if "cluster_exists" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterExists",
                "true" if value["cluster_exists"] else "false",
            )
        )
    if "sorting_entities" in value:
        import capo_redshift.types.snapshot_sorting_entity_list

        capo_redshift.types.snapshot_sorting_entity_list.serialize_query(
            value["sorting_entities"], pairs, f"{key_prefix}SortingEntities"
        )


def deserialize_query(el: Element) -> DescribeClusterSnapshotsMessage:
    out: DescribeClusterSnapshotsMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_snapshot_arn = el.find("SnapshotArn")
    if child_snapshot_arn is not None:
        out["snapshot_arn"] = str(child_snapshot_arn.text or "")
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_redshift.types.t_stamp

        out["start_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_redshift.types.t_stamp

        out["end_time"] = capo_redshift.types.t_stamp.deserialize_query(child_end_time)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_owner_account = el.find("OwnerAccount")
    if child_owner_account is not None:
        out["owner_account"] = str(child_owner_account.text or "")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_redshift.types.tag_key_list

        out["tag_keys"] = capo_redshift.types.tag_key_list.deserialize_query(
            child_tag_keys
        )
    child_tag_values = el.find("TagValues")
    if child_tag_values is not None:
        import capo_redshift.types.tag_value_list

        out["tag_values"] = capo_redshift.types.tag_value_list.deserialize_query(
            child_tag_values
        )
    child_cluster_exists = el.find("ClusterExists")
    if child_cluster_exists is not None:
        out["cluster_exists"] = (child_cluster_exists.text or "").lower() == "true"
    child_sorting_entities = el.find("SortingEntities")
    if child_sorting_entities is not None:
        import capo_redshift.types.snapshot_sorting_entity_list

        out["sorting_entities"] = (
            capo_redshift.types.snapshot_sorting_entity_list.deserialize_query(
                child_sorting_entities
            )
        )
    return out
