"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserImportJobType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.completion_message_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.long_type
    import capo_cognito_identity_provider.types.password_hashing_algorithm_type
    import capo_cognito_identity_provider.types.pre_signed_url_type
    import capo_cognito_identity_provider.types.user_import_job_id_type
    import capo_cognito_identity_provider.types.user_import_job_name_type
    import capo_cognito_identity_provider.types.user_import_job_status_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class UserImportJobType(TypedDict, closed=True):
    job_name: NotRequired[
        "capo_cognito_identity_provider.types.user_import_job_name_type.UserImportJobNameType"
    ]
    """<p>The friendly name of the user import job.</p>"""
    job_id: NotRequired[
        "capo_cognito_identity_provider.types.user_import_job_id_type.UserImportJobIdType"
    ]
    """<p>The ID of the user import job.</p>"""
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that the users are being imported into.</p>"""
    pre_signed_url: NotRequired[
        "capo_cognito_identity_provider.types.pre_signed_url_type.PreSignedUrlType"
    ]
    """<p>The pre-signed URL target for uploading the CSV file.</p>"""
    creation_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    start_date: NotRequired["capo_cognito_identity_provider.types.date_type.DateType"]
    """<p>The date when the user import job was started.</p>"""
    completion_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date when the user import job was completed.</p>"""
    status: NotRequired[
        "capo_cognito_identity_provider.types.user_import_job_status_type.UserImportJobStatusType"
    ]
    """<p>The status of the user import job. One of the following:</p> <ul> <li> <p> <code>Created</code> - The job was created but not started.</p> </li> <li> <p> <code>Pending</code> - A transition state. You have started the job, but it has not begun importing users yet.</p> </li> <li> <p> <code>InProgress</code> - The job has started, and users are being imported.</p> </li> <li> <p> <code>Stopping</code> - You have stopped the job, but the job has not stopped importing users yet.</p> </li> <li> <p> <code>Stopped</code> - You have stopped the job, and the job has stopped importing users.</p> </li> <li> <p> <code>Succeeded</code> - The job has completed successfully.</p> </li> <li> <p> <code>Failed</code> - The job has stopped due to an error.</p> </li> <li> <p> <code>Expired</code> - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job can't be started.</p> </li> </ul>"""
    cloud_watch_logs_role_arn: NotRequired[
        "capo_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The role Amazon Resource Name (ARN) for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.</p>"""
    imported_users: "capo_cognito_identity_provider.types.long_type.LongType"
    """<p>The number of users that were successfully imported.</p>"""
    skipped_users: "capo_cognito_identity_provider.types.long_type.LongType"
    """<p>The number of users that were skipped.</p>"""
    failed_users: "capo_cognito_identity_provider.types.long_type.LongType"
    """<p>The number of users that couldn't be imported.</p>"""
    completion_message: NotRequired[
        "capo_cognito_identity_provider.types.completion_message_type.CompletionMessageType"
    ]
    """<p>The message returned when the user import job is completed.</p>"""
    password_hashing_algorithm: NotRequired[
        "capo_cognito_identity_provider.types.password_hashing_algorithm_type.PasswordHashingAlgorithmType"
    ]
    """<p>The password hashing algorithm used to generate the hashes in the CSV file for this import job.</p> <p>Valid values: <code>BCRYPT</code> | <code>SCRYPT</code> | <code>ARGON2ID</code> | <code>PBKDF2_SHA256</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserImportJobType) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "pre_signed_url" in value:
        out["PreSignedUrl"] = value["pre_signed_url"]
    if "creation_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CreationDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "start_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["StartDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["start_date"]
            )
        )
    if "completion_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CompletionDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["completion_date"]
            )
        )
    if "status" in value:
        import capo_cognito_identity_provider.types.user_import_job_status_type

        out["Status"] = (
            capo_cognito_identity_provider.types.user_import_job_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "cloud_watch_logs_role_arn" in value:
        out["CloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    out["ImportedUsers"] = value.get("imported_users", 0)
    out["SkippedUsers"] = value.get("skipped_users", 0)
    out["FailedUsers"] = value.get("failed_users", 0)
    if "completion_message" in value:
        out["CompletionMessage"] = value["completion_message"]
    if "password_hashing_algorithm" in value:
        import capo_cognito_identity_provider.types.password_hashing_algorithm_type

        out["PasswordHashingAlgorithm"] = (
            capo_cognito_identity_provider.types.password_hashing_algorithm_type.serialize_aws_json_1_1(
                value["password_hashing_algorithm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserImportJobType:
    out: UserImportJobType = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    if data.get("PreSignedUrl") is not None:
        out["pre_signed_url"] = data["PreSignedUrl"]
    if data.get("CreationDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if data.get("StartDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["start_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["StartDate"]
            )
        )
    if data.get("CompletionDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["completion_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CompletionDate"]
            )
        )
    if data.get("Status") is not None:
        import capo_cognito_identity_provider.types.user_import_job_status_type

        out["status"] = (
            capo_cognito_identity_provider.types.user_import_job_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("CloudWatchLogsRoleArn") is not None:
        out["cloud_watch_logs_role_arn"] = data["CloudWatchLogsRoleArn"]
    if data.get("ImportedUsers") is not None:
        out["imported_users"] = data["ImportedUsers"]
    else:
        out["imported_users"] = 0
    if data.get("SkippedUsers") is not None:
        out["skipped_users"] = data["SkippedUsers"]
    else:
        out["skipped_users"] = 0
    if data.get("FailedUsers") is not None:
        out["failed_users"] = data["FailedUsers"]
    else:
        out["failed_users"] = 0
    if data.get("CompletionMessage") is not None:
        out["completion_message"] = data["CompletionMessage"]
    if data.get("PasswordHashingAlgorithm") is not None:
        import capo_cognito_identity_provider.types.password_hashing_algorithm_type

        out["password_hashing_algorithm"] = (
            capo_cognito_identity_provider.types.password_hashing_algorithm_type.deserialize_aws_json_1_1(
                data["PasswordHashingAlgorithm"]
            )
        )
    return out
