"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureEventHubSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_event_hub_namespace_name
    import capo_observabilityadmin.types.azure_region
    import capo_observabilityadmin.types.azure_resource_id
    import capo_observabilityadmin.types.azure_subscription_id


class AzureEventHubSummary(TypedDict, closed=True):
    resource_id: "capo_observabilityadmin.types.azure_resource_id.AzureResourceId"
    """<p>The Azure Resource Manager ID of the Event Hub.</p>"""
    event_hub_name: "str"
    """<p>The name of the Event Hub.</p>"""
    namespace_name: "capo_observabilityadmin.types.azure_event_hub_namespace_name.AzureEventHubNamespaceName"
    """<p>The name of the Event Hubs namespace that contains the Event Hub.</p>"""
    fully_qualified_namespace: "str"
    """<p>The fully qualified host name of the Event Hubs namespace, for example <code>&lt;namespace&gt;.servicebus.windows.net</code>. The suffix differs in sovereign clouds.</p>"""
    region: NotRequired["capo_observabilityadmin.types.azure_region.AzureRegion"]
    """<p>The Azure Region of the Event Hub, for example <code>eastus</code>.</p>"""
    subscription_id: NotRequired[
        "capo_observabilityadmin.types.azure_subscription_id.AzureSubscriptionId"
    ]
    """<p>The Azure subscription that contains the Event Hub.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureEventHubSummary) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    out["EventHubName"] = value["event_hub_name"]
    out["NamespaceName"] = value["namespace_name"]
    out["FullyQualifiedNamespace"] = value["fully_qualified_namespace"]
    if "region" in value:
        out["Region"] = value["region"]
    if "subscription_id" in value:
        out["SubscriptionId"] = value["subscription_id"]
    return out


def deserialize_json(data: dict) -> AzureEventHubSummary:
    out: AzureEventHubSummary = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("EventHubName") is not None:
        out["event_hub_name"] = data["EventHubName"]
    else:
        out["event_hub_name"] = ""
    if data.get("NamespaceName") is not None:
        out["namespace_name"] = data["NamespaceName"]
    else:
        out["namespace_name"] = ""
    if data.get("FullyQualifiedNamespace") is not None:
        out["fully_qualified_namespace"] = data["FullyQualifiedNamespace"]
    else:
        out["fully_qualified_namespace"] = ""
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("SubscriptionId") is not None:
        out["subscription_id"] = data["SubscriptionId"]
    return out
