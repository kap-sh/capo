"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretListEntry``."""

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
    import capo_secrets_manager.types.role_arn_type
    import capo_secrets_manager.types.rotation_enabled_type
    import capo_secrets_manager.types.rotation_lambda_arn_type
    import capo_secrets_manager.types.rotation_rules_type
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.secret_name_type
    import capo_secrets_manager.types.secret_versions_to_stages_map_type
    import capo_secrets_manager.types.tag_list_type
    import capo_secrets_manager.types.timestamp_type


class SecretListEntry(TypedDict, closed=True):
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The Amazon Resource Name (ARN) of the secret.</p>"""
    name: NotRequired["capo_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The friendly name of the secret. </p>"""
    type: NotRequired["capo_secrets_manager.types.medea_type_type.MedeaTypeType"]
    """<p>The exact string that identifies the third-party partner that holds the external secret. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html">Managed external secret partners</a>.</p>"""
    description: NotRequired[
        "capo_secrets_manager.types.description_type.DescriptionType"
    ]
    """<p>The user-provided description of the secret.</p>"""
    kms_key_id: NotRequired["capo_secrets_manager.types.kms_key_id_type.KmsKeyIdType"]
    """<p>The ARN of the KMS key that Secrets Manager uses to encrypt the secret value. If the secret is encrypted with the Amazon Web Services managed key <code>aws/secretsmanager</code>, this field is omitted.</p>"""
    rotation_enabled: NotRequired[
        "capo_secrets_manager.types.rotation_enabled_type.RotationEnabledType"
    ]
    """<p>Indicates whether automatic, scheduled rotation is enabled for this secret.</p>"""
    rotation_lambda_arn: NotRequired[
        "capo_secrets_manager.types.rotation_lambda_arn_type.RotationLambdaARNType"
    ]
    """<p>The ARN of an Amazon Web Services Lambda function invoked by Secrets Manager to rotate and expire the secret either automatically per the schedule or manually by a call to <a href="https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html"> <code>RotateSecret</code> </a>.</p>"""
    rotation_rules: NotRequired[
        "capo_secrets_manager.types.rotation_rules_type.RotationRulesType"
    ]
    """<p>A structure that defines the rotation configuration for the secret.</p>"""
    external_secret_rotation_metadata: NotRequired[
        "capo_secrets_manager.types.external_secret_rotation_metadata_type.ExternalSecretRotationMetadataType"
    ]
    """<p>The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information about the required information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html">Managed external secrets partners</a>.</p>"""
    external_secret_rotation_role_arn: NotRequired[
        "capo_secrets_manager.types.role_arn_type.RoleARNType"
    ]
    """<p>The role that Secrets Manager assumes to call APIs required to perform the rotation. For more information about the required information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html">Managed external secrets partners</a>.</p>"""
    last_rotated_date: NotRequired[
        "capo_secrets_manager.types.last_rotated_date_type.LastRotatedDateType"
    ]
    """<p>The most recent date and time that the Secrets Manager rotation process was successfully completed. This value is null if the secret hasn't ever rotated.</p>"""
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
    """<p>The date and time the deletion of the secret occurred. Not present on active secrets. The secret can be recovered until the number of days in the recovery window has passed, as specified in the <code>RecoveryWindowInDays</code> parameter of the <a href="https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteSecret.html"> <code>DeleteSecret</code> </a> operation.</p>"""
    next_rotation_date: NotRequired[
        "capo_secrets_manager.types.next_rotation_date_type.NextRotationDateType"
    ]
    """<p>The next rotation is scheduled to occur on or before this date. If the secret isn't configured for rotation or rotation has been disabled, Secrets Manager returns null.</p>"""
    tags: NotRequired["capo_secrets_manager.types.tag_list_type.TagListType"]
    """<p>The list of user-defined tags associated with the secret. To add tags to a secret, use <a href="https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_TagResource.html"> <code>TagResource</code> </a>. To remove tags, use <a href="https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UntagResource.html"> <code>UntagResource</code> </a>.</p>"""
    secret_versions_to_stages: NotRequired[
        "capo_secrets_manager.types.secret_versions_to_stages_map_type.SecretVersionsToStagesMapType"
    ]
    """<p>A list of all of the currently assigned <code>SecretVersionStage</code> staging labels and the <code>SecretVersionId</code> attached to each one. Staging labels are used to keep track of the different versions during the rotation process.</p> <note> <p>A version that does not have any <code>SecretVersionStage</code> is considered deprecated and subject to deletion. Such versions are not included in this list.</p> </note>"""
    owning_service: NotRequired[
        "capo_secrets_manager.types.owning_service_type.OwningServiceType"
    ]
    """<p>Returns the name of the service that created the secret.</p>"""
    created_date: NotRequired["capo_secrets_manager.types.timestamp_type.TimestampType"]
    """<p>The date and time when a secret was created.</p>"""
    primary_region: NotRequired["capo_secrets_manager.types.region_type.RegionType"]
    """<p>The Region where Secrets Manager originated the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretListEntry) -> dict:
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
    if "secret_versions_to_stages" in value:
        import capo_secrets_manager.types.secret_versions_to_stages_map_type

        out["SecretVersionsToStages"] = (
            capo_secrets_manager.types.secret_versions_to_stages_map_type.serialize_aws_json_1_1(
                value["secret_versions_to_stages"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> SecretListEntry:
    out: SecretListEntry = {}  # type: ignore[typeddict-item]
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
    if data.get("SecretVersionsToStages") is not None:
        import capo_secrets_manager.types.secret_versions_to_stages_map_type

        out["secret_versions_to_stages"] = (
            capo_secrets_manager.types.secret_versions_to_stages_map_type.deserialize_aws_json_1_1(
                data["SecretVersionsToStages"]
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
    return out
