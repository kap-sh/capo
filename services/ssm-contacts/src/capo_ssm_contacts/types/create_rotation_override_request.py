"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateRotationOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.idempotency_token
    import capo_ssm_contacts.types.rotation_override_contacts_arn_list
    import capo_ssm_contacts.types.ssm_contacts_arn


class CreateRotationOverrideRequest(TypedDict, closed=True):
    rotation_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the rotation to create an override for.</p>"""
    new_contact_ids: "capo_ssm_contacts.types.rotation_override_contacts_arn_list.RotationOverrideContactsArnList"
    """<p>The Amazon Resource Names (ARNs) of the contacts to replace those in the current on-call rotation with.</p> <p>If you want to include any current team members in the override shift, you must include their ARNs in the new contact ID list.</p>"""
    start_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The date and time when the override goes into effect.</p>"""
    end_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The date and time when the override ends.</p>"""
    idempotency_token: NotRequired[
        "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token that ensures that the operation is called only once with the specified details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRotationOverrideRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    import capo_ssm_contacts.types.rotation_override_contacts_arn_list

    out["NewContactIds"] = (
        capo_ssm_contacts.types.rotation_override_contacts_arn_list.serialize_aws_json_1_1(
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
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRotationOverrideRequest:
    out: CreateRotationOverrideRequest = {}  # type: ignore[typeddict-item]
    if data.get("RotationId") is not None:
        out["rotation_id"] = data["RotationId"]
    else:
        out["rotation_id"] = ""
    if data.get("NewContactIds") is not None:
        import capo_ssm_contacts.types.rotation_override_contacts_arn_list

        out["new_contact_ids"] = (
            capo_ssm_contacts.types.rotation_override_contacts_arn_list.deserialize_aws_json_1_1(
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
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
