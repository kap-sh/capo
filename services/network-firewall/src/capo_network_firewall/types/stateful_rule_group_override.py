"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleGroupOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.override_action


class StatefulRuleGroupOverride(TypedDict, closed=True):
    action: NotRequired["capo_network_firewall.types.override_action.OverrideAction"]
    """<p>The action that changes the rule group from <code>DROP</code> to <code>ALERT</code>. This only applies to managed rule groups.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRuleGroupOverride) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_network_firewall.types.override_action

        out["Action"] = (
            capo_network_firewall.types.override_action.serialize_aws_json_1_0(
                value["action"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StatefulRuleGroupOverride:
    out: StatefulRuleGroupOverride = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_network_firewall.types.override_action

        out["action"] = (
            capo_network_firewall.types.override_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StatefulRuleGroupOverride) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_network_firewall.types.override_action

        out["Action"] = capo_network_firewall.types.override_action.serialize_cbor(
            value["action"]
        )
    return out


def deserialize_cbor(data: dict) -> StatefulRuleGroupOverride:
    out: StatefulRuleGroupOverride = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_network_firewall.types.override_action

        out["action"] = capo_network_firewall.types.override_action.deserialize_cbor(
            data["Action"]
        )
    return out
