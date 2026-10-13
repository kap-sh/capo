"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetRecommenderResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_config
    import capo_customer_profiles.types.recommender_recipe_name
    import capo_customer_profiles.types.recommender_status
    import capo_customer_profiles.types.recommender_update
    import capo_customer_profiles.types.recommender_version_name
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.training_metrics_list


class GetRecommenderResponse(TypedDict, closed=True):
    recommender_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the recommender.</p>"""
    recommender_recipe_name: (
        "capo_customer_profiles.types.recommender_recipe_name.RecommenderRecipeName"
    )
    """<p>The name of the recipe used by the recommender to generate recommendations.</p>"""
    recommender_schema_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender schema associated with this recommender.</p>"""
    recommender_config: NotRequired[
        "capo_customer_profiles.types.recommender_config.RecommenderConfig"
    ]
    """<p>The configuration settings for the recommender, including parameters and settings that define its behavior.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>A detailed description of the recommender providing information about its purpose and functionality.</p>"""
    status: NotRequired[
        "capo_customer_profiles.types.recommender_status.RecommenderStatus"
    ]
    """<p>The current status of the recommender, indicating whether it is active, creating, updating, or in another state.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the recommender was edited.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the recommender was created.</p>"""
    failure_reason: NotRequired["str"]
    """<p>If the recommender fails, provides the reason for the failure.</p>"""
    latest_recommender_update: NotRequired[
        "capo_customer_profiles.types.recommender_update.RecommenderUpdate"
    ]
    """<p>Information about the most recent update performed on the recommender, including status and timestamp.</p>"""
    active_recommender_version_name: NotRequired[
        "capo_customer_profiles.types.recommender_version_name.RecommenderVersionName"
    ]
    """<p>The name of the recommender version currently serving recommendations. Omitted when no active recommender version is set.</p>"""
    training_metrics: NotRequired[
        "capo_customer_profiles.types.training_metrics_list.TrainingMetricsList"
    ]
    """<p>A set of metrics that provide information about the recommender's training performance and accuracy.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderResponse) -> dict:
    out: dict = {}
    out["RecommenderName"] = value["recommender_name"]
    import capo_customer_profiles.types.recommender_recipe_name

    out["RecommenderRecipeName"] = (
        capo_customer_profiles.types.recommender_recipe_name.serialize_json(
            value["recommender_recipe_name"]
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
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "latest_recommender_update" in value:
        import capo_customer_profiles.types.recommender_update

        out["LatestRecommenderUpdate"] = (
            capo_customer_profiles.types.recommender_update.serialize_json(
                value["latest_recommender_update"]
            )
        )
    if "active_recommender_version_name" in value:
        out["ActiveRecommenderVersionName"] = value["active_recommender_version_name"]
    if "training_metrics" in value:
        import capo_customer_profiles.types.training_metrics_list

        out["TrainingMetrics"] = (
            capo_customer_profiles.types.training_metrics_list.serialize_json(
                value["training_metrics"]
            )
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetRecommenderResponse:
    out: GetRecommenderResponse = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderName") is not None:
        out["recommender_name"] = data["RecommenderName"]
    else:
        raise DeserializationError("GetRecommenderResponse.recommender_name required")
    if data.get("RecommenderRecipeName") is not None:
        import capo_customer_profiles.types.recommender_recipe_name

        out["recommender_recipe_name"] = (
            capo_customer_profiles.types.recommender_recipe_name.deserialize_json(
                data["RecommenderRecipeName"]
            )
        )
    else:
        raise DeserializationError(
            "GetRecommenderResponse.recommender_recipe_name required"
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
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
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
    if data.get("ActiveRecommenderVersionName") is not None:
        out["active_recommender_version_name"] = data["ActiveRecommenderVersionName"]
    if data.get("TrainingMetrics") is not None:
        import capo_customer_profiles.types.training_metrics_list

        out["training_metrics"] = (
            capo_customer_profiles.types.training_metrics_list.deserialize_json(
                data["TrainingMetrics"]
            )
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetRecommenderResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
