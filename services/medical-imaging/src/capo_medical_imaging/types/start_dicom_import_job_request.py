"""Generated from Smithy shape ``com.amazonaws.medicalimaging#StartDICOMImportJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.aws_account_id
    import capo_medical_imaging.types.client_token
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.import_configuration
    import capo_medical_imaging.types.job_name
    import capo_medical_imaging.types.role_arn
    import capo_medical_imaging.types.s3_uri


class StartDICOMImportJobRequest(TypedDict, closed=True):
    job_name: NotRequired["capo_medical_imaging.types.job_name.JobName"]
    """<p>The import job name.</p>"""
    data_access_role_arn: "capo_medical_imaging.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants permission to access medical imaging resources.</p>"""
    client_token: "capo_medical_imaging.types.client_token.ClientToken"
    """<p>A unique identifier for API idempotency.</p>"""
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    input_s3_uri: "capo_medical_imaging.types.s3_uri.S3Uri"
    """<p>The input prefix path for the S3 bucket that contains the DICOM files to be imported.</p>"""
    output_s3_uri: "capo_medical_imaging.types.s3_uri.S3Uri"
    """<p>The output prefix of the S3 bucket to upload the results of the DICOM import job.</p>"""
    input_owner_account_id: NotRequired[
        "capo_medical_imaging.types.aws_account_id.AwsAccountId"
    ]
    """<p>The account ID of the source S3 bucket owner.</p>"""
    import_configuration: NotRequired[
        "capo_medical_imaging.types.import_configuration.ImportConfiguration"
    ]
    """<p>The import configuration for the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDICOMImportJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    out["dataAccessRoleArn"] = value["data_access_role_arn"]
    out["clientToken"] = value["client_token"]
    out["inputS3Uri"] = value["input_s3_uri"]
    out["outputS3Uri"] = value["output_s3_uri"]
    if "input_owner_account_id" in value:
        out["inputOwnerAccountId"] = value["input_owner_account_id"]
    if "import_configuration" in value:
        import capo_medical_imaging.types.import_configuration

        out["importConfiguration"] = (
            capo_medical_imaging.types.import_configuration.serialize_json(
                value["import_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartDICOMImportJobRequest:
    out: StartDICOMImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    if data.get("dataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["dataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartDICOMImportJobRequest.data_access_role_arn required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("StartDICOMImportJobRequest.client_token required")
    if data.get("inputS3Uri") is not None:
        out["input_s3_uri"] = data["inputS3Uri"]
    else:
        raise DeserializationError("StartDICOMImportJobRequest.input_s3_uri required")
    if data.get("outputS3Uri") is not None:
        out["output_s3_uri"] = data["outputS3Uri"]
    else:
        raise DeserializationError("StartDICOMImportJobRequest.output_s3_uri required")
    if data.get("inputOwnerAccountId") is not None:
        out["input_owner_account_id"] = data["inputOwnerAccountId"]
    if data.get("importConfiguration") is not None:
        import capo_medical_imaging.types.import_configuration

        out["import_configuration"] = (
            capo_medical_imaging.types.import_configuration.deserialize_json(
                data["importConfiguration"]
            )
        )
    return out


def redact_sensitive(value: StartDICOMImportJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "import_configuration" in value:
        import capo_medical_imaging.types.import_configuration

        out["import_configuration"] = (
            capo_medical_imaging.types.import_configuration.redact_sensitive(
                value["import_configuration"]
            )
        )
    return out
