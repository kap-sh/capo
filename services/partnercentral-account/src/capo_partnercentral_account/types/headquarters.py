"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#Headquarters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.country_code
    import capo_partnercentral_account.types.subdivision_code


class Headquarters(TypedDict, closed=True):
    country_code: "capo_partnercentral_account.types.country_code.CountryCode"
    """<p>The ISO 3166-1 alpha-2 country code of the partner's headquarters. For example, <code>US</code>, <code>BR</code>, or <code>DE</code>.</p>"""
    subdivision_code: (
        "capo_partnercentral_account.types.subdivision_code.SubdivisionCode"
    )
    """<p>The subdivision portion of the ISO 3166-2 code for the partner's headquarters (for example, <code>SP</code> from <code>BR-SP</code>, <code>NSW</code> from <code>AU-NSW</code>, or <code>13</code> from <code>JP-13</code>).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Headquarters) -> dict:
    out: dict = {}
    out["CountryCode"] = value["country_code"]
    out["SubdivisionCode"] = value["subdivision_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Headquarters:
    out: Headquarters = {}  # type: ignore[typeddict-item]
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    else:
        out["country_code"] = ""
    if data.get("SubdivisionCode") is not None:
        out["subdivision_code"] = data["SubdivisionCode"]
    else:
        out["subdivision_code"] = ""
    return out
