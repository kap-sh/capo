"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.tag_map
    import capo_iotsitewise.types.workspace_encryption_configuration
    import capo_iotsitewise.types.workspace_name


class CreateWorkspaceRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace to create.</p>"""
    workspace_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A description for the workspace.</p>"""
    encryption_configuration: "capo_iotsitewise.types.workspace_encryption_configuration.WorkspaceEncryptionConfiguration"
    """<p>The encryption configuration for the workspace.</p>"""
    tags: NotRequired["capo_iotsitewise.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the workspace. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceRequest) -> dict:
    out: dict = {}
    out["workspaceName"] = value["workspace_name"]
    if "workspace_description" in value:
        out["workspaceDescription"] = value["workspace_description"]
    import capo_iotsitewise.types.workspace_encryption_configuration

    out["encryptionConfiguration"] = (
        capo_iotsitewise.types.workspace_encryption_configuration.serialize_json(
            value["encryption_configuration"]
        )
    )
    if "tags" in value:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceRequest:
    out: CreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        raise DeserializationError("CreateWorkspaceRequest.workspace_name required")
    if data.get("workspaceDescription") is not None:
        out["workspace_description"] = data["workspaceDescription"]
    if data.get("encryptionConfiguration") is not None:
        import capo_iotsitewise.types.workspace_encryption_configuration

        out["encryption_configuration"] = (
            capo_iotsitewise.types.workspace_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWorkspaceRequest.encryption_configuration required"
        )
    if data.get("tags") is not None:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
