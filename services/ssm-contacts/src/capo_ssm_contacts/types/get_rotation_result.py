"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetRotationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.recurrence_settings
    import capo_ssm_contacts.types.rotation_contacts_arn_list
    import capo_ssm_contacts.types.rotation_name
    import capo_ssm_contacts.types.ssm_contacts_arn
    import capo_ssm_contacts.types.time_zone_id


class GetRotationResult(TypedDict, closed=True):
    rotation_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the on-call rotation.</p>"""
    name: "capo_ssm_contacts.types.rotation_name.RotationName"
    """<p>The name of the on-call rotation.</p>"""
    contact_ids: (
        "capo_ssm_contacts.types.rotation_contacts_arn_list.RotationContactsArnList"
    )
    """<p>The Amazon Resource Names (ARNs) of the contacts assigned to the on-call rotation team.</p>"""
    start_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The specified start time for the on-call rotation.</p>"""
    time_zone_id: "capo_ssm_contacts.types.time_zone_id.TimeZoneId"
    """<p>The time zone that the rotation’s activity is based on, in Internet Assigned Numbers Authority (IANA) format.</p>"""
    recurrence: "capo_ssm_contacts.types.recurrence_settings.RecurrenceSettings"
    """<p>Specifies how long a rotation lasts before restarting at the beginning of the shift order.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRotationResult) -> dict:
    out: dict = {}
    out["RotationArn"] = value["rotation_arn"]
    out["Name"] = value["name"]
    import capo_ssm_contacts.types.rotation_contacts_arn_list

    out["ContactIds"] = (
        capo_ssm_contacts.types.rotation_contacts_arn_list.serialize_aws_json_1_1(
            value["contact_ids"]
        )
    )
    import capo_ssm_contacts.types.date_time

    out["StartTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["start_time"]
    )
    out["TimeZoneId"] = value["time_zone_id"]
    import capo_ssm_contacts.types.recurrence_settings

    out["Recurrence"] = (
        capo_ssm_contacts.types.recurrence_settings.serialize_aws_json_1_1(
            value["recurrence"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRotationResult:
    out: GetRotationResult = {}  # type: ignore[typeddict-item]
    if data.get("RotationArn") is not None:
        out["rotation_arn"] = data["RotationArn"]
    else:
        out["rotation_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ContactIds") is not None:
        import capo_ssm_contacts.types.rotation_contacts_arn_list

        out["contact_ids"] = (
            capo_ssm_contacts.types.rotation_contacts_arn_list.deserialize_aws_json_1_1(
                data["ContactIds"]
            )
        )
    else:
        out["contact_ids"] = []
    if data.get("StartTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["start_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("TimeZoneId") is not None:
        out["time_zone_id"] = data["TimeZoneId"]
    else:
        out["time_zone_id"] = ""
    if data.get("Recurrence") is not None:
        import capo_ssm_contacts.types.recurrence_settings

        out["recurrence"] = (
            capo_ssm_contacts.types.recurrence_settings.deserialize_aws_json_1_1(
                data["Recurrence"]
            )
        )
    else:
        raise DeserializationError("GetRotationResult.recurrence required")
    return out
