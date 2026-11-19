"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderAgentAccessConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.agent_access_setting_list
    import capo_appstream.types.boolean_object
    import capo_appstream.types.s3_bucket_arn
    import capo_appstream.types.screen_image_format
    import capo_appstream.types.screen_resolution
    import capo_appstream.types.user_control_mode


class ImageBuilderAgentAccessConfig(TypedDict, closed=True):
    settings: NotRequired[
        "capo_appstream.types.agent_access_setting_list.AgentAccessSettingList"
    ]
    """<p>The list of agent access settings that define permissions for each agent action. You must specify at least one setting, and at least one agent action must be enabled.</p>"""
    s3_bucket_arn: NotRequired["capo_appstream.types.s3_bucket_arn.S3BucketArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 bucket where agent screenshots are stored. Required when ScreenshotsUploadEnabled is true.</p>"""
    screenshots_upload_enabled: NotRequired[
        "capo_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Specifies whether screenshot uploads to Amazon S3 are enabled for agent sessions.</p>"""
    screen_resolution: NotRequired[
        "capo_appstream.types.screen_resolution.ScreenResolution"
    ]
    """<p>The screen resolution for the agent streaming environment.</p> <ul> <li> <p>W_1280xH_720 - 1280 x 720 pixels.</p> </li> </ul>"""
    screen_image_format: NotRequired[
        "capo_appstream.types.screen_image_format.ScreenImageFormat"
    ]
    """<p>The image format for agent screen captures.</p> <ul> <li> <p>PNG - PNG format.</p> </li> <li> <p>JPEG - JPEG format.</p> </li> </ul>"""
    user_control_mode: NotRequired[
        "capo_appstream.types.user_control_mode.UserControlMode"
    ]
    """<p>The user control mode for agent sessions. This setting determines how users can interact with agent sessions.</p> <ul> <li> <p>VIEW_ONLY - Users can view and observe agent actions as they happen.</p> </li> <li> <p>VIEW_STOP - Users can view agent actions and stop the agent if needed.</p> </li> <li> <p>DISABLED - Users cannot view or stop the agent session.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilderAgentAccessConfig) -> dict:
    out: dict = {}
    if "settings" in value:
        import capo_appstream.types.agent_access_setting_list

        out["Settings"] = (
            capo_appstream.types.agent_access_setting_list.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "s3_bucket_arn" in value:
        out["S3BucketArn"] = value["s3_bucket_arn"]
    if "screenshots_upload_enabled" in value:
        out["ScreenshotsUploadEnabled"] = value["screenshots_upload_enabled"]
    if "screen_resolution" in value:
        import capo_appstream.types.screen_resolution

        out["ScreenResolution"] = (
            capo_appstream.types.screen_resolution.serialize_aws_json_1_1(
                value["screen_resolution"]
            )
        )
    if "screen_image_format" in value:
        import capo_appstream.types.screen_image_format

        out["ScreenImageFormat"] = (
            capo_appstream.types.screen_image_format.serialize_aws_json_1_1(
                value["screen_image_format"]
            )
        )
    if "user_control_mode" in value:
        import capo_appstream.types.user_control_mode

        out["UserControlMode"] = (
            capo_appstream.types.user_control_mode.serialize_aws_json_1_1(
                value["user_control_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageBuilderAgentAccessConfig:
    out: ImageBuilderAgentAccessConfig = {}  # type: ignore[typeddict-item]
    if data.get("Settings") is not None:
        import capo_appstream.types.agent_access_setting_list

        out["settings"] = (
            capo_appstream.types.agent_access_setting_list.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if data.get("S3BucketArn") is not None:
        out["s3_bucket_arn"] = data["S3BucketArn"]
    if data.get("ScreenshotsUploadEnabled") is not None:
        out["screenshots_upload_enabled"] = data["ScreenshotsUploadEnabled"]
    if data.get("ScreenResolution") is not None:
        import capo_appstream.types.screen_resolution

        out["screen_resolution"] = (
            capo_appstream.types.screen_resolution.deserialize_aws_json_1_1(
                data["ScreenResolution"]
            )
        )
    if data.get("ScreenImageFormat") is not None:
        import capo_appstream.types.screen_image_format

        out["screen_image_format"] = (
            capo_appstream.types.screen_image_format.deserialize_aws_json_1_1(
                data["ScreenImageFormat"]
            )
        )
    if data.get("UserControlMode") is not None:
        import capo_appstream.types.user_control_mode

        out["user_control_mode"] = (
            capo_appstream.types.user_control_mode.deserialize_aws_json_1_1(
                data["UserControlMode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageBuilderAgentAccessConfig) -> dict:
    out: dict = {}
    if "settings" in value:
        import capo_appstream.types.agent_access_setting_list

        out["Settings"] = capo_appstream.types.agent_access_setting_list.serialize_cbor(
            value["settings"]
        )
    if "s3_bucket_arn" in value:
        out["S3BucketArn"] = value["s3_bucket_arn"]
    if "screenshots_upload_enabled" in value:
        out["ScreenshotsUploadEnabled"] = value["screenshots_upload_enabled"]
    if "screen_resolution" in value:
        import capo_appstream.types.screen_resolution

        out["ScreenResolution"] = capo_appstream.types.screen_resolution.serialize_cbor(
            value["screen_resolution"]
        )
    if "screen_image_format" in value:
        import capo_appstream.types.screen_image_format

        out["ScreenImageFormat"] = (
            capo_appstream.types.screen_image_format.serialize_cbor(
                value["screen_image_format"]
            )
        )
    if "user_control_mode" in value:
        import capo_appstream.types.user_control_mode

        out["UserControlMode"] = capo_appstream.types.user_control_mode.serialize_cbor(
            value["user_control_mode"]
        )
    return out


def deserialize_cbor(data: dict) -> ImageBuilderAgentAccessConfig:
    out: ImageBuilderAgentAccessConfig = {}  # type: ignore[typeddict-item]
    if data.get("Settings") is not None:
        import capo_appstream.types.agent_access_setting_list

        out["settings"] = (
            capo_appstream.types.agent_access_setting_list.deserialize_cbor(
                data["Settings"]
            )
        )
    if data.get("S3BucketArn") is not None:
        out["s3_bucket_arn"] = data["S3BucketArn"]
    if data.get("ScreenshotsUploadEnabled") is not None:
        out["screenshots_upload_enabled"] = data["ScreenshotsUploadEnabled"]
    if data.get("ScreenResolution") is not None:
        import capo_appstream.types.screen_resolution

        out["screen_resolution"] = (
            capo_appstream.types.screen_resolution.deserialize_cbor(
                data["ScreenResolution"]
            )
        )
    if data.get("ScreenImageFormat") is not None:
        import capo_appstream.types.screen_image_format

        out["screen_image_format"] = (
            capo_appstream.types.screen_image_format.deserialize_cbor(
                data["ScreenImageFormat"]
            )
        )
    if data.get("UserControlMode") is not None:
        import capo_appstream.types.user_control_mode

        out["user_control_mode"] = (
            capo_appstream.types.user_control_mode.deserialize_cbor(
                data["UserControlMode"]
            )
        )
    return out
