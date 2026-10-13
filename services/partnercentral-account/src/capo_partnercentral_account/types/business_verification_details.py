"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#BusinessVerificationDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.country_code
    import capo_partnercentral_account.types.jurisdiction_code
    import capo_partnercentral_account.types.legal_name
    import capo_partnercentral_account.types.registration_id


class BusinessVerificationDetails(TypedDict, closed=True):
    legal_name: "capo_partnercentral_account.types.legal_name.LegalName"
    """<p>The official legal name of the business as registered with the appropriate government authorities.</p>"""
    registration_id: "capo_partnercentral_account.types.registration_id.RegistrationId"
    """<p>The unique business registration identifier assigned by the government or regulatory authority, such as a company registration number or tax identification number.</p>"""
    country_code: "capo_partnercentral_account.types.country_code.CountryCode"
    """<p>The ISO 3166-1 alpha-2 country code where the business is legally registered and operates.</p>"""
    jurisdiction_of_incorporation: NotRequired[
        "capo_partnercentral_account.types.jurisdiction_code.JurisdictionCode"
    ]
    """<p>The specific legal jurisdiction or state where the business was incorporated or registered, providing additional location context beyond the country code.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessVerificationDetails) -> dict:
    out: dict = {}
    out["LegalName"] = value["legal_name"]
    out["RegistrationId"] = value["registration_id"]
    out["CountryCode"] = value["country_code"]
    if "jurisdiction_of_incorporation" in value:
        out["JurisdictionOfIncorporation"] = value["jurisdiction_of_incorporation"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BusinessVerificationDetails:
    out: BusinessVerificationDetails = {}  # type: ignore[typeddict-item]
    if data.get("LegalName") is not None:
        out["legal_name"] = data["LegalName"]
    else:
        raise DeserializationError("BusinessVerificationDetails.legal_name required")
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "BusinessVerificationDetails.registration_id required"
        )
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    else:
        raise DeserializationError("BusinessVerificationDetails.country_code required")
    if data.get("JurisdictionOfIncorporation") is not None:
        out["jurisdiction_of_incorporation"] = data["JurisdictionOfIncorporation"]
    return out


def redact_sensitive(value: BusinessVerificationDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "legal_name" in value:
        out["legal_name"] = "*** Sensitive Data Redacted ***"
    if "registration_id" in value:
        out["registration_id"] = "*** Sensitive Data Redacted ***"
    return out
