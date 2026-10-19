"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UserAccessLoggingSettingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.kinesis_stream_arn


class UserAccessLoggingSettingsSummary(TypedDict, closed=True):
    user_access_logging_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user access logging settings.</p>"""
    kinesis_stream_arn: NotRequired[
        "capo_workspaces_web.types.kinesis_stream_arn.KinesisStreamArn"
    ]
    """<p>The ARN of the Kinesis stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessLoggingSettingsSummary) -> dict:
    out: dict = {}
    out["userAccessLoggingSettingsArn"] = value["user_access_logging_settings_arn"]
    if "kinesis_stream_arn" in value:
        out["kinesisStreamArn"] = value["kinesis_stream_arn"]
    return out


def deserialize_json(data: dict) -> UserAccessLoggingSettingsSummary:
    out: UserAccessLoggingSettingsSummary = {}  # type: ignore[typeddict-item]
    if data.get("userAccessLoggingSettingsArn") is not None:
        out["user_access_logging_settings_arn"] = data["userAccessLoggingSettingsArn"]
    else:
        out["user_access_logging_settings_arn"] = ""
    if data.get("kinesisStreamArn") is not None:
        out["kinesis_stream_arn"] = data["kinesisStreamArn"]
    return out
