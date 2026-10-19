"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetKeyspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.arn
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.region_list
    import capo_keyspaces.types.replication_group_status_list
    import capo_keyspaces.types.rs


class GetKeyspaceResponse(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace.</p>"""
    resource_arn: "capo_keyspaces.types.arn.ARN"
    """<p>Returns the ARN of the keyspace.</p>"""
    replication_strategy: "capo_keyspaces.types.rs.rs"
    """<p> Returns the replication strategy of the keyspace. The options are <code>SINGLE_REGION</code> or <code>MULTI_REGION</code>. </p>"""
    replication_regions: NotRequired["capo_keyspaces.types.region_list.RegionList"]
    """<p> If the <code>replicationStrategy</code> of the keyspace is <code>MULTI_REGION</code>, a list of replication Regions is returned. </p>"""
    replication_group_statuses: NotRequired[
        "capo_keyspaces.types.replication_group_status_list.ReplicationGroupStatusList"
    ]
    """<p> A list of all Regions the keyspace is replicated in after the update keyspace operation and their status. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetKeyspaceResponse) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["resourceArn"] = value["resource_arn"]
    out["replicationStrategy"] = value["replication_strategy"]
    if "replication_regions" in value:
        import capo_keyspaces.types.region_list

        out["replicationRegions"] = (
            capo_keyspaces.types.region_list.serialize_aws_json_1_0(
                value["replication_regions"]
            )
        )
    if "replication_group_statuses" in value:
        import capo_keyspaces.types.replication_group_status_list

        out["replicationGroupStatuses"] = (
            capo_keyspaces.types.replication_group_status_list.serialize_aws_json_1_0(
                value["replication_group_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetKeyspaceResponse:
    out: GetKeyspaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("replicationStrategy") is not None:
        out["replication_strategy"] = data["replicationStrategy"]
    else:
        out["replication_strategy"] = ""
    if data.get("replicationRegions") is not None:
        import capo_keyspaces.types.region_list

        out["replication_regions"] = (
            capo_keyspaces.types.region_list.deserialize_aws_json_1_0(
                data["replicationRegions"]
            )
        )
    if data.get("replicationGroupStatuses") is not None:
        import capo_keyspaces.types.replication_group_status_list

        out["replication_group_statuses"] = (
            capo_keyspaces.types.replication_group_status_list.deserialize_aws_json_1_0(
                data["replicationGroupStatuses"]
            )
        )
    return out
