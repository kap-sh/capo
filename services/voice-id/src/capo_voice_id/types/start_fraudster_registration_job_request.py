"""Generated from Smithy shape ``com.amazonaws.voiceid#StartFraudsterRegistrationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.client_token_string
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.iam_role_arn
    import capo_voice_id.types.input_data_config
    import capo_voice_id.types.job_name
    import capo_voice_id.types.output_data_config
    import capo_voice_id.types.registration_config


class StartFraudsterRegistrationJobRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_voice_id.types.client_token_string.ClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    job_name: NotRequired["capo_voice_id.types.job_name.JobName"]
    """<p>The name of the new fraudster registration job.</p>"""
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the fraudster registration job and in which the fraudsters are registered.</p>"""
    data_access_role_arn: "capo_voice_id.types.iam_role_arn.IamRoleArn"
    """<p>The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the Job output file. Refer to the <a href="https://docs.aws.amazon.com/connect/latest/adminguide/voiceid-fraudster-watchlist.html">Create and edit a fraudster watchlist</a> documentation for the permissions needed in this role.</p>"""
    registration_config: NotRequired[
        "capo_voice_id.types.registration_config.RegistrationConfig"
    ]
    """<p>The registration config containing details such as the action to take when a duplicate fraudster is detected, and the similarity threshold to use for detecting a duplicate fraudster. </p>"""
    input_data_config: "capo_voice_id.types.input_data_config.InputDataConfig"
    """<p>The input data config containing an S3 URI for the input manifest file that contains the list of fraudster registration requests.</p>"""
    output_data_config: "capo_voice_id.types.output_data_config.OutputDataConfig"
    """<p>The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFraudsterRegistrationJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    out["DomainId"] = value["domain_id"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "registration_config" in value:
        import capo_voice_id.types.registration_config

        out["RegistrationConfig"] = (
            capo_voice_id.types.registration_config.serialize_aws_json_1_0(
                value["registration_config"]
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


def deserialize_aws_json_1_0(data: dict) -> StartFraudsterRegistrationJobRequest:
    out: StartFraudsterRegistrationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError(
            "StartFraudsterRegistrationJobRequest.domain_id required"
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartFraudsterRegistrationJobRequest.data_access_role_arn required"
        )
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
    else:
        raise DeserializationError(
            "StartFraudsterRegistrationJobRequest.input_data_config required"
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
            "StartFraudsterRegistrationJobRequest.output_data_config required"
        )
    return out
