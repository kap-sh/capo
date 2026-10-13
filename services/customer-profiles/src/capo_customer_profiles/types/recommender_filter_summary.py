"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderFilterSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_filter_expression
    import capo_customer_profiles.types.recommender_filter_name
    import capo_customer_profiles.types.recommender_filter_status
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class RecommenderFilterSummary(TypedDict, closed=True):
    recommender_filter_name: NotRequired[
        "capo_customer_profiles.types.recommender_filter_name.RecommenderFilterName"
    ]
    """<p>The name of the recommender filter.</p>"""
    recommender_schema_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender schema associated with this recommender filter.</p>"""
    recommender_filter_expression: NotRequired[
        "capo_customer_profiles.types.recommender_filter_expression.RecommenderFilterExpression"
    ]
    """<p>The filter expression that defines which items to include or exclude from recommendations.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the recommender filter was created.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>A description of the recommender filter's purpose and characteristics.</p>"""
    status: NotRequired[
        "capo_customer_profiles.types.recommender_filter_status.RecommenderFilterStatus"
    ]
    """<p>The current operational status of the recommender filter.</p>"""
    failure_reason: NotRequired["str"]
    """<p>If the recommender filter is in a failed state, provides the reason for the failure.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderFilterSummary) -> dict:
    out: dict = {}
    if "recommender_filter_name" in value:
        out["RecommenderFilterName"] = value["recommender_filter_name"]
    if "recommender_schema_name" in value:
        out["RecommenderSchemaName"] = value["recommender_schema_name"]
    if "recommender_filter_expression" in value:
        out["RecommenderFilterExpression"] = value["recommender_filter_expression"]
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_customer_profiles.types.recommender_filter_status

        out["Status"] = (
            capo_customer_profiles.types.recommender_filter_status.serialize_json(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RecommenderFilterSummary:
    out: RecommenderFilterSummary = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderFilterName") is not None:
        out["recommender_filter_name"] = data["RecommenderFilterName"]
    if data.get("RecommenderSchemaName") is not None:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    if data.get("RecommenderFilterExpression") is not None:
        out["recommender_filter_expression"] = data["RecommenderFilterExpression"]
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_customer_profiles.types.recommender_filter_status

        out["status"] = (
            capo_customer_profiles.types.recommender_filter_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: RecommenderFilterSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommender_filter_expression" in value:
        out["recommender_filter_expression"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
