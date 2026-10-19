"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteDataProviderMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteDataProviderMessage(TypedDict, closed=True):
    data_provider_identifier: "capo_database_migration_service.types.string.String"
    """<p>The identifier of the data provider to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataProviderMessage) -> dict:
    out: dict = {}
    out["DataProviderIdentifier"] = value["data_provider_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataProviderMessage:
    out: DeleteDataProviderMessage = {}  # type: ignore[typeddict-item]
    if data.get("DataProviderIdentifier") is not None:
        out["data_provider_identifier"] = data["DataProviderIdentifier"]
    else:
        out["data_provider_identifier"] = ""
    return out
