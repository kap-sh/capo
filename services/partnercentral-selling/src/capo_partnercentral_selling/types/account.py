"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Account``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.address
    import capo_partnercentral_selling.types.aws_account
    import capo_partnercentral_selling.types.duns_number
    import capo_partnercentral_selling.types.industry
    import capo_partnercentral_selling.types.name
    import capo_partnercentral_selling.types.website_url


class Account(TypedDict, closed=True):
    industry: NotRequired["capo_partnercentral_selling.types.industry.Industry"]
    """<p>Specifies the industry the end <code>Customer</code> belongs to that's associated with the <code>Opportunity</code>. It refers to the category or sector where the customer's business operates. This is a required field.</p>"""
    other_industry: NotRequired["str"]
    """<p>Specifies the end <code>Customer</code>'s industry associated with the <code>Opportunity</code>, when the selected value in the <code>Industry</code> field is <code>Other</code>.</p>"""
    company_name: "capo_partnercentral_selling.types.name.Name"
    """<p>Specifies the end <code>Customer</code>'s company name associated with the <code>Opportunity</code>.</p>"""
    website_url: NotRequired["capo_partnercentral_selling.types.website_url.WebsiteUrl"]
    """<p>Specifies the end customer's company website URL associated with the <code>Opportunity</code>. This value is crucial to map the customer within the Amazon Web Services CRM system. This field is required in all cases except when the opportunity is related to national security.</p>"""
    aws_account_id: NotRequired[
        "capo_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>Specifies the <code>Customer</code> Amazon Web Services account ID associated with the <code>Opportunity</code>.</p>"""
    address: NotRequired["capo_partnercentral_selling.types.address.Address"]
    """<p>Specifies the end <code>Customer</code>'s address details associated with the <code>Opportunity</code>.</p>"""
    duns: NotRequired["capo_partnercentral_selling.types.duns_number.DunsNumber"]
    """<p>Indicates the <code>Customer</code> DUNS number, if available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Account) -> dict:
    out: dict = {}
    if "industry" in value:
        import capo_partnercentral_selling.types.industry

        out["Industry"] = (
            capo_partnercentral_selling.types.industry.serialize_aws_json_1_0(
                value["industry"]
            )
        )
    if "other_industry" in value:
        out["OtherIndustry"] = value["other_industry"]
    out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "address" in value:
        import capo_partnercentral_selling.types.address

        out["Address"] = (
            capo_partnercentral_selling.types.address.serialize_aws_json_1_0(
                value["address"]
            )
        )
    if "duns" in value:
        out["Duns"] = value["duns"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if data.get("Industry") is not None:
        import capo_partnercentral_selling.types.industry

        out["industry"] = (
            capo_partnercentral_selling.types.industry.deserialize_aws_json_1_0(
                data["Industry"]
            )
        )
    if data.get("OtherIndustry") is not None:
        out["other_industry"] = data["OtherIndustry"]
    if data.get("CompanyName") is not None:
        out["company_name"] = data["CompanyName"]
    else:
        out["company_name"] = ""
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    if data.get("Address") is not None:
        import capo_partnercentral_selling.types.address

        out["address"] = (
            capo_partnercentral_selling.types.address.deserialize_aws_json_1_0(
                data["Address"]
            )
        )
    if data.get("Duns") is not None:
        out["duns"] = data["Duns"]
    return out


def redact_sensitive(value: Account) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "company_name" in value:
        out["company_name"] = "*** Sensitive Data Redacted ***"
    if "website_url" in value:
        out["website_url"] = "*** Sensitive Data Redacted ***"
    if "aws_account_id" in value:
        out["aws_account_id"] = "*** Sensitive Data Redacted ***"
    if "address" in value:
        import capo_partnercentral_selling.types.address

        out["address"] = capo_partnercentral_selling.types.address.redact_sensitive(
            value["address"]
        )
    if "duns" in value:
        out["duns"] = "*** Sensitive Data Redacted ***"
    return out
