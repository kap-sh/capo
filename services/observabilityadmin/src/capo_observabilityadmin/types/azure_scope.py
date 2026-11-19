"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_region_list
    import capo_observabilityadmin.types.azure_resource_id_scope_list
    import capo_observabilityadmin.types.azure_resource_type_list
    import capo_observabilityadmin.types.azure_subscription_scope
    import capo_observabilityadmin.types.tag_filter_list


class AzureScope(TypedDict, closed=True):
    subscriptions: NotRequired[
        "capo_observabilityadmin.types.azure_subscription_scope.AzureSubscriptionScope"
    ]
    """<p>The subscriptions to find resources in: all subscriptions that the connector can read, or a list of subscriptions. Required when you use <code>Regions</code> and <code>ResourceTypes</code>.</p>"""
    regions: NotRequired[
        "capo_observabilityadmin.types.azure_region_list.AzureRegionList"
    ]
    """<p>The Azure Regions to find resources in. Required when you use <code>Subscriptions</code> and <code>ResourceTypes</code>.</p>"""
    resource_types: NotRequired[
        "capo_observabilityadmin.types.azure_resource_type_list.AzureResourceTypeList"
    ]
    """<p>The Azure resource types to find. Required when you use <code>Subscriptions</code> and <code>Regions</code>.</p>"""
    tag_filters: NotRequired[
        "capo_observabilityadmin.types.tag_filter_list.TagFilterList"
    ]
    """<p>Limits the resources found by <code>Subscriptions</code>, <code>Regions</code>, and <code>ResourceTypes</code> to those that have these tags. You can specify up to 50 filters.</p>"""
    resources: NotRequired[
        "capo_observabilityadmin.types.azure_resource_id_scope_list.AzureResourceIdScopeList"
    ]
    """<p>Specific Azure resources, listed by Azure Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureScope) -> dict:
    out: dict = {}
    if "subscriptions" in value:
        import capo_observabilityadmin.types.azure_subscription_scope

        out["Subscriptions"] = (
            capo_observabilityadmin.types.azure_subscription_scope.serialize_json(
                value["subscriptions"]
            )
        )
    if "regions" in value:
        import capo_observabilityadmin.types.azure_region_list

        out["Regions"] = capo_observabilityadmin.types.azure_region_list.serialize_json(
            value["regions"]
        )
    if "resource_types" in value:
        import capo_observabilityadmin.types.azure_resource_type_list

        out["ResourceTypes"] = (
            capo_observabilityadmin.types.azure_resource_type_list.serialize_json(
                value["resource_types"]
            )
        )
    if "tag_filters" in value:
        import capo_observabilityadmin.types.tag_filter_list

        out["TagFilters"] = (
            capo_observabilityadmin.types.tag_filter_list.serialize_json(
                value["tag_filters"]
            )
        )
    if "resources" in value:
        import capo_observabilityadmin.types.azure_resource_id_scope_list

        out["Resources"] = (
            capo_observabilityadmin.types.azure_resource_id_scope_list.serialize_json(
                value["resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> AzureScope:
    out: AzureScope = {}  # type: ignore[typeddict-item]
    if data.get("Subscriptions") is not None:
        import capo_observabilityadmin.types.azure_subscription_scope

        out["subscriptions"] = (
            capo_observabilityadmin.types.azure_subscription_scope.deserialize_json(
                data["Subscriptions"]
            )
        )
    if data.get("Regions") is not None:
        import capo_observabilityadmin.types.azure_region_list

        out["regions"] = (
            capo_observabilityadmin.types.azure_region_list.deserialize_json(
                data["Regions"]
            )
        )
    if data.get("ResourceTypes") is not None:
        import capo_observabilityadmin.types.azure_resource_type_list

        out["resource_types"] = (
            capo_observabilityadmin.types.azure_resource_type_list.deserialize_json(
                data["ResourceTypes"]
            )
        )
    if data.get("TagFilters") is not None:
        import capo_observabilityadmin.types.tag_filter_list

        out["tag_filters"] = (
            capo_observabilityadmin.types.tag_filter_list.deserialize_json(
                data["TagFilters"]
            )
        )
    if data.get("Resources") is not None:
        import capo_observabilityadmin.types.azure_resource_id_scope_list

        out["resources"] = (
            capo_observabilityadmin.types.azure_resource_id_scope_list.deserialize_json(
                data["Resources"]
            )
        )
    return out
