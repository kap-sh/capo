"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.headquarters
    import capo_partnercentral_account.types.industry_segment_list
    import capo_partnercentral_account.types.locale
    import capo_partnercentral_account.types.localized_content_list
    import capo_partnercentral_account.types.partner_profile_id
    import capo_partnercentral_account.types.primary_solution_type
    import capo_partnercentral_account.types.unicode_string
    import capo_partnercentral_account.types.url


class PartnerProfile(TypedDict, closed=True):
    display_name: "capo_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The public display name for the partner organization.</p>"""
    description: "capo_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>A description of the partner's business, services, and capabilities.</p>"""
    website_url: "capo_partnercentral_account.types.url.Url"
    """<p>The partner's primary website URL.</p>"""
    logo_url: "capo_partnercentral_account.types.url.Url"
    """<p>The URL to the partner's logo image.</p>"""
    primary_solution_type: (
        "capo_partnercentral_account.types.primary_solution_type.PrimarySolutionType"
    )
    """<p>The primary type of solution or service the partner provides.</p>"""
    industry_segments: (
        "capo_partnercentral_account.types.industry_segment_list.IndustrySegmentList"
    )
    """<p>The industry segments or verticals that the partner serves.</p>"""
    translation_source_locale: "capo_partnercentral_account.types.locale.Locale"
    """<p>The source locale used for automatic translation of profile content.</p>"""
    localized_contents: NotRequired[
        "capo_partnercentral_account.types.localized_content_list.LocalizedContentList"
    ]
    """<p>A list of localized content versions for different languages and regions.</p>"""
    headquarters: NotRequired[
        "capo_partnercentral_account.types.headquarters.Headquarters"
    ]
    """<p>The ISO 3166 country and subdivision codes for the partner's headquarters location. If no headquarters location is set, this field is not included in the response.</p>"""
    profile_id: NotRequired[
        "capo_partnercentral_account.types.partner_profile_id.PartnerProfileId"
    ]
    """<p>The unique identifier of the partner profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerProfile) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    out["Description"] = value["description"]
    out["WebsiteUrl"] = value["website_url"]
    out["LogoUrl"] = value["logo_url"]
    import capo_partnercentral_account.types.primary_solution_type

    out["PrimarySolutionType"] = (
        capo_partnercentral_account.types.primary_solution_type.serialize_aws_json_1_0(
            value["primary_solution_type"]
        )
    )
    import capo_partnercentral_account.types.industry_segment_list

    out["IndustrySegments"] = (
        capo_partnercentral_account.types.industry_segment_list.serialize_aws_json_1_0(
            value["industry_segments"]
        )
    )
    out["TranslationSourceLocale"] = value["translation_source_locale"]
    if "localized_contents" in value:
        import capo_partnercentral_account.types.localized_content_list

        out["LocalizedContents"] = (
            capo_partnercentral_account.types.localized_content_list.serialize_aws_json_1_0(
                value["localized_contents"]
            )
        )
    if "headquarters" in value:
        import capo_partnercentral_account.types.headquarters

        out["Headquarters"] = (
            capo_partnercentral_account.types.headquarters.serialize_aws_json_1_0(
                value["headquarters"]
            )
        )
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PartnerProfile:
    out: PartnerProfile = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        out["display_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    else:
        out["website_url"] = ""
    if data.get("LogoUrl") is not None:
        out["logo_url"] = data["LogoUrl"]
    else:
        out["logo_url"] = ""
    if data.get("PrimarySolutionType") is not None:
        import capo_partnercentral_account.types.primary_solution_type

        out["primary_solution_type"] = (
            capo_partnercentral_account.types.primary_solution_type.deserialize_aws_json_1_0(
                data["PrimarySolutionType"]
            )
        )
    else:
        import typing

        out["primary_solution_type"] = typing.cast(
            "capo_partnercentral_account.types.primary_solution_type.PrimarySolutionType",
            "",
        )
    if data.get("IndustrySegments") is not None:
        import capo_partnercentral_account.types.industry_segment_list

        out["industry_segments"] = (
            capo_partnercentral_account.types.industry_segment_list.deserialize_aws_json_1_0(
                data["IndustrySegments"]
            )
        )
    else:
        out["industry_segments"] = []
    if data.get("TranslationSourceLocale") is not None:
        out["translation_source_locale"] = data["TranslationSourceLocale"]
    else:
        out["translation_source_locale"] = ""
    if data.get("LocalizedContents") is not None:
        import capo_partnercentral_account.types.localized_content_list

        out["localized_contents"] = (
            capo_partnercentral_account.types.localized_content_list.deserialize_aws_json_1_0(
                data["LocalizedContents"]
            )
        )
    if data.get("Headquarters") is not None:
        import capo_partnercentral_account.types.headquarters

        out["headquarters"] = (
            capo_partnercentral_account.types.headquarters.deserialize_aws_json_1_0(
                data["Headquarters"]
            )
        )
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    return out
