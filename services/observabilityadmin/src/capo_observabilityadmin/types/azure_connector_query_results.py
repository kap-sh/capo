"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureConnectorQueryResults``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_event_hub_summaries
    import capo_observabilityadmin.types.azure_management_group_summaries
    import capo_observabilityadmin.types.azure_region_list
    import capo_observabilityadmin.types.azure_resource_identifier_summaries
    import capo_observabilityadmin.types.azure_resource_type_list
    import capo_observabilityadmin.types.azure_subscription_summaries


class AzureConnectorQueryResultsManagementGroupsMember(TypedDict, closed=True):
    ManagementGroups: "capo_observabilityadmin.types.azure_management_group_summaries.AzureManagementGroupSummaries"


class AzureConnectorQueryResultsSubscriptionsMember(TypedDict, closed=True):
    Subscriptions: "capo_observabilityadmin.types.azure_subscription_summaries.AzureSubscriptionSummaries"


class AzureConnectorQueryResultsResourceTypesMember(TypedDict, closed=True):
    ResourceTypes: (
        "capo_observabilityadmin.types.azure_resource_type_list.AzureResourceTypeList"
    )


class AzureConnectorQueryResultsRegionsMember(TypedDict, closed=True):
    Regions: "capo_observabilityadmin.types.azure_region_list.AzureRegionList"


class AzureConnectorQueryResultsResourceIdsMember(TypedDict, closed=True):
    ResourceIds: "capo_observabilityadmin.types.azure_resource_identifier_summaries.AzureResourceIdentifierSummaries"


class AzureConnectorQueryResultsEventHubsMember(TypedDict, closed=True):
    EventHubs: (
        "capo_observabilityadmin.types.azure_event_hub_summaries.AzureEventHubSummaries"
    )


AzureConnectorQueryResults: TypeAlias = (
    AzureConnectorQueryResultsManagementGroupsMember
    | AzureConnectorQueryResultsSubscriptionsMember
    | AzureConnectorQueryResultsResourceTypesMember
    | AzureConnectorQueryResultsRegionsMember
    | AzureConnectorQueryResultsResourceIdsMember
    | AzureConnectorQueryResultsEventHubsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AzureConnectorQueryResults) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AzureConnectorQueryResults: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ManagementGroups" in value:
        import capo_observabilityadmin.types.azure_management_group_summaries

        return {
            "ManagementGroups": capo_observabilityadmin.types.azure_management_group_summaries.serialize_json(
                value["ManagementGroups"]
            )
        }
    elif "Subscriptions" in value:
        import capo_observabilityadmin.types.azure_subscription_summaries

        return {
            "Subscriptions": capo_observabilityadmin.types.azure_subscription_summaries.serialize_json(
                value["Subscriptions"]
            )
        }
    elif "ResourceTypes" in value:
        import capo_observabilityadmin.types.azure_resource_type_list

        return {
            "ResourceTypes": capo_observabilityadmin.types.azure_resource_type_list.serialize_json(
                value["ResourceTypes"]
            )
        }
    elif "Regions" in value:
        import capo_observabilityadmin.types.azure_region_list

        return {
            "Regions": capo_observabilityadmin.types.azure_region_list.serialize_json(
                value["Regions"]
            )
        }
    elif "ResourceIds" in value:
        import capo_observabilityadmin.types.azure_resource_identifier_summaries

        return {
            "ResourceIds": capo_observabilityadmin.types.azure_resource_identifier_summaries.serialize_json(
                value["ResourceIds"]
            )
        }
    elif "EventHubs" in value:
        import capo_observabilityadmin.types.azure_event_hub_summaries

        return {
            "EventHubs": capo_observabilityadmin.types.azure_event_hub_summaries.serialize_json(
                value["EventHubs"]
            )
        }
    else:
        raise SerializationError("AzureConnectorQueryResults: no variant present")


def deserialize_json(data: dict) -> AzureConnectorQueryResults:
    if data.get("ManagementGroups") is not None:
        import capo_observabilityadmin.types.azure_management_group_summaries

        return {
            "ManagementGroups": capo_observabilityadmin.types.azure_management_group_summaries.deserialize_json(
                data["ManagementGroups"]
            )
        }
    elif data.get("Subscriptions") is not None:
        import capo_observabilityadmin.types.azure_subscription_summaries

        return {
            "Subscriptions": capo_observabilityadmin.types.azure_subscription_summaries.deserialize_json(
                data["Subscriptions"]
            )
        }
    elif data.get("ResourceTypes") is not None:
        import capo_observabilityadmin.types.azure_resource_type_list

        return {
            "ResourceTypes": capo_observabilityadmin.types.azure_resource_type_list.deserialize_json(
                data["ResourceTypes"]
            )
        }
    elif data.get("Regions") is not None:
        import capo_observabilityadmin.types.azure_region_list

        return {
            "Regions": capo_observabilityadmin.types.azure_region_list.deserialize_json(
                data["Regions"]
            )
        }
    elif data.get("ResourceIds") is not None:
        import capo_observabilityadmin.types.azure_resource_identifier_summaries

        return {
            "ResourceIds": capo_observabilityadmin.types.azure_resource_identifier_summaries.deserialize_json(
                data["ResourceIds"]
            )
        }
    elif data.get("EventHubs") is not None:
        import capo_observabilityadmin.types.azure_event_hub_summaries

        return {
            "EventHubs": capo_observabilityadmin.types.azure_event_hub_summaries.deserialize_json(
                data["EventHubs"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AzureConnectorQueryResults: no recognized variant key"
        )
