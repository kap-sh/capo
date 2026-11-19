"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Schedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.duration
    import capo_cloudwatch.types.expression
    import capo_cloudwatch.types.timezone


class Schedule(TypedDict, closed=True):
    expression: NotRequired["capo_cloudwatch.types.expression.Expression"]
    """<p>The schedule expression that defines when the mute rule activates. The expression must be between 1 and 256 characters in length.</p> <p>You can use one of two expression formats:</p> <ul> <li> <p> <b>Cron expressions</b> - For recurring mute windows. Format: <code>cron(Minutes Hours Day-of-month Month Day-of-week)</code> </p> <p>Examples:</p> <ul> <li> <p> <code>cron(0 2 * * *)</code> - Activates daily at 2:00 AM</p> </li> <li> <p> <code>cron(0 2 * * SUN)</code> - Activates every Sunday at 2:00 AM for weekly system maintenance</p> </li> <li> <p> <code>cron(0 1 1 * *)</code> - Activates on the first day of each month at 1:00 AM for monthly database maintenance</p> </li> <li> <p> <code>cron(0 18 * * FRI)</code> - Activates every Friday at 6:00 PM</p> </li> <li> <p> <code>cron(0 23 * * *)</code> - Activates every day at 11:00 PM during nightly backup operations</p> </li> </ul> <p>The characters <code>*</code>, <code>-</code>, and <code>,</code> are supported in all fields. English names can be used for the month (JAN-DEC) and day of week (SUN-SAT) fields.</p> </li> <li> <p> <b>At expressions</b> - For one-time mute windows. Format: <code>at(yyyy-MM-ddThh:mm)</code> </p> <p>Examples:</p> <ul> <li> <p> <code>at(2024-05-10T14:00)</code> - Activates once on May 10, 2024 at 2:00 PM during an active incident response session</p> </li> <li> <p> <code>at(2024-12-23T00:00)</code> - Activates once on December 23, 2024 at midnight during annual company shutdown</p> </li> </ul> </li> </ul>"""
    duration: NotRequired["capo_cloudwatch.types.duration.Duration"]
    """<p>The length of time that alarms remain muted when the schedule activates. The duration must be between 1 and 50 characters in length.</p> <p>Specify the duration using ISO 8601 duration format with a minimum of 1 minute (<code>PT1M</code>) and maximum of 15 days (<code>P15D</code>).</p> <p>Examples:</p> <ul> <li> <p> <code>PT4H</code> - 4 hours for weekly system maintenance</p> </li> <li> <p> <code>P2DT12H</code> - 2 days and 12 hours for weekend muting from Friday 6:00 PM to Monday 6:00 AM</p> </li> <li> <p> <code>PT6H</code> - 6 hours for monthly database maintenance</p> </li> <li> <p> <code>PT2H</code> - 2 hours for nightly backup operations</p> </li> <li> <p> <code>P7D</code> - 7 days for annual company shutdown</p> </li> </ul> <p>The duration begins when the schedule expression time is reached. For recurring schedules, the duration applies to each occurrence.</p>"""
    timezone: NotRequired["capo_cloudwatch.types.timezone.Timezone"]
    """<p>The time zone to use when evaluating the schedule expression. The time zone must be between 1 and 50 characters in length.</p> <p>Specify the time zone using standard timezone identifiers (for example, <code>America/New_York</code>, <code>Europe/London</code>, or <code>Asia/Tokyo</code>).</p> <p>If you don't specify a time zone, UTC is used by default. The time zone affects how cron and at expressions are interpreted, as well as start and expire dates you specify</p> <p>Examples:</p> <ul> <li> <p> <code>America/New_York</code> - Eastern Time (US)</p> </li> <li> <p> <code>America/Los_Angeles</code> - Pacific Time (US)</p> </li> <li> <p> <code>Europe/London</code> - British Time</p> </li> <li> <p> <code>Asia/Tokyo</code> - Japan Standard Time</p> </li> <li> <p> <code>UTC</code> - Coordinated Universal Time</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Schedule) -> dict:
    out: dict = {}
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    return out


# --- awsQuery ser/de ---
def serialize_query(value: Schedule, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "expression" in value:
        pairs.append((f"{key_prefix}Expression", str(value["expression"])))
    if "duration" in value:
        pairs.append((f"{key_prefix}Duration", str(value["duration"])))
    if "timezone" in value:
        pairs.append((f"{key_prefix}Timezone", str(value["timezone"])))


def deserialize_query(el: Element) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    child_expression = el.find("Expression")
    if child_expression is not None:
        out["expression"] = str(child_expression.text or "")
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = str(child_duration.text or "")
    child_timezone = el.find("Timezone")
    if child_timezone is not None:
        out["timezone"] = str(child_timezone.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Schedule) -> dict:
    out: dict = {}
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    return out


def deserialize_cbor(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    return out
