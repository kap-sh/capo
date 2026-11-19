"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureEventHubsQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_event_hub_namespace_name
    import capo_observabilityadmin.types.azure_query_scope
    import capo_observabilityadmin.types.azure_region


class AzureEventHubsQuery(TypedDict, closed=True):
    scope: NotRequired[
        "capo_observabilityadmin.types.azure_query_scope.AzureQueryScope"
    ]
    """<p>Limits the query to a management group or to specific subscriptions.</p>"""
    namespace_name: NotRequired[
        "capo_observabilityadmin.types.azure_event_hub_namespace_name.AzureEventHubNamespaceName"
    ]
    """<p>Limits the results to Event Hubs in this namespace.</p>"""
    region: NotRequired["capo_observabilityadmin.types.azure_region.AzureRegion"]
    """<p>Limits the results to one Azure Region, for example <code>eastus</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureEventHubsQuery) -> dict:
    out: dict = {}
    if "scope" in value:
        import capo_observabilityadmin.types.azure_query_scope

        out["Scope"] = capo_observabilityadmin.types.azure_query_scope.serialize_json(
            value["scope"]
        )
    if "namespace_name" in value:
        out["NamespaceName"] = value["namespace_name"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> AzureEventHubsQuery:
    out: AzureEventHubsQuery = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_observabilityadmin.types.azure_query_scope

        out["scope"] = capo_observabilityadmin.types.azure_query_scope.deserialize_json(
            data["Scope"]
        )
    if data.get("NamespaceName") is not None:
        out["namespace_name"] = data["NamespaceName"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    return out
