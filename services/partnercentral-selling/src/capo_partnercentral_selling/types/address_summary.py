"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AddressSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.address_part
    import capo_partnercentral_selling.types.country_code


class AddressSummary(TypedDict, closed=True):
    city: NotRequired["capo_partnercentral_selling.types.address_part.AddressPart"]
    """<p>Specifies the end <code>Customer</code>'s city associated with the <code>Opportunity</code>.</p>"""
    postal_code: NotRequired[
        "capo_partnercentral_selling.types.address_part.AddressPart"
    ]
    """<p>Specifies the end <code>Customer</code>'s postal code associated with the <code>Opportunity</code>.</p>"""
    state_or_region: NotRequired[
        "capo_partnercentral_selling.types.address_part.AddressPart"
    ]
    """<p>Specifies the end <code>Customer</code>'s state or region associated with the <code>Opportunity</code>.</p> <p>Valid values: <code>Alabama | Alaska | American Samoa | Arizona | Arkansas | California | Colorado | Connecticut | Delaware | Dist. of Columbia | Federated States of Micronesia | Florida | Georgia | Guam | Hawaii | Idaho | Illinois | Indiana | Iowa | Kansas | Kentucky | Louisiana | Maine | Marshall Islands | Maryland | Massachusetts | Michigan | Minnesota | Mississippi | Missouri | Montana | Nebraska | Nevada | New Hampshire | New Jersey | New Mexico | New York | North Carolina | North Dakota | Northern Mariana Islands | Ohio | Oklahoma | Oregon | Palau | Pennsylvania | Puerto Rico | Rhode Island | South Carolina | South Dakota | Tennessee | Texas | Utah | Vermont | Virginia | Virgin Islands | Washington | West Virginia | Wisconsin | Wyoming | APO/AE | AFO/FPO | FPO, AP</code> </p>"""
    country_code: NotRequired[
        "capo_partnercentral_selling.types.country_code.CountryCode"
    ]
    """<p>Specifies the end <code>Customer</code>'s country associated with the <code>Opportunity</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddressSummary) -> dict:
    out: dict = {}
    if "city" in value:
        out["City"] = value["city"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "state_or_region" in value:
        out["StateOrRegion"] = value["state_or_region"]
    if "country_code" in value:
        import capo_partnercentral_selling.types.country_code

        out["CountryCode"] = (
            capo_partnercentral_selling.types.country_code.serialize_aws_json_1_0(
                value["country_code"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AddressSummary:
    out: AddressSummary = {}  # type: ignore[typeddict-item]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    if data.get("StateOrRegion") is not None:
        out["state_or_region"] = data["StateOrRegion"]
    if data.get("CountryCode") is not None:
        import capo_partnercentral_selling.types.country_code

        out["country_code"] = (
            capo_partnercentral_selling.types.country_code.deserialize_aws_json_1_0(
                data["CountryCode"]
            )
        )
    return out


def redact_sensitive(value: AddressSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "city" in value:
        out["city"] = "*** Sensitive Data Redacted ***"
    if "postal_code" in value:
        out["postal_code"] = "*** Sensitive Data Redacted ***"
    if "state_or_region" in value:
        out["state_or_region"] = "*** Sensitive Data Redacted ***"
    if "country_code" in value:
        out["country_code"] = "*** Sensitive Data Redacted ***"
    return out
