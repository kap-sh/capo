"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadCustomer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_maturity
    import capo_partnercentral_selling.types.company_name
    import capo_partnercentral_selling.types.lead_address
    import capo_partnercentral_selling.types.lead_industry
    import capo_partnercentral_selling.types.lead_market_segment
    import capo_partnercentral_selling.types.lead_website_url


class LeadCustomer(TypedDict, closed=True):
    industry: NotRequired[
        "capo_partnercentral_selling.types.lead_industry.LeadIndustry"
    ]
    """<p>Specifies the industry sector to which the lead customer's company belongs. This categorization helps in understanding the customer's business context and tailoring appropriate solutions.</p>"""
    company_name: "capo_partnercentral_selling.types.company_name.CompanyName"
    """<p>The name of the lead customer's company. This field is essential for identifying and tracking the customer organization associated with the lead.</p>"""
    website_url: NotRequired[
        "capo_partnercentral_selling.types.lead_website_url.LeadWebsiteUrl"
    ]
    """<p>The website URL of the lead customer's company. This provides additional context about the customer organization and helps verify company legitimacy and size.</p>"""
    address: NotRequired["capo_partnercentral_selling.types.lead_address.LeadAddress"]
    """<p>The address information for the lead customer.</p>"""
    aws_maturity: NotRequired[
        "capo_partnercentral_selling.types.aws_maturity.AwsMaturity"
    ]
    """<p>Indicates the customer's level of experience and adoption with AWS services. This assessment helps determine the appropriate engagement approach and solution complexity.</p>"""
    market_segment: NotRequired[
        "capo_partnercentral_selling.types.lead_market_segment.LeadMarketSegment"
    ]
    """<p>Specifies the market segment classification of the lead customer, such as enterprise, mid-market, or small business. This segmentation helps in targeting appropriate solutions and engagement strategies.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadCustomer) -> dict:
    out: dict = {}
    if "industry" in value:
        out["Industry"] = value["industry"]
    out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    if "address" in value:
        import capo_partnercentral_selling.types.lead_address

        out["Address"] = (
            capo_partnercentral_selling.types.lead_address.serialize_aws_json_1_0(
                value["address"]
            )
        )
    if "aws_maturity" in value:
        out["AwsMaturity"] = value["aws_maturity"]
    if "market_segment" in value:
        out["MarketSegment"] = value["market_segment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadCustomer:
    out: LeadCustomer = {}  # type: ignore[typeddict-item]
    if data.get("Industry") is not None:
        out["industry"] = data["Industry"]
    if data.get("CompanyName") is not None:
        out["company_name"] = data["CompanyName"]
    else:
        raise DeserializationError("LeadCustomer.company_name required")
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    if data.get("Address") is not None:
        import capo_partnercentral_selling.types.lead_address

        out["address"] = (
            capo_partnercentral_selling.types.lead_address.deserialize_aws_json_1_0(
                data["Address"]
            )
        )
    if data.get("AwsMaturity") is not None:
        out["aws_maturity"] = data["AwsMaturity"]
    if data.get("MarketSegment") is not None:
        out["market_segment"] = data["MarketSegment"]
    return out


def redact_sensitive(value: LeadCustomer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "company_name" in value:
        out["company_name"] = "*** Sensitive Data Redacted ***"
    if "website_url" in value:
        out["website_url"] = "*** Sensitive Data Redacted ***"
    if "address" in value:
        import capo_partnercentral_selling.types.lead_address

        out["address"] = (
            capo_partnercentral_selling.types.lead_address.redact_sensitive(
                value["address"]
            )
        )
    return out
