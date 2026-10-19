"""Generated from Smithy shape ``com.amazonaws.datazone#GitPropertiesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.connection_status


class GitPropertiesOutput(TypedDict, closed=True):
    code_connection_arn: "str"
    """<p>The ARN of the CodeConnections connection used to connect to the Git repository.</p>"""
    repository_id: "str"
    """<p>The ID of the Git repository. This is the owner and repository name, for example, owner/repo-name.</p>"""
    default_branch: "str"
    """<p>The default branch of the Git repository.</p>"""
    status: NotRequired["capo_datazone.types.connection_status.ConnectionStatus"]
    """<p>The status of the Git connection.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message that describes why the Git connection failed. This member is populated when the connection status is CREATE_FAILED or UPDATE_FAILED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitPropertiesOutput) -> dict:
    out: dict = {}
    out["codeConnectionArn"] = value["code_connection_arn"]
    out["repositoryId"] = value["repository_id"]
    out["defaultBranch"] = value["default_branch"]
    if "status" in value:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.serialize_json(
            value["status"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> GitPropertiesOutput:
    out: GitPropertiesOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("status") is not None:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
