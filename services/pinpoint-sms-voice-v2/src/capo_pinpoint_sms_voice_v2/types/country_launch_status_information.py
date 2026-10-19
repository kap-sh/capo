"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CountryLaunchStatusInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.carrier_status_information_list
    import capo_pinpoint_sms_voice_v2.types.country_launch_status
    import capo_pinpoint_sms_voice_v2.types.iso_country_code


class CountryLaunchStatusInformation(TypedDict, closed=True):
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    status: "capo_pinpoint_sms_voice_v2.types.country_launch_status.CountryLaunchStatus"
    """<p>The launch status for this country.</p>"""
    rcs_platform_id: NotRequired["str"]
    """<p>The RCS platform identifier for this country.</p>"""
    registration_id: "str"
    """<p>The unique identifier of the registration associated with this country launch.</p>"""
    carrier_status: "capo_pinpoint_sms_voice_v2.types.carrier_status_information_list.CarrierStatusInformationList"
    """<p>An array of CarrierStatusInformation objects containing carrier-level launch status details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountryLaunchStatusInformation) -> dict:
    out: dict = {}
    out["IsoCountryCode"] = value["iso_country_code"]
    out["Status"] = value["status"]
    if "rcs_platform_id" in value:
        out["RcsPlatformId"] = value["rcs_platform_id"]
    out["RegistrationId"] = value["registration_id"]
    import capo_pinpoint_sms_voice_v2.types.carrier_status_information_list

    out["CarrierStatus"] = (
        capo_pinpoint_sms_voice_v2.types.carrier_status_information_list.serialize_aws_json_1_0(
            value["carrier_status"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CountryLaunchStatusInformation:
    out: CountryLaunchStatusInformation = {}  # type: ignore[typeddict-item]
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        out["iso_country_code"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("RcsPlatformId") is not None:
        out["rcs_platform_id"] = data["RcsPlatformId"]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    if data.get("CarrierStatus") is not None:
        import capo_pinpoint_sms_voice_v2.types.carrier_status_information_list

        out["carrier_status"] = (
            capo_pinpoint_sms_voice_v2.types.carrier_status_information_list.deserialize_aws_json_1_0(
                data["CarrierStatus"]
            )
        )
    else:
        out["carrier_status"] = []
    return out
