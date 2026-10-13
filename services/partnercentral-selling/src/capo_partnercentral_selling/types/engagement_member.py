"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementMember``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account
    import capo_partnercentral_selling.types.member_company_name


class EngagementMember(TypedDict, closed=True):
    company_name: NotRequired[
        "capo_partnercentral_selling.types.member_company_name.MemberCompanyName"
    ]
    """<p>The official name of the member's company or organization.</p>"""
    website_url: NotRequired["str"]
    """<p>The URL of the member company's website. This offers a way to find more information about the member organization and serves as an additional identifier. </p>"""
    account_id: NotRequired["capo_partnercentral_selling.types.aws_account.AwsAccount"]
    """<p>This is the unique identifier for the AWS account associated with the member organization. It's used for AWS-related operations and identity verification. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementMember) -> dict:
    out: dict = {}
    if "company_name" in value:
        out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementMember:
    out: EngagementMember = {}  # type: ignore[typeddict-item]
    if data.get("CompanyName") is not None:
        out["company_name"] = data["CompanyName"]
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out


def redact_sensitive(value: EngagementMember) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "company_name" in value:
        out["company_name"] = "*** Sensitive Data Redacted ***"
    if "account_id" in value:
        out["account_id"] = "*** Sensitive Data Redacted ***"
    return out
