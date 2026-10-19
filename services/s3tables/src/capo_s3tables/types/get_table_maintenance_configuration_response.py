"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableMaintenanceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_maintenance_configuration


class GetTableMaintenanceConfigurationResponse(TypedDict, closed=True):
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    configuration: "capo_s3tables.types.table_maintenance_configuration.TableMaintenanceConfiguration"
    """<p>Details about the maintenance configuration for the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableMaintenanceConfigurationResponse) -> dict:
    out: dict = {}
    out["tableARN"] = value["table_arn"]
    import capo_s3tables.types.table_maintenance_configuration

    out["configuration"] = (
        capo_s3tables.types.table_maintenance_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableMaintenanceConfigurationResponse:
    out: GetTableMaintenanceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("tableARN") is not None:
        out["table_arn"] = data["tableARN"]
    else:
        out["table_arn"] = ""
    if data.get("configuration") is not None:
        import capo_s3tables.types.table_maintenance_configuration

        out["configuration"] = (
            capo_s3tables.types.table_maintenance_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        out["configuration"] = {}
    return out
