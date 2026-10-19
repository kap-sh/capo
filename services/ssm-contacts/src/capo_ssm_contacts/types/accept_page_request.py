"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#AcceptPageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.accept_code
    import capo_ssm_contacts.types.accept_code_validation
    import capo_ssm_contacts.types.accept_type
    import capo_ssm_contacts.types.receipt_info
    import capo_ssm_contacts.types.ssm_contacts_arn


class AcceptPageRequest(TypedDict, closed=True):
    page_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the engagement to a contact channel.</p>"""
    contact_channel_id: NotRequired[
        "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    ]
    """<p>The ARN of the contact channel.</p>"""
    accept_type: "capo_ssm_contacts.types.accept_type.AcceptType"
    """<p>The type indicates if the page was <code>DELIVERED</code> or <code>READ</code>.</p>"""
    note: NotRequired["capo_ssm_contacts.types.receipt_info.ReceiptInfo"]
    """<p>Information provided by the user when the user acknowledges the page.</p>"""
    accept_code: "capo_ssm_contacts.types.accept_code.AcceptCode"
    """<p>A 6-digit code used to acknowledge the page.</p>"""
    accept_code_validation: NotRequired[
        "capo_ssm_contacts.types.accept_code_validation.AcceptCodeValidation"
    ]
    """<p>An optional field that Incident Manager uses to <code>ENFORCE</code> <code>AcceptCode</code> validation when acknowledging an page. Acknowledgement can occur by replying to a page, or when entering the AcceptCode in the console. Enforcing AcceptCode validation causes Incident Manager to verify that the code entered by the user matches the code sent by Incident Manager with the page.</p> <p>Incident Manager can also <code>IGNORE</code> <code>AcceptCode</code> validation. Ignoring <code>AcceptCode</code> validation causes Incident Manager to accept any value entered for the <code>AcceptCode</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptPageRequest) -> dict:
    out: dict = {}
    out["PageId"] = value["page_id"]
    if "contact_channel_id" in value:
        out["ContactChannelId"] = value["contact_channel_id"]
    import capo_ssm_contacts.types.accept_type

    out["AcceptType"] = capo_ssm_contacts.types.accept_type.serialize_aws_json_1_1(
        value["accept_type"]
    )
    if "note" in value:
        out["Note"] = value["note"]
    out["AcceptCode"] = value["accept_code"]
    if "accept_code_validation" in value:
        import capo_ssm_contacts.types.accept_code_validation

        out["AcceptCodeValidation"] = (
            capo_ssm_contacts.types.accept_code_validation.serialize_aws_json_1_1(
                value["accept_code_validation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptPageRequest:
    out: AcceptPageRequest = {}  # type: ignore[typeddict-item]
    if data.get("PageId") is not None:
        out["page_id"] = data["PageId"]
    else:
        out["page_id"] = ""
    if data.get("ContactChannelId") is not None:
        out["contact_channel_id"] = data["ContactChannelId"]
    if data.get("AcceptType") is not None:
        import capo_ssm_contacts.types.accept_type

        out["accept_type"] = (
            capo_ssm_contacts.types.accept_type.deserialize_aws_json_1_1(
                data["AcceptType"]
            )
        )
    else:
        import typing

        out["accept_type"] = typing.cast(
            "capo_ssm_contacts.types.accept_type.AcceptType", ""
        )
    if data.get("Note") is not None:
        out["note"] = data["Note"]
    if data.get("AcceptCode") is not None:
        out["accept_code"] = data["AcceptCode"]
    else:
        out["accept_code"] = ""
    if data.get("AcceptCodeValidation") is not None:
        import capo_ssm_contacts.types.accept_code_validation

        out["accept_code_validation"] = (
            capo_ssm_contacts.types.accept_code_validation.deserialize_aws_json_1_1(
                data["AcceptCodeValidation"]
            )
        )
    return out
