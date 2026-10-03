"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Node``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.availability_zone_string
    import capo_managedblockchain.types.instance_type_string
    import capo_managedblockchain.types.node_framework_attributes
    import capo_managedblockchain.types.node_log_publishing_configuration
    import capo_managedblockchain.types.node_status
    import capo_managedblockchain.types.output_tag_map
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.state_db_type
    import capo_managedblockchain.types.string
    import capo_managedblockchain.types.timestamp


class Node(TypedDict, closed=True):
    network_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the network that the node is on.</p>"""
    member_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the member to which the node belongs.</p> <p>Applies only to Hyperledger Fabric.</p>"""
    id: NotRequired["capo_managedblockchain.types.resource_id_string.ResourceIdString"]
    """<p>The unique identifier of the node.</p>"""
    instance_type: NotRequired[
        "capo_managedblockchain.types.instance_type_string.InstanceTypeString"
    ]
    """<p>The instance type of the node.</p>"""
    availability_zone: NotRequired[
        "capo_managedblockchain.types.availability_zone_string.AvailabilityZoneString"
    ]
    """<p>The Availability Zone in which the node exists. Required for Ethereum nodes. </p>"""
    framework_attributes: NotRequired[
        "capo_managedblockchain.types.node_framework_attributes.NodeFrameworkAttributes"
    ]
    """<p>Attributes of the blockchain framework being used.</p>"""
    log_publishing_configuration: NotRequired[
        "capo_managedblockchain.types.node_log_publishing_configuration.NodeLogPublishingConfiguration"
    ]
    """<p>Configuration properties for logging events associated with a peer node on a Hyperledger Fabric network on Managed Blockchain.</p>"""
    state_db: NotRequired["capo_managedblockchain.types.state_db_type.StateDBType"]
    """<p>The state database that the node uses. Values are <code>LevelDB</code> or <code>CouchDB</code>.</p> <p>Applies only to Hyperledger Fabric.</p>"""
    status: NotRequired["capo_managedblockchain.types.node_status.NodeStatus"]
    """<p>The status of the node.</p> <ul> <li> <p> <code>CREATING</code> - The Amazon Web Services account is in the process of creating a node.</p> </li> <li> <p> <code>AVAILABLE</code> - The node has been created and can participate in the network.</p> </li> <li> <p> <code>UNHEALTHY</code> - The node is impaired and might not function as expected. Amazon Managed Blockchain automatically finds nodes in this state and tries to recover them. If a node is recoverable, it returns to <code>AVAILABLE</code>. Otherwise, it moves to <code>FAILED</code> status.</p> </li> <li> <p> <code>CREATE_FAILED</code> - The Amazon Web Services account attempted to create a node and creation failed.</p> </li> <li> <p> <code>UPDATING</code> - The node is in the process of being updated.</p> </li> <li> <p> <code>DELETING</code> - The node is in the process of being deleted.</p> </li> <li> <p> <code>DELETED</code> - The node can no longer participate on the network.</p> </li> <li> <p> <code>FAILED</code> - The node is no longer functional, cannot be recovered, and must be deleted.</p> </li> <li> <p> <code>INACCESSIBLE_ENCRYPTION_KEY</code> - The node is impaired and might not function as expected because it cannot access the specified customer managed key in KMS for encryption at rest. Either the KMS key was disabled or deleted, or the grants on the key were revoked.</p> <p>The effect of disabling or deleting a key or of revoking a grant isn't immediate. It might take some time for the node resource to discover that the key is inaccessible. When a resource is in this state, we recommend deleting and recreating the resource.</p> </li> </ul>"""
    creation_date: NotRequired["capo_managedblockchain.types.timestamp.Timestamp"]
    """<p>The date and time that the node was created.</p>"""
    tags: NotRequired["capo_managedblockchain.types.output_tag_map.OutputTagMap"]
    """<p>Tags assigned to the node. Each tag consists of a key and optional value.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""
    arn: NotRequired["capo_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the node. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    kms_key_arn: NotRequired["capo_managedblockchain.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the customer managed key in Key Management Service (KMS) that the node uses for encryption at rest. If the value of this parameter is <code>"AWS Owned KMS Key"</code>, the node uses an Amazon Web Services owned KMS key for encryption. The node inherits this parameter from the member that it belongs to.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-at-rest.html">Encryption at Rest</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p> <p>Applies only to Hyperledger Fabric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Node) -> dict:
    out: dict = {}
    if "network_id" in value:
        out["NetworkId"] = value["network_id"]
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "framework_attributes" in value:
        import capo_managedblockchain.types.node_framework_attributes

        out["FrameworkAttributes"] = (
            capo_managedblockchain.types.node_framework_attributes.serialize_json(
                value["framework_attributes"]
            )
        )
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
    if "status" in value:
        import capo_managedblockchain.types.node_status

        out["Status"] = capo_managedblockchain.types.node_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import capo_managedblockchain.types.timestamp

        out["CreationDate"] = capo_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "tags" in value:
        import capo_managedblockchain.types.output_tag_map

        out["Tags"] = capo_managedblockchain.types.output_tag_map.serialize_json(
            value["tags"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if data.get("NetworkId") is not None:
        out["network_id"] = data["NetworkId"]
    if data.get("MemberId") is not None:
        out["member_id"] = data["MemberId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("FrameworkAttributes") is not None:
        import capo_managedblockchain.types.node_framework_attributes

        out["framework_attributes"] = (
            capo_managedblockchain.types.node_framework_attributes.deserialize_json(
                data["FrameworkAttributes"]
            )
        )
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
    if data.get("Status") is not None:
        import capo_managedblockchain.types.node_status

        out["status"] = capo_managedblockchain.types.node_status.deserialize_json(
            data["Status"]
        )
    if data.get("CreationDate") is not None:
        import capo_managedblockchain.types.timestamp

        out["creation_date"] = capo_managedblockchain.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("Tags") is not None:
        import capo_managedblockchain.types.output_tag_map

        out["tags"] = capo_managedblockchain.types.output_tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
