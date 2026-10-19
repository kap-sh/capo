"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeWorkspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.workspace_encryption_configuration_info
    import capo_iotsitewise.types.workspace_name
    import capo_iotsitewise.types.workspace_status


class DescribeWorkspaceResponse(TypedDict, closed=True):
    workspace_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the workspace.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    workspace_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The description of the workspace.</p>"""
    workspace_status: "capo_iotsitewise.types.workspace_status.WorkspaceStatus"
    """<p>The status of the workspace, which contains the state and any error message.</p>"""
    encryption_configuration: NotRequired[
        "capo_iotsitewise.types.workspace_encryption_configuration_info.WorkspaceEncryptionConfigurationInfo"
    ]
    """<p>The encryption configuration information for the workspace.</p>"""
    created_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the workspace was created, in Unix epoch time.</p>"""
    updated_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the workspace was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceResponse) -> dict:
    out: dict = {}
    out["workspaceArn"] = value["workspace_arn"]
    out["workspaceName"] = value["workspace_name"]
    if "workspace_description" in value:
        out["workspaceDescription"] = value["workspace_description"]
    import capo_iotsitewise.types.workspace_status

    out["workspaceStatus"] = capo_iotsitewise.types.workspace_status.serialize_json(
        value["workspace_status"]
    )
    if "encryption_configuration" in value:
        import capo_iotsitewise.types.workspace_encryption_configuration_info

        out["encryptionConfiguration"] = (
            capo_iotsitewise.types.workspace_encryption_configuration_info.serialize_json(
                value["encryption_configuration"]
            )
        )
    import capo_iotsitewise.types.timestamp

    out["createdAt"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_iotsitewise.types.timestamp

    out["updatedAt"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceResponse:
    out: DescribeWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceArn") is not None:
        out["workspace_arn"] = data["workspaceArn"]
    else:
        out["workspace_arn"] = ""
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("workspaceDescription") is not None:
        out["workspace_description"] = data["workspaceDescription"]
    if data.get("workspaceStatus") is not None:
        import capo_iotsitewise.types.workspace_status

        out["workspace_status"] = (
            capo_iotsitewise.types.workspace_status.deserialize_json(
                data["workspaceStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeWorkspaceResponse.workspace_status required"
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_iotsitewise.types.workspace_encryption_configuration_info

        out["encryption_configuration"] = (
            capo_iotsitewise.types.workspace_encryption_configuration_info.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_iotsitewise.types.timestamp

        out["created_at"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_iotsitewise.types.timestamp

        out["updated_at"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
