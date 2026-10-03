"""Generated from Smithy shape ``com.amazonaws.arczonalshift#CreatePracticeRunConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.allowed_windows
    import capo_arc_zonal_shift.types.blocked_dates
    import capo_arc_zonal_shift.types.blocked_windows
    import capo_arc_zonal_shift.types.blocking_alarms
    import capo_arc_zonal_shift.types.outcome_alarms
    import capo_arc_zonal_shift.types.resource_identifier


class CreatePracticeRunConfigurationRequest(TypedDict, closed=True):
    resource_identifier: (
        "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier of the resource that Amazon Web Services shifts traffic for with a practice run zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancer</a> </p> </li> </ul>"""
    blocked_windows: NotRequired[
        "capo_arc_zonal_shift.types.blocked_windows.BlockedWindows"
    ]
    """<p>Optionally, you can block ARC from starting practice runs for specific windows of days and times. </p> <p>The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.</p> <p>For example, say you run business report summaries three days a week. For this scenario, you could set the following recurring days and times as blocked windows, for example: <code>Mon:00:00-Mon:10:00 Wed-20:30-Wed:21:30 Fri-20:30-Fri:21:30</code>.</p> <important> <p>The <code>blockedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p> </important>"""
    blocked_dates: NotRequired["capo_arc_zonal_shift.types.blocked_dates.BlockedDates"]
    """<p>Optionally, you can block ARC from starting practice runs for a resource on specific calendar dates.</p> <p>The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.</p> <p>For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for <code>2024-05-01</code>.</p>"""
    blocking_alarms: NotRequired[
        "capo_arc_zonal_shift.types.blocking_alarms.BlockingAlarms"
    ]
    """<p> <i>Blocking alarms</i> for practice runs are optional alarms that you can specify that block practice runs when one or more of the alarms is in an <code>ALARM</code> state.</p>"""
    allowed_windows: NotRequired[
        "capo_arc_zonal_shift.types.allowed_windows.AllowedWindows"
    ]
    """<p>Optionally, you can allow ARC to start practice runs for specific windows of days and times. </p> <p>The format for allowed windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple allowed windows with spaces.</p> <p>For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: <code>Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00</code>.</p> <important> <p>The <code>allowedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p> </important>"""
    outcome_alarms: "capo_arc_zonal_shift.types.outcome_alarms.OutcomeAlarms"
    """<p> <i>Outcome alarms</i> for practice runs are alarms that you specify that end a practice run when one or more of the alarms is in an <code>ALARM</code> state.</p> <p>Configure one or more of these alarms to monitor the health of your application when traffic is shifted away from an Availability Zone during each practice run. You should configure these alarms to go into an <code>ALARM</code> state if you want to stop a zonal shift, to let traffic for the resource return to the original Availability Zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePracticeRunConfigurationRequest) -> dict:
    out: dict = {}
    out["resourceIdentifier"] = value["resource_identifier"]
    if "blocked_windows" in value:
        import capo_arc_zonal_shift.types.blocked_windows

        out["blockedWindows"] = (
            capo_arc_zonal_shift.types.blocked_windows.serialize_json(
                value["blocked_windows"]
            )
        )
    if "blocked_dates" in value:
        import capo_arc_zonal_shift.types.blocked_dates

        out["blockedDates"] = capo_arc_zonal_shift.types.blocked_dates.serialize_json(
            value["blocked_dates"]
        )
    if "blocking_alarms" in value:
        import capo_arc_zonal_shift.types.blocking_alarms

        out["blockingAlarms"] = (
            capo_arc_zonal_shift.types.blocking_alarms.serialize_json(
                value["blocking_alarms"]
            )
        )
    if "allowed_windows" in value:
        import capo_arc_zonal_shift.types.allowed_windows

        out["allowedWindows"] = (
            capo_arc_zonal_shift.types.allowed_windows.serialize_json(
                value["allowed_windows"]
            )
        )
    import capo_arc_zonal_shift.types.outcome_alarms

    out["outcomeAlarms"] = capo_arc_zonal_shift.types.outcome_alarms.serialize_json(
        value["outcome_alarms"]
    )
    return out


def deserialize_json(data: dict) -> CreatePracticeRunConfigurationRequest:
    out: CreatePracticeRunConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError(
            "CreatePracticeRunConfigurationRequest.resource_identifier required"
        )
    if data.get("blockedWindows") is not None:
        import capo_arc_zonal_shift.types.blocked_windows

        out["blocked_windows"] = (
            capo_arc_zonal_shift.types.blocked_windows.deserialize_json(
                data["blockedWindows"]
            )
        )
    if data.get("blockedDates") is not None:
        import capo_arc_zonal_shift.types.blocked_dates

        out["blocked_dates"] = (
            capo_arc_zonal_shift.types.blocked_dates.deserialize_json(
                data["blockedDates"]
            )
        )
    if data.get("blockingAlarms") is not None:
        import capo_arc_zonal_shift.types.blocking_alarms

        out["blocking_alarms"] = (
            capo_arc_zonal_shift.types.blocking_alarms.deserialize_json(
                data["blockingAlarms"]
            )
        )
    if data.get("allowedWindows") is not None:
        import capo_arc_zonal_shift.types.allowed_windows

        out["allowed_windows"] = (
            capo_arc_zonal_shift.types.allowed_windows.deserialize_json(
                data["allowedWindows"]
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
        raise DeserializationError(
            "CreatePracticeRunConfigurationRequest.outcome_alarms required"
        )
    return out
