"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_config
    import capo_customer_profiles.types.recommender_recipe_name
    import capo_customer_profiles.types.recommender_status
    import capo_customer_profiles.types.recommender_update
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class RecommenderSummary(TypedDict, closed=True):
    recommender_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender.</p>"""
    recipe_name: NotRequired[
        "capo_customer_profiles.types.recommender_recipe_name.RecommenderRecipeName"
    ]
    """<p>The name of the recipe used by this recommender.</p>"""
    recommender_schema_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender schema associated with this recommender.</p>"""
    recommender_config: NotRequired[
        "capo_customer_profiles.types.recommender_config.RecommenderConfig"
    ]
    """<p>The configuration settings applied to this recommender.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the recommender was created.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>A description of the recommender's purpose and characteristics.</p>"""
    status: NotRequired[
        "capo_customer_profiles.types.recommender_status.RecommenderStatus"
    ]
    """<p>The current operational status of the recommender.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the recommender was edited.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    failure_reason: NotRequired["str"]
    """<p>If the recommender is in a failed state, provides the reason for the failure.</p>"""
    latest_recommender_update: NotRequired[
        "capo_customer_profiles.types.recommender_update.RecommenderUpdate"
    ]
    """<p>Information about the most recent update performed on the recommender, including its status and timing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderSummary) -> dict:
    out: dict = {}
    if "recommender_name" in value:
        out["RecommenderName"] = value["recommender_name"]
    if "recipe_name" in value:
        import capo_customer_profiles.types.recommender_recipe_name

        out["RecipeName"] = (
            capo_customer_profiles.types.recommender_recipe_name.serialize_json(
                value["recipe_name"]
            )
        )
    if "recommender_schema_name" in value:
        out["RecommenderSchemaName"] = value["recommender_schema_name"]
    if "recommender_config" in value:
        import capo_customer_profiles.types.recommender_config

        out["RecommenderConfig"] = (
            capo_customer_profiles.types.recommender_config.serialize_json(
                value["recommender_config"]
            )
        )
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_customer_profiles.types.recommender_status

        out["Status"] = capo_customer_profiles.types.recommender_status.serialize_json(
            value["status"]
        )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "latest_recommender_update" in value:
        import capo_customer_profiles.types.recommender_update

        out["LatestRecommenderUpdate"] = (
            capo_customer_profiles.types.recommender_update.serialize_json(
                value["latest_recommender_update"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecommenderSummary:
    out: RecommenderSummary = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderName") is not None:
        out["recommender_name"] = data["RecommenderName"]
    if data.get("RecipeName") is not None:
        import capo_customer_profiles.types.recommender_recipe_name

        out["recipe_name"] = (
            capo_customer_profiles.types.recommender_recipe_name.deserialize_json(
                data["RecipeName"]
            )
        )
    if data.get("RecommenderSchemaName") is not None:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    if data.get("RecommenderConfig") is not None:
        import capo_customer_profiles.types.recommender_config

        out["recommender_config"] = (
            capo_customer_profiles.types.recommender_config.deserialize_json(
                data["RecommenderConfig"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_customer_profiles.types.recommender_status

        out["status"] = (
            capo_customer_profiles.types.recommender_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("LatestRecommenderUpdate") is not None:
        import capo_customer_profiles.types.recommender_update

        out["latest_recommender_update"] = (
            capo_customer_profiles.types.recommender_update.deserialize_json(
                data["LatestRecommenderUpdate"]
            )
        )
    return out


def redact_sensitive(value: RecommenderSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
