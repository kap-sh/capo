"""Generated from Smithy shape ``com.amazonaws.voiceid#SpeakerEnrollmentJob``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.enrollment_config
    import capo_voice_id.types.failure_details
    import capo_voice_id.types.iam_role_arn
    import capo_voice_id.types.input_data_config
    import capo_voice_id.types.job_id
    import capo_voice_id.types.job_name
    import capo_voice_id.types.job_progress
    import capo_voice_id.types.output_data_config
    import capo_voice_id.types.speaker_enrollment_job_status
    import capo_voice_id.types.timestamp


class SpeakerEnrollmentJob(TypedDict, closed=True):
    job_name: NotRequired["capo_voice_id.types.job_name.JobName"]
    """<p>The client-provided name for the speaker enrollment job.</p>"""
    job_id: NotRequired["capo_voice_id.types.job_id.JobId"]
    """<p>The service-generated identifier for the speaker enrollment job.</p>"""
    job_status: NotRequired[
        "capo_voice_id.types.speaker_enrollment_job_status.SpeakerEnrollmentJobStatus"
    ]
    """<p>The current status of the speaker enrollment job.</p>"""
    domain_id: NotRequired["capo_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the speaker enrollment job.</p>"""
    data_access_role_arn: NotRequired["capo_voice_id.types.iam_role_arn.IamRoleArn"]
    """<p>The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the job output file.</p>"""
    enrollment_config: NotRequired[
        "capo_voice_id.types.enrollment_config.EnrollmentConfig"
    ]
    """<p>The configuration that defines the action to take when the speaker is already enrolled in Voice ID, and the <code>FraudDetectionConfig</code> to use.</p>"""
    input_data_config: NotRequired[
        "capo_voice_id.types.input_data_config.InputDataConfig"
    ]
    """<p>The input data config containing an S3 URI for the input manifest file that contains the list of speaker enrollment job requests.</p>"""
    output_data_config: NotRequired[
        "capo_voice_id.types.output_data_config.OutputDataConfig"
    ]
    """<p>The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.</p>"""
    created_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when the speaker enrollment job was created.</p>"""
    ended_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when the speaker enrollment job ended. </p>"""
    failure_details: NotRequired["capo_voice_id.types.failure_details.FailureDetails"]
    """<p>Contains details that are populated when an entire batch job fails. In cases of individual registration job failures, the batch job as a whole doesn't fail; it is completed with a <code>JobStatus</code> of <code>COMPLETED_WITH_ERRORS</code>. You can use the job output file to identify the individual registration requests that failed.</p>"""
    job_progress: NotRequired["capo_voice_id.types.job_progress.JobProgress"]
    """<p>Provides details on job progress. This field shows the completed percentage of registration requests listed in the input file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpeakerEnrollmentJob) -> dict:
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
    if "enrollment_config" in value:
        import capo_voice_id.types.enrollment_config

        out["EnrollmentConfig"] = (
            capo_voice_id.types.enrollment_config.serialize_aws_json_1_0(
                value["enrollment_config"]
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


def deserialize_aws_json_1_0(data: dict) -> SpeakerEnrollmentJob:
    out: SpeakerEnrollmentJob = {}  # type: ignore[typeddict-item]
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
    if data.get("EnrollmentConfig") is not None:
        import capo_voice_id.types.enrollment_config

        out["enrollment_config"] = (
            capo_voice_id.types.enrollment_config.deserialize_aws_json_1_0(
                data["EnrollmentConfig"]
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


def redact_sensitive(value: SpeakerEnrollmentJob) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_name" in value:
        out["job_name"] = "*** Sensitive Data Redacted ***"
    return out
