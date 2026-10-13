"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadAddress``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.lead_country_code


class LeadAddress(TypedDict, closed=True):
    city: NotRequired["str"]
    """<p>The city of the lead customer's address.</p>"""
    postal_code: NotRequired["str"]
    """<p>The postal code of the lead customer's address.</p>"""
    state_or_region: NotRequired["str"]
    """<p>The state or region of the lead customer's address.</p>"""
    country_code: NotRequired[
        "capo_partnercentral_selling.types.lead_country_code.LeadCountryCode"
    ]
    """<p>The country code of the lead customer's address.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadAddress) -> dict:
    out: dict = {}
    if "city" in value:
        out["City"] = value["city"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "state_or_region" in value:
        out["StateOrRegion"] = value["state_or_region"]
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadAddress:
    out: LeadAddress = {}  # type: ignore[typeddict-item]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    if data.get("StateOrRegion") is not None:
        out["state_or_region"] = data["StateOrRegion"]
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    return out


def redact_sensitive(value: LeadAddress) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "country_code" in value:
        out["country_code"] = "*** Sensitive Data Redacted ***"
    return out
