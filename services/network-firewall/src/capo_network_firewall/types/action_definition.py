"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.publish_metric_action


class ActionDefinition(TypedDict, closed=True):
    publish_metric_action: NotRequired[
        "capo_network_firewall.types.publish_metric_action.PublishMetricAction"
    ]
    """<p>Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet. This setting defines a CloudWatch dimension value to be published.</p> <p>You can pair this custom action with any of the standard stateless rule actions. For example, you could pair this in a rule action with the standard action that forwards the packet for stateful inspection. Then, when a packet matches the rule, Network Firewall publishes metrics for the packet and forwards it. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionDefinition) -> dict:
    out: dict = {}
    if "publish_metric_action" in value:
        import capo_network_firewall.types.publish_metric_action

        out["PublishMetricAction"] = (
            capo_network_firewall.types.publish_metric_action.serialize_aws_json_1_0(
                value["publish_metric_action"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActionDefinition:
    out: ActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("PublishMetricAction") is not None:
        import capo_network_firewall.types.publish_metric_action

        out["publish_metric_action"] = (
            capo_network_firewall.types.publish_metric_action.deserialize_aws_json_1_0(
                data["PublishMetricAction"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionDefinition) -> dict:
    out: dict = {}
    if "publish_metric_action" in value:
        import capo_network_firewall.types.publish_metric_action

        out["PublishMetricAction"] = (
            capo_network_firewall.types.publish_metric_action.serialize_cbor(
                value["publish_metric_action"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ActionDefinition:
    out: ActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("PublishMetricAction") is not None:
        import capo_network_firewall.types.publish_metric_action

        out["publish_metric_action"] = (
            capo_network_firewall.types.publish_metric_action.deserialize_cbor(
                data["PublishMetricAction"]
            )
        )
    return out
