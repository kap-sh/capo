"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StartPHIDetectionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehendmedical.types.client_request_token_string
    import capo_comprehendmedical.types.iam_role_arn
    import capo_comprehendmedical.types.input_data_config
    import capo_comprehendmedical.types.job_name
    import capo_comprehendmedical.types.kms_key
    import capo_comprehendmedical.types.language_code
    import capo_comprehendmedical.types.output_data_config


class StartPHIDetectionJobRequest(TypedDict, closed=True):
    input_data_config: "capo_comprehendmedical.types.input_data_config.InputDataConfig"
    """<p>Specifies the format and location of the input data for the job.</p>"""
    output_data_config: (
        "capo_comprehendmedical.types.output_data_config.OutputDataConfig"
    )
    """<p>Specifies where to send the output files.</p>"""
    data_access_role_arn: "capo_comprehendmedical.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions-med.html#auth-role-permissions-med"> Role-Based Permissions Required for Asynchronous Operations</a>.</p>"""
    job_name: NotRequired["capo_comprehendmedical.types.job_name.JobName"]
    """<p>The identifier of the job.</p>"""
    client_request_token: NotRequired[
        "capo_comprehendmedical.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend Medical generates one.</p>"""
    kms_key: NotRequired["capo_comprehendmedical.types.kms_key.KMSKey"]
    """<p>An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.</p>"""
    language_code: "capo_comprehendmedical.types.language_code.LanguageCode"
    """<p>The language of the input documents. All documents must be in the same language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartPHIDetectionJobRequest) -> dict:
    out: dict = {}
    import capo_comprehendmedical.types.input_data_config

    out["InputDataConfig"] = (
        capo_comprehendmedical.types.input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    import capo_comprehendmedical.types.output_data_config

    out["OutputDataConfig"] = (
        capo_comprehendmedical.types.output_data_config.serialize_aws_json_1_1(
            value["output_data_config"]
        )
    )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    import capo_comprehendmedical.types.language_code

    out["LanguageCode"] = (
        capo_comprehendmedical.types.language_code.serialize_aws_json_1_1(
            value["language_code"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartPHIDetectionJobRequest:
    out: StartPHIDetectionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("InputDataConfig") is not None:
        import capo_comprehendmedical.types.input_data_config

        out["input_data_config"] = (
            capo_comprehendmedical.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartPHIDetectionJobRequest.input_data_config required"
        )
    if data.get("OutputDataConfig") is not None:
        import capo_comprehendmedical.types.output_data_config

        out["output_data_config"] = (
            capo_comprehendmedical.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartPHIDetectionJobRequest.output_data_config required"
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartPHIDetectionJobRequest.data_access_role_arn required"
        )
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("KMSKey") is not None:
        out["kms_key"] = data["KMSKey"]
    if data.get("LanguageCode") is not None:
        import capo_comprehendmedical.types.language_code

        out["language_code"] = (
            capo_comprehendmedical.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("StartPHIDetectionJobRequest.language_code required")
    return out
