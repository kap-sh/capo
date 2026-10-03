"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateNodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain.types.client_request_token_string
    import capo_managedblockchain.types.input_tag_map
    import capo_managedblockchain.types.node_configuration
    import capo_managedblockchain.types.resource_id_string


class CreateNodeInput(TypedDict, closed=True):
    client_request_token: "capo_managedblockchain.types.client_request_token_string.ClientRequestTokenString"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the CLI.</p>"""
    network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network for the node.</p> <p>Ethereum public networks have the following <code>NetworkId</code>s:</p> <ul> <li> <p> <code>n-ethereum-mainnet</code> </p> </li> </ul>"""
    member_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the member that owns this node.</p> <p>Applies only to Hyperledger Fabric.</p>"""
    node_configuration: (
        "capo_managedblockchain.types.node_configuration.NodeConfiguration"
    )
    """<p>The properties of a node configuration.</p>"""
    tags: NotRequired["capo_managedblockchain.types.input_tag_map.InputTagMap"]
    """<p>Tags to assign to the node.</p> <p> Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodeInput) -> dict:
    out: dict = {}
    out["ClientRequestToken"] = value["client_request_token"]
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    import capo_managedblockchain.types.node_configuration

    out["NodeConfiguration"] = (
        capo_managedblockchain.types.node_configuration.serialize_json(
            value["node_configuration"]
        )
    )
    if "tags" in value:
        import capo_managedblockchain.types.input_tag_map

        out["Tags"] = capo_managedblockchain.types.input_tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateNodeInput:
    out: CreateNodeInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError("CreateNodeInput.client_request_token required")
    if data.get("MemberId") is not None:
        out["member_id"] = data["MemberId"]
    if data.get("NodeConfiguration") is not None:
        import capo_managedblockchain.types.node_configuration

        out["node_configuration"] = (
            capo_managedblockchain.types.node_configuration.deserialize_json(
                data["NodeConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateNodeInput.node_configuration required")
    if data.get("Tags") is not None:
        import capo_managedblockchain.types.input_tag_map

        out["tags"] = capo_managedblockchain.types.input_tag_map.deserialize_json(
            data["Tags"]
        )
    return out
