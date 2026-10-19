"""Generated from Smithy shape ``com.amazonaws.devicefarm#InstallToRemoteAccessSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name


class InstallToRemoteAccessSessionRequest(TypedDict, closed=True):
    remote_access_session_arn: (
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.</p>"""
    app_arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the app about which you are requesting information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstallToRemoteAccessSessionRequest) -> dict:
    out: dict = {}
    out["remoteAccessSessionArn"] = value["remote_access_session_arn"]
    out["appArn"] = value["app_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstallToRemoteAccessSessionRequest:
    out: InstallToRemoteAccessSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("remoteAccessSessionArn") is not None:
        out["remote_access_session_arn"] = data["remoteAccessSessionArn"]
    else:
        out["remote_access_session_arn"] = ""
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        out["app_arn"] = ""
    return out
