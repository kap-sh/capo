"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#WeeklySetting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.day_of_week
    import capo_ssm_contacts.types.hand_off_time


class WeeklySetting(TypedDict, closed=True):
    day_of_week: "capo_ssm_contacts.types.day_of_week.DayOfWeek"
    """<p>The day of the week when weekly recurring on-call shift rotations begins.</p>"""
    hand_off_time: "capo_ssm_contacts.types.hand_off_time.HandOffTime"
    """<p>The time of day when a weekly recurring on-call shift rotation begins.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WeeklySetting) -> dict:
    out: dict = {}
    import capo_ssm_contacts.types.day_of_week

    out["DayOfWeek"] = capo_ssm_contacts.types.day_of_week.serialize_aws_json_1_1(
        value["day_of_week"]
    )
    import capo_ssm_contacts.types.hand_off_time

    out["HandOffTime"] = capo_ssm_contacts.types.hand_off_time.serialize_aws_json_1_1(
        value["hand_off_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WeeklySetting:
    out: WeeklySetting = {}  # type: ignore[typeddict-item]
    if data.get("DayOfWeek") is not None:
        import capo_ssm_contacts.types.day_of_week

        out["day_of_week"] = (
            capo_ssm_contacts.types.day_of_week.deserialize_aws_json_1_1(
                data["DayOfWeek"]
            )
        )
    else:
        import typing

        out["day_of_week"] = typing.cast(
            "capo_ssm_contacts.types.day_of_week.DayOfWeek", ""
        )
    if data.get("HandOffTime") is not None:
        import capo_ssm_contacts.types.hand_off_time

        out["hand_off_time"] = (
            capo_ssm_contacts.types.hand_off_time.deserialize_aws_json_1_1(
                data["HandOffTime"]
            )
        )
    else:
        raise DeserializationError("WeeklySetting.hand_off_time required")
    return out
