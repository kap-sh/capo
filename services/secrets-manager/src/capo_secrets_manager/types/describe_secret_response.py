"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DescribeSecretResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.deleted_date_type
    import capo_secrets_manager.types.description_type
    import capo_secrets_manager.types.external_secret_rotation_metadata_type
    import capo_secrets_manager.types.kms_key_id_type
    import capo_secrets_manager.types.last_accessed_date_type
    import capo_secrets_manager.types.last_changed_date_type
    import capo_secrets_manager.types.last_rotated_date_type
    import capo_secrets_manager.types.medea_type_type
    import capo_secrets_manager.types.next_rotation_date_type
    import capo_secrets_manager.types.owning_service_type
    import capo_secrets_manager.types.region_type
    import capo_secrets_manager.types.replication_status_list_type
    import capo_secrets_manager.types.role_arn_type
    import capo_secrets_manager.types.rotation_enabled_type
    import capo_secrets_manager.types.rotation_lambda_arn_type
    import capo_secrets_manager.types.rotation_rules_type
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.secret_name_type
    import capo_secrets_manager.types.secret_versions_to_stages_map_type
    import capo_secrets_manager.types.tag_list_type
    import capo_secrets_manager.types.timestamp_type


class DescribeSecretResponse(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["capo_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The name of the secret.</p>"""
    type: NotRequired["capo_secrets_manager.types.medea_type_type.MedeaTypeType"]
    """<p>The exact string that identifies the partner that holds the external secret. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html">Using Secrets Manager managed external secrets</a>.</p>"""
    description: NotRequired[
        "capo_secrets_manager.types.description_type.DescriptionType"
    ]
    """<p>The description of the secret.</p>"""
    kms_key_id: NotRequired["capo_secrets_manager.types.kms_key_id_type.KmsKeyIdType"]
    """<p>The key ID or alias ARN of the KMS key that Secrets Manager uses to encrypt the secret value. If the secret is encrypted with the Amazon Web Services managed key <code>aws/secretsmanager</code>, this field is omitted. Secrets created using the console use an KMS key ID.</p>"""
    rotation_enabled: NotRequired[
        "capo_secrets_manager.types.rotation_enabled_type.RotationEnabledType"
    ]
    """<p>Specifies whether automatic rotation is turned on for this secret. If the secret has never been configured for rotation, Secrets Manager returns null.</p> <p>To turn on rotation, use <a>RotateSecret</a>. To turn off rotation, use <a>CancelRotateSecret</a>.</p>"""
    rotation_lambda_arn: NotRequired[
        "capo_secrets_manager.types.rotation_lambda_arn_type.RotationLambdaARNType"
    ]
    """<p>The ARN of the Lambda function that Secrets Manager invokes to rotate the secret. </p>"""
    rotation_rules: NotRequired[
        "capo_secrets_manager.types.rotation_rules_type.RotationRulesType"
    ]
    """<p>The rotation schedule and Lambda function for this secret. If the secret previously had rotation turned on, but it is now turned off, this field shows the previous rotation schedule and rotation function. If the secret never had rotation turned on, this field is omitted.</p>"""
    external_secret_rotation_metadata: NotRequired[
        "capo_secrets_manager.types.external_secret_rotation_metadata_type.ExternalSecretRotationMetadataType"
    ]
    """<p>The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information about the required information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html">Managed external secrets partners</a>.</p>"""
    external_secret_rotation_role_arn: NotRequired[
        "capo_secrets_manager.types.role_arn_type.RoleARNType"
    ]
    """<p>The Amazon Resource Name (ARN) of the role that allows Secrets Manager to rotate a secret held by a third-party partner. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-security.html">Security and permissions</a>.</p>"""
    last_rotated_date: NotRequired[
        "capo_secrets_manager.types.last_rotated_date_type.LastRotatedDateType"
    ]
    """<p>The last date and time that Secrets Manager rotated the secret. If the secret isn't configured for rotation or rotation has been disabled, Secrets Manager returns null.</p>"""
    last_changed_date: NotRequired[
        "capo_secrets_manager.types.last_changed_date_type.LastChangedDateType"
    ]
    """<p>The last date and time that this secret was modified in any way.</p>"""
    last_accessed_date: NotRequired[
        "capo_secrets_manager.types.last_accessed_date_type.LastAccessedDateType"
    ]
    """<p>The date that the secret was last accessed in the Region. This field is omitted if the secret has never been retrieved in the Region.</p>"""
    deleted_date: NotRequired[
        "capo_secrets_manager.types.deleted_date_type.DeletedDateType"
    ]
    """<p>The date the secret is scheduled for deletion. If it is not scheduled for deletion, this field is omitted. When you delete a secret, Secrets Manager requires a recovery window of at least 7 days before deleting the secret. Some time after the deleted date, Secrets Manager deletes the secret, including all of its versions.</p> <p>If a secret is scheduled for deletion, then its details, including the encrypted secret value, is not accessible. To cancel a scheduled deletion and restore access to the secret, use <a>RestoreSecret</a>.</p>"""
    next_rotation_date: NotRequired[
        "capo_secrets_manager.types.next_rotation_date_type.NextRotationDateType"
    ]
    """<p>The next rotation is scheduled to occur on or before this date. If the secret isn't configured for rotation or rotation has been disabled, Secrets Manager returns null. If rotation fails, Secrets Manager retries the entire rotation process multiple times. If rotation is unsuccessful, this date may be in the past.</p> <p>This date represents the latest date that rotation will occur, but it is not an approximate rotation date. In some cases, for example if you turn off automatic rotation and then turn it back on, the next rotation may occur much sooner than this date.</p>"""
    tags: NotRequired["capo_secrets_manager.types.tag_list_type.TagListType"]
    """<p>The list of tags attached to the secret. To add tags to a secret, use <a>TagResource</a>. To remove tags, use <a>UntagResource</a>.</p>"""
    version_ids_to_stages: NotRequired[
        "capo_secrets_manager.types.secret_versions_to_stages_map_type.SecretVersionsToStagesMapType"
    ]
    """<p>A list of the versions of the secret that have staging labels attached. Versions that don't have staging labels are considered deprecated and Secrets Manager can delete them.</p> <p>Secrets Manager uses staging labels to indicate the status of a secret version during rotation. The three staging labels for rotation are: </p> <ul> <li> <p> <code>AWSCURRENT</code>, which indicates the current version of the secret.</p> </li> <li> <p> <code>AWSPENDING</code>, which indicates the version of the secret that contains new secret information that will become the next current version when rotation finishes.</p> <p>During rotation, Secrets Manager creates an <code>AWSPENDING</code> version ID before creating the new secret version. To check if a secret version exists, call <a>GetSecretValue</a>.</p> </li> <li> <p> <code>AWSPREVIOUS</code>, which indicates the previous current version of the secret. You can use this as the <i>last known good</i> version.</p> </li> </ul> <p>For more information about rotation and staging labels, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html">How rotation works</a>.</p>"""
    owning_service: NotRequired[
        "capo_secrets_manager.types.owning_service_type.OwningServiceType"
    ]
    """<p>The ID of the service that created this secret. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html">Secrets managed by other Amazon Web Services services</a>.</p>"""
    created_date: NotRequired["capo_secrets_manager.types.timestamp_type.TimestampType"]
    """<p>The date the secret was created.</p>"""
    primary_region: NotRequired["capo_secrets_manager.types.region_type.RegionType"]
    """<p>The Region the secret is in. If a secret is replicated to other Regions, the replicas are listed in <code>ReplicationStatus</code>. </p>"""
    replication_status: NotRequired[
        "capo_secrets_manager.types.replication_status_list_type.ReplicationStatusListType"
    ]
    """<p>A list of the replicas of this secret and their status: </p> <ul> <li> <p> <code>Failed</code>, which indicates that the replica was not created.</p> </li> <li> <p> <code>InProgress</code>, which indicates that Secrets Manager is in the process of creating the replica.</p> </li> <li> <p> <code>InSync</code>, which indicates that the replica was created.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSecretResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "rotation_enabled" in value:
        out["RotationEnabled"] = value["rotation_enabled"]
    if "rotation_lambda_arn" in value:
        out["RotationLambdaARN"] = value["rotation_lambda_arn"]
    if "rotation_rules" in value:
        import capo_secrets_manager.types.rotation_rules_type

        out["RotationRules"] = (
            capo_secrets_manager.types.rotation_rules_type.serialize_aws_json_1_1(
                value["rotation_rules"]
            )
        )
    if "external_secret_rotation_metadata" in value:
        import capo_secrets_manager.types.external_secret_rotation_metadata_type

        out["ExternalSecretRotationMetadata"] = (
            capo_secrets_manager.types.external_secret_rotation_metadata_type.serialize_aws_json_1_1(
                value["external_secret_rotation_metadata"]
            )
        )
    if "external_secret_rotation_role_arn" in value:
        out["ExternalSecretRotationRoleArn"] = value[
            "external_secret_rotation_role_arn"
        ]
    if "last_rotated_date" in value:
        import capo_secrets_manager.types.last_rotated_date_type

        out["LastRotatedDate"] = (
            capo_secrets_manager.types.last_rotated_date_type.serialize_aws_json_1_1(
                value["last_rotated_date"]
            )
        )
    if "last_changed_date" in value:
        import capo_secrets_manager.types.last_changed_date_type

        out["LastChangedDate"] = (
            capo_secrets_manager.types.last_changed_date_type.serialize_aws_json_1_1(
                value["last_changed_date"]
            )
        )
    if "last_accessed_date" in value:
        import capo_secrets_manager.types.last_accessed_date_type

        out["LastAccessedDate"] = (
            capo_secrets_manager.types.last_accessed_date_type.serialize_aws_json_1_1(
                value["last_accessed_date"]
            )
        )
    if "deleted_date" in value:
        import capo_secrets_manager.types.deleted_date_type

        out["DeletedDate"] = (
            capo_secrets_manager.types.deleted_date_type.serialize_aws_json_1_1(
                value["deleted_date"]
            )
        )
    if "next_rotation_date" in value:
        import capo_secrets_manager.types.next_rotation_date_type

        out["NextRotationDate"] = (
            capo_secrets_manager.types.next_rotation_date_type.serialize_aws_json_1_1(
                value["next_rotation_date"]
            )
        )
    if "tags" in value:
        import capo_secrets_manager.types.tag_list_type

        out["Tags"] = capo_secrets_manager.types.tag_list_type.serialize_aws_json_1_1(
            value["tags"]
        )
    if "version_ids_to_stages" in value:
        import capo_secrets_manager.types.secret_versions_to_stages_map_type

        out["VersionIdsToStages"] = (
            capo_secrets_manager.types.secret_versions_to_stages_map_type.serialize_aws_json_1_1(
                value["version_ids_to_stages"]
            )
        )
    if "owning_service" in value:
        out["OwningService"] = value["owning_service"]
    if "created_date" in value:
        import capo_secrets_manager.types.timestamp_type

        out["CreatedDate"] = (
            capo_secrets_manager.types.timestamp_type.serialize_aws_json_1_1(
                value["created_date"]
            )
        )
    if "primary_region" in value:
        out["PrimaryRegion"] = value["primary_region"]
    if "replication_status" in value:
        import capo_secrets_manager.types.replication_status_list_type

        out["ReplicationStatus"] = (
            capo_secrets_manager.types.replication_status_list_type.serialize_aws_json_1_1(
                value["replication_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSecretResponse:
    out: DescribeSecretResponse = {}  # type: ignore[typeddict-item]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("RotationEnabled") is not None:
        out["rotation_enabled"] = data["RotationEnabled"]
    if data.get("RotationLambdaARN") is not None:
        out["rotation_lambda_arn"] = data["RotationLambdaARN"]
    if data.get("RotationRules") is not None:
        import capo_secrets_manager.types.rotation_rules_type

        out["rotation_rules"] = (
            capo_secrets_manager.types.rotation_rules_type.deserialize_aws_json_1_1(
                data["RotationRules"]
            )
        )
    if data.get("ExternalSecretRotationMetadata") is not None:
        import capo_secrets_manager.types.external_secret_rotation_metadata_type

        out["external_secret_rotation_metadata"] = (
            capo_secrets_manager.types.external_secret_rotation_metadata_type.deserialize_aws_json_1_1(
                data["ExternalSecretRotationMetadata"]
            )
        )
    if data.get("ExternalSecretRotationRoleArn") is not None:
        out["external_secret_rotation_role_arn"] = data["ExternalSecretRotationRoleArn"]
    if data.get("LastRotatedDate") is not None:
        import capo_secrets_manager.types.last_rotated_date_type

        out["last_rotated_date"] = (
            capo_secrets_manager.types.last_rotated_date_type.deserialize_aws_json_1_1(
                data["LastRotatedDate"]
            )
        )
    if data.get("LastChangedDate") is not None:
        import capo_secrets_manager.types.last_changed_date_type

        out["last_changed_date"] = (
            capo_secrets_manager.types.last_changed_date_type.deserialize_aws_json_1_1(
                data["LastChangedDate"]
            )
        )
    if data.get("LastAccessedDate") is not None:
        import capo_secrets_manager.types.last_accessed_date_type

        out["last_accessed_date"] = (
            capo_secrets_manager.types.last_accessed_date_type.deserialize_aws_json_1_1(
                data["LastAccessedDate"]
            )
        )
    if data.get("DeletedDate") is not None:
        import capo_secrets_manager.types.deleted_date_type

        out["deleted_date"] = (
            capo_secrets_manager.types.deleted_date_type.deserialize_aws_json_1_1(
                data["DeletedDate"]
            )
        )
    if data.get("NextRotationDate") is not None:
        import capo_secrets_manager.types.next_rotation_date_type

        out["next_rotation_date"] = (
            capo_secrets_manager.types.next_rotation_date_type.deserialize_aws_json_1_1(
                data["NextRotationDate"]
            )
        )
    if data.get("Tags") is not None:
        import capo_secrets_manager.types.tag_list_type

        out["tags"] = capo_secrets_manager.types.tag_list_type.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("VersionIdsToStages") is not None:
        import capo_secrets_manager.types.secret_versions_to_stages_map_type

        out["version_ids_to_stages"] = (
            capo_secrets_manager.types.secret_versions_to_stages_map_type.deserialize_aws_json_1_1(
                data["VersionIdsToStages"]
            )
        )
    if data.get("OwningService") is not None:
        out["owning_service"] = data["OwningService"]
    if data.get("CreatedDate") is not None:
        import capo_secrets_manager.types.timestamp_type

        out["created_date"] = (
            capo_secrets_manager.types.timestamp_type.deserialize_aws_json_1_1(
                data["CreatedDate"]
            )
        )
    if data.get("PrimaryRegion") is not None:
        out["primary_region"] = data["PrimaryRegion"]
    if data.get("ReplicationStatus") is not None:
        import capo_secrets_manager.types.replication_status_list_type

        out["replication_status"] = (
            capo_secrets_manager.types.replication_status_list_type.deserialize_aws_json_1_1(
                data["ReplicationStatus"]
            )
        )
    return out
