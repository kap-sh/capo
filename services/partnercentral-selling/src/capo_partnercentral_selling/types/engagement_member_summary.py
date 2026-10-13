"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementMemberSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.member_company_name


class EngagementMemberSummary(TypedDict, closed=True):
    company_name: NotRequired[
        "capo_partnercentral_selling.types.member_company_name.MemberCompanyName"
    ]
    """<p>The official name of the member's company or organization.</p>"""
    website_url: NotRequired["str"]
    """<p>The URL of the member company's website. This offers a way to find more information about the member organization and serves as an additional identifier. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementMemberSummary) -> dict:
    out: dict = {}
    if "company_name" in value:
        out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementMemberSummary:
    out: EngagementMemberSummary = {}  # type: ignore[typeddict-item]
    if data.get("CompanyName") is not None:
        out["company_name"] = data["CompanyName"]
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    return out


def redact_sensitive(value: EngagementMemberSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "company_name" in value:
        out["company_name"] = "*** Sensitive Data Redacted ***"
    return out
