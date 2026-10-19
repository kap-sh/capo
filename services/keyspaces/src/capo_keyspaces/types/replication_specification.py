"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicationSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.region_list
    import capo_keyspaces.types.rs


class ReplicationSpecification(TypedDict, closed=True):
    replication_strategy: "capo_keyspaces.types.rs.rs"
    """<p> The <code>replicationStrategy</code> of a keyspace, the required value is <code>SINGLE_REGION</code> or <code>MULTI_REGION</code>. </p>"""
    region_list: NotRequired["capo_keyspaces.types.region_list.RegionList"]
    """<p> The <code>regionList</code> contains the Amazon Web Services Regions where the keyspace is replicated in. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicationSpecification) -> dict:
    out: dict = {}
    out["replicationStrategy"] = value["replication_strategy"]
    if "region_list" in value:
        import capo_keyspaces.types.region_list

        out["regionList"] = capo_keyspaces.types.region_list.serialize_aws_json_1_0(
            value["region_list"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicationSpecification:
    out: ReplicationSpecification = {}  # type: ignore[typeddict-item]
    if data.get("replicationStrategy") is not None:
        out["replication_strategy"] = data["replicationStrategy"]
    else:
        out["replication_strategy"] = ""
    if data.get("regionList") is not None:
        import capo_keyspaces.types.region_list

        out["region_list"] = capo_keyspaces.types.region_list.deserialize_aws_json_1_0(
            data["regionList"]
        )
    return out
