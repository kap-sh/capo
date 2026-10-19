"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.recommendation_settings
    import capo_database_migration_service.types.string


class StartRecommendationsRequest(TypedDict, closed=True):
    database_id: "capo_database_migration_service.types.string.String"
    """<p>The identifier of the source database to analyze and provide recommendations for.</p>"""
    settings: "capo_database_migration_service.types.recommendation_settings.RecommendationSettings"
    """<p>The settings in JSON format that Fleet Advisor uses to determine target engine recommendations. These parameters include target instance sizing and availability and durability settings. For target instance sizing, Fleet Advisor supports the following two options: total capacity and resource utilization. For availability and durability, Fleet Advisor supports the following two options: production (Multi-AZ deployments) and Dev/Test (Single-AZ deployments).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRecommendationsRequest) -> dict:
    out: dict = {}
    out["DatabaseId"] = value["database_id"]
    import capo_database_migration_service.types.recommendation_settings

    out["Settings"] = (
        capo_database_migration_service.types.recommendation_settings.serialize_aws_json_1_1(
            value["settings"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRecommendationsRequest:
    out: StartRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseId") is not None:
        out["database_id"] = data["DatabaseId"]
    else:
        out["database_id"] = ""
    if data.get("Settings") is not None:
        import capo_database_migration_service.types.recommendation_settings

        out["settings"] = (
            capo_database_migration_service.types.recommendation_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    else:
        raise DeserializationError("StartRecommendationsRequest.settings required")
    return out
