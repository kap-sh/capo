"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteFirewallPolicyV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_policy_v2_response


class DeleteFirewallPolicyV2Response(TypedDict, closed=True):
    firewall_policy_v2_response: "capo_network_firewall.types.firewall_policy_v2_response.FirewallPolicyV2Response"
    """<p>The high-level properties of the Next Generation policy that you asked to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFirewallPolicyV2Response) -> dict:
    out: dict = {}
    import capo_network_firewall.types.firewall_policy_v2_response

    out["FirewallPolicyV2Response"] = (
        capo_network_firewall.types.firewall_policy_v2_response.serialize_aws_json_1_0(
            value["firewall_policy_v2_response"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFirewallPolicyV2Response:
    out: DeleteFirewallPolicyV2Response = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyV2Response") is not None:
        import capo_network_firewall.types.firewall_policy_v2_response

        out["firewall_policy_v2_response"] = (
            capo_network_firewall.types.firewall_policy_v2_response.deserialize_aws_json_1_0(
                data["FirewallPolicyV2Response"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteFirewallPolicyV2Response.firewall_policy_v2_response required"
        )
    return out
