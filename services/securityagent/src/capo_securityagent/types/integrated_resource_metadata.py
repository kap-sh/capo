"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResourceMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityagent.types.azure_dev_ops_repository_metadata
    import capo_securityagent.types.bitbucket_repository_metadata
    import capo_securityagent.types.confluence_document_metadata
    import capo_securityagent.types.git_hub_repository_metadata
    import capo_securityagent.types.git_lab_repository_metadata


class _IntegratedResourceMetadata_githubRepository(TypedDict, closed=True):
    githubRepository: (
        "capo_securityagent.types.git_hub_repository_metadata.GitHubRepositoryMetadata"
    )


class _IntegratedResourceMetadata_gitlabRepository(TypedDict, closed=True):
    gitlabRepository: (
        "capo_securityagent.types.git_lab_repository_metadata.GitLabRepositoryMetadata"
    )


class _IntegratedResourceMetadata_bitbucketRepository(TypedDict, closed=True):
    bitbucketRepository: "capo_securityagent.types.bitbucket_repository_metadata.BitbucketRepositoryMetadata"


class _IntegratedResourceMetadata_confluenceDocument(TypedDict, closed=True):
    confluenceDocument: "capo_securityagent.types.confluence_document_metadata.ConfluenceDocumentMetadata"


class _IntegratedResourceMetadata_azureDevOpsRepository(TypedDict, closed=True):
    azureDevOpsRepository: "capo_securityagent.types.azure_dev_ops_repository_metadata.AzureDevOpsRepositoryMetadata"


IntegratedResourceMetadata: TypeAlias = (
    _IntegratedResourceMetadata_githubRepository
    | _IntegratedResourceMetadata_gitlabRepository
    | _IntegratedResourceMetadata_bitbucketRepository
    | _IntegratedResourceMetadata_confluenceDocument
    | _IntegratedResourceMetadata_azureDevOpsRepository
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResourceMetadata) -> dict:
    if "githubRepository" in value:
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
    else:
        raise DeserializationError(
            "IntegratedResourceMetadata: no recognized variant key"
        )
