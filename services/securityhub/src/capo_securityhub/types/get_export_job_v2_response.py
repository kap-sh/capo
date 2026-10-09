"""Generated from Smithy shape ``com.amazonaws.securityhub#GetExportJobV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.export_data_type
    import capo_securityhub.types.export_destination
    import capo_securityhub.types.export_failure_code
    import capo_securityhub.types.export_job_id
    import capo_securityhub.types.export_name
    import capo_securityhub.types.export_output
    import capo_securityhub.types.export_scopes
    import capo_securityhub.types.export_status
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.timestamp


class GetExportJobV2Response(TypedDict, closed=True):
    export_job_id: NotRequired["capo_securityhub.types.export_job_id.ExportJobId"]
    """<p>The unique identifier of the export job.</p>"""
    name: NotRequired["capo_securityhub.types.export_name.ExportName"]
    """<p>The user-provided name of the export job, if one was specified when the job was started.</p>"""
    status: NotRequired["capo_securityhub.types.export_status.ExportStatus"]
    """<p>The current state of the export job.</p>"""
    data_type: NotRequired["capo_securityhub.types.export_data_type.ExportDataType"]
    """<p>The category of data that the export job produces.</p>"""
    output_configuration: NotRequired[
        "capo_securityhub.types.export_output.ExportOutput"
    ]
    """<p>The output configuration that the export job was started with, including the format and any filters or selected fields.</p>"""
    scopes: NotRequired["capo_securityhub.types.export_scopes.ExportScopes"]
    """<p>The organization scopes that the export job was started with, echoed verbatim. This parameter is absent if the caller didn't supply <code>Scopes</code>. It contains only the organization or organizational unit (OU) identifiers that the caller submitted; it never contains resolved member-account identifiers.</p>"""
    destination: NotRequired[
        "capo_securityhub.types.export_destination.ExportDestination"
    ]
    """<p>The destination that the export job writes to.</p>"""
    failure_code: NotRequired[
        "capo_securityhub.types.export_failure_code.ExportFailureCode"
    ]
    """<p>A code that classifies why the export job failed. Present only when <code>Status</code> is <code>FAILED</code>.</p>"""
    failure_message: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A human-readable message that provides more detail about why the export job failed. Present only when <code>Status</code> is <code>FAILED</code>.</p>"""
    started_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The time when the export job was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    ended_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The time when the export job reached a terminal state (<code>SUCCEEDED</code>, <code>FAILED</code>, or <code>CANCELLED</code>). This parameter is absent while the job is <code>RUNNING</code>.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportJobV2Response) -> dict:
    out: dict = {}
    if "export_job_id" in value:
        out["ExportJobId"] = value["export_job_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_securityhub.types.export_status

        out["Status"] = capo_securityhub.types.export_status.serialize_json(
            value["status"]
        )
    if "data_type" in value:
        import capo_securityhub.types.export_data_type

        out["DataType"] = capo_securityhub.types.export_data_type.serialize_json(
            value["data_type"]
        )
    if "output_configuration" in value:
        import capo_securityhub.types.export_output

        out["OutputConfiguration"] = (
            capo_securityhub.types.export_output.serialize_json(
                value["output_configuration"]
            )
        )
    if "scopes" in value:
        import capo_securityhub.types.export_scopes

        out["Scopes"] = capo_securityhub.types.export_scopes.serialize_json(
            value["scopes"]
        )
    if "destination" in value:
        import capo_securityhub.types.export_destination

        out["Destination"] = capo_securityhub.types.export_destination.serialize_json(
            value["destination"]
        )
    if "failure_code" in value:
        import capo_securityhub.types.export_failure_code

        out["FailureCode"] = capo_securityhub.types.export_failure_code.serialize_json(
            value["failure_code"]
        )
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "started_at" in value:
        import capo_securityhub.types.timestamp

        out["StartedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_securityhub.types.timestamp

        out["EndedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["ended_at"]
        )
    return out


def deserialize_json(data: dict) -> GetExportJobV2Response:
    out: GetExportJobV2Response = {}  # type: ignore[typeddict-item]
    if data.get("ExportJobId") is not None:
        out["export_job_id"] = data["ExportJobId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_securityhub.types.export_status

        out["status"] = capo_securityhub.types.export_status.deserialize_json(
            data["Status"]
        )
    if data.get("DataType") is not None:
        import capo_securityhub.types.export_data_type

        out["data_type"] = capo_securityhub.types.export_data_type.deserialize_json(
            data["DataType"]
        )
    if data.get("OutputConfiguration") is not None:
        import capo_securityhub.types.export_output

        out["output_configuration"] = (
            capo_securityhub.types.export_output.deserialize_json(
                data["OutputConfiguration"]
            )
        )
    if data.get("Scopes") is not None:
        import capo_securityhub.types.export_scopes

        out["scopes"] = capo_securityhub.types.export_scopes.deserialize_json(
            data["Scopes"]
        )
    if data.get("Destination") is not None:
        import capo_securityhub.types.export_destination

        out["destination"] = capo_securityhub.types.export_destination.deserialize_json(
            data["Destination"]
        )
    if data.get("FailureCode") is not None:
        import capo_securityhub.types.export_failure_code

        out["failure_code"] = (
            capo_securityhub.types.export_failure_code.deserialize_json(
                data["FailureCode"]
            )
        )
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    if data.get("StartedAt") is not None:
        import capo_securityhub.types.timestamp

        out["started_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["StartedAt"]
        )
    if data.get("EndedAt") is not None:
        import capo_securityhub.types.timestamp

        out["ended_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["EndedAt"]
        )
    return out
