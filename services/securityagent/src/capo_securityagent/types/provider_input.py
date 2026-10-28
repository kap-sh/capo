"""Generated from Smithy shape ``com.amazonaws.securityagent#ProviderInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError
from capo_securityagent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityagent.types.azure_dev_ops_integration_input
    import capo_securityagent.types.bitbucket_data_center_integration_input
    import capo_securityagent.types.bitbucket_integration_input
    import capo_securityagent.types.confluence_integration_input
    import capo_securityagent.types.git_hub_integration_input
    import capo_securityagent.types.git_lab_integration_input
    import capo_securityagent.types.jira_integration_input


class ProviderInputGithubMember(TypedDict, closed=True):
    github: "capo_securityagent.types.git_hub_integration_input.GitHubIntegrationInput"


class ProviderInputGitlabMember(TypedDict, closed=True):
    gitlab: "capo_securityagent.types.git_lab_integration_input.GitLabIntegrationInput"


class ProviderInputBitbucketMember(TypedDict, closed=True):
    bitbucket: (
        "capo_securityagent.types.bitbucket_integration_input.BitbucketIntegrationInput"
    )


class ProviderInputConfluenceMember(TypedDict, closed=True):
    confluence: "capo_securityagent.types.confluence_integration_input.ConfluenceIntegrationInput"


class ProviderInputAzureDevOpsMember(TypedDict, closed=True):
    azureDevOps: "capo_securityagent.types.azure_dev_ops_integration_input.AzureDevOpsIntegrationInput"


class ProviderInputBitbucketDataCenterMember(TypedDict, closed=True):
    bitbucketDataCenter: "capo_securityagent.types.bitbucket_data_center_integration_input.BitbucketDataCenterIntegrationInput"


class ProviderInputJiraMember(TypedDict, closed=True):
    jira: "capo_securityagent.types.jira_integration_input.JiraIntegrationInput"


ProviderInput: TypeAlias = (
    ProviderInputGithubMember
    | ProviderInputGitlabMember
    | ProviderInputBitbucketMember
    | ProviderInputConfluenceMember
    | ProviderInputAzureDevOpsMember
    | ProviderInputBitbucketDataCenterMember
    | ProviderInputJiraMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProviderInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "github" in value:
        import capo_securityagent.types.git_hub_integration_input

        return {
            "github": capo_securityagent.types.git_hub_integration_input.serialize_json(
                value["github"]
            )
        }
    elif "gitlab" in value:
        import capo_securityagent.types.git_lab_integration_input

        return {
            "gitlab": capo_securityagent.types.git_lab_integration_input.serialize_json(
                value["gitlab"]
            )
        }
    elif "bitbucket" in value:
        import capo_securityagent.types.bitbucket_integration_input

        return {
            "bitbucket": capo_securityagent.types.bitbucket_integration_input.serialize_json(
                value["bitbucket"]
            )
        }
    elif "confluence" in value:
        import capo_securityagent.types.confluence_integration_input

        return {
            "confluence": capo_securityagent.types.confluence_integration_input.serialize_json(
                value["confluence"]
            )
        }
    elif "azureDevOps" in value:
        import capo_securityagent.types.azure_dev_ops_integration_input

        return {
            "azureDevOps": capo_securityagent.types.azure_dev_ops_integration_input.serialize_json(
                value["azureDevOps"]
            )
        }
    elif "bitbucketDataCenter" in value:
        import capo_securityagent.types.bitbucket_data_center_integration_input

        return {
            "bitbucketDataCenter": capo_securityagent.types.bitbucket_data_center_integration_input.serialize_json(
                value["bitbucketDataCenter"]
            )
        }
    elif "jira" in value:
        import capo_securityagent.types.jira_integration_input

        return {
            "jira": capo_securityagent.types.jira_integration_input.serialize_json(
                value["jira"]
            )
        }
    else:
        raise SerializationError("ProviderInput: no variant present")


def deserialize_json(data: dict) -> ProviderInput:
    if data.get("github") is not None:
        import capo_securityagent.types.git_hub_integration_input

        return {
            "github": capo_securityagent.types.git_hub_integration_input.deserialize_json(
                data["github"]
            )
        }
    elif data.get("gitlab") is not None:
        import capo_securityagent.types.git_lab_integration_input

        return {
            "gitlab": capo_securityagent.types.git_lab_integration_input.deserialize_json(
                data["gitlab"]
            )
        }
    elif data.get("bitbucket") is not None:
        import capo_securityagent.types.bitbucket_integration_input

        return {
            "bitbucket": capo_securityagent.types.bitbucket_integration_input.deserialize_json(
                data["bitbucket"]
            )
        }
    elif data.get("confluence") is not None:
        import capo_securityagent.types.confluence_integration_input

        return {
            "confluence": capo_securityagent.types.confluence_integration_input.deserialize_json(
                data["confluence"]
            )
        }
    elif data.get("azureDevOps") is not None:
        import capo_securityagent.types.azure_dev_ops_integration_input

        return {
            "azureDevOps": capo_securityagent.types.azure_dev_ops_integration_input.deserialize_json(
                data["azureDevOps"]
            )
        }
    elif data.get("bitbucketDataCenter") is not None:
        import capo_securityagent.types.bitbucket_data_center_integration_input

        return {
            "bitbucketDataCenter": capo_securityagent.types.bitbucket_data_center_integration_input.deserialize_json(
                data["bitbucketDataCenter"]
            )
        }
    elif data.get("jira") is not None:
        import capo_securityagent.types.jira_integration_input

        return {
            "jira": capo_securityagent.types.jira_integration_input.deserialize_json(
                data["jira"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProviderInput: no recognized variant key")


def redact_sensitive(value: ProviderInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "gitlab" in value:
        import capo_securityagent.types.git_lab_integration_input

        out["gitlab"] = (
            capo_securityagent.types.git_lab_integration_input.redact_sensitive(
                value["gitlab"]
            )
        )
    return out
