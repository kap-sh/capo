"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResourceMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError
from capo_securityagent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityagent.types.azure_dev_ops_repository_metadata
    import capo_securityagent.types.bitbucket_repository_metadata
    import capo_securityagent.types.confluence_document_metadata
    import capo_securityagent.types.git_hub_repository_metadata
    import capo_securityagent.types.git_lab_repository_metadata
    import capo_securityagent.types.jira_project_metadata


class IntegratedResourceMetadataGithubRepositoryMember(TypedDict, closed=True):
    githubRepository: (
        "capo_securityagent.types.git_hub_repository_metadata.GitHubRepositoryMetadata"
    )


class IntegratedResourceMetadataGitlabRepositoryMember(TypedDict, closed=True):
    gitlabRepository: (
        "capo_securityagent.types.git_lab_repository_metadata.GitLabRepositoryMetadata"
    )


class IntegratedResourceMetadataBitbucketRepositoryMember(TypedDict, closed=True):
    bitbucketRepository: "capo_securityagent.types.bitbucket_repository_metadata.BitbucketRepositoryMetadata"


class IntegratedResourceMetadataConfluenceDocumentMember(TypedDict, closed=True):
    confluenceDocument: "capo_securityagent.types.confluence_document_metadata.ConfluenceDocumentMetadata"


class IntegratedResourceMetadataAzureDevOpsRepositoryMember(TypedDict, closed=True):
    azureDevOpsRepository: "capo_securityagent.types.azure_dev_ops_repository_metadata.AzureDevOpsRepositoryMetadata"


class IntegratedResourceMetadataJiraProjectMember(TypedDict, closed=True):
    jiraProject: "capo_securityagent.types.jira_project_metadata.JiraProjectMetadata"


IntegratedResourceMetadata: TypeAlias = (
    IntegratedResourceMetadataGithubRepositoryMember
    | IntegratedResourceMetadataGitlabRepositoryMember
    | IntegratedResourceMetadataBitbucketRepositoryMember
    | IntegratedResourceMetadataConfluenceDocumentMember
    | IntegratedResourceMetadataAzureDevOpsRepositoryMember
    | IntegratedResourceMetadataJiraProjectMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResourceMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IntegratedResourceMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "githubRepository" in value:
        import capo_securityagent.types.git_hub_repository_metadata

        return {
            "githubRepository": capo_securityagent.types.git_hub_repository_metadata.serialize_json(
                value["githubRepository"]
            )
        }
    elif "gitlabRepository" in value:
        import capo_securityagent.types.git_lab_repository_metadata

        return {
            "gitlabRepository": capo_securityagent.types.git_lab_repository_metadata.serialize_json(
                value["gitlabRepository"]
            )
        }
    elif "bitbucketRepository" in value:
        import capo_securityagent.types.bitbucket_repository_metadata

        return {
            "bitbucketRepository": capo_securityagent.types.bitbucket_repository_metadata.serialize_json(
                value["bitbucketRepository"]
            )
        }
    elif "confluenceDocument" in value:
        import capo_securityagent.types.confluence_document_metadata

        return {
            "confluenceDocument": capo_securityagent.types.confluence_document_metadata.serialize_json(
                value["confluenceDocument"]
            )
        }
    elif "azureDevOpsRepository" in value:
        import capo_securityagent.types.azure_dev_ops_repository_metadata

        return {
            "azureDevOpsRepository": capo_securityagent.types.azure_dev_ops_repository_metadata.serialize_json(
                value["azureDevOpsRepository"]
            )
        }
    elif "jiraProject" in value:
        import capo_securityagent.types.jira_project_metadata

        return {
            "jiraProject": capo_securityagent.types.jira_project_metadata.serialize_json(
                value["jiraProject"]
            )
        }
    else:
        raise SerializationError("IntegratedResourceMetadata: no variant present")


def deserialize_json(data: dict) -> IntegratedResourceMetadata:
    if data.get("githubRepository") is not None:
        import capo_securityagent.types.git_hub_repository_metadata

        return {
            "githubRepository": capo_securityagent.types.git_hub_repository_metadata.deserialize_json(
                data["githubRepository"]
            )
        }
    elif data.get("gitlabRepository") is not None:
        import capo_securityagent.types.git_lab_repository_metadata

        return {
            "gitlabRepository": capo_securityagent.types.git_lab_repository_metadata.deserialize_json(
                data["gitlabRepository"]
            )
        }
    elif data.get("bitbucketRepository") is not None:
        import capo_securityagent.types.bitbucket_repository_metadata

        return {
            "bitbucketRepository": capo_securityagent.types.bitbucket_repository_metadata.deserialize_json(
                data["bitbucketRepository"]
            )
        }
    elif data.get("confluenceDocument") is not None:
        import capo_securityagent.types.confluence_document_metadata

        return {
            "confluenceDocument": capo_securityagent.types.confluence_document_metadata.deserialize_json(
                data["confluenceDocument"]
            )
        }
    elif data.get("azureDevOpsRepository") is not None:
        import capo_securityagent.types.azure_dev_ops_repository_metadata

        return {
            "azureDevOpsRepository": capo_securityagent.types.azure_dev_ops_repository_metadata.deserialize_json(
                data["azureDevOpsRepository"]
            )
        }
    elif data.get("jiraProject") is not None:
        import capo_securityagent.types.jira_project_metadata

        return {
            "jiraProject": capo_securityagent.types.jira_project_metadata.deserialize_json(
                data["jiraProject"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "IntegratedResourceMetadata: no recognized variant key"
        )
