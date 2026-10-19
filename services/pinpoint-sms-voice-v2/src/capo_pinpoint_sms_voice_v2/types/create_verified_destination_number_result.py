"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateVerifiedDestinationNumberResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.tag_list
    import capo_pinpoint_sms_voice_v2.types.verification_status


class CreateVerifiedDestinationNumberResult(TypedDict, closed=True):
    verified_destination_number_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the verified destination phone number.</p>"""
    verified_destination_number_id: "str"
    """<p>The unique identifier for the verified destination phone number.</p>"""
    destination_phone_number: (
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The verified destination phone number, in E.164 format.</p>"""
    status: "capo_pinpoint_sms_voice_v2.types.verification_status.VerificationStatus"
    """<p>The status of the verified destination phone number.</p> <ul> <li> <p> <code>PENDING</code>: The phone number hasn't been verified yet.</p> </li> <li> <p> <code>VERIFIED</code>: The phone number is verified and can receive messages.</p> </li> </ul>"""
    rcs_agent_id: NotRequired["str"]
    """<p>The unique identifier of the RCS agent associated with the verified destination number.</p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) to associate with the destination number.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the verified phone number was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVerifiedDestinationNumberResult) -> dict:
    out: dict = {}
    out["VerifiedDestinationNumberArn"] = value["verified_destination_number_arn"]
    out["VerifiedDestinationNumberId"] = value["verified_destination_number_id"]
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    out["Status"] = value["status"]
    if "rcs_agent_id" in value:
        out["RcsAgentId"] = value["rcs_agent_id"]
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVerifiedDestinationNumberResult:
    out: CreateVerifiedDestinationNumberResult = {}  # type: ignore[typeddict-item]
    if data.get("VerifiedDestinationNumberArn") is not None:
        out["verified_destination_number_arn"] = data["VerifiedDestinationNumberArn"]
    else:
        out["verified_destination_number_arn"] = ""
    if data.get("VerifiedDestinationNumberId") is not None:
        out["verified_destination_number_id"] = data["VerifiedDestinationNumberId"]
    else:
        out["verified_destination_number_id"] = ""
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        out["destination_phone_number"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("RcsAgentId") is not None:
        out["rcs_agent_id"] = data["RcsAgentId"]
    if data.get("Tags") is not None:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        import datetime

        out["created_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
