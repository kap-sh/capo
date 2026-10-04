"""Generated from Smithy shape ``com.amazonaws.securityagent#ProviderResourceCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityagent.types.azure_dev_ops_resource_capabilities
    import capo_securityagent.types.bitbucket_resource_capabilities
    import capo_securityagent.types.confluence_resource_capabilities
    import capo_securityagent.types.git_hub_resource_capabilities
    import capo_securityagent.types.git_lab_resource_capabilities


class _ProviderResourceCapabilities_github(TypedDict, closed=True):
    github: "capo_securityagent.types.git_hub_resource_capabilities.GitHubResourceCapabilities"


class _ProviderResourceCapabilities_gitlab(TypedDict, closed=True):
    gitlab: "capo_securityagent.types.git_lab_resource_capabilities.GitLabResourceCapabilities"


class _ProviderResourceCapabilities_bitbucket(TypedDict, closed=True):
    bitbucket: "capo_securityagent.types.bitbucket_resource_capabilities.BitbucketResourceCapabilities"


class _ProviderResourceCapabilities_confluence(TypedDict, closed=True):
    confluence: "capo_securityagent.types.confluence_resource_capabilities.ConfluenceResourceCapabilities"


class _ProviderResourceCapabilities_azureDevOps(TypedDict, closed=True):
    azureDevOps: "capo_securityagent.types.azure_dev_ops_resource_capabilities.AzureDevOpsResourceCapabilities"


ProviderResourceCapabilities: TypeAlias = (
    _ProviderResourceCapabilities_github
    | _ProviderResourceCapabilities_gitlab
    | _ProviderResourceCapabilities_bitbucket
    | _ProviderResourceCapabilities_confluence
    | _ProviderResourceCapabilities_azureDevOps
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderResourceCapabilities) -> dict:
    if "github" in value:
        import capo_securityagent.types.git_hub_resource_capabilities

        return {
            "github": capo_securityagent.types.git_hub_resource_capabilities.serialize_json(
                value["github"]
            )
        }
    elif "gitlab" in value:
        import capo_securityagent.types.git_lab_resource_capabilities

        return {
            "gitlab": capo_securityagent.types.git_lab_resource_capabilities.serialize_json(
                value["gitlab"]
            )
        }
    elif "bitbucket" in value:
        import capo_securityagent.types.bitbucket_resource_capabilities

        return {
            "bitbucket": capo_securityagent.types.bitbucket_resource_capabilities.serialize_json(
                value["bitbucket"]
            )
        }
    elif "confluence" in value:
        import capo_securityagent.types.confluence_resource_capabilities

        return {
            "confluence": capo_securityagent.types.confluence_resource_capabilities.serialize_json(
                value["confluence"]
            )
        }
    elif "azureDevOps" in value:
        import capo_securityagent.types.azure_dev_ops_resource_capabilities

        return {
            "azureDevOps": capo_securityagent.types.azure_dev_ops_resource_capabilities.serialize_json(
                value["azureDevOps"]
            )
        }
    else:
        raise SerializationError("ProviderResourceCapabilities: no variant present")


def deserialize_json(data: dict) -> ProviderResourceCapabilities:
    if data.get("github") is not None:
        import capo_securityagent.types.git_hub_resource_capabilities

        return {
            "github": capo_securityagent.types.git_hub_resource_capabilities.deserialize_json(
                data["github"]
            )
        }
    elif data.get("gitlab") is not None:
        import capo_securityagent.types.git_lab_resource_capabilities

        return {
            "gitlab": capo_securityagent.types.git_lab_resource_capabilities.deserialize_json(
                data["gitlab"]
            )
        }
    elif data.get("bitbucket") is not None:
        import capo_securityagent.types.bitbucket_resource_capabilities

        return {
            "bitbucket": capo_securityagent.types.bitbucket_resource_capabilities.deserialize_json(
                data["bitbucket"]
            )
        }
    elif data.get("confluence") is not None:
        import capo_securityagent.types.confluence_resource_capabilities

        return {
            "confluence": capo_securityagent.types.confluence_resource_capabilities.deserialize_json(
                data["confluence"]
            )
        }
    elif data.get("azureDevOps") is not None:
        import capo_securityagent.types.azure_dev_ops_resource_capabilities

        return {
            "azureDevOps": capo_securityagent.types.azure_dev_ops_resource_capabilities.deserialize_json(
                data["azureDevOps"]
            )
        }
    else:
        raise DeserializationError(
            "ProviderResourceCapabilities: no recognized variant key"
        )
