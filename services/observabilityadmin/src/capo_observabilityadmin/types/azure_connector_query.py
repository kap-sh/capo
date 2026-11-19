"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureConnectorQuery``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_event_hubs_query
    import capo_observabilityadmin.types.azure_management_groups_query
    import capo_observabilityadmin.types.azure_regions_query
    import capo_observabilityadmin.types.azure_resource_ids_query
    import capo_observabilityadmin.types.azure_resource_types_query
    import capo_observabilityadmin.types.azure_subscriptions_query


class AzureConnectorQueryManagementGroupsMember(TypedDict, closed=True):
    ManagementGroups: "capo_observabilityadmin.types.azure_management_groups_query.AzureManagementGroupsQuery"


class AzureConnectorQuerySubscriptionsMember(TypedDict, closed=True):
    Subscriptions: "capo_observabilityadmin.types.azure_subscriptions_query.AzureSubscriptionsQuery"


class AzureConnectorQueryResourceTypesMember(TypedDict, closed=True):
    ResourceTypes: "capo_observabilityadmin.types.azure_resource_types_query.AzureResourceTypesQuery"


class AzureConnectorQueryRegionsMember(TypedDict, closed=True):
    Regions: "capo_observabilityadmin.types.azure_regions_query.AzureRegionsQuery"


class AzureConnectorQueryResourceIdsMember(TypedDict, closed=True):
    ResourceIds: (
        "capo_observabilityadmin.types.azure_resource_ids_query.AzureResourceIdsQuery"
    )


class AzureConnectorQueryEventHubsMember(TypedDict, closed=True):
    EventHubs: (
        "capo_observabilityadmin.types.azure_event_hubs_query.AzureEventHubsQuery"
    )


AzureConnectorQuery: TypeAlias = (
    AzureConnectorQueryManagementGroupsMember
    | AzureConnectorQuerySubscriptionsMember
    | AzureConnectorQueryResourceTypesMember
    | AzureConnectorQueryRegionsMember
    | AzureConnectorQueryResourceIdsMember
    | AzureConnectorQueryEventHubsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AzureConnectorQuery) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AzureConnectorQuery: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ManagementGroups" in value:
        import capo_observabilityadmin.types.azure_management_groups_query

        return {
            "ManagementGroups": capo_observabilityadmin.types.azure_management_groups_query.serialize_json(
                value["ManagementGroups"]
            )
        }
    elif "Subscriptions" in value:
        import capo_observabilityadmin.types.azure_subscriptions_query

        return {
            "Subscriptions": capo_observabilityadmin.types.azure_subscriptions_query.serialize_json(
                value["Subscriptions"]
            )
        }
    elif "ResourceTypes" in value:
        import capo_observabilityadmin.types.azure_resource_types_query

        return {
            "ResourceTypes": capo_observabilityadmin.types.azure_resource_types_query.serialize_json(
                value["ResourceTypes"]
            )
        }
    elif "Regions" in value:
        import capo_observabilityadmin.types.azure_regions_query

        return {
            "Regions": capo_observabilityadmin.types.azure_regions_query.serialize_json(
                value["Regions"]
            )
        }
    elif "ResourceIds" in value:
        import capo_observabilityadmin.types.azure_resource_ids_query

        return {
            "ResourceIds": capo_observabilityadmin.types.azure_resource_ids_query.serialize_json(
                value["ResourceIds"]
            )
        }
    elif "EventHubs" in value:
        import capo_observabilityadmin.types.azure_event_hubs_query

        return {
            "EventHubs": capo_observabilityadmin.types.azure_event_hubs_query.serialize_json(
                value["EventHubs"]
            )
        }
    else:
        raise SerializationError("AzureConnectorQuery: no variant present")


def deserialize_json(data: dict) -> AzureConnectorQuery:
    if data.get("ManagementGroups") is not None:
        import capo_observabilityadmin.types.azure_management_groups_query

        return {
            "ManagementGroups": capo_observabilityadmin.types.azure_management_groups_query.deserialize_json(
                data["ManagementGroups"]
            )
        }
    elif data.get("Subscriptions") is not None:
        import capo_observabilityadmin.types.azure_subscriptions_query

        return {
            "Subscriptions": capo_observabilityadmin.types.azure_subscriptions_query.deserialize_json(
                data["Subscriptions"]
            )
        }
    elif data.get("ResourceTypes") is not None:
        import capo_observabilityadmin.types.azure_resource_types_query

        return {
            "ResourceTypes": capo_observabilityadmin.types.azure_resource_types_query.deserialize_json(
                data["ResourceTypes"]
            )
        }
    elif data.get("Regions") is not None:
        import capo_observabilityadmin.types.azure_regions_query

        return {
            "Regions": capo_observabilityadmin.types.azure_regions_query.deserialize_json(
                data["Regions"]
            )
        }
    elif data.get("ResourceIds") is not None:
        import capo_observabilityadmin.types.azure_resource_ids_query

        return {
            "ResourceIds": capo_observabilityadmin.types.azure_resource_ids_query.deserialize_json(
                data["ResourceIds"]
            )
        }
    elif data.get("EventHubs") is not None:
        import capo_observabilityadmin.types.azure_event_hubs_query

        return {
            "EventHubs": capo_observabilityadmin.types.azure_event_hubs_query.deserialize_json(
                data["EventHubs"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AzureConnectorQuery: no recognized variant key")
