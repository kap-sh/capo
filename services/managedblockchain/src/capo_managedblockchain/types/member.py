"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Member``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.description_string
    import capo_managedblockchain.types.member_framework_attributes
    import capo_managedblockchain.types.member_log_publishing_configuration
    import capo_managedblockchain.types.member_status
    import capo_managedblockchain.types.network_member_name_string
    import capo_managedblockchain.types.output_tag_map
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.string
    import capo_managedblockchain.types.timestamp


class Member(TypedDict, closed=True):
    network_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the network to which the member belongs.</p>"""
    id: NotRequired["capo_managedblockchain.types.resource_id_string.ResourceIdString"]
    """<p>The unique identifier of the member.</p>"""
    name: NotRequired[
        "capo_managedblockchain.types.network_member_name_string.NetworkMemberNameString"
    ]
    """<p>The name of the member.</p>"""
    description: NotRequired[
        "capo_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p>An optional description for the member.</p>"""
    framework_attributes: NotRequired[
        "capo_managedblockchain.types.member_framework_attributes.MemberFrameworkAttributes"
    ]
    """<p>Attributes relevant to a member for the blockchain framework that the Managed Blockchain network uses.</p>"""
    log_publishing_configuration: NotRequired[
        "capo_managedblockchain.types.member_log_publishing_configuration.MemberLogPublishingConfiguration"
    ]
    """<p>Configuration properties for logging events associated with a member.</p>"""
    status: NotRequired["capo_managedblockchain.types.member_status.MemberStatus"]
    """<p>The status of a member.</p> <ul> <li> <p> <code>CREATING</code> - The Amazon Web Services account is in the process of creating a member.</p> </li> <li> <p> <code>AVAILABLE</code> - The member has been created and can participate in the network.</p> </li> <li> <p> <code>CREATE_FAILED</code> - The Amazon Web Services account attempted to create a member and creation failed.</p> </li> <li> <p> <code>UPDATING</code> - The member is in the process of being updated.</p> </li> <li> <p> <code>DELETING</code> - The member and all associated resources are in the process of being deleted. Either the Amazon Web Services account that owns the member deleted it, or the member is being deleted as the result of an <code>APPROVED</code> <code>PROPOSAL</code> to remove the member.</p> </li> <li> <p> <code>DELETED</code> - The member can no longer participate on the network and all associated resources are deleted. Either the Amazon Web Services account that owns the member deleted it, or the member is being deleted as the result of an <code>APPROVED</code> <code>PROPOSAL</code> to remove the member.</p> </li> <li> <p> <code>INACCESSIBLE_ENCRYPTION_KEY</code> - The member is impaired and might not function as expected because it cannot access the specified customer managed key in KMS for encryption at rest. Either the KMS key was disabled or deleted, or the grants on the key were revoked.</p> <p>The effect of disabling or deleting a key or of revoking a grant isn't immediate. It might take some time for the member resource to discover that the key is inaccessible. When a resource is in this state, we recommend deleting and recreating the resource.</p> </li> </ul>"""
    creation_date: NotRequired["capo_managedblockchain.types.timestamp.Timestamp"]
    """<p>The date and time that the member was created.</p>"""
    tags: NotRequired["capo_managedblockchain.types.output_tag_map.OutputTagMap"]
    """<p>Tags assigned to the member. Tags consist of a key and optional value.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""
    arn: NotRequired["capo_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the member. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    kms_key_arn: NotRequired["capo_managedblockchain.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the customer managed key in Key Management Service (KMS) that the member uses for encryption at rest. If the value of this parameter is <code>"AWS Owned KMS Key"</code>, the member uses an Amazon Web Services owned KMS key for encryption. This parameter is inherited by the nodes that this member owns.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-at-rest.html">Encryption at Rest</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    out: dict = {}
    if "network_id" in value:
        out["NetworkId"] = value["network_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "framework_attributes" in value:
        import capo_managedblockchain.types.member_framework_attributes

        out["FrameworkAttributes"] = (
            capo_managedblockchain.types.member_framework_attributes.serialize_json(
                value["framework_attributes"]
            )
        )
    if "log_publishing_configuration" in value:
        import capo_managedblockchain.types.member_log_publishing_configuration

        out["LogPublishingConfiguration"] = (
            capo_managedblockchain.types.member_log_publishing_configuration.serialize_json(
                value["log_publishing_configuration"]
            )
        )
    if "status" in value:
        import capo_managedblockchain.types.member_status

        out["Status"] = capo_managedblockchain.types.member_status.serialize_json(
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


def deserialize_json(data: dict) -> Member:
    out: Member = {}  # type: ignore[typeddict-item]
    if data.get("NetworkId") is not None:
        out["network_id"] = data["NetworkId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FrameworkAttributes") is not None:
        import capo_managedblockchain.types.member_framework_attributes

        out["framework_attributes"] = (
            capo_managedblockchain.types.member_framework_attributes.deserialize_json(
                data["FrameworkAttributes"]
            )
        )
    if data.get("LogPublishingConfiguration") is not None:
        import capo_managedblockchain.types.member_log_publishing_configuration

        out["log_publishing_configuration"] = (
            capo_managedblockchain.types.member_log_publishing_configuration.deserialize_json(
                data["LogPublishingConfiguration"]
            )
        )
    if data.get("Status") is not None:
        import capo_managedblockchain.types.member_status

        out["status"] = capo_managedblockchain.types.member_status.deserialize_json(
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
