"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateNetworkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain.types.client_request_token_string
    import capo_managedblockchain.types.description_string
    import capo_managedblockchain.types.framework
    import capo_managedblockchain.types.framework_version_string
    import capo_managedblockchain.types.input_tag_map
    import capo_managedblockchain.types.member_configuration
    import capo_managedblockchain.types.name_string
    import capo_managedblockchain.types.network_framework_configuration
    import capo_managedblockchain.types.voting_policy


class CreateNetworkInput(TypedDict, closed=True):
    client_request_token: "capo_managedblockchain.types.client_request_token_string.ClientRequestTokenString"
    """<p>This is a unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the Amazon Web Services CLI. </p>"""
    name: "capo_managedblockchain.types.name_string.NameString"
    """<p>The name of the network.</p>"""
    description: NotRequired[
        "capo_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p>An optional description for the network.</p>"""
    framework: "capo_managedblockchain.types.framework.Framework"
    """<p>The blockchain framework that the network uses.</p>"""
    framework_version: (
        "capo_managedblockchain.types.framework_version_string.FrameworkVersionString"
    )
    """<p>The version of the blockchain framework that the network uses.</p>"""
    framework_configuration: NotRequired[
        "capo_managedblockchain.types.network_framework_configuration.NetworkFrameworkConfiguration"
    ]
    """<p> Configuration properties of the blockchain framework relevant to the network configuration. </p>"""
    voting_policy: "capo_managedblockchain.types.voting_policy.VotingPolicy"
    """<p> The voting rules used by the network to determine if a proposal is approved. </p>"""
    member_configuration: (
        "capo_managedblockchain.types.member_configuration.MemberConfiguration"
    )
    """<p>Configuration properties for the first member within the network.</p>"""
    tags: NotRequired["capo_managedblockchain.types.input_tag_map.InputTagMap"]
    """<p>Tags to assign to the network.</p> <p> Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkInput) -> dict:
    out: dict = {}
    out["ClientRequestToken"] = value["client_request_token"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_managedblockchain.types.framework

    out["Framework"] = capo_managedblockchain.types.framework.serialize_json(
        value["framework"]
    )
    out["FrameworkVersion"] = value["framework_version"]
    if "framework_configuration" in value:
        import capo_managedblockchain.types.network_framework_configuration

        out["FrameworkConfiguration"] = (
            capo_managedblockchain.types.network_framework_configuration.serialize_json(
                value["framework_configuration"]
            )
        )
    import capo_managedblockchain.types.voting_policy

    out["VotingPolicy"] = capo_managedblockchain.types.voting_policy.serialize_json(
        value["voting_policy"]
    )
    import capo_managedblockchain.types.member_configuration

    out["MemberConfiguration"] = (
        capo_managedblockchain.types.member_configuration.serialize_json(
            value["member_configuration"]
        )
    )
    if "tags" in value:
        import capo_managedblockchain.types.input_tag_map

        out["Tags"] = capo_managedblockchain.types.input_tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateNetworkInput:
    out: CreateNetworkInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError("CreateNetworkInput.client_request_token required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateNetworkInput.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Framework") is not None:
        import capo_managedblockchain.types.framework

        out["framework"] = capo_managedblockchain.types.framework.deserialize_json(
            data["Framework"]
        )
    else:
        raise DeserializationError("CreateNetworkInput.framework required")
    if data.get("FrameworkVersion") is not None:
        out["framework_version"] = data["FrameworkVersion"]
    else:
        raise DeserializationError("CreateNetworkInput.framework_version required")
    if data.get("FrameworkConfiguration") is not None:
        import capo_managedblockchain.types.network_framework_configuration

        out["framework_configuration"] = (
            capo_managedblockchain.types.network_framework_configuration.deserialize_json(
                data["FrameworkConfiguration"]
            )
        )
    if data.get("VotingPolicy") is not None:
        import capo_managedblockchain.types.voting_policy

        out["voting_policy"] = (
            capo_managedblockchain.types.voting_policy.deserialize_json(
                data["VotingPolicy"]
            )
        )
    else:
        raise DeserializationError("CreateNetworkInput.voting_policy required")
    if data.get("MemberConfiguration") is not None:
        import capo_managedblockchain.types.member_configuration

        out["member_configuration"] = (
            capo_managedblockchain.types.member_configuration.deserialize_json(
                data["MemberConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateNetworkInput.member_configuration required")
    if data.get("Tags") is not None:
        import capo_managedblockchain.types.input_tag_map

        out["tags"] = capo_managedblockchain.types.input_tag_map.deserialize_json(
            data["Tags"]
        )
    return out
