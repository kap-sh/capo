"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#VerificationResponseDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.business_verification_response
    import capo_partnercentral_account.types.registrant_verification_response


class _VerificationResponseDetails_BusinessVerificationResponse(TypedDict, closed=True):
    BusinessVerificationResponse: "capo_partnercentral_account.types.business_verification_response.BusinessVerificationResponse"


class _VerificationResponseDetails_RegistrantVerificationResponse(
    TypedDict, closed=True
):
    RegistrantVerificationResponse: "capo_partnercentral_account.types.registrant_verification_response.RegistrantVerificationResponse"


VerificationResponseDetails: TypeAlias = (
    _VerificationResponseDetails_BusinessVerificationResponse
    | _VerificationResponseDetails_RegistrantVerificationResponse
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerificationResponseDetails) -> dict:
    if "BusinessVerificationResponse" in value:
        import capo_partnercentral_account.types.business_verification_response

        return {
            "BusinessVerificationResponse": capo_partnercentral_account.types.business_verification_response.serialize_aws_json_1_0(
                value["BusinessVerificationResponse"]
            )
        }
    elif "RegistrantVerificationResponse" in value:
        import capo_partnercentral_account.types.registrant_verification_response

        return {
            "RegistrantVerificationResponse": capo_partnercentral_account.types.registrant_verification_response.serialize_aws_json_1_0(
                value["RegistrantVerificationResponse"]
            )
        }
    else:
        raise SerializationError("VerificationResponseDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> VerificationResponseDetails:
    if data.get("BusinessVerificationResponse") is not None:
        import capo_partnercentral_account.types.business_verification_response

        return {
            "BusinessVerificationResponse": capo_partnercentral_account.types.business_verification_response.deserialize_aws_json_1_0(
                data["BusinessVerificationResponse"]
            )
        }
    elif data.get("RegistrantVerificationResponse") is not None:
        import capo_partnercentral_account.types.registrant_verification_response

        return {
            "RegistrantVerificationResponse": capo_partnercentral_account.types.registrant_verification_response.deserialize_aws_json_1_0(
                data["RegistrantVerificationResponse"]
            )
        }
    else:
        raise DeserializationError(
            "VerificationResponseDetails: no recognized variant key"
        )


def redact_sensitive(value: VerificationResponseDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "BusinessVerificationResponse" in value:
        import capo_partnercentral_account.types.business_verification_response

        out["BusinessVerificationResponse"] = (
            capo_partnercentral_account.types.business_verification_response.redact_sensitive(
                value["BusinessVerificationResponse"]
            )
        )
    return out
