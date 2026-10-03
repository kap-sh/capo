"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Rotation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.recurrence_settings
    import capo_ssm_contacts.types.rotation_name
    import capo_ssm_contacts.types.ssm_contacts_arn
    import capo_ssm_contacts.types.ssm_contacts_arn_list
    import capo_ssm_contacts.types.time_zone_id


class Rotation(TypedDict, closed=True):
    rotation_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the rotation.</p>"""
    name: "capo_ssm_contacts.types.rotation_name.RotationName"
    """<p>The name of the rotation.</p>"""
    contact_ids: NotRequired[
        "capo_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the contacts assigned to the rotation team.</p>"""
    start_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The date and time the rotation becomes active.</p>"""
    time_zone_id: NotRequired["capo_ssm_contacts.types.time_zone_id.TimeZoneId"]
    """<p>The time zone the rotation’s activity is based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". </p>"""
    recurrence: NotRequired[
        "capo_ssm_contacts.types.recurrence_settings.RecurrenceSettings"
    ]
    """<p>Information about when an on-call rotation is in effect and how long the rotation period lasts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rotation) -> dict:
    out: dict = {}
    out["RotationArn"] = value["rotation_arn"]
    out["Name"] = value["name"]
    if "contact_ids" in value:
        import capo_ssm_contacts.types.ssm_contacts_arn_list

        out["ContactIds"] = (
            capo_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
                value["contact_ids"]
            )
        )
    if "start_time" in value:
        import capo_ssm_contacts.types.date_time

        out["StartTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "time_zone_id" in value:
        out["TimeZoneId"] = value["time_zone_id"]
    if "recurrence" in value:
        import capo_ssm_contacts.types.recurrence_settings

        out["Recurrence"] = (
            capo_ssm_contacts.types.recurrence_settings.serialize_aws_json_1_1(
                value["recurrence"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Rotation:
    out: Rotation = {}  # type: ignore[typeddict-item]
    if data.get("RotationArn") is not None:
        out["rotation_arn"] = data["RotationArn"]
    else:
        raise DeserializationError("Rotation.rotation_arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Rotation.name required")
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
    if data.get("TimeZoneId") is not None:
        out["time_zone_id"] = data["TimeZoneId"]
    if data.get("Recurrence") is not None:
        import capo_ssm_contacts.types.recurrence_settings

        out["recurrence"] = (
            capo_ssm_contacts.types.recurrence_settings.deserialize_aws_json_1_1(
                data["Recurrence"]
            )
        )
    return out
