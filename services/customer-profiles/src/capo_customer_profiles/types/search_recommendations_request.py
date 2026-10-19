"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SearchRecommendationsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.candidate_id_list
    import capo_customer_profiles.types.key_values_list
    import capo_customer_profiles.types.max_size500
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommendation_diversity_config
    import capo_customer_profiles.types.recommendation_metadata
    import capo_customer_profiles.types.recommender
    import capo_customer_profiles.types.recommender_context


class SearchRecommendationsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    key_name: "capo_customer_profiles.types.name.name"
    """<p>A searchable identifier of a customer profile. You can use a predefined key, such as <code>_profileId</code>, <code>_phone</code>, or <code>_email</code>, or a custom-defined key.</p>"""
    key_values: "capo_customer_profiles.types.key_values_list.KeyValuesList"
    """<p>A list of key values. Provide one value for each field of the search key.</p>"""
    recommender: "capo_customer_profiles.types.recommender.Recommender"
    """<p>The recommender used to generate the recommendations.</p>"""
    candidate_ids: NotRequired[
        "capo_customer_profiles.types.candidate_id_list.CandidateIdList"
    ]
    """<p>A list of item IDs to rank for the user. Use this when you want to re-rank a specific set of items rather than getting recommendations from the full item catalog. Required for personalized-ranking use cases.</p>"""
    context: NotRequired[
        "capo_customer_profiles.types.recommender_context.RecommenderContext"
    ]
    """<p>The contextual metadata used to provide dynamic runtime information to tailor recommendations.</p>"""
    diversity: NotRequired[
        "capo_customer_profiles.types.recommendation_diversity_config.RecommendationDiversityConfig"
    ]
    """<p>Runtime diversity configuration for this request. Enables diversity-aware recommendations and optionally supplies values for placeholder-based diversity caps configured on the recommender.</p>"""
    metadata: NotRequired[
        "capo_customer_profiles.types.recommendation_metadata.RecommendationMetadata"
    ]
    """<p>Configuration for metadata to include in recommendation responses.</p>"""
    max_recommendations: NotRequired[
        "capo_customer_profiles.types.max_size500.MaxSize500"
    ]
    """<p>The maximum number of recommendations to return. The default value is 5.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRecommendationsRequest) -> dict:
    out: dict = {}
    out["KeyName"] = value["key_name"]
    import capo_customer_profiles.types.key_values_list

    out["KeyValues"] = capo_customer_profiles.types.key_values_list.serialize_json(
        value["key_values"]
    )
    import capo_customer_profiles.types.recommender

    out["Recommender"] = capo_customer_profiles.types.recommender.serialize_json(
        value["recommender"]
    )
    if "candidate_ids" in value:
        import capo_customer_profiles.types.candidate_id_list

        out["CandidateIds"] = (
            capo_customer_profiles.types.candidate_id_list.serialize_json(
                value["candidate_ids"]
            )
        )
    if "context" in value:
        import capo_customer_profiles.types.recommender_context

        out["Context"] = (
            capo_customer_profiles.types.recommender_context.serialize_json(
                value["context"]
            )
        )
    if "diversity" in value:
        import capo_customer_profiles.types.recommendation_diversity_config

        out["Diversity"] = (
            capo_customer_profiles.types.recommendation_diversity_config.serialize_json(
                value["diversity"]
            )
        )
    if "metadata" in value:
        import capo_customer_profiles.types.recommendation_metadata

        out["Metadata"] = (
            capo_customer_profiles.types.recommendation_metadata.serialize_json(
                value["metadata"]
            )
        )
    if "max_recommendations" in value:
        out["MaxRecommendations"] = value["max_recommendations"]
    return out


def deserialize_json(data: dict) -> SearchRecommendationsRequest:
    out: SearchRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    else:
        out["key_name"] = ""
    if data.get("KeyValues") is not None:
        import capo_customer_profiles.types.key_values_list

        out["key_values"] = (
            capo_customer_profiles.types.key_values_list.deserialize_json(
                data["KeyValues"]
            )
        )
    else:
        out["key_values"] = []
    if data.get("Recommender") is not None:
        import capo_customer_profiles.types.recommender

        out["recommender"] = capo_customer_profiles.types.recommender.deserialize_json(
            data["Recommender"]
        )
    else:
        raise DeserializationError("SearchRecommendationsRequest.recommender required")
    if data.get("CandidateIds") is not None:
        import capo_customer_profiles.types.candidate_id_list

        out["candidate_ids"] = (
            capo_customer_profiles.types.candidate_id_list.deserialize_json(
                data["CandidateIds"]
            )
        )
    if data.get("Context") is not None:
        import capo_customer_profiles.types.recommender_context

        out["context"] = (
            capo_customer_profiles.types.recommender_context.deserialize_json(
                data["Context"]
            )
        )
    if data.get("Diversity") is not None:
        import capo_customer_profiles.types.recommendation_diversity_config

        out["diversity"] = (
            capo_customer_profiles.types.recommendation_diversity_config.deserialize_json(
                data["Diversity"]
            )
        )
    if data.get("Metadata") is not None:
        import capo_customer_profiles.types.recommendation_metadata

        out["metadata"] = (
            capo_customer_profiles.types.recommendation_metadata.deserialize_json(
                data["Metadata"]
            )
        )
    if data.get("MaxRecommendations") is not None:
        out["max_recommendations"] = data["MaxRecommendations"]
    return out


def redact_sensitive(value: SearchRecommendationsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key_values" in value:
        out["key_values"] = "*** Sensitive Data Redacted ***"
    if "recommender" in value:
        import capo_customer_profiles.types.recommender

        out["recommender"] = capo_customer_profiles.types.recommender.redact_sensitive(
            value["recommender"]
        )
    if "context" in value:
        out["context"] = "*** Sensitive Data Redacted ***"
    return out
