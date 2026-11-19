"""Generated from Smithy shape ``com.amazonaws.securityhub#ProviderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.azure_provider_configuration
    import capo_securityhub.types.gcp_provider_configuration
    import capo_securityhub.types.jira_cloud_provider_configuration
    import capo_securityhub.types.service_now_provider_configuration


class ProviderConfigurationJiraCloudMember(TypedDict, closed=True):
    JiraCloud: "capo_securityhub.types.jira_cloud_provider_configuration.JiraCloudProviderConfiguration"


class ProviderConfigurationServiceNowMember(TypedDict, closed=True):
    ServiceNow: "capo_securityhub.types.service_now_provider_configuration.ServiceNowProviderConfiguration"


class ProviderConfigurationAzureMember(TypedDict, closed=True):
    Azure: (
        "capo_securityhub.types.azure_provider_configuration.AzureProviderConfiguration"
    )


class ProviderConfigurationGCPMember(TypedDict, closed=True):
    GCP: "capo_securityhub.types.gcp_provider_configuration.GcpProviderConfiguration"


ProviderConfiguration: TypeAlias = (
    ProviderConfigurationJiraCloudMember
    | ProviderConfigurationServiceNowMember
    | ProviderConfigurationAzureMember
    | ProviderConfigurationGCPMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProviderConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "JiraCloud" in value:
        import capo_securityhub.types.jira_cloud_provider_configuration

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_provider_configuration.serialize_json(
                value["JiraCloud"]
            )
        }
    elif "ServiceNow" in value:
        import capo_securityhub.types.service_now_provider_configuration

        return {
            "ServiceNow": capo_securityhub.types.service_now_provider_configuration.serialize_json(
                value["ServiceNow"]
            )
        }
    elif "Azure" in value:
        import capo_securityhub.types.azure_provider_configuration

        return {
            "Azure": capo_securityhub.types.azure_provider_configuration.serialize_json(
                value["Azure"]
            )
        }
    elif "GCP" in value:
        import capo_securityhub.types.gcp_provider_configuration

        return {
            "GCP": capo_securityhub.types.gcp_provider_configuration.serialize_json(
                value["GCP"]
            )
        }
    else:
        raise SerializationError("ProviderConfiguration: no variant present")


def deserialize_json(data: dict) -> ProviderConfiguration:
    if data.get("JiraCloud") is not None:
        import capo_securityhub.types.jira_cloud_provider_configuration

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_provider_configuration.deserialize_json(
                data["JiraCloud"]
            )
        }
    elif data.get("ServiceNow") is not None:
        import capo_securityhub.types.service_now_provider_configuration

        return {
            "ServiceNow": capo_securityhub.types.service_now_provider_configuration.deserialize_json(
                data["ServiceNow"]
            )
        }
    elif data.get("Azure") is not None:
        import capo_securityhub.types.azure_provider_configuration

        return {
            "Azure": capo_securityhub.types.azure_provider_configuration.deserialize_json(
                data["Azure"]
            )
        }
    elif data.get("GCP") is not None:
        import capo_securityhub.types.gcp_provider_configuration

        return {
            "GCP": capo_securityhub.types.gcp_provider_configuration.deserialize_json(
                data["GCP"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProviderConfiguration: no recognized variant key")
