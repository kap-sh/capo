"""Generated from Smithy shape ``com.amazonaws.dax#IncreaseReplicationFactorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.availability_zone_list
    import capo_dax.types.integer
    import capo_dax.types.string


class IncreaseReplicationFactorRequest(TypedDict, closed=True):
    cluster_name: "capo_dax.types.string.String"
    """<p>The name of the DAX cluster that will receive additional nodes.</p>"""
    new_replication_factor: "capo_dax.types.integer.Integer"
    """<p>The new number of nodes for the DAX cluster.</p>"""
    availability_zones: NotRequired[
        "capo_dax.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>The Availability Zones (AZs) in which the cluster nodes will be created. All nodes belonging to the cluster are placed in these Availability Zones. Use this parameter if you want to distribute the nodes across multiple AZs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncreaseReplicationFactorRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    out["NewReplicationFactor"] = value["new_replication_factor"]
    if "availability_zones" in value:
        import capo_dax.types.availability_zone_list

        out["AvailabilityZones"] = (
            capo_dax.types.availability_zone_list.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IncreaseReplicationFactorRequest:
    out: IncreaseReplicationFactorRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("NewReplicationFactor") is not None:
        out["new_replication_factor"] = data["NewReplicationFactor"]
    else:
        out["new_replication_factor"] = 0
    if data.get("AvailabilityZones") is not None:
        import capo_dax.types.availability_zone_list

        out["availability_zones"] = (
            capo_dax.types.availability_zone_list.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    return out
