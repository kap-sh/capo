"""Generated from Smithy shape ``com.amazonaws.securityhub#ProviderUpdateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.azure_update_configuration
    import capo_securityhub.types.jira_cloud_update_configuration
    import capo_securityhub.types.service_now_update_configuration


class _ProviderUpdateConfiguration_JiraCloud(TypedDict, closed=True):
    JiraCloud: "capo_securityhub.types.jira_cloud_update_configuration.JiraCloudUpdateConfiguration"


class _ProviderUpdateConfiguration_ServiceNow(TypedDict, closed=True):
    ServiceNow: "capo_securityhub.types.service_now_update_configuration.ServiceNowUpdateConfiguration"


class _ProviderUpdateConfiguration_Azure(TypedDict, closed=True):
    Azure: "capo_securityhub.types.azure_update_configuration.AzureUpdateConfiguration"


ProviderUpdateConfiguration: TypeAlias = (
    _ProviderUpdateConfiguration_JiraCloud
    | _ProviderUpdateConfiguration_ServiceNow
    | _ProviderUpdateConfiguration_Azure
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderUpdateConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProviderUpdateConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "JiraCloud" in value:
        import capo_securityhub.types.jira_cloud_update_configuration

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_update_configuration.serialize_json(
                value["JiraCloud"]
            )
        }
    elif "ServiceNow" in value:
        import capo_securityhub.types.service_now_update_configuration

        return {
            "ServiceNow": capo_securityhub.types.service_now_update_configuration.serialize_json(
                value["ServiceNow"]
            )
        }
    elif "Azure" in value:
        import capo_securityhub.types.azure_update_configuration

        return {
            "Azure": capo_securityhub.types.azure_update_configuration.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError("ProviderUpdateConfiguration: no variant present")


def deserialize_json(data: dict) -> ProviderUpdateConfiguration:
    if data.get("JiraCloud") is not None:
        import capo_securityhub.types.jira_cloud_update_configuration

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_update_configuration.deserialize_json(
                data["JiraCloud"]
            )
        }
    elif data.get("ServiceNow") is not None:
        import capo_securityhub.types.service_now_update_configuration

        return {
            "ServiceNow": capo_securityhub.types.service_now_update_configuration.deserialize_json(
                data["ServiceNow"]
            )
        }
    elif data.get("Azure") is not None:
        import capo_securityhub.types.azure_update_configuration

        return {
            "Azure": capo_securityhub.types.azure_update_configuration.deserialize_json(
                data["Azure"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ProviderUpdateConfiguration: no recognized variant key"
        )
