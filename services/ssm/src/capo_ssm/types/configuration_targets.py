"""Generated from Smithy shape ``com.amazonaws.ssm#ConfigurationTargets``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError, SerializationError
from capo_ssm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm.types.azure_subscription_list


class ConfigurationTargetsSubscriptionsMember(TypedDict, closed=True):
    Subscriptions: "capo_ssm.types.azure_subscription_list.AzureSubscriptionList"


ConfigurationTargets: TypeAlias = (
    ConfigurationTargetsSubscriptionsMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationTargets) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConfigurationTargets: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Subscriptions" in value:
        import capo_ssm.types.azure_subscription_list

        return {
            "Subscriptions": capo_ssm.types.azure_subscription_list.serialize_aws_json_1_1(
                value["Subscriptions"]
            )
        }
    else:
        raise SerializationError("ConfigurationTargets: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ConfigurationTargets:
    if data.get("Subscriptions") is not None:
        import capo_ssm.types.azure_subscription_list

        return {
            "Subscriptions": capo_ssm.types.azure_subscription_list.deserialize_aws_json_1_1(
                data["Subscriptions"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ConfigurationTargets: no recognized variant key")
