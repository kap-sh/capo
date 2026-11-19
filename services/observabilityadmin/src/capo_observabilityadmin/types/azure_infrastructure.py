"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureInfrastructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_event_hub_configuration_list
    import capo_observabilityadmin.types.azure_flow_logs_infrastructure
    import capo_observabilityadmin.types.azure_subscription_id


class AzureInfrastructure(TypedDict, closed=True):
    subscription_id: NotRequired[
        "capo_observabilityadmin.types.azure_subscription_id.AzureSubscriptionId"
    ]
    """<p>The Azure subscription in which the setup creates the Event Hubs namespaces and, for <code>AwsManaged</code> Flow Logs, the Storage Accounts. You must specify this value if an <code>AzureScopeItem</code> collects <code>ResourceLogs</code>, or if you specify <code>EventHubs</code> or <code>AwsManaged</code> Flow Logs.</p>"""
    event_hubs: NotRequired[
        "capo_observabilityadmin.types.azure_event_hub_configuration_list.AzureEventHubConfigurationList"
    ]
    """<p>The Event Hubs configuration. Specify exactly one entry, which applies to the Event Hubs in every Azure Region. This value applies only if an <code>AzureScopeItem</code> collects <code>ResourceLogs</code>. If you omit it, the setup uses default settings.</p>"""
    flow_logs: NotRequired[
        "capo_observabilityadmin.types.azure_flow_logs_infrastructure.AzureFlowLogsInfrastructure"
    ]
    """<p>The location of your Flow Logs. You must specify this value if an <code>AzureScopeItem</code> collects <code>FlowLogs</code>, and you can specify it only in that case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureInfrastructure) -> dict:
    out: dict = {}
    if "subscription_id" in value:
        out["SubscriptionId"] = value["subscription_id"]
    if "event_hubs" in value:
        import capo_observabilityadmin.types.azure_event_hub_configuration_list

        out["EventHubs"] = (
            capo_observabilityadmin.types.azure_event_hub_configuration_list.serialize_json(
                value["event_hubs"]
            )
        )
    if "flow_logs" in value:
        import capo_observabilityadmin.types.azure_flow_logs_infrastructure

        out["FlowLogs"] = (
            capo_observabilityadmin.types.azure_flow_logs_infrastructure.serialize_json(
                value["flow_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AzureInfrastructure:
    out: AzureInfrastructure = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionId") is not None:
        out["subscription_id"] = data["SubscriptionId"]
    if data.get("EventHubs") is not None:
        import capo_observabilityadmin.types.azure_event_hub_configuration_list

        out["event_hubs"] = (
            capo_observabilityadmin.types.azure_event_hub_configuration_list.deserialize_json(
                data["EventHubs"]
            )
        )
    if data.get("FlowLogs") is not None:
        import capo_observabilityadmin.types.azure_flow_logs_infrastructure

        out["flow_logs"] = (
            capo_observabilityadmin.types.azure_flow_logs_infrastructure.deserialize_json(
                data["FlowLogs"]
            )
        )
    return out
