"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureResourceIdsQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_query_scope
    import capo_observabilityadmin.types.azure_region
    import capo_observabilityadmin.types.azure_resource_type
    import capo_observabilityadmin.types.tag_filter_list


class AzureResourceIdsQuery(TypedDict, closed=True):
    scope: NotRequired[
        "capo_observabilityadmin.types.azure_query_scope.AzureQueryScope"
    ]
    """<p>Limits the query to a management group or to specific subscriptions.</p>"""
    resource_type: NotRequired[
        "capo_observabilityadmin.types.azure_resource_type.AzureResourceType"
    ]
    """<p>Limits the results to one Azure resource type, for example <code>Microsoft.Compute/virtualMachines</code>.</p>"""
    region: NotRequired["capo_observabilityadmin.types.azure_region.AzureRegion"]
    """<p>Limits the results to one Azure Region, for example <code>eastus</code>.</p>"""
    tag_filters: NotRequired[
        "capo_observabilityadmin.types.tag_filter_list.TagFilterList"
    ]
    """<p>Limits the results to resources that have these tags. A resource must match the filters for all tag keys, and any of the values for each key. The service matches tag keys and values case-insensitively, as Azure does.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureResourceIdsQuery) -> dict:
    out: dict = {}
    if "scope" in value:
        import capo_observabilityadmin.types.azure_query_scope

        out["Scope"] = capo_observabilityadmin.types.azure_query_scope.serialize_json(
            value["scope"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "region" in value:
        out["Region"] = value["region"]
    if "tag_filters" in value:
        import capo_observabilityadmin.types.tag_filter_list

        out["TagFilters"] = (
            capo_observabilityadmin.types.tag_filter_list.serialize_json(
                value["tag_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> AzureResourceIdsQuery:
    out: AzureResourceIdsQuery = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_observabilityadmin.types.azure_query_scope

        out["scope"] = capo_observabilityadmin.types.azure_query_scope.deserialize_json(
            data["Scope"]
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("TagFilters") is not None:
        import capo_observabilityadmin.types.tag_filter_list

        out["tag_filters"] = (
            capo_observabilityadmin.types.tag_filter_list.deserialize_json(
                data["TagFilters"]
            )
        )
    return out
