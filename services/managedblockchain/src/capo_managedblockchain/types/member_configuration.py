"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.description_string
    import capo_managedblockchain.types.input_tag_map
    import capo_managedblockchain.types.member_framework_configuration
    import capo_managedblockchain.types.member_log_publishing_configuration
    import capo_managedblockchain.types.network_member_name_string


class MemberConfiguration(TypedDict, closed=True):
    name: "capo_managedblockchain.types.network_member_name_string.NetworkMemberNameString"
    """<p>The name of the member.</p>"""
    description: NotRequired[
        "capo_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p>An optional description of the member.</p>"""
    framework_configuration: "capo_managedblockchain.types.member_framework_configuration.MemberFrameworkConfiguration"
    """<p>Configuration properties of the blockchain framework relevant to the member.</p>"""
    log_publishing_configuration: NotRequired[
        "capo_managedblockchain.types.member_log_publishing_configuration.MemberLogPublishingConfiguration"
    ]
    """<p>Configuration properties for logging events associated with a member of a Managed Blockchain network.</p>"""
    tags: NotRequired["capo_managedblockchain.types.input_tag_map.InputTagMap"]
    """<p>Tags assigned to the member. Tags consist of a key and optional value. </p> <p>When specifying tags during creation, you can specify multiple key-value pairs in a single request, with an overall maximum of 50 tags added to each resource.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""
    kms_key_arn: NotRequired["capo_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the customer managed key in Key Management Service (KMS) to use for encryption at rest in the member. This parameter is inherited by any nodes that this member creates. For more information, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-at-rest.html">Encryption at Rest</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p> <p>Use one of the following options to specify this parameter:</p> <ul> <li> <p> <b>Undefined or empty string</b> - By default, use an KMS key that is owned and managed by Amazon Web Services on your behalf.</p> </li> <li> <p> <b>A valid symmetric customer managed KMS key</b> - Use the specified KMS key in your account that you create, own, and manage.</p> <p>Amazon Managed Blockchain doesn't support asymmetric keys. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">Using symmetric and asymmetric keys</a> in the <i>Key Management Service Developer Guide</i>.</p> <p>The following is an example of a KMS key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberConfiguration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_managedblockchain.types.member_framework_configuration

    out["FrameworkConfiguration"] = (
        capo_managedblockchain.types.member_framework_configuration.serialize_json(
            value["framework_configuration"]
        )
    )
    if "log_publishing_configuration" in value:
        import capo_managedblockchain.types.member_log_publishing_configuration

        out["LogPublishingConfiguration"] = (
            capo_managedblockchain.types.member_log_publishing_configuration.serialize_json(
                value["log_publishing_configuration"]
            )
        )
    if "tags" in value:
        import capo_managedblockchain.types.input_tag_map

        out["Tags"] = capo_managedblockchain.types.input_tag_map.serialize_json(
            value["tags"]
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> MemberConfiguration:
    out: MemberConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("MemberConfiguration.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FrameworkConfiguration") is not None:
        import capo_managedblockchain.types.member_framework_configuration

        out["framework_configuration"] = (
            capo_managedblockchain.types.member_framework_configuration.deserialize_json(
                data["FrameworkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "MemberConfiguration.framework_configuration required"
        )
    if data.get("LogPublishingConfiguration") is not None:
        import capo_managedblockchain.types.member_log_publishing_configuration

        out["log_publishing_configuration"] = (
            capo_managedblockchain.types.member_log_publishing_configuration.deserialize_json(
                data["LogPublishingConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_managedblockchain.types.input_tag_map

        out["tags"] = capo_managedblockchain.types.input_tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
