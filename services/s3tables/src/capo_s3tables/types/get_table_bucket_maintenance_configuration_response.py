"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketMaintenanceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_bucket_maintenance_configuration


class GetTableBucketMaintenanceConfigurationResponse(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.</p>"""
    configuration: "capo_s3tables.types.table_bucket_maintenance_configuration.TableBucketMaintenanceConfiguration"
    """<p>Details about the maintenance configuration for the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketMaintenanceConfigurationResponse) -> dict:
    out: dict = {}
    out["tableBucketARN"] = value["table_bucket_arn"]
    import capo_s3tables.types.table_bucket_maintenance_configuration

    out["configuration"] = (
        capo_s3tables.types.table_bucket_maintenance_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableBucketMaintenanceConfigurationResponse:
    out: GetTableBucketMaintenanceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("tableBucketARN") is not None:
        out["table_bucket_arn"] = data["tableBucketARN"]
    else:
        out["table_bucket_arn"] = ""
    if data.get("configuration") is not None:
        import capo_s3tables.types.table_bucket_maintenance_configuration

        out["configuration"] = (
            capo_s3tables.types.table_bucket_maintenance_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        out["configuration"] = {}
    return out
