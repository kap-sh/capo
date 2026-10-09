"""Generated from Smithy shape ``com.amazonaws.devopsagent#GitLabConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.association_id
    import capo_devops_agent.types.role_arn


class GitLabConfiguration(TypedDict, closed=True):
    project_id: "str"
    """<p>GitLab numeric project ID.</p>"""
    project_path: "str"
    """<p>Full GitLab project path (e.g., namespace/project-name).</p>"""
    instance_identifier: NotRequired["str"]
    """<p>GitLab instance identifier (e.g., gitlab.com or e2e.gamma.dev.us-east-1.gitlab.falco.ai.aws.dev)</p>"""
    runtime_role_arn: NotRequired["capo_devops_agent.types.role_arn.RoleArn"]
    """<p>Optional role ARN that AIDevOps assumes at runtime for automatic verification testing and VPC connectivity on this association.</p>"""
    release_management_association_id: NotRequired[
        "capo_devops_agent.types.association_id.AssociationId"
    ]
    """<p>The identifier of the release management association that this project maps to for automatic verification testing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabConfiguration) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    out["projectPath"] = value["project_path"]
    if "instance_identifier" in value:
        out["instanceIdentifier"] = value["instance_identifier"]
    if "runtime_role_arn" in value:
        out["runtimeRoleArn"] = value["runtime_role_arn"]
    if "release_management_association_id" in value:
        out["releaseManagementAssociationId"] = value[
            "release_management_association_id"
        ]
    return out


def deserialize_json(data: dict) -> GitLabConfiguration:
    out: GitLabConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("GitLabConfiguration.project_id required")
    if data.get("projectPath") is not None:
        out["project_path"] = data["projectPath"]
    else:
        raise DeserializationError("GitLabConfiguration.project_path required")
    if data.get("instanceIdentifier") is not None:
        out["instance_identifier"] = data["instanceIdentifier"]
    if data.get("runtimeRoleArn") is not None:
        out["runtime_role_arn"] = data["runtimeRoleArn"]
    if data.get("releaseManagementAssociationId") is not None:
        out["release_management_association_id"] = data[
            "releaseManagementAssociationId"
        ]
    return out
