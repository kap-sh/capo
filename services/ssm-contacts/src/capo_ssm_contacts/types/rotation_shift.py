"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RotationShift``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.shift_details
    import capo_ssm_contacts.types.shift_type
    import capo_ssm_contacts.types.ssm_contacts_arn_list


class RotationShift(TypedDict, closed=True):
    contact_ids: NotRequired[
        "capo_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the contacts who are part of the shift rotation. </p>"""
    start_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The time a shift rotation begins.</p>"""
    end_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The time a shift rotation ends.</p>"""
    type: NotRequired["capo_ssm_contacts.types.shift_type.ShiftType"]
    """<p>The type of shift rotation.</p>"""
    shift_details: NotRequired["capo_ssm_contacts.types.shift_details.ShiftDetails"]
    """<p>Additional information about an on-call rotation shift.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationShift) -> dict:
    out: dict = {}
    if "contact_ids" in value:
        import capo_ssm_contacts.types.ssm_contacts_arn_list

        out["ContactIds"] = (
            capo_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
                value["contact_ids"]
            )
        )
    import capo_ssm_contacts.types.date_time

    out["StartTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["start_time"]
    )
    import capo_ssm_contacts.types.date_time

    out["EndTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["end_time"]
    )
    if "type" in value:
        import capo_ssm_contacts.types.shift_type

        out["Type"] = capo_ssm_contacts.types.shift_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "shift_details" in value:
        import capo_ssm_contacts.types.shift_details

        out["ShiftDetails"] = (
            capo_ssm_contacts.types.shift_details.serialize_aws_json_1_1(
                value["shift_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RotationShift:
    out: RotationShift = {}  # type: ignore[typeddict-item]
    if data.get("ContactIds") is not None:
        import capo_ssm_contacts.types.ssm_contacts_arn_list

        out["contact_ids"] = (
            capo_ssm_contacts.types.ssm_contacts_arn_list.deserialize_aws_json_1_1(
                data["ContactIds"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["start_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["end_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Type") is not None:
        import capo_ssm_contacts.types.shift_type

        out["type"] = capo_ssm_contacts.types.shift_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("ShiftDetails") is not None:
        import capo_ssm_contacts.types.shift_details

        out["shift_details"] = (
            capo_ssm_contacts.types.shift_details.deserialize_aws_json_1_1(
                data["ShiftDetails"]
            )
        )
    return out
