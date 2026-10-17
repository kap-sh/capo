"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityagent.types.azure_dev_ops_repository_resource
    import capo_securityagent.types.bitbucket_repository_resource
    import capo_securityagent.types.confluence_document_resource
    import capo_securityagent.types.git_hub_repository_resource
    import capo_securityagent.types.git_lab_repository_resource


class _IntegratedResource_githubRepository(TypedDict, closed=True):
    githubRepository: (
        "capo_securityagent.types.git_hub_repository_resource.GitHubRepositoryResource"
    )


class _IntegratedResource_gitlabRepository(TypedDict, closed=True):
    gitlabRepository: (
        "capo_securityagent.types.git_lab_repository_resource.GitLabRepositoryResource"
    )


class _IntegratedResource_bitbucketRepository(TypedDict, closed=True):
    bitbucketRepository: "capo_securityagent.types.bitbucket_repository_resource.BitbucketRepositoryResource"


class _IntegratedResource_confluenceDocument(TypedDict, closed=True):
    confluenceDocument: "capo_securityagent.types.confluence_document_resource.ConfluenceDocumentResource"


class _IntegratedResource_azureDevOpsRepository(TypedDict, closed=True):
    azureDevOpsRepository: "capo_securityagent.types.azure_dev_ops_repository_resource.AzureDevOpsRepositoryResource"


IntegratedResource: TypeAlias = (
    _IntegratedResource_githubRepository
    | _IntegratedResource_gitlabRepository
    | _IntegratedResource_bitbucketRepository
    | _IntegratedResource_confluenceDocument
    | _IntegratedResource_azureDevOpsRepository
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResource) -> dict:
    if "githubRepository" in value:
        import capo_securityagent.types.git_hub_repository_resource

        return {
            "githubRepository": capo_securityagent.types.git_hub_repository_resource.serialize_json(
                value["githubRepository"]
            )
        }
    elif "gitlabRepository" in value:
        import capo_securityagent.types.git_lab_repository_resource

        return {
            "gitlabRepository": capo_securityagent.types.git_lab_repository_resource.serialize_json(
                value["gitlabRepository"]
            )
        }
    elif "bitbucketRepository" in value:
        import capo_securityagent.types.bitbucket_repository_resource

        return {
            "bitbucketRepository": capo_securityagent.types.bitbucket_repository_resource.serialize_json(
                value["bitbucketRepository"]
            )
        }
    elif "confluenceDocument" in value:
        import capo_securityagent.types.confluence_document_resource

        return {
            "confluenceDocument": capo_securityagent.types.confluence_document_resource.serialize_json(
                value["confluenceDocument"]
            )
        }
    elif "azureDevOpsRepository" in value:
        import capo_securityagent.types.azure_dev_ops_repository_resource

        return {
            "azureDevOpsRepository": capo_securityagent.types.azure_dev_ops_repository_resource.serialize_json(
                value["azureDevOpsRepository"]
            )
        }
    else:
        raise SerializationError("IntegratedResource: no variant present")


def deserialize_json(data: dict) -> IntegratedResource:
    if data.get("githubRepository") is not None:
        import capo_securityagent.types.git_hub_repository_resource

        return {
            "githubRepository": capo_securityagent.types.git_hub_repository_resource.deserialize_json(
                data["githubRepository"]
            )
        }
    elif data.get("gitlabRepository") is not None:
        import capo_securityagent.types.git_lab_repository_resource

        return {
            "gitlabRepository": capo_securityagent.types.git_lab_repository_resource.deserialize_json(
                data["gitlabRepository"]
            )
        }
    elif data.get("bitbucketRepository") is not None:
        import capo_securityagent.types.bitbucket_repository_resource

        return {
            "bitbucketRepository": capo_securityagent.types.bitbucket_repository_resource.deserialize_json(
                data["bitbucketRepository"]
            )
        }
    elif data.get("confluenceDocument") is not None:
        import capo_securityagent.types.confluence_document_resource

        return {
            "confluenceDocument": capo_securityagent.types.confluence_document_resource.deserialize_json(
                data["confluenceDocument"]
            )
        }
    elif data.get("azureDevOpsRepository") is not None:
        import capo_securityagent.types.azure_dev_ops_repository_resource

        return {
            "azureDevOpsRepository": capo_securityagent.types.azure_dev_ops_repository_resource.deserialize_json(
                data["azureDevOpsRepository"]
            )
        }
    else:
        raise DeserializationError("IntegratedResource: no recognized variant key")
