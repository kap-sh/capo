"""Generated from Smithy shape ``com.amazonaws.voiceid#StartSpeakerEnrollmentJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.client_token_string
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.enrollment_config
    import capo_voice_id.types.iam_role_arn
    import capo_voice_id.types.input_data_config
    import capo_voice_id.types.job_name
    import capo_voice_id.types.output_data_config


class StartSpeakerEnrollmentJobRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_voice_id.types.client_token_string.ClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    job_name: NotRequired["capo_voice_id.types.job_name.JobName"]
    """<p>A name for your speaker enrollment job.</p>"""
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the speaker enrollment job and in which the speakers are enrolled. </p>"""
    data_access_role_arn: "capo_voice_id.types.iam_role_arn.IamRoleArn"
    """<p>The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the job output file. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/voiceid-batch-enrollment.html">Batch enrollment using audio data from prior calls</a> for the permissions needed in this role.</p>"""
    enrollment_config: NotRequired[
        "capo_voice_id.types.enrollment_config.EnrollmentConfig"
    ]
    """<p>The enrollment config that contains details such as the action to take when a speaker is already enrolled in Voice ID or when a speaker is identified as a fraudster.</p>"""
    input_data_config: "capo_voice_id.types.input_data_config.InputDataConfig"
    """<p>The input data config containing the S3 location for the input manifest file that contains the list of speaker enrollment requests.</p>"""
    output_data_config: "capo_voice_id.types.output_data_config.OutputDataConfig"
    """<p>The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartSpeakerEnrollmentJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    out["DomainId"] = value["domain_id"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "enrollment_config" in value:
        import capo_voice_id.types.enrollment_config

        out["EnrollmentConfig"] = (
            capo_voice_id.types.enrollment_config.serialize_aws_json_1_0(
                value["enrollment_config"]
            )
        )
    import capo_voice_id.types.input_data_config

    out["InputDataConfig"] = (
        capo_voice_id.types.input_data_config.serialize_aws_json_1_0(
            value["input_data_config"]
        )
    )
    import capo_voice_id.types.output_data_config

    out["OutputDataConfig"] = (
        capo_voice_id.types.output_data_config.serialize_aws_json_1_0(
            value["output_data_config"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartSpeakerEnrollmentJobRequest:
    out: StartSpeakerEnrollmentJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError(
            "StartSpeakerEnrollmentJobRequest.domain_id required"
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartSpeakerEnrollmentJobRequest.data_access_role_arn required"
        )
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
    else:
        raise DeserializationError(
            "StartSpeakerEnrollmentJobRequest.input_data_config required"
        )
    if data.get("OutputDataConfig") is not None:
        import capo_voice_id.types.output_data_config

        out["output_data_config"] = (
            capo_voice_id.types.output_data_config.deserialize_aws_json_1_0(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartSpeakerEnrollmentJobRequest.output_data_config required"
        )
    return out
