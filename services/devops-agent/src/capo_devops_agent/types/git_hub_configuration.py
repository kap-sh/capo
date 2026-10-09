"""Generated from Smithy shape ``com.amazonaws.devopsagent#GitHubConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.association_id
    import capo_devops_agent.types.github_repo_owner_type
    import capo_devops_agent.types.role_arn


class GitHubConfiguration(TypedDict, closed=True):
    repo_name: "str"
    """<p>Associated Github repo name</p>"""
    repo_id: "str"
    """<p>Associated Github repo ID</p>"""
    owner: "str"
    """<p>The GitHub repository owner name.</p>"""
    owner_type: "capo_devops_agent.types.github_repo_owner_type.GithubRepoOwnerType"
    instance_identifier: NotRequired["str"]
    """<p>GitHub instance identifier (e.g., github.com or github.enterprise.com)</p>"""
    runtime_role_arn: NotRequired["capo_devops_agent.types.role_arn.RoleArn"]
    """<p>Optional role ARN that AIDevOps assumes at runtime for automatic verification testing and VPC connectivity on this association.</p>"""
    release_management_association_id: NotRequired[
        "capo_devops_agent.types.association_id.AssociationId"
    ]
    """<p>The identifier of the release management association that this repository maps to for automatic verification testing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubConfiguration) -> dict:
    out: dict = {}
    out["repoName"] = value["repo_name"]
    out["repoId"] = value["repo_id"]
    out["owner"] = value["owner"]
    import capo_devops_agent.types.github_repo_owner_type

    out["ownerType"] = capo_devops_agent.types.github_repo_owner_type.serialize_json(
        value["owner_type"]
    )
    if "instance_identifier" in value:
        out["instanceIdentifier"] = value["instance_identifier"]
    if "runtime_role_arn" in value:
        out["runtimeRoleArn"] = value["runtime_role_arn"]
    if "release_management_association_id" in value:
        out["releaseManagementAssociationId"] = value[
            "release_management_association_id"
        ]
    return out


def deserialize_json(data: dict) -> GitHubConfiguration:
    out: GitHubConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("repoName") is not None:
        out["repo_name"] = data["repoName"]
    else:
        raise DeserializationError("GitHubConfiguration.repo_name required")
    if data.get("repoId") is not None:
        out["repo_id"] = data["repoId"]
    else:
        raise DeserializationError("GitHubConfiguration.repo_id required")
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    else:
        raise DeserializationError("GitHubConfiguration.owner required")
    if data.get("ownerType") is not None:
        import capo_devops_agent.types.github_repo_owner_type

        out["owner_type"] = (
            capo_devops_agent.types.github_repo_owner_type.deserialize_json(
                data["ownerType"]
            )
        )
    else:
        raise DeserializationError("GitHubConfiguration.owner_type required")
    if data.get("instanceIdentifier") is not None:
        out["instance_identifier"] = data["instanceIdentifier"]
    if data.get("runtimeRoleArn") is not None:
        out["runtime_role_arn"] = data["runtimeRoleArn"]
    if data.get("releaseManagementAssociationId") is not None:
        out["release_management_association_id"] = data[
            "releaseManagementAssociationId"
        ]
    return out
