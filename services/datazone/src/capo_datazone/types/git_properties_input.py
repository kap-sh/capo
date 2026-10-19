"""Generated from Smithy shape ``com.amazonaws.datazone#GitPropertiesInput``."""

from typing_extensions import TypedDict


class GitPropertiesInput(TypedDict, closed=True):
    code_connection_arn: "str"
    """<p>The ARN of the CodeConnections connection used to connect to the Git repository.</p>"""
    repository_id: "str"
    """<p>The ID of the Git repository. This is the owner and repository name, for example, owner/repo-name.</p>"""
    default_branch: "str"
    """<p>The default branch of the Git repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitPropertiesInput) -> dict:
    out: dict = {}
    out["codeConnectionArn"] = value["code_connection_arn"]
    out["repositoryId"] = value["repository_id"]
    out["defaultBranch"] = value["default_branch"]
    return out


def deserialize_json(data: dict) -> GitPropertiesInput:
    out: GitPropertiesInput = {}  # type: ignore[typeddict-item]
    if data.get("codeConnectionArn") is not None:
        out["code_connection_arn"] = data["codeConnectionArn"]
    else:
        out["code_connection_arn"] = ""
    if data.get("repositoryId") is not None:
        out["repository_id"] = data["repositoryId"]
    else:
        out["repository_id"] = ""
    if data.get("defaultBranch") is not None:
        out["default_branch"] = data["defaultBranch"]
    else:
        out["default_branch"] = ""
    return out
