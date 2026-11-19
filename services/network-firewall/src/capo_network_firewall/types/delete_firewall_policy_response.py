"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteFirewallPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_policy_response


class DeleteFirewallPolicyResponse(TypedDict, closed=True):
    firewall_policy_response: (
        "capo_network_firewall.types.firewall_policy_response.FirewallPolicyResponse"
    )
    """<p>The object containing the definition of the <a>FirewallPolicyResponse</a> that you asked to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFirewallPolicyResponse) -> dict:
    out: dict = {}
    import capo_network_firewall.types.firewall_policy_response

    out["FirewallPolicyResponse"] = (
        capo_network_firewall.types.firewall_policy_response.serialize_aws_json_1_0(
            value["firewall_policy_response"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFirewallPolicyResponse:
    out: DeleteFirewallPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyResponse") is not None:
        import capo_network_firewall.types.firewall_policy_response

        out["firewall_policy_response"] = (
            capo_network_firewall.types.firewall_policy_response.deserialize_aws_json_1_0(
                data["FirewallPolicyResponse"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteFirewallPolicyResponse.firewall_policy_response required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteFirewallPolicyResponse) -> dict:
    out: dict = {}
    import capo_network_firewall.types.firewall_policy_response

    out["FirewallPolicyResponse"] = (
        capo_network_firewall.types.firewall_policy_response.serialize_cbor(
            value["firewall_policy_response"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> DeleteFirewallPolicyResponse:
    out: DeleteFirewallPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyResponse") is not None:
        import capo_network_firewall.types.firewall_policy_response

        out["firewall_policy_response"] = (
            capo_network_firewall.types.firewall_policy_response.deserialize_cbor(
                data["FirewallPolicyResponse"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteFirewallPolicyResponse.firewall_policy_response required"
        )
    return out
