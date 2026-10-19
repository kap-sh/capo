"""Generated from Smithy shape ``com.amazonaws.dax#DecreaseReplicationFactorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dax.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dax.types.availability_zone_list
    import capo_dax.types.integer
    import capo_dax.types.node_identifier_list
    import capo_dax.types.string


class DecreaseReplicationFactorRequest(TypedDict, closed=True):
    cluster_name: "capo_dax.types.string.String"
    """<p>The name of the DAX cluster from which you want to remove nodes.</p>"""
    new_replication_factor: "capo_dax.types.integer.Integer"
    """<p>The new number of nodes for the DAX cluster.</p>"""
    availability_zones: NotRequired[
        "capo_dax.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>The Availability Zone(s) from which to remove nodes.</p>"""
    node_ids_to_remove: NotRequired[
        "capo_dax.types.node_identifier_list.NodeIdentifierList"
    ]
    """<p>The unique identifiers of the nodes to be removed from the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecreaseReplicationFactorRequest) -> dict:
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
    if "node_ids_to_remove" in value:
        import capo_dax.types.node_identifier_list

        out["NodeIdsToRemove"] = (
            capo_dax.types.node_identifier_list.serialize_aws_json_1_1(
                value["node_ids_to_remove"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DecreaseReplicationFactorRequest:
    out: DecreaseReplicationFactorRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError(
            "DecreaseReplicationFactorRequest.cluster_name required"
        )
    if data.get("NewReplicationFactor") is not None:
        out["new_replication_factor"] = data["NewReplicationFactor"]
    else:
        raise DeserializationError(
            "DecreaseReplicationFactorRequest.new_replication_factor required"
        )
    if data.get("AvailabilityZones") is not None:
        import capo_dax.types.availability_zone_list

        out["availability_zones"] = (
            capo_dax.types.availability_zone_list.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    if data.get("NodeIdsToRemove") is not None:
        import capo_dax.types.node_identifier_list

        out["node_ids_to_remove"] = (
            capo_dax.types.node_identifier_list.deserialize_aws_json_1_1(
                data["NodeIdsToRemove"]
            )
        )
    return out
