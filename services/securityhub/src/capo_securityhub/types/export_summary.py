"""Generated from Smithy shape ``com.amazonaws.securityhub#ExportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.export_data_type
    import capo_securityhub.types.export_destination
    import capo_securityhub.types.export_failure_code
    import capo_securityhub.types.export_job_id
    import capo_securityhub.types.export_name
    import capo_securityhub.types.export_output_summary
    import capo_securityhub.types.export_scopes
    import capo_securityhub.types.export_status
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.timestamp


class ExportSummary(TypedDict, closed=True):
    export_job_id: NotRequired["capo_securityhub.types.export_job_id.ExportJobId"]
    """<p>The unique identifier of the export job.</p>"""
    name: NotRequired["capo_securityhub.types.export_name.ExportName"]
    """<p>The user-provided name of the export job, if one was specified.</p>"""
    status: NotRequired["capo_securityhub.types.export_status.ExportStatus"]
    """<p>The current state of the export job.</p>"""
    data_type: NotRequired["capo_securityhub.types.export_data_type.ExportDataType"]
    """<p>The category of data that the export job produces.</p>"""
    output_configuration: NotRequired[
        "capo_securityhub.types.export_output_summary.ExportOutputSummary"
    ]
    """<p>The output configuration of the export job. For findings exports, this reports the output format. Present only for findings exports; absent for other data types.</p>"""
    scopes: NotRequired["capo_securityhub.types.export_scopes.ExportScopes"]
    """<p>The organization scopes that the export job was started with, echoed verbatim. Absent if the caller didn't supply <code>Scopes</code>.</p>"""
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
    """<p>A human-readable message about why the export job failed. Present only when <code>Status</code> is <code>FAILED</code>.</p>"""
    started_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The time when the export job was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    ended_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The time when the export job reached a terminal state. Absent while the job is <code>RUNNING</code>.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportSummary) -> dict:
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
        import capo_securityhub.types.export_output_summary

        out["OutputConfiguration"] = (
            capo_securityhub.types.export_output_summary.serialize_json(
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


def deserialize_json(data: dict) -> ExportSummary:
    out: ExportSummary = {}  # type: ignore[typeddict-item]
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
        import capo_securityhub.types.export_output_summary

        out["output_configuration"] = (
            capo_securityhub.types.export_output_summary.deserialize_json(
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
