"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ComprehendMedicalAsyncJobProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.any_length_string
    import capo_comprehendmedical.types.iam_role_arn
    import capo_comprehendmedical.types.input_data_config
    import capo_comprehendmedical.types.job_id
    import capo_comprehendmedical.types.job_name
    import capo_comprehendmedical.types.job_status
    import capo_comprehendmedical.types.kms_key
    import capo_comprehendmedical.types.language_code
    import capo_comprehendmedical.types.manifest_file_path
    import capo_comprehendmedical.types.model_version
    import capo_comprehendmedical.types.output_data_config
    import capo_comprehendmedical.types.timestamp


class ComprehendMedicalAsyncJobProperties(TypedDict, closed=True):
    job_id: NotRequired["capo_comprehendmedical.types.job_id.JobId"]
    """<p>The identifier assigned to the detection job.</p>"""
    job_name: NotRequired["capo_comprehendmedical.types.job_name.JobName"]
    """<p>The name that you assigned to the detection job.</p>"""
    job_status: NotRequired["capo_comprehendmedical.types.job_status.JobStatus"]
    """<p>The current status of the detection job. If the status is <code>FAILED</code>, the <code>Message</code> field shows the reason for the failure.</p>"""
    message: NotRequired[
        "capo_comprehendmedical.types.any_length_string.AnyLengthString"
    ]
    """<p>A description of the status of a job.</p>"""
    submit_time: NotRequired["capo_comprehendmedical.types.timestamp.Timestamp"]
    """<p>The time that the detection job was submitted for processing.</p>"""
    end_time: NotRequired["capo_comprehendmedical.types.timestamp.Timestamp"]
    """<p>The time that the detection job completed.</p>"""
    expiration_time: NotRequired["capo_comprehendmedical.types.timestamp.Timestamp"]
    """<p>The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the <code>ListEntitiesDetectionV2Job</code> or the <code>ListPHIDetectionJobs</code> operation.</p>"""
    input_data_config: NotRequired[
        "capo_comprehendmedical.types.input_data_config.InputDataConfig"
    ]
    """<p>The input data configuration that you supplied when you created the detection job.</p>"""
    output_data_config: NotRequired[
        "capo_comprehendmedical.types.output_data_config.OutputDataConfig"
    ]
    """<p>The output data configuration that you supplied when you created the detection job.</p>"""
    language_code: NotRequired[
        "capo_comprehendmedical.types.language_code.LanguageCode"
    ]
    """<p>The language code of the input documents.</p>"""
    data_access_role_arn: NotRequired[
        "capo_comprehendmedical.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.</p>"""
    manifest_file_path: NotRequired[
        "capo_comprehendmedical.types.manifest_file_path.ManifestFilePath"
    ]
    """<p>The path to the file that describes the results of a batch job.</p>"""
    kms_key: NotRequired["capo_comprehendmedical.types.kms_key.KMSKey"]
    """<p>The AWS Key Management Service key, if any, used to encrypt the output files. </p>"""
    model_version: NotRequired[
        "capo_comprehendmedical.types.model_version.ModelVersion"
    ]
    """<p>The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComprehendMedicalAsyncJobProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_comprehendmedical.types.job_status

        out["JobStatus"] = (
            capo_comprehendmedical.types.job_status.serialize_aws_json_1_1(
                value["job_status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submit_time" in value:
        import capo_comprehendmedical.types.timestamp

        out["SubmitTime"] = (
            capo_comprehendmedical.types.timestamp.serialize_aws_json_1_1(
                value["submit_time"]
            )
        )
    if "end_time" in value:
        import capo_comprehendmedical.types.timestamp

        out["EndTime"] = capo_comprehendmedical.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "expiration_time" in value:
        import capo_comprehendmedical.types.timestamp

        out["ExpirationTime"] = (
            capo_comprehendmedical.types.timestamp.serialize_aws_json_1_1(
                value["expiration_time"]
            )
        )
    if "input_data_config" in value:
        import capo_comprehendmedical.types.input_data_config

        out["InputDataConfig"] = (
            capo_comprehendmedical.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import capo_comprehendmedical.types.output_data_config

        out["OutputDataConfig"] = (
            capo_comprehendmedical.types.output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "language_code" in value:
        import capo_comprehendmedical.types.language_code

        out["LanguageCode"] = (
            capo_comprehendmedical.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "manifest_file_path" in value:
        out["ManifestFilePath"] = value["manifest_file_path"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComprehendMedicalAsyncJobProperties:
    out: ComprehendMedicalAsyncJobProperties = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_comprehendmedical.types.job_status

        out["job_status"] = (
            capo_comprehendmedical.types.job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("SubmitTime") is not None:
        import capo_comprehendmedical.types.timestamp

        out["submit_time"] = (
            capo_comprehendmedical.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_comprehendmedical.types.timestamp

        out["end_time"] = (
            capo_comprehendmedical.types.timestamp.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if data.get("ExpirationTime") is not None:
        import capo_comprehendmedical.types.timestamp

        out["expiration_time"] = (
            capo_comprehendmedical.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    if data.get("InputDataConfig") is not None:
        import capo_comprehendmedical.types.input_data_config

        out["input_data_config"] = (
            capo_comprehendmedical.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_comprehendmedical.types.output_data_config

        out["output_data_config"] = (
            capo_comprehendmedical.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if data.get("LanguageCode") is not None:
        import capo_comprehendmedical.types.language_code

        out["language_code"] = (
            capo_comprehendmedical.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("ManifestFilePath") is not None:
        out["manifest_file_path"] = data["ManifestFilePath"]
    if data.get("KMSKey") is not None:
        out["kms_key"] = data["KMSKey"]
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComprehendMedicalAsyncJobProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_comprehendmedical.types.job_status

        out["JobStatus"] = capo_comprehendmedical.types.job_status.serialize_cbor(
            value["job_status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submit_time" in value:
        import capo_comprehendmedical.types.timestamp

        out["SubmitTime"] = capo_comprehendmedical.types.timestamp.serialize_cbor(
            value["submit_time"]
        )
    if "end_time" in value:
        import capo_comprehendmedical.types.timestamp

        out["EndTime"] = capo_comprehendmedical.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "expiration_time" in value:
        import capo_comprehendmedical.types.timestamp

        out["ExpirationTime"] = capo_comprehendmedical.types.timestamp.serialize_cbor(
            value["expiration_time"]
        )
    if "input_data_config" in value:
        import capo_comprehendmedical.types.input_data_config

        out["InputDataConfig"] = (
            capo_comprehendmedical.types.input_data_config.serialize_cbor(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import capo_comprehendmedical.types.output_data_config

        out["OutputDataConfig"] = (
            capo_comprehendmedical.types.output_data_config.serialize_cbor(
                value["output_data_config"]
            )
        )
    if "language_code" in value:
        import capo_comprehendmedical.types.language_code

        out["LanguageCode"] = capo_comprehendmedical.types.language_code.serialize_cbor(
            value["language_code"]
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "manifest_file_path" in value:
        out["ManifestFilePath"] = value["manifest_file_path"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    return out


def deserialize_cbor(data: dict) -> ComprehendMedicalAsyncJobProperties:
    out: ComprehendMedicalAsyncJobProperties = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_comprehendmedical.types.job_status

        out["job_status"] = capo_comprehendmedical.types.job_status.deserialize_cbor(
            data["JobStatus"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("SubmitTime") is not None:
        import capo_comprehendmedical.types.timestamp

        out["submit_time"] = capo_comprehendmedical.types.timestamp.deserialize_cbor(
            data["SubmitTime"]
        )
    if data.get("EndTime") is not None:
        import capo_comprehendmedical.types.timestamp

        out["end_time"] = capo_comprehendmedical.types.timestamp.deserialize_cbor(
            data["EndTime"]
        )
    if data.get("ExpirationTime") is not None:
        import capo_comprehendmedical.types.timestamp

        out["expiration_time"] = (
            capo_comprehendmedical.types.timestamp.deserialize_cbor(
                data["ExpirationTime"]
            )
        )
    if data.get("InputDataConfig") is not None:
        import capo_comprehendmedical.types.input_data_config

        out["input_data_config"] = (
            capo_comprehendmedical.types.input_data_config.deserialize_cbor(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_comprehendmedical.types.output_data_config

        out["output_data_config"] = (
            capo_comprehendmedical.types.output_data_config.deserialize_cbor(
                data["OutputDataConfig"]
            )
        )
    if data.get("LanguageCode") is not None:
        import capo_comprehendmedical.types.language_code

        out["language_code"] = (
            capo_comprehendmedical.types.language_code.deserialize_cbor(
                data["LanguageCode"]
            )
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("ManifestFilePath") is not None:
        out["manifest_file_path"] = data["ManifestFilePath"]
    if data.get("KMSKey") is not None:
        out["kms_key"] = data["KMSKey"]
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    return out
