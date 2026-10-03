"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationTaskAssessmentRunMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.exclude_test_list
    import capo_database_migration_service.types.include_test_list
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.tag_list


class StartReplicationTaskAssessmentRunMessage(TypedDict, closed=True):
    replication_task_arn: "capo_database_migration_service.types.string.String"
    """<p>Amazon Resource Name (ARN) of the migration task associated with the premigration assessment run that you want to start.</p>"""
    service_access_role_arn: "capo_database_migration_service.types.string.String"
    """<p>ARN of the service role needed to start the assessment run. The role must allow the <code>iam:PassRole</code> action.</p>"""
    result_location_bucket: "capo_database_migration_service.types.string.String"
    """<p>Amazon S3 bucket where you want DMS to store the results of this assessment run.</p>"""
    result_location_folder: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Folder within an Amazon S3 bucket where you want DMS to store the results of this assessment run.</p>"""
    result_encryption_mode: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Encryption mode that you can specify to encrypt the results of this assessment run. If you don't specify this request parameter, DMS stores the assessment run results without encryption. You can specify one of the options following:</p> <ul> <li> <p> <code>"SSE_S3"</code> – The server-side encryption provided as a default by Amazon S3.</p> </li> <li> <p> <code>"SSE_KMS"</code> – Key Management Service (KMS) encryption. This encryption can use either a custom KMS encryption key that you specify or the default KMS encryption key that DMS provides.</p> </li> </ul>"""
    result_kms_key_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>ARN of a custom KMS encryption key that you specify when you set <code>ResultEncryptionMode</code> to <code>"SSE_KMS</code>".</p>"""
    assessment_run_name: "capo_database_migration_service.types.string.String"
    """<p>Unique name to identify the assessment run.</p>"""
    include_only: NotRequired[
        "capo_database_migration_service.types.include_test_list.IncludeTestList"
    ]
    """<p>Space-separated list of names for specific individual assessments that you want to include. These names come from the default list of individual assessments that DMS supports for the associated migration task. This task is specified by <code>ReplicationTaskArn</code>.</p> <note> <p>You can't set a value for <code>IncludeOnly</code> if you also set a value for <code>Exclude</code> in the API operation. </p> <p>To identify the names of the default individual assessments that DMS supports for the associated migration task, run the <code>DescribeApplicableIndividualAssessments</code> operation using its own <code>ReplicationTaskArn</code> request parameter.</p> </note>"""
    exclude: NotRequired[
        "capo_database_migration_service.types.exclude_test_list.ExcludeTestList"
    ]
    """<p>Space-separated list of names for specific individual assessments that you want to exclude. These names come from the default list of individual assessments that DMS supports for the associated migration task. This task is specified by <code>ReplicationTaskArn</code>.</p> <note> <p>You can't set a value for <code>Exclude</code> if you also set a value for <code>IncludeOnly</code> in the API operation.</p> <p>To identify the names of the default individual assessments that DMS supports for the associated migration task, run the <code>DescribeApplicableIndividualAssessments</code> operation using its own <code>ReplicationTaskArn</code> request parameter.</p> </note>"""
    tags: NotRequired["capo_database_migration_service.types.tag_list.TagList"]
    """<p>One or more tags to be assigned to the premigration assessment run that you want to start.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationTaskAssessmentRunMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
    out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    out["ResultLocationBucket"] = value["result_location_bucket"]
    if "result_location_folder" in value:
        out["ResultLocationFolder"] = value["result_location_folder"]
    if "result_encryption_mode" in value:
        out["ResultEncryptionMode"] = value["result_encryption_mode"]
    if "result_kms_key_arn" in value:
        out["ResultKmsKeyArn"] = value["result_kms_key_arn"]
    out["AssessmentRunName"] = value["assessment_run_name"]
    if "include_only" in value:
        import capo_database_migration_service.types.include_test_list

        out["IncludeOnly"] = (
            capo_database_migration_service.types.include_test_list.serialize_aws_json_1_1(
                value["include_only"]
            )
        )
    if "exclude" in value:
        import capo_database_migration_service.types.exclude_test_list

        out["Exclude"] = (
            capo_database_migration_service.types.exclude_test_list.serialize_aws_json_1_1(
                value["exclude"]
            )
        )
    if "tags" in value:
        import capo_database_migration_service.types.tag_list

        out["Tags"] = (
            capo_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplicationTaskAssessmentRunMessage:
    out: StartReplicationTaskAssessmentRunMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskArn") is not None:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        raise DeserializationError(
            "StartReplicationTaskAssessmentRunMessage.replication_task_arn required"
        )
    if data.get("ServiceAccessRoleArn") is not None:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartReplicationTaskAssessmentRunMessage.service_access_role_arn required"
        )
    if data.get("ResultLocationBucket") is not None:
        out["result_location_bucket"] = data["ResultLocationBucket"]
    else:
        raise DeserializationError(
            "StartReplicationTaskAssessmentRunMessage.result_location_bucket required"
        )
    if data.get("ResultLocationFolder") is not None:
        out["result_location_folder"] = data["ResultLocationFolder"]
    if data.get("ResultEncryptionMode") is not None:
        out["result_encryption_mode"] = data["ResultEncryptionMode"]
    if data.get("ResultKmsKeyArn") is not None:
        out["result_kms_key_arn"] = data["ResultKmsKeyArn"]
    if data.get("AssessmentRunName") is not None:
        out["assessment_run_name"] = data["AssessmentRunName"]
    else:
        raise DeserializationError(
            "StartReplicationTaskAssessmentRunMessage.assessment_run_name required"
        )
    if data.get("IncludeOnly") is not None:
        import capo_database_migration_service.types.include_test_list

        out["include_only"] = (
            capo_database_migration_service.types.include_test_list.deserialize_aws_json_1_1(
                data["IncludeOnly"]
            )
        )
    if data.get("Exclude") is not None:
        import capo_database_migration_service.types.exclude_test_list

        out["exclude"] = (
            capo_database_migration_service.types.exclude_test_list.deserialize_aws_json_1_1(
                data["Exclude"]
            )
        )
    if data.get("Tags") is not None:
        import capo_database_migration_service.types.tag_list

        out["tags"] = (
            capo_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    return out
