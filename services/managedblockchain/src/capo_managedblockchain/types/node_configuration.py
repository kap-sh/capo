"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.availability_zone_string
    import capo_managedblockchain.types.instance_type_string
    import capo_managedblockchain.types.node_log_publishing_configuration
    import capo_managedblockchain.types.state_db_type


class NodeConfiguration(TypedDict, closed=True):
    instance_type: (
        "capo_managedblockchain.types.instance_type_string.InstanceTypeString"
    )
    """<p>The Amazon Managed Blockchain instance type for the node.</p>"""
    availability_zone: NotRequired[
        "capo_managedblockchain.types.availability_zone_string.AvailabilityZoneString"
    ]
    """<p>The Availability Zone in which the node exists. Required for Ethereum nodes. </p>"""
    log_publishing_configuration: NotRequired[
        "capo_managedblockchain.types.node_log_publishing_configuration.NodeLogPublishingConfiguration"
    ]
    """<p>Configuration properties for logging events associated with a peer node on a Hyperledger Fabric network on Managed Blockchain. </p>"""
    state_db: NotRequired["capo_managedblockchain.types.state_db_type.StateDBType"]
    """<p>The state database that the node uses. Values are <code>LevelDB</code> or <code>CouchDB</code>. When using an Amazon Managed Blockchain network with Hyperledger Fabric version 1.4 or later, the default is <code>CouchDB</code>.</p> <p>Applies only to Hyperledger Fabric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeConfiguration) -> dict:
    out: dict = {}
    out["InstanceType"] = value["instance_type"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "log_publishing_configuration" in value:
        import capo_managedblockchain.types.node_log_publishing_configuration

        out["LogPublishingConfiguration"] = (
            capo_managedblockchain.types.node_log_publishing_configuration.serialize_json(
                value["log_publishing_configuration"]
            )
        )
    if "state_db" in value:
        import capo_managedblockchain.types.state_db_type

        out["StateDB"] = capo_managedblockchain.types.state_db_type.serialize_json(
            value["state_db"]
        )
    return out


def deserialize_json(data: dict) -> NodeConfiguration:
    out: NodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    else:
        out["instance_type"] = ""
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("LogPublishingConfiguration") is not None:
        import capo_managedblockchain.types.node_log_publishing_configuration

        out["log_publishing_configuration"] = (
            capo_managedblockchain.types.node_log_publishing_configuration.deserialize_json(
                data["LogPublishingConfiguration"]
            )
        )
    if data.get("StateDB") is not None:
        import capo_managedblockchain.types.state_db_type

        out["state_db"] = capo_managedblockchain.types.state_db_type.deserialize_json(
            data["StateDB"]
        )
    return out
