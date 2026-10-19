"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderFilterRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_filter_expression
    import capo_customer_profiles.types.recommender_filter_name
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.tag_map


class CreateRecommenderFilterRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_filter_name: (
        "capo_customer_profiles.types.recommender_filter_name.RecommenderFilterName"
    )
    """<p>The name of the recommender filter. The name must be unique within the domain.</p>"""
    recommender_filter_expression: "capo_customer_profiles.types.recommender_filter_expression.RecommenderFilterExpression"
    """<p>The filter expression that defines which items to include or exclude from recommendations.</p>"""
    recommender_schema_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender schema to use for this recommender filter. If not specified, the default schema is used.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>A description of the recommender filter.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderFilterRequest) -> dict:
    out: dict = {}
    out["RecommenderFilterExpression"] = value["recommender_filter_expression"]
    if "recommender_schema_name" in value:
        out["RecommenderSchemaName"] = value["recommender_schema_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRecommenderFilterRequest:
    out: CreateRecommenderFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderFilterExpression") is not None:
        out["recommender_filter_expression"] = data["RecommenderFilterExpression"]
    else:
        out["recommender_filter_expression"] = ""
    if data.get("RecommenderSchemaName") is not None:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateRecommenderFilterRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommender_filter_expression" in value:
        out["recommender_filter_expression"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
