"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateRotationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.idempotency_token
    import capo_ssm_contacts.types.recurrence_settings
    import capo_ssm_contacts.types.rotation_contacts_arn_list
    import capo_ssm_contacts.types.rotation_name
    import capo_ssm_contacts.types.tags_list
    import capo_ssm_contacts.types.time_zone_id


class CreateRotationRequest(TypedDict, closed=True):
    name: "capo_ssm_contacts.types.rotation_name.RotationName"
    """<p>The name of the rotation.</p>"""
    contact_ids: (
        "capo_ssm_contacts.types.rotation_contacts_arn_list.RotationContactsArnList"
    )
    """<p>The Amazon Resource Names (ARNs) of the contacts to add to the rotation.</p> <note> <p>Only the <code>PERSONAL</code> contact type is supported. The contact types <code>ESCALATION</code> and <code>ONCALL_SCHEDULE</code> are not supported for this operation. </p> </note> <p>The order that you list the contacts in is their shift order in the rotation schedule. To change the order of the contact's shifts, use the <a>UpdateRotation</a> operation.</p>"""
    start_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The date and time that the rotation goes into effect.</p>"""
    time_zone_id: "capo_ssm_contacts.types.time_zone_id.TimeZoneId"
    """<p>The time zone to base the rotation’s activity on in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the <a href="https://www.iana.org/time-zones">Time Zone Database</a> on the IANA website.</p> <note> <p>Designators for time zones that don’t support Daylight Savings Time rules, such as Pacific Standard Time (PST), are not supported.</p> </note>"""
    recurrence: "capo_ssm_contacts.types.recurrence_settings.RecurrenceSettings"
    """<p>Information about the rule that specifies when a shift's team members rotate.</p>"""
    tags: NotRequired["capo_ssm_contacts.types.tags_list.TagsList"]
    """<p>Optional metadata to assign to the rotation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html">Tagging Incident Manager resources</a> in the <i>Incident Manager User Guide</i>.</p>"""
    idempotency_token: NotRequired[
        "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token that ensures that the operation is called only once with the specified details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRotationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_ssm_contacts.types.rotation_contacts_arn_list

    out["ContactIds"] = (
        capo_ssm_contacts.types.rotation_contacts_arn_list.serialize_aws_json_1_1(
            value["contact_ids"]
        )
    )
    if "start_time" in value:
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
    if "tags" in value:
        import capo_ssm_contacts.types.tags_list

        out["Tags"] = capo_ssm_contacts.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRotationRequest:
    out: CreateRotationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRotationRequest.name required")
    if data.get("ContactIds") is not None:
        import capo_ssm_contacts.types.rotation_contacts_arn_list

        out["contact_ids"] = (
            capo_ssm_contacts.types.rotation_contacts_arn_list.deserialize_aws_json_1_1(
                data["ContactIds"]
            )
        )
    else:
        raise DeserializationError("CreateRotationRequest.contact_ids required")
    if data.get("StartTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["start_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("TimeZoneId") is not None:
        out["time_zone_id"] = data["TimeZoneId"]
    else:
        raise DeserializationError("CreateRotationRequest.time_zone_id required")
    if data.get("Recurrence") is not None:
        import capo_ssm_contacts.types.recurrence_settings

        out["recurrence"] = (
            capo_ssm_contacts.types.recurrence_settings.deserialize_aws_json_1_1(
                data["Recurrence"]
            )
        )
    else:
        raise DeserializationError("CreateRotationRequest.recurrence required")
    if data.get("Tags") is not None:
        import capo_ssm_contacts.types.tags_list

        out["tags"] = capo_ssm_contacts.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
