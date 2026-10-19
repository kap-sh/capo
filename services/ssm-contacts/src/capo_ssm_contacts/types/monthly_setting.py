"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#MonthlySetting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.day_of_month
    import capo_ssm_contacts.types.hand_off_time


class MonthlySetting(TypedDict, closed=True):
    day_of_month: "capo_ssm_contacts.types.day_of_month.DayOfMonth"
    """<p>The day of the month when monthly recurring on-call rotations begin.</p>"""
    hand_off_time: "capo_ssm_contacts.types.hand_off_time.HandOffTime"
    """<p>The time of day when a monthly recurring on-call shift rotation begins.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonthlySetting) -> dict:
    out: dict = {}
    out["DayOfMonth"] = value["day_of_month"]
    import capo_ssm_contacts.types.hand_off_time

    out["HandOffTime"] = capo_ssm_contacts.types.hand_off_time.serialize_aws_json_1_1(
        value["hand_off_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonthlySetting:
    out: MonthlySetting = {}  # type: ignore[typeddict-item]
    if data.get("DayOfMonth") is not None:
        out["day_of_month"] = data["DayOfMonth"]
    else:
        out["day_of_month"] = 0
    if data.get("HandOffTime") is not None:
        import capo_ssm_contacts.types.hand_off_time

        out["hand_off_time"] = (
            capo_ssm_contacts.types.hand_off_time.deserialize_aws_json_1_1(
                data["HandOffTime"]
            )
        )
    else:
        raise DeserializationError("MonthlySetting.hand_off_time required")
    return out
