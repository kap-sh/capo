"""Generated from Smithy shape ``com.amazonaws.opensearch#StartMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.application_id
    import capo_opensearch.types.client_token
    import capo_opensearch.types.migration_options


class StartMigrationRequest(TypedDict, closed=True):
    application_id: "capo_opensearch.types.application_id.ApplicationId"
    """<p>The unique identifier of the OpenSearch application to migrate saved objects into.</p>"""
    migration_options: "capo_opensearch.types.migration_options.MigrationOptions"
    """<p>The configuration options for the migration, including the source data source, target workspace, export filters, and conflict resolution strategy.</p>"""
    client_token: NotRequired["capo_opensearch.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon OpenSearch Service ignores the request but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMigrationRequest) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    import capo_opensearch.types.migration_options

    out["migrationOptions"] = capo_opensearch.types.migration_options.serialize_json(
        value["migration_options"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartMigrationRequest:
    out: StartMigrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("migrationOptions") is not None:
        import capo_opensearch.types.migration_options

        out["migration_options"] = (
            capo_opensearch.types.migration_options.deserialize_json(
                data["migrationOptions"]
            )
        )
    else:
        raise DeserializationError("StartMigrationRequest.migration_options required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
