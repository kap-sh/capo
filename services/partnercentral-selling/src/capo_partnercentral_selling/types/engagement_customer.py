"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementCustomer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.company_name
    import capo_partnercentral_selling.types.company_website_url
    import capo_partnercentral_selling.types.country_code
    import capo_partnercentral_selling.types.industry


class EngagementCustomer(TypedDict, closed=True):
    industry: "capo_partnercentral_selling.types.industry.Industry"
    """<p>Specifies the industry to which the customer’s company belongs. This field helps categorize the opportunity based on the customer’s business sector.</p>"""
    company_name: "capo_partnercentral_selling.types.company_name.CompanyName"
    """<p>Represents the name of the customer’s company associated with the Engagement Invitation. This field is used to identify the customer.</p>"""
    website_url: (
        "capo_partnercentral_selling.types.company_website_url.CompanyWebsiteUrl"
    )
    """<p>Provides the website URL of the customer’s company. This field helps partners verify the legitimacy and size of the customer organization.</p>"""
    country_code: "capo_partnercentral_selling.types.country_code.CountryCode"
    """<p>Indicates the country in which the customer’s company operates. This field is useful for understanding regional requirements or compliance needs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementCustomer) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.industry

    out["Industry"] = capo_partnercentral_selling.types.industry.serialize_aws_json_1_0(
        value["industry"]
    )
    out["CompanyName"] = value["company_name"]
    out["WebsiteUrl"] = value["website_url"]
    import capo_partnercentral_selling.types.country_code

    out["CountryCode"] = (
        capo_partnercentral_selling.types.country_code.serialize_aws_json_1_0(
            value["country_code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementCustomer:
    out: EngagementCustomer = {}  # type: ignore[typeddict-item]
    if data.get("Industry") is not None:
        import capo_partnercentral_selling.types.industry

        out["industry"] = (
            capo_partnercentral_selling.types.industry.deserialize_aws_json_1_0(
                data["Industry"]
            )
        )
    else:
        raise DeserializationError("EngagementCustomer.industry required")
    if data.get("CompanyName") is not None:
        out["company_name"] = data["CompanyName"]
    else:
        raise DeserializationError("EngagementCustomer.company_name required")
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    else:
        raise DeserializationError("EngagementCustomer.website_url required")
    if data.get("CountryCode") is not None:
        import capo_partnercentral_selling.types.country_code

        out["country_code"] = (
            capo_partnercentral_selling.types.country_code.deserialize_aws_json_1_0(
                data["CountryCode"]
            )
        )
    else:
        raise DeserializationError("EngagementCustomer.country_code required")
    return out


def redact_sensitive(value: EngagementCustomer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "company_name" in value:
        out["company_name"] = "*** Sensitive Data Redacted ***"
    if "website_url" in value:
        out["website_url"] = "*** Sensitive Data Redacted ***"
    if "country_code" in value:
        out["country_code"] = "*** Sensitive Data Redacted ***"
    return out
