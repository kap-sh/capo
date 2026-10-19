"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdateAutoshiftObserverNotificationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.autoshift_observer_notification_status


class UpdateAutoshiftObserverNotificationStatusResponse(TypedDict, closed=True):
    status: "capo_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus"
    """<p>The status for autoshift observer notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutoshiftObserverNotificationStatusResponse) -> dict:
    out: dict = {}
    import capo_arc_zonal_shift.types.autoshift_observer_notification_status

    out["status"] = (
        capo_arc_zonal_shift.types.autoshift_observer_notification_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAutoshiftObserverNotificationStatusResponse:
    out: UpdateAutoshiftObserverNotificationStatusResponse = {}  # type: ignore[typeddict-item]
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
