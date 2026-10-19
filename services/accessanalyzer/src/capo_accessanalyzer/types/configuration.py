"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Configuration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError
from capo_accessanalyzer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_accessanalyzer.types.dynamodb_stream_configuration
    import capo_accessanalyzer.types.dynamodb_table_configuration
    import capo_accessanalyzer.types.ebs_snapshot_configuration
    import capo_accessanalyzer.types.ecr_repository_configuration
    import capo_accessanalyzer.types.efs_file_system_configuration
    import capo_accessanalyzer.types.iam_role_configuration
    import capo_accessanalyzer.types.kms_key_configuration
    import capo_accessanalyzer.types.rds_db_cluster_snapshot_configuration
    import capo_accessanalyzer.types.rds_db_snapshot_configuration
    import capo_accessanalyzer.types.s3_bucket_configuration
    import capo_accessanalyzer.types.s3_express_directory_bucket_configuration
    import capo_accessanalyzer.types.secrets_manager_secret_configuration
    import capo_accessanalyzer.types.sns_topic_configuration
    import capo_accessanalyzer.types.sqs_queue_configuration


class _Configuration_ebsSnapshot(TypedDict, closed=True):
    ebsSnapshot: (
        "capo_accessanalyzer.types.ebs_snapshot_configuration.EbsSnapshotConfiguration"
    )


class _Configuration_ecrRepository(TypedDict, closed=True):
    ecrRepository: "capo_accessanalyzer.types.ecr_repository_configuration.EcrRepositoryConfiguration"


class _Configuration_iamRole(TypedDict, closed=True):
    iamRole: "capo_accessanalyzer.types.iam_role_configuration.IamRoleConfiguration"


class _Configuration_efsFileSystem(TypedDict, closed=True):
    efsFileSystem: "capo_accessanalyzer.types.efs_file_system_configuration.EfsFileSystemConfiguration"


class _Configuration_kmsKey(TypedDict, closed=True):
    kmsKey: "capo_accessanalyzer.types.kms_key_configuration.KmsKeyConfiguration"


class _Configuration_rdsDbClusterSnapshot(TypedDict, closed=True):
    rdsDbClusterSnapshot: "capo_accessanalyzer.types.rds_db_cluster_snapshot_configuration.RdsDbClusterSnapshotConfiguration"


class _Configuration_rdsDbSnapshot(TypedDict, closed=True):
    rdsDbSnapshot: "capo_accessanalyzer.types.rds_db_snapshot_configuration.RdsDbSnapshotConfiguration"


class _Configuration_secretsManagerSecret(TypedDict, closed=True):
    secretsManagerSecret: "capo_accessanalyzer.types.secrets_manager_secret_configuration.SecretsManagerSecretConfiguration"


class _Configuration_s3Bucket(TypedDict, closed=True):
    s3Bucket: "capo_accessanalyzer.types.s3_bucket_configuration.S3BucketConfiguration"


class _Configuration_snsTopic(TypedDict, closed=True):
    snsTopic: "capo_accessanalyzer.types.sns_topic_configuration.SnsTopicConfiguration"


class _Configuration_sqsQueue(TypedDict, closed=True):
    sqsQueue: "capo_accessanalyzer.types.sqs_queue_configuration.SqsQueueConfiguration"


class _Configuration_s3ExpressDirectoryBucket(TypedDict, closed=True):
    s3ExpressDirectoryBucket: "capo_accessanalyzer.types.s3_express_directory_bucket_configuration.S3ExpressDirectoryBucketConfiguration"


class _Configuration_dynamodbStream(TypedDict, closed=True):
    dynamodbStream: "capo_accessanalyzer.types.dynamodb_stream_configuration.DynamodbStreamConfiguration"


class _Configuration_dynamodbTable(TypedDict, closed=True):
    dynamodbTable: "capo_accessanalyzer.types.dynamodb_table_configuration.DynamodbTableConfiguration"


Configuration: TypeAlias = (
    _Configuration_ebsSnapshot
    | _Configuration_ecrRepository
    | _Configuration_iamRole
    | _Configuration_efsFileSystem
    | _Configuration_kmsKey
    | _Configuration_rdsDbClusterSnapshot
    | _Configuration_rdsDbSnapshot
    | _Configuration_secretsManagerSecret
    | _Configuration_s3Bucket
    | _Configuration_snsTopic
    | _Configuration_sqsQueue
    | _Configuration_s3ExpressDirectoryBucket
    | _Configuration_dynamodbStream
    | _Configuration_dynamodbTable
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Configuration: cannot serialize unknown variant {value.name!r}"
        )
    elif "ebsSnapshot" in value:
        import capo_accessanalyzer.types.ebs_snapshot_configuration

        return {
            "ebsSnapshot": capo_accessanalyzer.types.ebs_snapshot_configuration.serialize_json(
                value["ebsSnapshot"]
            )
        }
    elif "ecrRepository" in value:
        import capo_accessanalyzer.types.ecr_repository_configuration

        return {
            "ecrRepository": capo_accessanalyzer.types.ecr_repository_configuration.serialize_json(
                value["ecrRepository"]
            )
        }
    elif "iamRole" in value:
        import capo_accessanalyzer.types.iam_role_configuration

        return {
            "iamRole": capo_accessanalyzer.types.iam_role_configuration.serialize_json(
                value["iamRole"]
            )
        }
    elif "efsFileSystem" in value:
        import capo_accessanalyzer.types.efs_file_system_configuration

        return {
            "efsFileSystem": capo_accessanalyzer.types.efs_file_system_configuration.serialize_json(
                value["efsFileSystem"]
            )
        }
    elif "kmsKey" in value:
        import capo_accessanalyzer.types.kms_key_configuration

        return {
            "kmsKey": capo_accessanalyzer.types.kms_key_configuration.serialize_json(
                value["kmsKey"]
            )
        }
    elif "rdsDbClusterSnapshot" in value:
        import capo_accessanalyzer.types.rds_db_cluster_snapshot_configuration

        return {
            "rdsDbClusterSnapshot": capo_accessanalyzer.types.rds_db_cluster_snapshot_configuration.serialize_json(
                value["rdsDbClusterSnapshot"]
            )
        }
    elif "rdsDbSnapshot" in value:
        import capo_accessanalyzer.types.rds_db_snapshot_configuration

        return {
            "rdsDbSnapshot": capo_accessanalyzer.types.rds_db_snapshot_configuration.serialize_json(
                value["rdsDbSnapshot"]
            )
        }
    elif "secretsManagerSecret" in value:
        import capo_accessanalyzer.types.secrets_manager_secret_configuration

        return {
            "secretsManagerSecret": capo_accessanalyzer.types.secrets_manager_secret_configuration.serialize_json(
                value["secretsManagerSecret"]
            )
        }
    elif "s3Bucket" in value:
        import capo_accessanalyzer.types.s3_bucket_configuration

        return {
            "s3Bucket": capo_accessanalyzer.types.s3_bucket_configuration.serialize_json(
                value["s3Bucket"]
            )
        }
    elif "snsTopic" in value:
        import capo_accessanalyzer.types.sns_topic_configuration

        return {
            "snsTopic": capo_accessanalyzer.types.sns_topic_configuration.serialize_json(
                value["snsTopic"]
            )
        }
    elif "sqsQueue" in value:
        import capo_accessanalyzer.types.sqs_queue_configuration

        return {
            "sqsQueue": capo_accessanalyzer.types.sqs_queue_configuration.serialize_json(
                value["sqsQueue"]
            )
        }
    elif "s3ExpressDirectoryBucket" in value:
        import capo_accessanalyzer.types.s3_express_directory_bucket_configuration

        return {
            "s3ExpressDirectoryBucket": capo_accessanalyzer.types.s3_express_directory_bucket_configuration.serialize_json(
                value["s3ExpressDirectoryBucket"]
            )
        }
    elif "dynamodbStream" in value:
        import capo_accessanalyzer.types.dynamodb_stream_configuration

        return {
            "dynamodbStream": capo_accessanalyzer.types.dynamodb_stream_configuration.serialize_json(
                value["dynamodbStream"]
            )
        }
    elif "dynamodbTable" in value:
        import capo_accessanalyzer.types.dynamodb_table_configuration

        return {
            "dynamodbTable": capo_accessanalyzer.types.dynamodb_table_configuration.serialize_json(
                value["dynamodbTable"]
            )
        }
    else:
        raise SerializationError("Configuration: no variant present")


def deserialize_json(data: dict) -> Configuration:
    if data.get("ebsSnapshot") is not None:
        import capo_accessanalyzer.types.ebs_snapshot_configuration

        return {
            "ebsSnapshot": capo_accessanalyzer.types.ebs_snapshot_configuration.deserialize_json(
                data["ebsSnapshot"]
            )
        }
    elif data.get("ecrRepository") is not None:
        import capo_accessanalyzer.types.ecr_repository_configuration

        return {
            "ecrRepository": capo_accessanalyzer.types.ecr_repository_configuration.deserialize_json(
                data["ecrRepository"]
            )
        }
    elif data.get("iamRole") is not None:
        import capo_accessanalyzer.types.iam_role_configuration

        return {
            "iamRole": capo_accessanalyzer.types.iam_role_configuration.deserialize_json(
                data["iamRole"]
            )
        }
    elif data.get("efsFileSystem") is not None:
        import capo_accessanalyzer.types.efs_file_system_configuration

        return {
            "efsFileSystem": capo_accessanalyzer.types.efs_file_system_configuration.deserialize_json(
                data["efsFileSystem"]
            )
        }
    elif data.get("kmsKey") is not None:
        import capo_accessanalyzer.types.kms_key_configuration

        return {
            "kmsKey": capo_accessanalyzer.types.kms_key_configuration.deserialize_json(
                data["kmsKey"]
            )
        }
    elif data.get("rdsDbClusterSnapshot") is not None:
        import capo_accessanalyzer.types.rds_db_cluster_snapshot_configuration

        return {
            "rdsDbClusterSnapshot": capo_accessanalyzer.types.rds_db_cluster_snapshot_configuration.deserialize_json(
                data["rdsDbClusterSnapshot"]
            )
        }
    elif data.get("rdsDbSnapshot") is not None:
        import capo_accessanalyzer.types.rds_db_snapshot_configuration

        return {
            "rdsDbSnapshot": capo_accessanalyzer.types.rds_db_snapshot_configuration.deserialize_json(
                data["rdsDbSnapshot"]
            )
        }
    elif data.get("secretsManagerSecret") is not None:
        import capo_accessanalyzer.types.secrets_manager_secret_configuration

        return {
            "secretsManagerSecret": capo_accessanalyzer.types.secrets_manager_secret_configuration.deserialize_json(
                data["secretsManagerSecret"]
            )
        }
    elif data.get("s3Bucket") is not None:
        import capo_accessanalyzer.types.s3_bucket_configuration

        return {
            "s3Bucket": capo_accessanalyzer.types.s3_bucket_configuration.deserialize_json(
                data["s3Bucket"]
            )
        }
    elif data.get("snsTopic") is not None:
        import capo_accessanalyzer.types.sns_topic_configuration

        return {
            "snsTopic": capo_accessanalyzer.types.sns_topic_configuration.deserialize_json(
                data["snsTopic"]
            )
        }
    elif data.get("sqsQueue") is not None:
        import capo_accessanalyzer.types.sqs_queue_configuration

        return {
            "sqsQueue": capo_accessanalyzer.types.sqs_queue_configuration.deserialize_json(
                data["sqsQueue"]
            )
        }
    elif data.get("s3ExpressDirectoryBucket") is not None:
        import capo_accessanalyzer.types.s3_express_directory_bucket_configuration

        return {
            "s3ExpressDirectoryBucket": capo_accessanalyzer.types.s3_express_directory_bucket_configuration.deserialize_json(
                data["s3ExpressDirectoryBucket"]
            )
        }
    elif data.get("dynamodbStream") is not None:
        import capo_accessanalyzer.types.dynamodb_stream_configuration

        return {
            "dynamodbStream": capo_accessanalyzer.types.dynamodb_stream_configuration.deserialize_json(
                data["dynamodbStream"]
            )
        }
    elif data.get("dynamodbTable") is not None:
        import capo_accessanalyzer.types.dynamodb_table_configuration

        return {
            "dynamodbTable": capo_accessanalyzer.types.dynamodb_table_configuration.deserialize_json(
                data["dynamodbTable"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Configuration: no recognized variant key")
