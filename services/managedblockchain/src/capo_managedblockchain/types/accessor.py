"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Accessor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.accessor_billing_token_string
    import capo_managedblockchain.types.accessor_network_type
    import capo_managedblockchain.types.accessor_status
    import capo_managedblockchain.types.accessor_type
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.output_tag_map
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.timestamp


class Accessor(TypedDict, closed=True):
    id: NotRequired["capo_managedblockchain.types.resource_id_string.ResourceIdString"]
    """<p>The unique identifier of the accessor.</p>"""
    type: NotRequired["capo_managedblockchain.types.accessor_type.AccessorType"]
    """<p>The type of the accessor.</p> <note> <p>Currently, accessor type is restricted to <code>BILLING_TOKEN</code>.</p> </note>"""
    billing_token: NotRequired[
        "capo_managedblockchain.types.accessor_billing_token_string.AccessorBillingTokenString"
    ]
    """<p>The billing token is a property of the Accessor. Use this token to when making calls to the blockchain network. The billing token is used to track your accessor token for billing requests.</p>"""
    status: NotRequired["capo_managedblockchain.types.accessor_status.AccessorStatus"]
    """<p>The current status of the accessor.</p>"""
    creation_date: NotRequired["capo_managedblockchain.types.timestamp.Timestamp"]
    """<p>The creation date and time of the accessor.</p>"""
    arn: NotRequired["capo_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the accessor. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    tags: NotRequired["capo_managedblockchain.types.output_tag_map.OutputTagMap"]
    """<p>The tags assigned to the Accessor.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""
    network_type: NotRequired[
        "capo_managedblockchain.types.accessor_network_type.AccessorNetworkType"
    ]
    """<p>The blockchain network that the Accessor token is created for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Accessor) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_managedblockchain.types.accessor_type

        out["Type"] = capo_managedblockchain.types.accessor_type.serialize_json(
            value["type"]
        )
    if "billing_token" in value:
        out["BillingToken"] = value["billing_token"]
    if "status" in value:
        import capo_managedblockchain.types.accessor_status

        out["Status"] = capo_managedblockchain.types.accessor_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import capo_managedblockchain.types.timestamp

        out["CreationDate"] = capo_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "tags" in value:
        import capo_managedblockchain.types.output_tag_map

        out["Tags"] = capo_managedblockchain.types.output_tag_map.serialize_json(
            value["tags"]
        )
    if "network_type" in value:
        import capo_managedblockchain.types.accessor_network_type

        out["NetworkType"] = (
            capo_managedblockchain.types.accessor_network_type.serialize_json(
                value["network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> Accessor:
    out: Accessor = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_managedblockchain.types.accessor_type

        out["type"] = capo_managedblockchain.types.accessor_type.deserialize_json(
            data["Type"]
        )
    if data.get("BillingToken") is not None:
        out["billing_token"] = data["BillingToken"]
    if data.get("Status") is not None:
        import capo_managedblockchain.types.accessor_status

        out["status"] = capo_managedblockchain.types.accessor_status.deserialize_json(
            data["Status"]
        )
    if data.get("CreationDate") is not None:
        import capo_managedblockchain.types.timestamp

        out["creation_date"] = capo_managedblockchain.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Tags") is not None:
        import capo_managedblockchain.types.output_tag_map

        out["tags"] = capo_managedblockchain.types.output_tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("NetworkType") is not None:
        import capo_managedblockchain.types.accessor_network_type

        out["network_type"] = (
            capo_managedblockchain.types.accessor_network_type.deserialize_json(
                data["NetworkType"]
            )
        )
    return out
