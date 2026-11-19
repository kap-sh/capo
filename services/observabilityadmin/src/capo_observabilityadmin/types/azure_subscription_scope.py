"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureSubscriptionScope``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.all_subscriptions
    import capo_observabilityadmin.types.azure_subscription_id_list


class AzureSubscriptionScopeAllMember(TypedDict, closed=True):
    All: "capo_observabilityadmin.types.all_subscriptions.AllSubscriptions"


class AzureSubscriptionScopeIdsMember(TypedDict, closed=True):
    Ids: "capo_observabilityadmin.types.azure_subscription_id_list.AzureSubscriptionIdList"


AzureSubscriptionScope: TypeAlias = (
    AzureSubscriptionScopeAllMember
    | AzureSubscriptionScopeIdsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AzureSubscriptionScope) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AzureSubscriptionScope: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "All" in value:
        import capo_observabilityadmin.types.all_subscriptions

        return {
            "All": capo_observabilityadmin.types.all_subscriptions.serialize_json(
                value["All"]
            )
        }
    elif "Ids" in value:
        import capo_observabilityadmin.types.azure_subscription_id_list

        return {
            "Ids": capo_observabilityadmin.types.azure_subscription_id_list.serialize_json(
                value["Ids"]
            )
        }
    else:
        raise SerializationError("AzureSubscriptionScope: no variant present")


def deserialize_json(data: dict) -> AzureSubscriptionScope:
    if data.get("All") is not None:
        import capo_observabilityadmin.types.all_subscriptions

        return {
            "All": capo_observabilityadmin.types.all_subscriptions.deserialize_json(
                data["All"]
            )
        }
    elif data.get("Ids") is not None:
        import capo_observabilityadmin.types.azure_subscription_id_list

        return {
            "Ids": capo_observabilityadmin.types.azure_subscription_id_list.deserialize_json(
                data["Ids"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AzureSubscriptionScope: no recognized variant key")
