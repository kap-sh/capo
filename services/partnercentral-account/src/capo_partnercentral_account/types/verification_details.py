"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#VerificationDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.business_verification_details
    import capo_partnercentral_account.types.registrant_verification_details


class _VerificationDetails_BusinessVerificationDetails(TypedDict, closed=True):
    BusinessVerificationDetails: "capo_partnercentral_account.types.business_verification_details.BusinessVerificationDetails"


class _VerificationDetails_RegistrantVerificationDetails(TypedDict, closed=True):
    RegistrantVerificationDetails: "capo_partnercentral_account.types.registrant_verification_details.RegistrantVerificationDetails"


VerificationDetails: TypeAlias = (
    _VerificationDetails_BusinessVerificationDetails
    | _VerificationDetails_RegistrantVerificationDetails
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerificationDetails) -> dict:
    if "BusinessVerificationDetails" in value:
        import capo_partnercentral_account.types.business_verification_details

        return {
            "BusinessVerificationDetails": capo_partnercentral_account.types.business_verification_details.serialize_aws_json_1_0(
                value["BusinessVerificationDetails"]
            )
        }
    elif "RegistrantVerificationDetails" in value:
        import capo_partnercentral_account.types.registrant_verification_details

        return {
            "RegistrantVerificationDetails": capo_partnercentral_account.types.registrant_verification_details.serialize_aws_json_1_0(
                value["RegistrantVerificationDetails"]
            )
        }
    else:
        raise SerializationError("VerificationDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> VerificationDetails:
    if data.get("BusinessVerificationDetails") is not None:
        import capo_partnercentral_account.types.business_verification_details

        return {
            "BusinessVerificationDetails": capo_partnercentral_account.types.business_verification_details.deserialize_aws_json_1_0(
                data["BusinessVerificationDetails"]
            )
        }
    elif data.get("RegistrantVerificationDetails") is not None:
        import capo_partnercentral_account.types.registrant_verification_details

        return {
            "RegistrantVerificationDetails": capo_partnercentral_account.types.registrant_verification_details.deserialize_aws_json_1_0(
                data["RegistrantVerificationDetails"]
            )
        }
    else:
        raise DeserializationError("VerificationDetails: no recognized variant key")


def redact_sensitive(value: VerificationDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "BusinessVerificationDetails" in value:
        import capo_partnercentral_account.types.business_verification_details

        out["BusinessVerificationDetails"] = (
            capo_partnercentral_account.types.business_verification_details.redact_sensitive(
                value["BusinessVerificationDetails"]
            )
        )
    return out
