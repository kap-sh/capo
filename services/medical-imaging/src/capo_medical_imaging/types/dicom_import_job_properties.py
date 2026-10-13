"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DICOMImportJobProperties``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.import_configuration
    import capo_medical_imaging.types.job_id
    import capo_medical_imaging.types.job_name
    import capo_medical_imaging.types.job_status
    import capo_medical_imaging.types.message
    import capo_medical_imaging.types.role_arn
    import capo_medical_imaging.types.s3_uri


class DICOMImportJobProperties(TypedDict, closed=True):
    job_id: "capo_medical_imaging.types.job_id.JobId"
    """<p>The import job identifier.</p>"""
    job_name: "capo_medical_imaging.types.job_name.JobName"
    """<p>The import job name.</p>"""
    job_status: "capo_medical_imaging.types.job_status.JobStatus"
    """<p>The filters for listing import jobs based on status.</p>"""
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    data_access_role_arn: "capo_medical_imaging.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) that grants permissions to access medical imaging resources.</p>"""
    ended_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp for when the import job was ended.</p>"""
    submitted_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp for when the import job was submitted.</p>"""
    input_s3_uri: "capo_medical_imaging.types.s3_uri.S3Uri"
    """<p>The input prefix path for the S3 bucket that contains the DICOM P10 files to be imported.</p>"""
    output_s3_uri: "capo_medical_imaging.types.s3_uri.S3Uri"
    """<p>The output prefix of the S3 bucket to upload the results of the DICOM import job.</p>"""
    message: NotRequired["capo_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an import job fails.</p>"""
    import_configuration: NotRequired[
        "capo_medical_imaging.types.import_configuration.ImportConfiguration"
    ]
    """<p>The object containing <code>DicomJsonMetadataImportConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DICOMImportJobProperties) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["jobName"] = value["job_name"]
    import capo_medical_imaging.types.job_status

    out["jobStatus"] = capo_medical_imaging.types.job_status.serialize_json(
        value["job_status"]
    )
    out["datastoreId"] = value["datastore_id"]
    out["dataAccessRoleArn"] = value["data_access_role_arn"]
    if "ended_at" in value:
        import capo_medical_imaging.types.date

        out["endedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["ended_at"]
        )
    if "submitted_at" in value:
        import capo_medical_imaging.types.date

        out["submittedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["submitted_at"]
        )
    out["inputS3Uri"] = value["input_s3_uri"]
    out["outputS3Uri"] = value["output_s3_uri"]
    if "message" in value:
        out["message"] = value["message"]
    if "import_configuration" in value:
        import capo_medical_imaging.types.import_configuration

        out["importConfiguration"] = (
            capo_medical_imaging.types.import_configuration.serialize_json(
                value["import_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DICOMImportJobProperties:
    out: DICOMImportJobProperties = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("DICOMImportJobProperties.job_id required")
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("DICOMImportJobProperties.job_name required")
    if data.get("jobStatus") is not None:
        import capo_medical_imaging.types.job_status

        out["job_status"] = capo_medical_imaging.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        raise DeserializationError("DICOMImportJobProperties.job_status required")
    if data.get("datastoreId") is not None:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("DICOMImportJobProperties.datastore_id required")
    if data.get("dataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["dataAccessRoleArn"]
    else:
        raise DeserializationError(
            "DICOMImportJobProperties.data_access_role_arn required"
        )
    if data.get("endedAt") is not None:
        import capo_medical_imaging.types.date

        out["ended_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["endedAt"]
        )
    if data.get("submittedAt") is not None:
        import capo_medical_imaging.types.date

        out["submitted_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["submittedAt"]
        )
    if data.get("inputS3Uri") is not None:
        out["input_s3_uri"] = data["inputS3Uri"]
    else:
        raise DeserializationError("DICOMImportJobProperties.input_s3_uri required")
    if data.get("outputS3Uri") is not None:
        out["output_s3_uri"] = data["outputS3Uri"]
    else:
        raise DeserializationError("DICOMImportJobProperties.output_s3_uri required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("importConfiguration") is not None:
        import capo_medical_imaging.types.import_configuration

        out["import_configuration"] = (
            capo_medical_imaging.types.import_configuration.deserialize_json(
                data["importConfiguration"]
            )
        )
    return out


def redact_sensitive(value: DICOMImportJobProperties) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "import_configuration" in value:
        import capo_medical_imaging.types.import_configuration

        out["import_configuration"] = (
            capo_medical_imaging.types.import_configuration.redact_sensitive(
                value["import_configuration"]
            )
        )
    return out
