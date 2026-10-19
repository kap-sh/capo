"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_information_list


class DescribeRegistrationsResult(TypedDict, closed=True):
    registrations: "capo_pinpoint_sms_voice_v2.types.registration_information_list.RegistrationInformationList"
    """<p>An array of RegistrationInformation objects.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationsResult) -> dict:
    out: dict = {}
    import capo_pinpoint_sms_voice_v2.types.registration_information_list

    out["Registrations"] = (
        capo_pinpoint_sms_voice_v2.types.registration_information_list.serialize_aws_json_1_0(
            value["registrations"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationsResult:
    out: DescribeRegistrationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Registrations") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_information_list

        out["registrations"] = (
            capo_pinpoint_sms_voice_v2.types.registration_information_list.deserialize_aws_json_1_0(
                data["Registrations"]
            )
        )
    else:
        out["registrations"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
