"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#VerificationDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError, SerializationError
from capo_partnercentral_account.types._unknown import UnknownUnionMember

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
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerificationDetails) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"VerificationDetails: cannot serialize unknown variant {value.name!r}"
        )
    elif "BusinessVerificationDetails" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("VerificationDetails: no recognized variant key")


def redact_sensitive(value: VerificationDetails) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "BusinessVerificationDetails" in value:
        import capo_partnercentral_account.types.business_verification_details

        out["BusinessVerificationDetails"] = (
            capo_partnercentral_account.types.business_verification_details.redact_sensitive(
                value["BusinessVerificationDetails"]
            )
        )
    return out
