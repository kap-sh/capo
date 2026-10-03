"""Generated from Smithy shape ``com.amazonaws.fms#StatefulEngineOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.rule_order
    import capo_fms.types.stream_exception_policy


class StatefulEngineOptions(TypedDict, closed=True):
    rule_order: NotRequired["capo_fms.types.rule_order.RuleOrder"]
    """<p>Indicates how to manage the order of stateful rule evaluation for the policy. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html">Evaluation order for stateful rules</a> in the <i>Network Firewall Developer Guide</i>.</p> <p>Default: <code>DEFAULT_ACTION_ORDER</code> </p>"""
    stream_exception_policy: NotRequired[
        "capo_fms.types.stream_exception_policy.StreamExceptionPolicy"
    ]
    """<p>Indicates how Network Firewall should handle traffic when a network connection breaks midstream.</p> <ul> <li> <p> <code>DROP</code> - Fail closed and drop all subsequent traffic going to the firewall.</p> </li> <li> <p> <code>CONTINUE</code> - Continue to apply rules to subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on context. For example, with a stateful rule that drops HTTP traffic, Network Firewall won't match subsequent traffic because the it won't have the context from session initialization, which defines the application layer protocol as HTTP. However, a TCP-layer rule using a <code>flow:stateless</code> rule would still match, and so would the <code>aws:drop_strict</code> default action. </p> </li> <li> <p> <code>REJECT</code> - Fail closed and drop all subsequent traffic going to the firewall. With this option, Network Firewall also sends a TCP reject packet back to the client so the client can immediately establish a new session. With the new session, Network Firewall will have context and will apply rules appropriately.</p> <p>For applications that are reliant on long-lived TCP connections that trigger Gateway Load Balancer idle timeouts, this is the recommended setting. </p> </li> <li> <p> <code>FMS_IGNORE</code> - Firewall Manager doesn't monitor or modify the Network Firewall stream exception policy settings. </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/stream-exception-policy.html">Stream exception policy in your firewall policy</a> in the <i>Network Firewall Developer Guide</i>.</p> <p>Default: <code>FMS_IGNORE</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatefulEngineOptions) -> dict:
    out: dict = {}
    if "rule_order" in value:
        import capo_fms.types.rule_order

        out["RuleOrder"] = capo_fms.types.rule_order.serialize_aws_json_1_1(
            value["rule_order"]
        )
    if "stream_exception_policy" in value:
        import capo_fms.types.stream_exception_policy

        out["StreamExceptionPolicy"] = (
            capo_fms.types.stream_exception_policy.serialize_aws_json_1_1(
                value["stream_exception_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatefulEngineOptions:
    out: StatefulEngineOptions = {}  # type: ignore[typeddict-item]
    if data.get("RuleOrder") is not None:
        import capo_fms.types.rule_order

        out["rule_order"] = capo_fms.types.rule_order.deserialize_aws_json_1_1(
            data["RuleOrder"]
        )
    if data.get("StreamExceptionPolicy") is not None:
        import capo_fms.types.stream_exception_policy

        out["stream_exception_policy"] = (
            capo_fms.types.stream_exception_policy.deserialize_aws_json_1_1(
                data["StreamExceptionPolicy"]
            )
        )
    return out
