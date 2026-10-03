"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#VerifiedDestinationNumberInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.verification_status


class VerifiedDestinationNumberInformation(TypedDict, closed=True):
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
    created_timestamp: "datetime.datetime"
    """<p>The time when the destination phone number was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerifiedDestinationNumberInformation) -> dict:
    out: dict = {}
    out["VerifiedDestinationNumberArn"] = value["verified_destination_number_arn"]
    out["VerifiedDestinationNumberId"] = value["verified_destination_number_id"]
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    out["Status"] = value["status"]
    if "rcs_agent_id" in value:
        out["RcsAgentId"] = value["rcs_agent_id"]
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> VerifiedDestinationNumberInformation:
    out: VerifiedDestinationNumberInformation = {}  # type: ignore[typeddict-item]
    if data.get("VerifiedDestinationNumberArn") is not None:
        out["verified_destination_number_arn"] = data["VerifiedDestinationNumberArn"]
    else:
        raise DeserializationError(
            "VerifiedDestinationNumberInformation.verified_destination_number_arn required"
        )
    if data.get("VerifiedDestinationNumberId") is not None:
        out["verified_destination_number_id"] = data["VerifiedDestinationNumberId"]
    else:
        raise DeserializationError(
            "VerifiedDestinationNumberInformation.verified_destination_number_id required"
        )
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "VerifiedDestinationNumberInformation.destination_phone_number required"
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError(
            "VerifiedDestinationNumberInformation.status required"
        )
    if data.get("RcsAgentId") is not None:
        out["rcs_agent_id"] = data["RcsAgentId"]
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "VerifiedDestinationNumberInformation.created_timestamp required"
        )
    return out
