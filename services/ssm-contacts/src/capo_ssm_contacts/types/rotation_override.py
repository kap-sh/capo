"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RotationOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.ssm_contacts_arn_list
    import capo_ssm_contacts.types.uuid


class RotationOverride(TypedDict, closed=True):
    rotation_override_id: "capo_ssm_contacts.types.uuid.Uuid"
    """<p>The Amazon Resource Name (ARN) of the override to an on-call rotation.</p>"""
    new_contact_ids: "capo_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    """<p>The Amazon Resource Names (ARNs) of the contacts assigned to the override of the on-call rotation.</p>"""
    start_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The time a rotation override begins.</p>"""
    end_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The time a rotation override ends.</p>"""
    create_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The time a rotation override was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationOverride) -> dict:
    out: dict = {}
    out["RotationOverrideId"] = value["rotation_override_id"]
    import capo_ssm_contacts.types.ssm_contacts_arn_list

    out["NewContactIds"] = (
        capo_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
            value["new_contact_ids"]
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
    import capo_ssm_contacts.types.date_time

    out["CreateTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["create_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RotationOverride:
    out: RotationOverride = {}  # type: ignore[typeddict-item]
    if data.get("RotationOverrideId") is not None:
        out["rotation_override_id"] = data["RotationOverrideId"]
    else:
        out["rotation_override_id"] = ""
    if data.get("NewContactIds") is not None:
        import capo_ssm_contacts.types.ssm_contacts_arn_list

        out["new_contact_ids"] = (
            capo_ssm_contacts.types.ssm_contacts_arn_list.deserialize_aws_json_1_1(
                data["NewContactIds"]
            )
        )
    else:
        out["new_contact_ids"] = []
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
    if data.get("CreateTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["create_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
