"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigStreamDeliveryInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.date
    import capo_config_service.types.delivery_status
    import capo_config_service.types.string


class ConfigStreamDeliveryInfo(TypedDict, closed=True):
    last_status: NotRequired["capo_config_service.types.delivery_status.DeliveryStatus"]
    """<p>Status of the last attempted delivery.</p> <p> <b>Note</b> Providing an SNS topic on a <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html">DeliveryChannel</a> for Config is optional. If the SNS delivery is turned off, the last status will be <b>Not_Applicable</b>.</p>"""
    last_error_code: NotRequired["capo_config_service.types.string.String"]
    """<p>The error code from the last attempted delivery.</p>"""
    last_error_message: NotRequired["capo_config_service.types.string.String"]
    """<p>The error message from the last attempted delivery.</p>"""
    last_status_change_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time from the last status change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigStreamDeliveryInfo) -> dict:
    out: dict = {}
    if "last_status" in value:
        import capo_config_service.types.delivery_status

        out["lastStatus"] = (
            capo_config_service.types.delivery_status.serialize_aws_json_1_1(
                value["last_status"]
            )
        )
    if "last_error_code" in value:
        out["lastErrorCode"] = value["last_error_code"]
    if "last_error_message" in value:
        out["lastErrorMessage"] = value["last_error_message"]
    if "last_status_change_time" in value:
        import capo_config_service.types.date

        out["lastStatusChangeTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_status_change_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigStreamDeliveryInfo:
    out: ConfigStreamDeliveryInfo = {}  # type: ignore[typeddict-item]
    if data.get("lastStatus") is not None:
        import capo_config_service.types.delivery_status

        out["last_status"] = (
            capo_config_service.types.delivery_status.deserialize_aws_json_1_1(
                data["lastStatus"]
            )
        )
    if data.get("lastErrorCode") is not None:
        out["last_error_code"] = data["lastErrorCode"]
    if data.get("lastErrorMessage") is not None:
        out["last_error_message"] = data["lastErrorMessage"]
    if data.get("lastStatusChangeTime") is not None:
        import capo_config_service.types.date

        out["last_status_change_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["lastStatusChangeTime"]
            )
        )
    return out
