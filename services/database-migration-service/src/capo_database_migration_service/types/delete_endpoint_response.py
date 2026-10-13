"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteEndpointResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.endpoint


class DeleteEndpointResponse(TypedDict, closed=True):
    endpoint: NotRequired["capo_database_migration_service.types.endpoint.Endpoint"]
    """<p>The endpoint that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import capo_database_migration_service.types.endpoint

        out["Endpoint"] = (
            capo_database_migration_service.types.endpoint.serialize_aws_json_1_1(
                value["endpoint"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEndpointResponse:
    out: DeleteEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("Endpoint") is not None:
        import capo_database_migration_service.types.endpoint

        out["endpoint"] = (
            capo_database_migration_service.types.endpoint.deserialize_aws_json_1_1(
                data["Endpoint"]
            )
        )
    return out


def redact_sensitive(value: DeleteEndpointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoint" in value:
        import capo_database_migration_service.types.endpoint

        out["endpoint"] = (
            capo_database_migration_service.types.endpoint.redact_sensitive(
                value["endpoint"]
            )
        )
    return out
