"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RecurrenceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.daily_settings
    import capo_ssm_contacts.types.monthly_settings
    import capo_ssm_contacts.types.number_of_on_calls
    import capo_ssm_contacts.types.recurrence_multiplier
    import capo_ssm_contacts.types.shift_coverages_map
    import capo_ssm_contacts.types.weekly_settings


class RecurrenceSettings(TypedDict, closed=True):
    monthly_settings: NotRequired[
        "capo_ssm_contacts.types.monthly_settings.MonthlySettings"
    ]
    """<p>Information about on-call rotations that recur monthly.</p>"""
    weekly_settings: NotRequired[
        "capo_ssm_contacts.types.weekly_settings.WeeklySettings"
    ]
    """<p>Information about on-call rotations that recur weekly.</p>"""
    daily_settings: NotRequired["capo_ssm_contacts.types.daily_settings.DailySettings"]
    """<p>Information about on-call rotations that recur daily.</p>"""
    number_of_on_calls: "capo_ssm_contacts.types.number_of_on_calls.NumberOfOnCalls"
    """<p>The number of contacts, or shift team members designated to be on call concurrently during a shift. For example, in an on-call schedule that contains ten contacts, a value of <code>2</code> designates that two of them are on call at any given time.</p>"""
    shift_coverages: NotRequired[
        "capo_ssm_contacts.types.shift_coverages_map.ShiftCoveragesMap"
    ]
    """<p>Information about the days of the week that the on-call rotation coverage includes.</p>"""
    recurrence_multiplier: (
        "capo_ssm_contacts.types.recurrence_multiplier.RecurrenceMultiplier"
    )
    """<p>The number of days, weeks, or months a single rotation lasts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecurrenceSettings) -> dict:
    out: dict = {}
    if "monthly_settings" in value:
        import capo_ssm_contacts.types.monthly_settings

        out["MonthlySettings"] = (
            capo_ssm_contacts.types.monthly_settings.serialize_aws_json_1_1(
                value["monthly_settings"]
            )
        )
    if "weekly_settings" in value:
        import capo_ssm_contacts.types.weekly_settings

        out["WeeklySettings"] = (
            capo_ssm_contacts.types.weekly_settings.serialize_aws_json_1_1(
                value["weekly_settings"]
            )
        )
    if "daily_settings" in value:
        import capo_ssm_contacts.types.daily_settings

        out["DailySettings"] = (
            capo_ssm_contacts.types.daily_settings.serialize_aws_json_1_1(
                value["daily_settings"]
            )
        )
    out["NumberOfOnCalls"] = value["number_of_on_calls"]
    if "shift_coverages" in value:
        import capo_ssm_contacts.types.shift_coverages_map

        out["ShiftCoverages"] = (
            capo_ssm_contacts.types.shift_coverages_map.serialize_aws_json_1_1(
                value["shift_coverages"]
            )
        )
    out["RecurrenceMultiplier"] = value["recurrence_multiplier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecurrenceSettings:
    out: RecurrenceSettings = {}  # type: ignore[typeddict-item]
    if data.get("MonthlySettings") is not None:
        import capo_ssm_contacts.types.monthly_settings

        out["monthly_settings"] = (
            capo_ssm_contacts.types.monthly_settings.deserialize_aws_json_1_1(
                data["MonthlySettings"]
            )
        )
    if data.get("WeeklySettings") is not None:
        import capo_ssm_contacts.types.weekly_settings

        out["weekly_settings"] = (
            capo_ssm_contacts.types.weekly_settings.deserialize_aws_json_1_1(
                data["WeeklySettings"]
            )
        )
    if data.get("DailySettings") is not None:
        import capo_ssm_contacts.types.daily_settings

        out["daily_settings"] = (
            capo_ssm_contacts.types.daily_settings.deserialize_aws_json_1_1(
                data["DailySettings"]
            )
        )
    if data.get("NumberOfOnCalls") is not None:
        out["number_of_on_calls"] = data["NumberOfOnCalls"]
    else:
        out["number_of_on_calls"] = 0
    if data.get("ShiftCoverages") is not None:
        import capo_ssm_contacts.types.shift_coverages_map

        out["shift_coverages"] = (
            capo_ssm_contacts.types.shift_coverages_map.deserialize_aws_json_1_1(
                data["ShiftCoverages"]
            )
        )
    if data.get("RecurrenceMultiplier") is not None:
        out["recurrence_multiplier"] = data["RecurrenceMultiplier"]
    else:
        out["recurrence_multiplier"] = 0
    return out
