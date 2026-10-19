"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableMaintenanceJobStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_maintenance_job_status


class GetTableMaintenanceJobStatusResponse(TypedDict, closed=True):
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    status: "capo_s3tables.types.table_maintenance_job_status.TableMaintenanceJobStatus"
    """<p>The status of the maintenance job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableMaintenanceJobStatusResponse) -> dict:
    out: dict = {}
    out["tableARN"] = value["table_arn"]
    import capo_s3tables.types.table_maintenance_job_status

    out["status"] = capo_s3tables.types.table_maintenance_job_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> GetTableMaintenanceJobStatusResponse:
    out: GetTableMaintenanceJobStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("tableARN") is not None:
        out["table_arn"] = data["tableARN"]
    else:
        out["table_arn"] = ""
    if data.get("status") is not None:
        import capo_s3tables.types.table_maintenance_job_status

        out["status"] = (
            capo_s3tables.types.table_maintenance_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        out["status"] = {}
    return out
