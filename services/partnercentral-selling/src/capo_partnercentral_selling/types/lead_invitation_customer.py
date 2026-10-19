"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadInvitationCustomer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_maturity
    import capo_partnercentral_selling.types.company_name
    import capo_partnercentral_selling.types.lead_country_code
    import capo_partnercentral_selling.types.lead_industry
    import capo_partnercentral_selling.types.lead_market_segment
    import capo_partnercentral_selling.types.lead_website_url


class LeadInvitationCustomer(TypedDict, closed=True):
    industry: NotRequired[
        "capo_partnercentral_selling.types.lead_industry.LeadIndustry"
    ]
    """<p>Specifies the industry sector of the customer company associated with the lead invitation. This categorization helps partners understand the customer's business context and assess solution fit.</p>"""
    company_name: "capo_partnercentral_selling.types.company_name.CompanyName"
    """<p>The name of the customer company associated with the lead invitation. This field identifies the target organization for the lead engagement opportunity.</p>"""
    website_url: NotRequired[
        "capo_partnercentral_selling.types.lead_website_url.LeadWebsiteUrl"
    ]
    """<p>The website URL of the customer company. This provides additional context about the customer organization and helps partners verify company details and assess business size and legitimacy.</p>"""
    country_code: "capo_partnercentral_selling.types.lead_country_code.LeadCountryCode"
    """<p>The country code indicating the geographic location of the customer company. This information helps partners understand regional requirements and assess their ability to serve the customer effectively.</p>"""
    aws_maturity: NotRequired[
        "capo_partnercentral_selling.types.aws_maturity.AwsMaturity"
    ]
    """<p>Indicates the customer's level of experience and adoption with AWS services. This assessment helps partners understand the customer's cloud maturity and tailor their engagement approach accordingly.</p>"""
    market_segment: NotRequired[
        "capo_partnercentral_selling.types.lead_market_segment.LeadMarketSegment"
    ]
    """<p>Specifies the market segment classification of the customer, such as enterprise, mid-market, or small business. This segmentation helps partners determine the appropriate solution complexity and engagement strategy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadInvitationCustomer) -> dict:
    out: dict = {}
    if "industry" in value:
        out["Industry"] = value["industry"]
    out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    out["CountryCode"] = value.get("country_code", "")
    if "aws_maturity" in value:
        out["AwsMaturity"] = value["aws_maturity"]
    if "market_segment" in value:
        out["MarketSegment"] = value["market_segment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadInvitationCustomer:
    out: LeadInvitationCustomer = {}  # type: ignore[typeddict-item]
    if data.get("Industry") is not None:
        out["industry"] = data["Industry"]
    if data.get("CompanyName") is not None:
        out["company_name"] = data["CompanyName"]
    else:
        out["company_name"] = ""
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    else:
        out["country_code"] = ""
    if data.get("AwsMaturity") is not None:
        out["aws_maturity"] = data["AwsMaturity"]
    if data.get("MarketSegment") is not None:
        out["market_segment"] = data["MarketSegment"]
    return out


def redact_sensitive(value: LeadInvitationCustomer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "company_name" in value:
        out["company_name"] = "*** Sensitive Data Redacted ***"
    if "website_url" in value:
        out["website_url"] = "*** Sensitive Data Redacted ***"
    if "country_code" in value:
        out["country_code"] = "*** Sensitive Data Redacted ***"
    return out
