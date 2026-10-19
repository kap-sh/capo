"""Generated from Smithy shape ``com.amazonaws.ecs#FSxWindowsFileServerVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.f_sx_windows_file_server_authorization_config
    import capo_ecs.types.string


class FSxWindowsFileServerVolumeConfiguration(TypedDict, closed=True):
    file_system_id: "capo_ecs.types.string.String"
    """<p>The Amazon FSx for Windows File Server file system ID to use.</p>"""
    root_directory: "capo_ecs.types.string.String"
    """<p>The directory within the Amazon FSx for Windows File Server file system to mount as the root directory inside the host.</p>"""
    authorization_config: "capo_ecs.types.f_sx_windows_file_server_authorization_config.FSxWindowsFileServerAuthorizationConfig"
    """<p>The authorization configuration details for the Amazon FSx for Windows File Server file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FSxWindowsFileServerVolumeConfiguration) -> dict:
    out: dict = {}
    out["fileSystemId"] = value["file_system_id"]
    out["rootDirectory"] = value["root_directory"]
    import capo_ecs.types.f_sx_windows_file_server_authorization_config

    out["authorizationConfig"] = (
        capo_ecs.types.f_sx_windows_file_server_authorization_config.serialize_aws_json_1_1(
            value["authorization_config"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FSxWindowsFileServerVolumeConfiguration:
    out: FSxWindowsFileServerVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    else:
        out["file_system_id"] = ""
    if data.get("rootDirectory") is not None:
        out["root_directory"] = data["rootDirectory"]
    else:
        out["root_directory"] = ""
    if data.get("authorizationConfig") is not None:
        import capo_ecs.types.f_sx_windows_file_server_authorization_config

        out["authorization_config"] = (
            capo_ecs.types.f_sx_windows_file_server_authorization_config.deserialize_aws_json_1_1(
                data["authorizationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "FSxWindowsFileServerVolumeConfiguration.authorization_config required"
        )
    return out
