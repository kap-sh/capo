"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyEndpointEncryptionModeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.endpoint_encryption_mode


class ModifyEndpointEncryptionModeRequest(TypedDict, closed=True):
    directory_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p> The identifier of the directory.</p>"""
    endpoint_encryption_mode: (
        "capo_workspaces.types.endpoint_encryption_mode.EndpointEncryptionMode"
    )
    """<p>The encryption mode used for endpoint connections when streaming to WorkSpaces Personal or WorkSpace Pools.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyEndpointEncryptionModeRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_workspaces.types.endpoint_encryption_mode

    out["EndpointEncryptionMode"] = (
        capo_workspaces.types.endpoint_encryption_mode.serialize_aws_json_1_1(
            value["endpoint_encryption_mode"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyEndpointEncryptionModeRequest:
    out: ModifyEndpointEncryptionModeRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("EndpointEncryptionMode") is not None:
        import capo_workspaces.types.endpoint_encryption_mode

        out["endpoint_encryption_mode"] = (
            capo_workspaces.types.endpoint_encryption_mode.deserialize_aws_json_1_1(
                data["EndpointEncryptionMode"]
            )
        )
    else:
        import typing

        out["endpoint_encryption_mode"] = typing.cast(
            "capo_workspaces.types.endpoint_encryption_mode.EndpointEncryptionMode", ""
        )
    return out
