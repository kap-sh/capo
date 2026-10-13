"""Generated from Smithy shape ``com.amazonaws.voiceid#FraudsterRegistrationJob``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.failure_details
    import capo_voice_id.types.fraudster_registration_job_status
    import capo_voice_id.types.iam_role_arn
    import capo_voice_id.types.input_data_config
    import capo_voice_id.types.job_id
    import capo_voice_id.types.job_name
    import capo_voice_id.types.job_progress
    import capo_voice_id.types.output_data_config
    import capo_voice_id.types.registration_config
    import capo_voice_id.types.timestamp


class FraudsterRegistrationJob(TypedDict, closed=True):
    job_name: NotRequired["capo_voice_id.types.job_name.JobName"]
    """<p>The client-provided name for the fraudster registration job.</p>"""
    job_id: NotRequired["capo_voice_id.types.job_id.JobId"]
    """<p>The service-generated identifier for the fraudster registration job.</p>"""
    job_status: NotRequired[
        "capo_voice_id.types.fraudster_registration_job_status.FraudsterRegistrationJobStatus"
    ]
    """<p>The current status of the fraudster registration job.</p>"""
    domain_id: NotRequired["capo_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the fraudster registration job.</p>"""
    data_access_role_arn: NotRequired["capo_voice_id.types.iam_role_arn.IamRoleArn"]
    """<p>The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the job output file.</p>"""
    registration_config: NotRequired[
        "capo_voice_id.types.registration_config.RegistrationConfig"
    ]
    """<p>The registration config containing details such as the action to take when a duplicate fraudster is detected, and the similarity threshold to use for detecting a duplicate fraudster.</p>"""
    input_data_config: NotRequired[
        "capo_voice_id.types.input_data_config.InputDataConfig"
    ]
    """<p>The input data config containing an S3 URI for the input manifest file that contains the list of fraudster registration job requests.</p>"""
    output_data_config: NotRequired[
        "capo_voice_id.types.output_data_config.OutputDataConfig"
    ]
    """<p>The output data config containing the S3 location where you want Voice ID to write your job output file; you must also include a KMS key ID in order to encrypt the file.</p>"""
    created_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when the fraudster registration job was created.</p>"""
    ended_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when the fraudster registration job ended.</p>"""
    failure_details: NotRequired["capo_voice_id.types.failure_details.FailureDetails"]
    """<p>Contains details that are populated when an entire batch job fails. In cases of individual registration job failures, the batch job as a whole doesn't fail; it is completed with a <code>JobStatus</code> of <code>COMPLETED_WITH_ERRORS</code>. You can use the job output file to identify the individual registration requests that failed.</p>"""
    job_progress: NotRequired["capo_voice_id.types.job_progress.JobProgress"]
    """<p>Shows the completed percentage of registration requests listed in the input file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FraudsterRegistrationJob) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_status" in value:
        out["JobStatus"] = value["job_status"]
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "registration_config" in value:
        import capo_voice_id.types.registration_config

        out["RegistrationConfig"] = (
            capo_voice_id.types.registration_config.serialize_aws_json_1_0(
                value["registration_config"]
            )
        )
    if "input_data_config" in value:
        import capo_voice_id.types.input_data_config

        out["InputDataConfig"] = (
            capo_voice_id.types.input_data_config.serialize_aws_json_1_0(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import capo_voice_id.types.output_data_config

        out["OutputDataConfig"] = (
            capo_voice_id.types.output_data_config.serialize_aws_json_1_0(
                value["output_data_config"]
            )
        )
    if "created_at" in value:
        import capo_voice_id.types.timestamp

        out["CreatedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "ended_at" in value:
        import capo_voice_id.types.timestamp

        out["EndedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["ended_at"]
        )
    if "failure_details" in value:
        import capo_voice_id.types.failure_details

        out["FailureDetails"] = (
            capo_voice_id.types.failure_details.serialize_aws_json_1_0(
                value["failure_details"]
            )
        )
    if "job_progress" in value:
        import capo_voice_id.types.job_progress

        out["JobProgress"] = capo_voice_id.types.job_progress.serialize_aws_json_1_0(
            value["job_progress"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FraudsterRegistrationJob:
    out: FraudsterRegistrationJob = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobStatus") is not None:
        out["job_status"] = data["JobStatus"]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("RegistrationConfig") is not None:
        import capo_voice_id.types.registration_config

        out["registration_config"] = (
            capo_voice_id.types.registration_config.deserialize_aws_json_1_0(
                data["RegistrationConfig"]
            )
        )
    if data.get("InputDataConfig") is not None:
        import capo_voice_id.types.input_data_config

        out["input_data_config"] = (
            capo_voice_id.types.input_data_config.deserialize_aws_json_1_0(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_voice_id.types.output_data_config

        out["output_data_config"] = (
            capo_voice_id.types.output_data_config.deserialize_aws_json_1_0(
                data["OutputDataConfig"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_voice_id.types.timestamp

        out["created_at"] = capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if data.get("EndedAt") is not None:
        import capo_voice_id.types.timestamp

        out["ended_at"] = capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["EndedAt"]
        )
    if data.get("FailureDetails") is not None:
        import capo_voice_id.types.failure_details

        out["failure_details"] = (
            capo_voice_id.types.failure_details.deserialize_aws_json_1_0(
                data["FailureDetails"]
            )
        )
    if data.get("JobProgress") is not None:
        import capo_voice_id.types.job_progress

        out["job_progress"] = capo_voice_id.types.job_progress.deserialize_aws_json_1_0(
            data["JobProgress"]
        )
    return out


def redact_sensitive(value: FraudsterRegistrationJob) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_name" in value:
        out["job_name"] = "*** Sensitive Data Redacted ***"
    return out
