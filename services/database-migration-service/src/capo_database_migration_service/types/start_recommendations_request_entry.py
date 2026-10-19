"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartRecommendationsRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.recommendation_settings
    import capo_database_migration_service.types.string


class StartRecommendationsRequestEntry(TypedDict, closed=True):
    database_id: "capo_database_migration_service.types.string.String"
    """<p>The identifier of the source database.</p>"""
    settings: "capo_database_migration_service.types.recommendation_settings.RecommendationSettings"
    """<p>The required target engine settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRecommendationsRequestEntry) -> dict:
    out: dict = {}
    out["DatabaseId"] = value["database_id"]
    import capo_database_migration_service.types.recommendation_settings

    out["Settings"] = (
        capo_database_migration_service.types.recommendation_settings.serialize_aws_json_1_1(
            value["settings"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRecommendationsRequestEntry:
    out: StartRecommendationsRequestEntry = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("StartRecommendationsRequestEntry.settings required")
    return out
