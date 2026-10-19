"""Generated from Smithy shape ``com.amazonaws.arczonalshift#PracticeRunConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.allowed_windows
    import capo_arc_zonal_shift.types.blocked_dates
    import capo_arc_zonal_shift.types.blocked_windows
    import capo_arc_zonal_shift.types.blocking_alarms
    import capo_arc_zonal_shift.types.outcome_alarms


class PracticeRunConfiguration(TypedDict, closed=True):
    blocking_alarms: NotRequired[
        "capo_arc_zonal_shift.types.blocking_alarms.BlockingAlarms"
    ]
    """<p> <i>Blocking alarms</i> for practice runs are optional alarms that you can specify that block practice runs when one or more of the alarms is in an <code>ALARM</code> state.</p>"""
    outcome_alarms: "capo_arc_zonal_shift.types.outcome_alarms.OutcomeAlarms"
    """<p> <i>Outcome alarms</i> for practice runs are alarms that you specify that end a practice run when one or more of the alarms is in an <code>ALARM</code> state.</p>"""
    blocked_windows: NotRequired[
        "capo_arc_zonal_shift.types.blocked_windows.BlockedWindows"
    ]
    """<p>An array of one or more windows of days and times that you can block ARC from starting practice runs for a resource.</p> <p>Specify the blocked windows in UTC, using the format <code>DAY:HH:MM-DAY:HH:MM</code>, separated by spaces. For example, <code>MON:18:30-MON:19:30 TUE:18:30-TUE:19:30</code>.</p> <p>The <code>blockedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p>"""
    allowed_windows: NotRequired[
        "capo_arc_zonal_shift.types.allowed_windows.AllowedWindows"
    ]
    """<p>An array of one or more windows of days and times that you can allow ARC to start practice runs for a resource.</p> <p>For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: <code>Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00</code>.</p> <p>The <code>allowedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p>"""
    blocked_dates: "capo_arc_zonal_shift.types.blocked_dates.BlockedDates"
    """<p>An array of one or more dates that you can specify when Amazon Web Services does not start practice runs for a resource.</p> <p>Specify blocked dates, in UTC, in the format <code>YYYY-MM-DD</code>, separated by spaces. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PracticeRunConfiguration) -> dict:
    out: dict = {}
    if "blocking_alarms" in value:
        import capo_arc_zonal_shift.types.blocking_alarms

        out["blockingAlarms"] = (
            capo_arc_zonal_shift.types.blocking_alarms.serialize_json(
                value["blocking_alarms"]
            )
        )
    import capo_arc_zonal_shift.types.outcome_alarms

    out["outcomeAlarms"] = capo_arc_zonal_shift.types.outcome_alarms.serialize_json(
        value["outcome_alarms"]
    )
    if "blocked_windows" in value:
        import capo_arc_zonal_shift.types.blocked_windows

        out["blockedWindows"] = (
            capo_arc_zonal_shift.types.blocked_windows.serialize_json(
                value["blocked_windows"]
            )
        )
    if "allowed_windows" in value:
        import capo_arc_zonal_shift.types.allowed_windows

        out["allowedWindows"] = (
            capo_arc_zonal_shift.types.allowed_windows.serialize_json(
                value["allowed_windows"]
            )
        )
    import capo_arc_zonal_shift.types.blocked_dates

    out["blockedDates"] = capo_arc_zonal_shift.types.blocked_dates.serialize_json(
        value.get("blocked_dates", [])
    )
    return out


def deserialize_json(data: dict) -> PracticeRunConfiguration:
    out: PracticeRunConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("blockingAlarms") is not None:
        import capo_arc_zonal_shift.types.blocking_alarms

        out["blocking_alarms"] = (
            capo_arc_zonal_shift.types.blocking_alarms.deserialize_json(
                data["blockingAlarms"]
            )
        )
    if data.get("outcomeAlarms") is not None:
        import capo_arc_zonal_shift.types.outcome_alarms

        out["outcome_alarms"] = (
            capo_arc_zonal_shift.types.outcome_alarms.deserialize_json(
                data["outcomeAlarms"]
            )
        )
    else:
        out["outcome_alarms"] = []
    if data.get("blockedWindows") is not None:
        import capo_arc_zonal_shift.types.blocked_windows

        out["blocked_windows"] = (
            capo_arc_zonal_shift.types.blocked_windows.deserialize_json(
                data["blockedWindows"]
            )
        )
    if data.get("allowedWindows") is not None:
        import capo_arc_zonal_shift.types.allowed_windows

        out["allowed_windows"] = (
            capo_arc_zonal_shift.types.allowed_windows.deserialize_json(
                data["allowedWindows"]
            )
        )
    if data.get("blockedDates") is not None:
        import capo_arc_zonal_shift.types.blocked_dates

        out["blocked_dates"] = (
            capo_arc_zonal_shift.types.blocked_dates.deserialize_json(
                data["blockedDates"]
            )
        )
    else:
        out["blocked_dates"] = []
    return out
