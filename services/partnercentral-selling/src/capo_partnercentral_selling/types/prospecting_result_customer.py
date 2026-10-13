"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProspectingResultCustomer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.country_code
    import capo_partnercentral_selling.types.eligible_programs_list
    import capo_partnercentral_selling.types.industry
    import capo_partnercentral_selling.types.prospecting_account_name
    import capo_partnercentral_selling.types.prospecting_company_size
    import capo_partnercentral_selling.types.prospecting_geo
    import capo_partnercentral_selling.types.prospecting_public_profile_summary
    import capo_partnercentral_selling.types.prospecting_region
    import capo_partnercentral_selling.types.prospecting_segment
    import capo_partnercentral_selling.types.prospecting_sub_industry
    import capo_partnercentral_selling.types.prospecting_sub_region


class ProspectingResultCustomer(TypedDict, closed=True):
    account_name: NotRequired[
        "capo_partnercentral_selling.types.prospecting_account_name.ProspectingAccountName"
    ]
    """<p>The name of the prospected customer account.</p>"""
    geo: NotRequired["capo_partnercentral_selling.types.prospecting_geo.ProspectingGeo"]
    """<p>The geographic region classification of the prospected customer account.</p>"""
    region: NotRequired[
        "capo_partnercentral_selling.types.prospecting_region.ProspectingRegion"
    ]
    """<p>The specific region of the prospected customer account.</p>"""
    sub_region: NotRequired[
        "capo_partnercentral_selling.types.prospecting_sub_region.ProspectingSubRegion"
    ]
    """<p>The subregion classification of the prospected customer account.</p>"""
    country: NotRequired["capo_partnercentral_selling.types.country_code.CountryCode"]
    """<p>The country code of the prospected customer account.</p>"""
    industry: NotRequired["capo_partnercentral_selling.types.industry.Industry"]
    """<p>The industry classification of the prospected customer account.</p>"""
    sub_industry: NotRequired[
        "capo_partnercentral_selling.types.prospecting_sub_industry.ProspectingSubIndustry"
    ]
    """<p>The sub-industry classification of the prospected customer account. This provides more granular categorization within the primary industry.</p>"""
    segment: NotRequired[
        "capo_partnercentral_selling.types.prospecting_segment.ProspectingSegment"
    ]
    """<p>The market segment classification of the prospected customer account.</p>"""
    company_size: NotRequired[
        "capo_partnercentral_selling.types.prospecting_company_size.ProspectingCompanySize"
    ]
    """<p>The company size classification of the prospected customer account.</p>"""
    eligible_programs: NotRequired[
        "capo_partnercentral_selling.types.eligible_programs_list.EligibleProgramsList"
    ]
    """<p>A list of AWS Greenfield programs that the prospected customer is eligible for. Use this list to identify relevant go-to-market opportunities.</p>"""
    public_profile_summary: NotRequired[
        "capo_partnercentral_selling.types.prospecting_public_profile_summary.ProspectingPublicProfileSummary"
    ]
    """<p>A summary of publicly available information about the prospected customer. The system uses this summary to generate customer insights and inform engagement strategies.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProspectingResultCustomer) -> dict:
    out: dict = {}
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "geo" in value:
        out["Geo"] = value["geo"]
    if "region" in value:
        out["Region"] = value["region"]
    if "sub_region" in value:
        out["SubRegion"] = value["sub_region"]
    if "country" in value:
        import capo_partnercentral_selling.types.country_code

        out["Country"] = (
            capo_partnercentral_selling.types.country_code.serialize_aws_json_1_0(
                value["country"]
            )
        )
    if "industry" in value:
        import capo_partnercentral_selling.types.industry

        out["Industry"] = (
            capo_partnercentral_selling.types.industry.serialize_aws_json_1_0(
                value["industry"]
            )
        )
    if "sub_industry" in value:
        out["SubIndustry"] = value["sub_industry"]
    if "segment" in value:
        out["Segment"] = value["segment"]
    if "company_size" in value:
        out["CompanySize"] = value["company_size"]
    if "eligible_programs" in value:
        import capo_partnercentral_selling.types.eligible_programs_list

        out["EligiblePrograms"] = (
            capo_partnercentral_selling.types.eligible_programs_list.serialize_aws_json_1_0(
                value["eligible_programs"]
            )
        )
    if "public_profile_summary" in value:
        out["PublicProfileSummary"] = value["public_profile_summary"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProspectingResultCustomer:
    out: ProspectingResultCustomer = {}  # type: ignore[typeddict-item]
    if data.get("AccountName") is not None:
        out["account_name"] = data["AccountName"]
    if data.get("Geo") is not None:
        out["geo"] = data["Geo"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("SubRegion") is not None:
        out["sub_region"] = data["SubRegion"]
    if data.get("Country") is not None:
        import capo_partnercentral_selling.types.country_code

        out["country"] = (
            capo_partnercentral_selling.types.country_code.deserialize_aws_json_1_0(
                data["Country"]
            )
        )
    if data.get("Industry") is not None:
        import capo_partnercentral_selling.types.industry

        out["industry"] = (
            capo_partnercentral_selling.types.industry.deserialize_aws_json_1_0(
                data["Industry"]
            )
        )
    if data.get("SubIndustry") is not None:
        out["sub_industry"] = data["SubIndustry"]
    if data.get("Segment") is not None:
        out["segment"] = data["Segment"]
    if data.get("CompanySize") is not None:
        out["company_size"] = data["CompanySize"]
    if data.get("EligiblePrograms") is not None:
        import capo_partnercentral_selling.types.eligible_programs_list

        out["eligible_programs"] = (
            capo_partnercentral_selling.types.eligible_programs_list.deserialize_aws_json_1_0(
                data["EligiblePrograms"]
            )
        )
    if data.get("PublicProfileSummary") is not None:
        out["public_profile_summary"] = data["PublicProfileSummary"]
    return out


def redact_sensitive(value: ProspectingResultCustomer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "country" in value:
        out["country"] = "*** Sensitive Data Redacted ***"
    return out
