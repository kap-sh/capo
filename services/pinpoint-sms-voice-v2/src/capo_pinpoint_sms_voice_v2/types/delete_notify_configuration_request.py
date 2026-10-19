"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteNotifyConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn


class DeleteNotifyConfigurationRequest(TypedDict, closed=True):
    notify_configuration_id: "capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn.NotifyConfigurationIdOrArn"
    """<p>The identifier of the notify configuration to delete. The NotifyConfigurationId can be found using the <a>DescribeNotifyConfigurations</a> operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteNotifyConfigurationRequest) -> dict:
    out: dict = {}
    out["NotifyConfigurationId"] = value["notify_configuration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteNotifyConfigurationRequest:
    out: DeleteNotifyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("NotifyConfigurationId") is not None:
        out["notify_configuration_id"] = data["NotifyConfigurationId"]
    else:
        out["notify_configuration_id"] = ""
    return out
