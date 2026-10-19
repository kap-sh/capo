"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateUserImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.password_hashing_algorithm_type
    import capo_cognito_identity_provider.types.user_import_job_name_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class CreateUserImportJobRequest(TypedDict, closed=True):
    job_name: "capo_cognito_identity_provider.types.user_import_job_name_type.UserImportJobNameType"
    """<p>A friendly name for the user import job.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that you want to import users into.</p>"""
    cloud_watch_logs_role_arn: "capo_cognito_identity_provider.types.arn_type.ArnType"
    """<p>You must specify an IAM role that has permission to log import-job results to Amazon CloudWatch Logs. This parameter is the ARN of that role.</p>"""
    password_hashing_algorithm: NotRequired[
        "capo_cognito_identity_provider.types.password_hashing_algorithm_type.PasswordHashingAlgorithmType"
    ]
    """<p>The password hashing algorithm used to generate the hashes in the CSV file for this import job.</p> <p>Valid values: <code>BCRYPT</code> | <code>SCRYPT</code> | <code>ARGON2ID</code> | <code>PBKDF2_SHA256</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserImportJobRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    out["UserPoolId"] = value["user_pool_id"]
    out["CloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    if "password_hashing_algorithm" in value:
        import capo_cognito_identity_provider.types.password_hashing_algorithm_type

        out["PasswordHashingAlgorithm"] = (
            capo_cognito_identity_provider.types.password_hashing_algorithm_type.serialize_aws_json_1_1(
                value["password_hashing_algorithm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserImportJobRequest:
    out: CreateUserImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        out["job_name"] = ""
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("CloudWatchLogsRoleArn") is not None:
        out["cloud_watch_logs_role_arn"] = data["CloudWatchLogsRoleArn"]
    else:
        out["cloud_watch_logs_role_arn"] = ""
    if data.get("PasswordHashingAlgorithm") is not None:
        import capo_cognito_identity_provider.types.password_hashing_algorithm_type

        out["password_hashing_algorithm"] = (
            capo_cognito_identity_provider.types.password_hashing_algorithm_type.deserialize_aws_json_1_1(
                data["PasswordHashingAlgorithm"]
            )
        )
    return out
