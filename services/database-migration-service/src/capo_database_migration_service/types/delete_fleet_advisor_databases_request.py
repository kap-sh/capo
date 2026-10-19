"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteFleetAdvisorDatabasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string_list


class DeleteFleetAdvisorDatabasesRequest(TypedDict, closed=True):
    database_ids: "capo_database_migration_service.types.string_list.StringList"
    """<p>The IDs of the Fleet Advisor collector databases to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetAdvisorDatabasesRequest) -> dict:
    out: dict = {}
    import capo_database_migration_service.types.string_list

    out["DatabaseIds"] = (
        capo_database_migration_service.types.string_list.serialize_aws_json_1_1(
            value["database_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetAdvisorDatabasesRequest:
    out: DeleteFleetAdvisorDatabasesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseIds") is not None:
        import capo_database_migration_service.types.string_list

        out["database_ids"] = (
            capo_database_migration_service.types.string_list.deserialize_aws_json_1_1(
                data["DatabaseIds"]
            )
        )
    else:
        out["database_ids"] = []
    return out
