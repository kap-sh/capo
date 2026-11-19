"""Generated from Smithy shape ``com.amazonaws.securityhub#ProviderUpdateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.azure_update_configuration
    import capo_securityhub.types.gcp_update_configuration
    import capo_securityhub.types.jira_cloud_update_configuration
    import capo_securityhub.types.service_now_update_configuration


class ProviderUpdateConfigurationJiraCloudMember(TypedDict, closed=True):
    JiraCloud: "capo_securityhub.types.jira_cloud_update_configuration.JiraCloudUpdateConfiguration"


class ProviderUpdateConfigurationServiceNowMember(TypedDict, closed=True):
    ServiceNow: "capo_securityhub.types.service_now_update_configuration.ServiceNowUpdateConfiguration"


class ProviderUpdateConfigurationAzureMember(TypedDict, closed=True):
    Azure: "capo_securityhub.types.azure_update_configuration.AzureUpdateConfiguration"


class ProviderUpdateConfigurationGCPMember(TypedDict, closed=True):
    GCP: "capo_securityhub.types.gcp_update_configuration.GcpUpdateConfiguration"


ProviderUpdateConfiguration: TypeAlias = (
    ProviderUpdateConfigurationJiraCloudMember
    | ProviderUpdateConfigurationServiceNowMember
    | ProviderUpdateConfigurationAzureMember
    | ProviderUpdateConfigurationGCPMember
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
    elif "GCP" in value:
        import capo_securityhub.types.gcp_update_configuration

        return {
            "GCP": capo_securityhub.types.gcp_update_configuration.serialize_json(
                value["GCP"]
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
    elif data.get("GCP") is not None:
        import capo_securityhub.types.gcp_update_configuration

        return {
            "GCP": capo_securityhub.types.gcp_update_configuration.deserialize_json(
                data["GCP"]
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
