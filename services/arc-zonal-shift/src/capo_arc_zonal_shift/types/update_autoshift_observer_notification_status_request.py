"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdateAutoshiftObserverNotificationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.autoshift_observer_notification_status


class UpdateAutoshiftObserverNotificationStatusRequest(TypedDict, closed=True):
    status: "capo_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus"
    """<p>The status to set for autoshift observer notification. If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the Amazon EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutoshiftObserverNotificationStatusRequest) -> dict:
    out: dict = {}
    import capo_arc_zonal_shift.types.autoshift_observer_notification_status

    out["status"] = (
        capo_arc_zonal_shift.types.autoshift_observer_notification_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAutoshiftObserverNotificationStatusRequest:
    out: UpdateAutoshiftObserverNotificationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_arc_zonal_shift.types.autoshift_observer_notification_status

        out["status"] = (
            capo_arc_zonal_shift.types.autoshift_observer_notification_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus",
            "",
        )
    return out
