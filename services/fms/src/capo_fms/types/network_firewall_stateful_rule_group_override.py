"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallStatefulRuleGroupOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.network_firewall_override_action


class NetworkFirewallStatefulRuleGroupOverride(TypedDict, closed=True):
    action: NotRequired[
        "capo_fms.types.network_firewall_override_action.NetworkFirewallOverrideAction"
    ]
    """<p>The action that changes the rule group from <code>DROP</code> to <code>ALERT</code>. This only applies to managed rule groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallStatefulRuleGroupOverride) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_fms.types.network_firewall_override_action

        out["Action"] = (
            capo_fms.types.network_firewall_override_action.serialize_aws_json_1_1(
                value["action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkFirewallStatefulRuleGroupOverride:
    out: NetworkFirewallStatefulRuleGroupOverride = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_fms.types.network_firewall_override_action

        out["action"] = (
            capo_fms.types.network_firewall_override_action.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkFirewallStatefulRuleGroupOverride) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_fms.types.network_firewall_override_action

        out["Action"] = capo_fms.types.network_firewall_override_action.serialize_cbor(
            value["action"]
        )
    return out


def deserialize_cbor(data: dict) -> NetworkFirewallStatefulRuleGroupOverride:
    out: NetworkFirewallStatefulRuleGroupOverride = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_fms.types.network_firewall_override_action

        out["action"] = (
            capo_fms.types.network_firewall_override_action.deserialize_cbor(
                data["Action"]
            )
        )
    return out
