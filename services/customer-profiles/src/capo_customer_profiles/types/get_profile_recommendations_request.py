"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetProfileRecommendationsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.candidate_id_list
    import capo_customer_profiles.types.max_size500
    import capo_customer_profiles.types.metadata_config
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommendation_diversity_config
    import capo_customer_profiles.types.recommender_context
    import capo_customer_profiles.types.recommender_filters
    import capo_customer_profiles.types.recommender_promotional_filters
    import capo_customer_profiles.types.uuid


class GetProfileRecommendationsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the profile for which to retrieve recommendations.</p>"""
    recommender_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the recommender.</p>"""
    context: NotRequired[
        "capo_customer_profiles.types.recommender_context.RecommenderContext"
    ]
    """<p>The contextual metadata used to provide dynamic runtime information to tailor recommendations.</p>"""
    recommender_filters: NotRequired[
        "capo_customer_profiles.types.recommender_filters.RecommenderFilters"
    ]
    """<p>A list of filters to apply to the returned recommendations. Filters define criteria for including or excluding items from the recommendation results.</p>"""
    recommender_promotional_filters: NotRequired[
        "capo_customer_profiles.types.recommender_promotional_filters.RecommenderPromotionalFilters"
    ]
    """<p>A list of promotional filters to apply to the recommendations. Promotional filters allow you to promote specific items within a configurable subset of recommendation results.</p>"""
    candidate_ids: NotRequired[
        "capo_customer_profiles.types.candidate_id_list.CandidateIdList"
    ]
    """<p>A list of item IDs to rank for the user. Use this when you want to re-rank a specific set of items rather than getting recommendations from the full item catalog. Required for personalized-ranking use cases.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size500.MaxSize500"]
    """<p>The maximum number of recommendations to return. The default value is 10.</p>"""
    metadata_config: NotRequired[
        "capo_customer_profiles.types.metadata_config.MetadataConfig"
    ]
    """<p>Configuration for including item metadata in the recommendation response. Use this to specify which metadata columns to return alongside recommended items.</p>"""
    diversity_config: NotRequired[
        "capo_customer_profiles.types.recommendation_diversity_config.RecommendationDiversityConfig"
    ]
    """<p>Runtime diversity configuration for this request. Enables diversity-aware recommendations and optionally supplies values for placeholder-based diversity caps configured on the recommender.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileRecommendationsRequest) -> dict:
    out: dict = {}
    out["RecommenderName"] = value["recommender_name"]
    if "context" in value:
        import capo_customer_profiles.types.recommender_context

        out["Context"] = (
            capo_customer_profiles.types.recommender_context.serialize_json(
                value["context"]
            )
        )
    if "recommender_filters" in value:
        import capo_customer_profiles.types.recommender_filters

        out["RecommenderFilters"] = (
            capo_customer_profiles.types.recommender_filters.serialize_json(
                value["recommender_filters"]
            )
        )
    if "recommender_promotional_filters" in value:
        import capo_customer_profiles.types.recommender_promotional_filters

        out["RecommenderPromotionalFilters"] = (
            capo_customer_profiles.types.recommender_promotional_filters.serialize_json(
                value["recommender_promotional_filters"]
            )
        )
    if "candidate_ids" in value:
        import capo_customer_profiles.types.candidate_id_list

        out["CandidateIds"] = (
            capo_customer_profiles.types.candidate_id_list.serialize_json(
                value["candidate_ids"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "metadata_config" in value:
        import capo_customer_profiles.types.metadata_config

        out["MetadataConfig"] = (
            capo_customer_profiles.types.metadata_config.serialize_json(
                value["metadata_config"]
            )
        )
    if "diversity_config" in value:
        import capo_customer_profiles.types.recommendation_diversity_config

        out["DiversityConfig"] = (
            capo_customer_profiles.types.recommendation_diversity_config.serialize_json(
                value["diversity_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetProfileRecommendationsRequest:
    out: GetProfileRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderName") is not None:
        out["recommender_name"] = data["RecommenderName"]
    else:
        out["recommender_name"] = ""
    if data.get("Context") is not None:
        import capo_customer_profiles.types.recommender_context

        out["context"] = (
            capo_customer_profiles.types.recommender_context.deserialize_json(
                data["Context"]
            )
        )
    if data.get("RecommenderFilters") is not None:
        import capo_customer_profiles.types.recommender_filters

        out["recommender_filters"] = (
            capo_customer_profiles.types.recommender_filters.deserialize_json(
                data["RecommenderFilters"]
            )
        )
    if data.get("RecommenderPromotionalFilters") is not None:
        import capo_customer_profiles.types.recommender_promotional_filters

        out["recommender_promotional_filters"] = (
            capo_customer_profiles.types.recommender_promotional_filters.deserialize_json(
                data["RecommenderPromotionalFilters"]
            )
        )
    if data.get("CandidateIds") is not None:
        import capo_customer_profiles.types.candidate_id_list

        out["candidate_ids"] = (
            capo_customer_profiles.types.candidate_id_list.deserialize_json(
                data["CandidateIds"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("MetadataConfig") is not None:
        import capo_customer_profiles.types.metadata_config

        out["metadata_config"] = (
            capo_customer_profiles.types.metadata_config.deserialize_json(
                data["MetadataConfig"]
            )
        )
    if data.get("DiversityConfig") is not None:
        import capo_customer_profiles.types.recommendation_diversity_config

        out["diversity_config"] = (
            capo_customer_profiles.types.recommendation_diversity_config.deserialize_json(
                data["DiversityConfig"]
            )
        )
    return out


def redact_sensitive(value: GetProfileRecommendationsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "context" in value:
        out["context"] = "*** Sensitive Data Redacted ***"
    if "recommender_filters" in value:
        import capo_customer_profiles.types.recommender_filters

        out["recommender_filters"] = (
            capo_customer_profiles.types.recommender_filters.redact_sensitive(
                value["recommender_filters"]
            )
        )
    if "recommender_promotional_filters" in value:
        import capo_customer_profiles.types.recommender_promotional_filters

        out["recommender_promotional_filters"] = (
            capo_customer_profiles.types.recommender_promotional_filters.redact_sensitive(
                value["recommender_promotional_filters"]
            )
        )
    return out
