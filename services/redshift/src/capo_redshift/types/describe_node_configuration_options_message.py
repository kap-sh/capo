"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeNodeConfigurationOptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.action_type
    import capo_redshift.types.integer_optional
    import capo_redshift.types.node_configuration_options_filter_list
    import capo_redshift.types.string


class DescribeNodeConfigurationOptionsMessage(TypedDict, closed=True):
    action_type: NotRequired["capo_redshift.types.action_type.ActionType"]
    """<p>The action type to evaluate for possible node configurations. Specify "restore-cluster" to get configuration combinations based on an existing snapshot. Specify "recommend-node-config" to get configuration recommendations based on an existing cluster or snapshot. Specify "resize-cluster" to get configuration combinations for elastic resize based on an existing cluster. </p>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster to evaluate for possible node configurations.</p>"""
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the snapshot to evaluate for possible node configurations.</p>"""
    snapshot_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the snapshot associated with the message to describe node configuration.</p>"""
    owner_account: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.</p>"""
    filters: NotRequired[
        "capo_redshift.types.node_configuration_options_filter_list.NodeConfigurationOptionsFilterList"
    ]
    """<p>A set of name, operator, and value items to filter the results.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeNodeConfigurationOptions</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>500</code> </p> <p>Constraints: minimum 100, maximum 500.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeNodeConfigurationOptionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "action_type" in value:
        import capo_redshift.types.action_type

        capo_redshift.types.action_type.serialize_query(
            value["action_type"], pairs, f"{key_prefix}ActionType"
        )
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
    if "owner_account" in value:
        pairs.append((f"{key_prefix}OwnerAccount", str(value["owner_account"])))
    if "filters" in value:
        import capo_redshift.types.node_configuration_options_filter_list

        capo_redshift.types.node_configuration_options_filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeNodeConfigurationOptionsMessage:
    out: DescribeNodeConfigurationOptionsMessage = {}  # type: ignore[typeddict-item]
    child_action_type = el.find("ActionType")
    if child_action_type is not None:
        import capo_redshift.types.action_type

        out["action_type"] = capo_redshift.types.action_type.deserialize_query(
            child_action_type
        )
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_snapshot_arn = el.find("SnapshotArn")
    if child_snapshot_arn is not None:
        out["snapshot_arn"] = str(child_snapshot_arn.text or "")
    child_owner_account = el.find("OwnerAccount")
    if child_owner_account is not None:
        out["owner_account"] = str(child_owner_account.text or "")
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_redshift.types.node_configuration_options_filter_list

        out["filters"] = (
            capo_redshift.types.node_configuration_options_filter_list.deserialize_query(
                child_filters
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
