"""Generated from Smithy shape ``com.amazonaws.mturk#UpdateNotificationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.boolean
    import capo_mturk.types.entity_id
    import capo_mturk.types.notification_specification


class UpdateNotificationSettingsRequest(TypedDict, closed=True):
    hit_type_id: "capo_mturk.types.entity_id.EntityId"
    """<p> The ID of the HIT type whose notification specification is being updated. </p>"""
    notification: NotRequired[
        "capo_mturk.types.notification_specification.NotificationSpecification"
    ]
    """<p> The notification specification for the HIT type. </p>"""
    active: NotRequired["capo_mturk.types.boolean.Boolean"]
    """<p> Specifies whether notifications are sent for HITs of this HIT type, according to the notification specification. You must specify either the Notification parameter or the Active parameter for the call to UpdateNotificationSettings to succeed. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNotificationSettingsRequest) -> dict:
    out: dict = {}
    out["HITTypeId"] = value["hit_type_id"]
    if "notification" in value:
        import capo_mturk.types.notification_specification

        out["Notification"] = (
            capo_mturk.types.notification_specification.serialize_aws_json_1_1(
                value["notification"]
            )
        )
    if "active" in value:
        out["Active"] = value["active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNotificationSettingsRequest:
    out: UpdateNotificationSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("HITTypeId") is not None:
        out["hit_type_id"] = data["HITTypeId"]
    else:
        out["hit_type_id"] = ""
    if data.get("Notification") is not None:
        import capo_mturk.types.notification_specification

        out["notification"] = (
            capo_mturk.types.notification_specification.deserialize_aws_json_1_1(
                data["Notification"]
            )
        )
    if data.get("Active") is not None:
        out["active"] = data["Active"]
    return out
