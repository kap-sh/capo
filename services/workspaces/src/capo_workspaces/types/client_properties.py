"""Generated from Smithy shape ``com.amazonaws.workspaces#ClientProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.client_experience_policy
    import capo_workspaces.types.log_upload_enum
    import capo_workspaces.types.reconnect_enum


class ClientProperties(TypedDict, closed=True):
    reconnect_enabled: NotRequired["capo_workspaces.types.reconnect_enum.ReconnectEnum"]
    """<p>Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When enabled, users can choose to reconnect to their WorkSpaces without re-entering their credentials. </p>"""
    log_upload_enabled: NotRequired[
        "capo_workspaces.types.log_upload_enum.LogUploadEnum"
    ]
    """<p>Specifies whether users can upload diagnostic log files of Amazon WorkSpaces client directly to WorkSpaces to troubleshoot issues when using the WorkSpaces client. When enabled, the log files will be sent to WorkSpaces automatically and will be applied to all users in the specified directory.</p>"""
    client_experience_policy: NotRequired[
        "capo_workspaces.types.client_experience_policy.ClientExperiencePolicy"
    ]
    """<p>The client experience policy that determines which client experience the user sees. Administrators can set this policy to control the client experience for users in a directory. Valid values include <code>FORCE_CLASSIC</code>, <code>FORCE_UI_2026</code>, and <code>USER_CHOICE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientProperties) -> dict:
    out: dict = {}
    if "reconnect_enabled" in value:
        import capo_workspaces.types.reconnect_enum

        out["ReconnectEnabled"] = (
            capo_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["reconnect_enabled"]
            )
        )
    if "log_upload_enabled" in value:
        import capo_workspaces.types.log_upload_enum

        out["LogUploadEnabled"] = (
            capo_workspaces.types.log_upload_enum.serialize_aws_json_1_1(
                value["log_upload_enabled"]
            )
        )
    if "client_experience_policy" in value:
        out["ClientExperiencePolicy"] = value["client_experience_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientProperties:
    out: ClientProperties = {}  # type: ignore[typeddict-item]
    if data.get("ReconnectEnabled") is not None:
        import capo_workspaces.types.reconnect_enum

        out["reconnect_enabled"] = (
            capo_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["ReconnectEnabled"]
            )
        )
    if data.get("LogUploadEnabled") is not None:
        import capo_workspaces.types.log_upload_enum

        out["log_upload_enabled"] = (
            capo_workspaces.types.log_upload_enum.deserialize_aws_json_1_1(
                data["LogUploadEnabled"]
            )
        )
    if data.get("ClientExperiencePolicy") is not None:
        out["client_experience_policy"] = data["ClientExperiencePolicy"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClientProperties) -> dict:
    out: dict = {}
    if "reconnect_enabled" in value:
        import capo_workspaces.types.reconnect_enum

        out["ReconnectEnabled"] = capo_workspaces.types.reconnect_enum.serialize_cbor(
            value["reconnect_enabled"]
        )
    if "log_upload_enabled" in value:
        import capo_workspaces.types.log_upload_enum

        out["LogUploadEnabled"] = capo_workspaces.types.log_upload_enum.serialize_cbor(
            value["log_upload_enabled"]
        )
    if "client_experience_policy" in value:
        out["ClientExperiencePolicy"] = value["client_experience_policy"]
    return out


def deserialize_cbor(data: dict) -> ClientProperties:
    out: ClientProperties = {}  # type: ignore[typeddict-item]
    if data.get("ReconnectEnabled") is not None:
        import capo_workspaces.types.reconnect_enum

        out["reconnect_enabled"] = (
            capo_workspaces.types.reconnect_enum.deserialize_cbor(
                data["ReconnectEnabled"]
            )
        )
    if data.get("LogUploadEnabled") is not None:
        import capo_workspaces.types.log_upload_enum

        out["log_upload_enabled"] = (
            capo_workspaces.types.log_upload_enum.deserialize_cbor(
                data["LogUploadEnabled"]
            )
        )
    if data.get("ClientExperiencePolicy") is not None:
        out["client_experience_policy"] = data["ClientExperiencePolicy"]
    return out
