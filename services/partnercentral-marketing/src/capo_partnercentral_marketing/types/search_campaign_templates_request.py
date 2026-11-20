"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#SearchCampaignTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.aws_service_filter_list
    import capo_partnercentral_marketing.types.campaign_template_collection_filter_list
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.customer_segment_filter_list
    import capo_partnercentral_marketing.types.industry_filter_list
    import capo_partnercentral_marketing.types.language_filter_list
    import capo_partnercentral_marketing.types.max_results
    import capo_partnercentral_marketing.types.next_token
    import capo_partnercentral_marketing.types.template_search_text
    import capo_partnercentral_marketing.types.theme_filter_list
    import capo_partnercentral_marketing.types.use_case_filter_list


class SearchCampaignTemplatesRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox). AWS and Sandbox templates may differ."""
    search_text: NotRequired[
        "capo_partnercentral_marketing.types.template_search_text.TemplateSearchText"
    ]
    """Free-text query matched against the template's name and description. Any word may match, and the last word matches as a prefix when it has 3 or more characters, so `nov` finds Amazon Nova. A template whose name holds the query as a phrase ranks first, then whole-word matches, then prefix-only ones. Omit to browse the whole catalog. Text analysis is derived from each template's own LanguageCode, never from the language filter."""
    industry: NotRequired[
        "capo_partnercentral_marketing.types.industry_filter_list.IndustryFilterList"
    ]
    """Restrict to templates in these industries. Values within this member are OR-ed; distinct facet members are AND-ed. Exact, case-sensitive match."""
    use_case: NotRequired[
        "capo_partnercentral_marketing.types.use_case_filter_list.UseCaseFilterList"
    ]
    """Restrict to templates with these campaign use cases. Values within this member are OR-ed; distinct facet members are AND-ed. Exact, case-sensitive match."""
    language: NotRequired[
        "capo_partnercentral_marketing.types.language_filter_list.LanguageFilterList"
    ]
    """Restrict to templates in these language(s), matched by each template's `LanguageCode`. Values within this member are OR-ed; distinct facet members are AND-ed. Narrows results; it does not reinterpret SearchText."""
    aws_services: NotRequired[
        "capo_partnercentral_marketing.types.aws_service_filter_list.AwsServiceFilterList"
    ]
    """Restrict to templates promoting these AWS services. Values within this member are OR-ed; distinct facet members are AND-ed. Exact, case-sensitive match."""
    customer_segments: NotRequired[
        "capo_partnercentral_marketing.types.customer_segment_filter_list.CustomerSegmentFilterList"
    ]
    """Restrict to templates for these customer segments. Values within this member are OR-ed; distinct facet members are AND-ed. A template that names no customer segment matches every value."""
    themes: NotRequired[
        "capo_partnercentral_marketing.types.theme_filter_list.ThemeFilterList"
    ]
    """Restrict to templates with these themes. Values within this member are OR-ed; distinct facet members are AND-ed. A template that names no theme matches every value."""
    collection: NotRequired[
        "capo_partnercentral_marketing.types.campaign_template_collection_filter_list.CampaignTemplateCollectionFilterList"
    ]
    """Restrict to templates in these collections. Values within this member are OR-ed; distinct facet members are AND-ed. Omit for no restriction; there is no default."""
    max_results: NotRequired[
        "capo_partnercentral_marketing.types.max_results.MaxResults"
    ]
    """Maximum results per page."""
    next_token: NotRequired["capo_partnercentral_marketing.types.next_token.NextToken"]
    """Pagination token."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchCampaignTemplatesRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    if "search_text" in value:
        out["SearchText"] = value["search_text"]
    if "industry" in value:
        import capo_partnercentral_marketing.types.industry_filter_list

        out["Industry"] = (
            capo_partnercentral_marketing.types.industry_filter_list.serialize_cbor(
                value["industry"]
            )
        )
    if "use_case" in value:
        import capo_partnercentral_marketing.types.use_case_filter_list

        out["UseCase"] = (
            capo_partnercentral_marketing.types.use_case_filter_list.serialize_cbor(
                value["use_case"]
            )
        )
    if "language" in value:
        import capo_partnercentral_marketing.types.language_filter_list

        out["Language"] = (
            capo_partnercentral_marketing.types.language_filter_list.serialize_cbor(
                value["language"]
            )
        )
    if "aws_services" in value:
        import capo_partnercentral_marketing.types.aws_service_filter_list

        out["AwsServices"] = (
            capo_partnercentral_marketing.types.aws_service_filter_list.serialize_cbor(
                value["aws_services"]
            )
        )
    if "customer_segments" in value:
        import capo_partnercentral_marketing.types.customer_segment_filter_list

        out["CustomerSegments"] = (
            capo_partnercentral_marketing.types.customer_segment_filter_list.serialize_cbor(
                value["customer_segments"]
            )
        )
    if "themes" in value:
        import capo_partnercentral_marketing.types.theme_filter_list

        out["Themes"] = (
            capo_partnercentral_marketing.types.theme_filter_list.serialize_cbor(
                value["themes"]
            )
        )
    if "collection" in value:
        import capo_partnercentral_marketing.types.campaign_template_collection_filter_list

        out["Collection"] = (
            capo_partnercentral_marketing.types.campaign_template_collection_filter_list.serialize_cbor(
                value["collection"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> SearchCampaignTemplatesRequest:
    out: SearchCampaignTemplatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_marketing.types.catalog

        out["catalog"] = capo_partnercentral_marketing.types.catalog.deserialize_cbor(
            data["Catalog"]
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_marketing.types.catalog.Catalog", ""
        )
    if data.get("SearchText") is not None:
        out["search_text"] = data["SearchText"]
    if data.get("Industry") is not None:
        import capo_partnercentral_marketing.types.industry_filter_list

        out["industry"] = (
            capo_partnercentral_marketing.types.industry_filter_list.deserialize_cbor(
                data["Industry"]
            )
        )
    if data.get("UseCase") is not None:
        import capo_partnercentral_marketing.types.use_case_filter_list

        out["use_case"] = (
            capo_partnercentral_marketing.types.use_case_filter_list.deserialize_cbor(
                data["UseCase"]
            )
        )
    if data.get("Language") is not None:
        import capo_partnercentral_marketing.types.language_filter_list

        out["language"] = (
            capo_partnercentral_marketing.types.language_filter_list.deserialize_cbor(
                data["Language"]
            )
        )
    if data.get("AwsServices") is not None:
        import capo_partnercentral_marketing.types.aws_service_filter_list

        out["aws_services"] = (
            capo_partnercentral_marketing.types.aws_service_filter_list.deserialize_cbor(
                data["AwsServices"]
            )
        )
    if data.get("CustomerSegments") is not None:
        import capo_partnercentral_marketing.types.customer_segment_filter_list

        out["customer_segments"] = (
            capo_partnercentral_marketing.types.customer_segment_filter_list.deserialize_cbor(
                data["CustomerSegments"]
            )
        )
    if data.get("Themes") is not None:
        import capo_partnercentral_marketing.types.theme_filter_list

        out["themes"] = (
            capo_partnercentral_marketing.types.theme_filter_list.deserialize_cbor(
                data["Themes"]
            )
        )
    if data.get("Collection") is not None:
        import capo_partnercentral_marketing.types.campaign_template_collection_filter_list

        out["collection"] = (
            capo_partnercentral_marketing.types.campaign_template_collection_filter_list.deserialize_cbor(
                data["Collection"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
