"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ProvisionedCapacityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.account_settings_notification_configuration
    import capo_timestream_query.types.query_tcu


class ProvisionedCapacityRequest(TypedDict, closed=True):
    target_query_tcu: "capo_timestream_query.types.query_tcu.QueryTCU"
    """<p>The target compute capacity for querying data, specified in Timestream Compute Units (TCUs).</p>"""
    notification_configuration: NotRequired[
        "capo_timestream_query.types.account_settings_notification_configuration.AccountSettingsNotificationConfiguration"
    ]
    """<p>Configuration settings for notifications related to the provisioned capacity update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionedCapacityRequest) -> dict:
    out: dict = {}
    out["TargetQueryTCU"] = value["target_query_tcu"]
    if "notification_configuration" in value:
        import capo_timestream_query.types.account_settings_notification_configuration

        out["NotificationConfiguration"] = (
            capo_timestream_query.types.account_settings_notification_configuration.serialize_aws_json_1_0(
                value["notification_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProvisionedCapacityRequest:
    out: ProvisionedCapacityRequest = {}  # type: ignore[typeddict-item]
    if data.get("TargetQueryTCU") is not None:
        out["target_query_tcu"] = data["TargetQueryTCU"]
    else:
        out["target_query_tcu"] = 0
    if data.get("NotificationConfiguration") is not None:
        import capo_timestream_query.types.account_settings_notification_configuration

        out["notification_configuration"] = (
            capo_timestream_query.types.account_settings_notification_configuration.deserialize_aws_json_1_0(
                data["NotificationConfiguration"]
            )
        )
    return out
