"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.alert_id
    import capo_cloudwatchomni.types.alert_state_info
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.notification_status
    import capo_cloudwatchomni.types.profile_id
    import capo_cloudwatchomni.types.space_id


class AlertSummary(TypedDict, closed=True):
    name: "str"
    """The name of the alert."""
    alert_id: NotRequired["capo_cloudwatchomni.types.alert_id.AlertId"]
    """The stable alert identifier (see {@link Alert#alertId}). Use it to address the alert; it is also the ARN's resource id."""
    space_id: NotRequired["capo_cloudwatchomni.types.space_id.SpaceId"]
    """The ID of the space the alert belongs to."""
    profile_id: NotRequired["capo_cloudwatchomni.types.profile_id.ProfileId"]
    """The ID of the access profile associated with the alert."""
    notification_status: NotRequired[
        "capo_cloudwatchomni.types.notification_status.NotificationStatus"
    ]
    """Whether notifications are enabled."""
    state: "capo_cloudwatchomni.types.alert_state_info.AlertStateInfo"
    """Live evaluation state (read-only, system-managed)."""
    created_at: "datetime.datetime"
    """The timestamp when the alert was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the alert was last updated."""
    alert_arn: "capo_cloudwatchomni.types.arn.Arn"
    """The Amazon Resource Name (ARN) of the alert."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "alert_id" in value:
        out["alertId"] = value["alert_id"]
    if "space_id" in value:
        out["spaceId"] = value["space_id"]
    if "profile_id" in value:
        out["profileId"] = value["profile_id"]
    if "notification_status" in value:
        import capo_cloudwatchomni.types.notification_status

        out["notificationStatus"] = (
            capo_cloudwatchomni.types.notification_status.serialize_cbor(
                value["notification_status"]
            )
        )
    import capo_cloudwatchomni.types.alert_state_info

    out["state"] = capo_cloudwatchomni.types.alert_state_info.serialize_cbor(
        value["state"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    out["alertArn"] = value["alert_arn"]
    return out


def deserialize_cbor(data: dict) -> AlertSummary:
    out: AlertSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("alertId") is not None:
        out["alert_id"] = data["alertId"]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    if data.get("notificationStatus") is not None:
        import capo_cloudwatchomni.types.notification_status

        out["notification_status"] = (
            capo_cloudwatchomni.types.notification_status.deserialize_cbor(
                data["notificationStatus"]
            )
        )
    if data.get("state") is not None:
        import capo_cloudwatchomni.types.alert_state_info

        out["state"] = capo_cloudwatchomni.types.alert_state_info.deserialize_cbor(
            data["state"]
        )
    else:
        raise DeserializationError("AlertSummary.state required")
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("alertArn") is not None:
        out["alert_arn"] = data["alertArn"]
    else:
        out["alert_arn"] = ""
    return out
