"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UserAccessLoggingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.arn_list
    import capo_workspaces_web.types.kinesis_stream_arn


class UserAccessLoggingSettings(TypedDict, closed=True):
    user_access_logging_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user access logging settings.</p>"""
    associated_portal_arns: NotRequired["capo_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this user access logging settings is associated with.</p>"""
    kinesis_stream_arn: NotRequired[
        "capo_workspaces_web.types.kinesis_stream_arn.KinesisStreamArn"
    ]
    """<p>The ARN of the Kinesis stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessLoggingSettings) -> dict:
    out: dict = {}
    out["userAccessLoggingSettingsArn"] = value["user_access_logging_settings_arn"]
    if "associated_portal_arns" in value:
        import capo_workspaces_web.types.arn_list

        out["associatedPortalArns"] = capo_workspaces_web.types.arn_list.serialize_json(
            value["associated_portal_arns"]
        )
    if "kinesis_stream_arn" in value:
        out["kinesisStreamArn"] = value["kinesis_stream_arn"]
    return out


def deserialize_json(data: dict) -> UserAccessLoggingSettings:
    out: UserAccessLoggingSettings = {}  # type: ignore[typeddict-item]
    if data.get("userAccessLoggingSettingsArn") is not None:
        out["user_access_logging_settings_arn"] = data["userAccessLoggingSettingsArn"]
    else:
        out["user_access_logging_settings_arn"] = ""
    if data.get("associatedPortalArns") is not None:
        import capo_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            capo_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if data.get("kinesisStreamArn") is not None:
        out["kinesis_stream_arn"] = data["kinesisStreamArn"]
    return out
