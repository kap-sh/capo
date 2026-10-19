"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Receipt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.receipt_info
    import capo_ssm_contacts.types.receipt_type
    import capo_ssm_contacts.types.ssm_contacts_arn


class Receipt(TypedDict, closed=True):
    contact_channel_arn: NotRequired[
        "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the contact channel Incident Manager engaged.</p>"""
    receipt_type: "capo_ssm_contacts.types.receipt_type.ReceiptType"
    """<p>The type follows the engagement cycle, <code>SENT</code>, <code>DELIVERED</code>, and <code>READ</code>.</p>"""
    receipt_info: NotRequired["capo_ssm_contacts.types.receipt_info.ReceiptInfo"]
    """<p>Information provided during the page acknowledgement.</p>"""
    receipt_time: "capo_ssm_contacts.types.date_time.DateTime"
    """<p>The time receipt was <code>SENT</code>, <code>DELIVERED</code>, or <code>READ</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Receipt) -> dict:
    out: dict = {}
    if "contact_channel_arn" in value:
        out["ContactChannelArn"] = value["contact_channel_arn"]
    import capo_ssm_contacts.types.receipt_type

    out["ReceiptType"] = capo_ssm_contacts.types.receipt_type.serialize_aws_json_1_1(
        value["receipt_type"]
    )
    if "receipt_info" in value:
        out["ReceiptInfo"] = value["receipt_info"]
    import capo_ssm_contacts.types.date_time

    out["ReceiptTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["receipt_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Receipt:
    out: Receipt = {}  # type: ignore[typeddict-item]
    if data.get("ContactChannelArn") is not None:
        out["contact_channel_arn"] = data["ContactChannelArn"]
    if data.get("ReceiptType") is not None:
        import capo_ssm_contacts.types.receipt_type

        out["receipt_type"] = (
            capo_ssm_contacts.types.receipt_type.deserialize_aws_json_1_1(
                data["ReceiptType"]
            )
        )
    else:
        import typing

        out["receipt_type"] = typing.cast(
            "capo_ssm_contacts.types.receipt_type.ReceiptType", ""
        )
    if data.get("ReceiptInfo") is not None:
        out["receipt_info"] = data["ReceiptInfo"]
    if data.get("ReceiptTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["receipt_time"] = (
            capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["ReceiptTime"]
            )
        )
    else:
        import datetime

        out["receipt_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
