"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetRecommenderFilterResponse``."""

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


class GetRecommenderFilterResponse(TypedDict, closed=True):
    recommender_filter_name: (
        "capo_customer_profiles.types.recommender_filter_name.RecommenderFilterName"
    )
    """<p>The name of the recommender filter.</p>"""
    recommender_filter_expression: "capo_customer_profiles.types.recommender_filter_expression.RecommenderFilterExpression"
    """<p>The filter expression that defines which items to include or exclude from recommendations.</p>"""
    recommender_schema_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender schema associated with this recommender filter.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the recommender filter was created.</p>"""
    status: (
        "capo_customer_profiles.types.recommender_filter_status.RecommenderFilterStatus"
    )
    """<p>The status of the recommender filter.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the recommender filter.</p>"""
    failure_reason: NotRequired["str"]
    """<p>If the recommender filter failed, provides the reason for the failure.</p>"""
    tags: "capo_customer_profiles.types.tag_map.TagMap"
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderFilterResponse) -> dict:
    out: dict = {}
    out["RecommenderFilterName"] = value["recommender_filter_name"]
    out["RecommenderFilterExpression"] = value["recommender_filter_expression"]
    if "recommender_schema_name" in value:
        out["RecommenderSchemaName"] = value["recommender_schema_name"]
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.recommender_filter_status

    out["Status"] = (
        capo_customer_profiles.types.recommender_filter_status.serialize_json(
            value["status"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    import capo_customer_profiles.types.tag_map

    out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetRecommenderFilterResponse:
    out: GetRecommenderFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderFilterName") is not None:
        out["recommender_filter_name"] = data["RecommenderFilterName"]
    else:
        out["recommender_filter_name"] = ""
    if data.get("RecommenderFilterExpression") is not None:
        out["recommender_filter_expression"] = data["RecommenderFilterExpression"]
    else:
        out["recommender_filter_expression"] = ""
    if data.get("RecommenderSchemaName") is not None:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Status") is not None:
        import capo_customer_profiles.types.recommender_filter_status

        out["status"] = (
            capo_customer_profiles.types.recommender_filter_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_customer_profiles.types.recommender_filter_status.RecommenderFilterStatus",
            "",
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    else:
        out["tags"] = {}
    return out


def redact_sensitive(value: GetRecommenderFilterResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommender_filter_expression" in value:
        out["recommender_filter_expression"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
