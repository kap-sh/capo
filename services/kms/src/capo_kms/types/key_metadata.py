"""Generated from Smithy shape ``com.amazonaws.kms#KeyMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.arn_type
    import capo_kms.types.aws_account_id_type
    import capo_kms.types.backing_key_id_type
    import capo_kms.types.boolean_type
    import capo_kms.types.cloud_hsm_cluster_id_type
    import capo_kms.types.custom_key_store_id_type
    import capo_kms.types.customer_master_key_spec
    import capo_kms.types.date_type
    import capo_kms.types.description_type
    import capo_kms.types.encryption_algorithm_spec_list
    import capo_kms.types.expiration_model_type
    import capo_kms.types.key_agreement_algorithm_spec_list
    import capo_kms.types.key_id_type
    import capo_kms.types.key_manager_type
    import capo_kms.types.key_spec
    import capo_kms.types.key_state
    import capo_kms.types.key_usage_type
    import capo_kms.types.mac_algorithm_spec_list
    import capo_kms.types.multi_region_configuration
    import capo_kms.types.nullable_boolean_type
    import capo_kms.types.origin_type
    import capo_kms.types.pending_window_in_days_type
    import capo_kms.types.signing_algorithm_spec_list
    import capo_kms.types.xks_key_configuration_type


class KeyMetadata(TypedDict, closed=True):
    aws_account_id: NotRequired["capo_kms.types.aws_account_id_type.AWSAccountIdType"]
    """<p>The twelve-digit account ID of the Amazon Web Services account that owns the KMS key.</p>"""
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>The globally unique identifier for the KMS key.</p>"""
    arn: NotRequired["capo_kms.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name (ARN) of the KMS key. For examples, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms">Key Management Service (KMS)</a> in the Example ARNs section of the <i>Amazon Web Services General Reference</i>.</p>"""
    creation_date: NotRequired["capo_kms.types.date_type.DateType"]
    """<p>The date and time when the KMS key was created.</p>"""
    enabled: "capo_kms.types.boolean_type.BooleanType"
    """<p>Specifies whether the KMS key is enabled. When <code>KeyState</code> is <code>Enabled</code> this value is true, otherwise it is false.</p>"""
    description: NotRequired["capo_kms.types.description_type.DescriptionType"]
    """<p>The description of the KMS key.</p>"""
    key_usage: NotRequired["capo_kms.types.key_usage_type.KeyUsageType"]
    """<p>The <a href="https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations">cryptographic operations</a> for which you can use the KMS key.</p>"""
    key_state: NotRequired["capo_kms.types.key_state.KeyState"]
    """<p>The current status of the KMS key.</p> <p>For more information about how key state affects the use of a KMS key, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html">Key states of KMS keys</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    deletion_date: NotRequired["capo_kms.types.date_type.DateType"]
    """<p>The date and time after which KMS deletes this KMS key. This value is present only when the KMS key is scheduled for deletion, that is, when its <code>KeyState</code> is <code>PendingDeletion</code>.</p> <p>When the primary key in a multi-Region key is scheduled for deletion but still has replica keys, its key state is <code>PendingReplicaDeletion</code> and the length of its waiting period is displayed in the <code>PendingDeletionWindowInDays</code> field.</p>"""
    valid_to: NotRequired["capo_kms.types.date_type.DateType"]
    """<p>The earliest time at which any imported key material permanently associated with this KMS key expires. When a key material expires, KMS deletes the key material and the KMS key becomes unusable. This value is present only for KMS keys whose <code>Origin</code> is <code>EXTERNAL</code> and the <code>ExpirationModel</code> is <code>KEY_MATERIAL_EXPIRES</code>, otherwise this value is omitted.</p>"""
    origin: NotRequired["capo_kms.types.origin_type.OriginType"]
    """<p>The source of the key material for the KMS key. When this value is <code>AWS_KMS</code>, KMS created the key material. When this value is <code>EXTERNAL</code>, the key material was imported or the KMS key doesn't have any key material. When this value is <code>AWS_CLOUDHSM</code>, the key material was created in the CloudHSM cluster associated with a custom key store.</p>"""
    custom_key_store_id: NotRequired[
        "capo_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    ]
    """<p>A unique identifier for the <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html">custom key store</a> that contains the KMS key. This field is present only when the KMS key is created in a custom key store.</p>"""
    cloud_hsm_cluster_id: NotRequired[
        "capo_kms.types.cloud_hsm_cluster_id_type.CloudHsmClusterIdType"
    ]
    """<p>The cluster ID of the CloudHSM cluster that contains the key material for the KMS key. When you create a KMS key in an CloudHSM <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html">custom key store</a>, KMS creates the key material for the KMS key in the associated CloudHSM cluster. This field is present only when the KMS key is created in an CloudHSM key store.</p>"""
    expiration_model: NotRequired[
        "capo_kms.types.expiration_model_type.ExpirationModelType"
    ]
    """<p>Specifies whether the KMS key's key material expires. This value is present only when <code>Origin</code> is <code>EXTERNAL</code>, otherwise this value is omitted.</p>"""
    key_manager: NotRequired["capo_kms.types.key_manager_type.KeyManagerType"]
    """<p>The manager of the KMS key. KMS keys in your Amazon Web Services account are either customer managed or Amazon Web Services managed. For more information about the difference, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys">KMS keys</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    customer_master_key_spec: NotRequired[
        "capo_kms.types.customer_master_key_spec.CustomerMasterKeySpec"
    ]
    """<p>Instead, use the <code>KeySpec</code> field.</p> <p>The <code>KeySpec</code> and <code>CustomerMasterKeySpec</code> fields have the same value. We recommend that you use the <code>KeySpec</code> field in your code. However, to avoid breaking changes, KMS supports both fields.</p>"""
    key_spec: NotRequired["capo_kms.types.key_spec.KeySpec"]
    """<p>Describes the type of key material in the KMS key.</p>"""
    encryption_algorithms: NotRequired[
        "capo_kms.types.encryption_algorithm_spec_list.EncryptionAlgorithmSpecList"
    ]
    """<p>The encryption algorithms that the KMS key supports. You cannot use the KMS key with other encryption algorithms within KMS.</p> <p>This value is present only when the <code>KeyUsage</code> of the KMS key is <code>ENCRYPT_DECRYPT</code>.</p>"""
    signing_algorithms: NotRequired[
        "capo_kms.types.signing_algorithm_spec_list.SigningAlgorithmSpecList"
    ]
    """<p>The signing algorithms that the KMS key supports. You cannot use the KMS key with other signing algorithms within KMS.</p> <p>This field appears only when the <code>KeyUsage</code> of the KMS key is <code>SIGN_VERIFY</code>.</p>"""
    key_agreement_algorithms: NotRequired[
        "capo_kms.types.key_agreement_algorithm_spec_list.KeyAgreementAlgorithmSpecList"
    ]
    """<p>The key agreement algorithm used to derive a shared secret.</p>"""
    multi_region: NotRequired[
        "capo_kms.types.nullable_boolean_type.NullableBooleanType"
    ]
    """<p>Indicates whether the KMS key is a multi-Region (<code>True</code>) or regional (<code>False</code>) key. This value is <code>True</code> for multi-Region primary and replica keys and <code>False</code> for regional KMS keys.</p> <p>For more information about multi-Region keys, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html">Multi-Region keys in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    multi_region_configuration: NotRequired[
        "capo_kms.types.multi_region_configuration.MultiRegionConfiguration"
    ]
    """<p>Lists the primary and replica keys in same multi-Region key. This field is present only when the value of the <code>MultiRegion</code> field is <code>True</code>.</p> <p>For more information about any listed KMS key, use the <a>DescribeKey</a> operation.</p> <ul> <li> <p> <code>MultiRegionKeyType</code> indicates whether the KMS key is a <code>PRIMARY</code> or <code>REPLICA</code> key.</p> </li> <li> <p> <code>PrimaryKey</code> displays the key ARN and Region of the primary key. This field displays the current KMS key if it is the primary key.</p> </li> <li> <p> <code>ReplicaKeys</code> displays the key ARNs and Regions of all replica keys. This field includes the current KMS key if it is a replica key.</p> </li> </ul>"""
    pending_deletion_window_in_days: NotRequired[
        "capo_kms.types.pending_window_in_days_type.PendingWindowInDaysType"
    ]
    """<p>The waiting period before the primary key in a multi-Region key is deleted. This waiting period begins when the last of its replica keys is deleted. This value is present only when the <code>KeyState</code> of the KMS key is <code>PendingReplicaDeletion</code>. That indicates that the KMS key is the primary key in a multi-Region key, it is scheduled for deletion, and it still has existing replica keys.</p> <p>When a single-Region KMS key or a multi-Region replica key is scheduled for deletion, its deletion date is displayed in the <code>DeletionDate</code> field. However, when the primary key in a multi-Region key is scheduled for deletion, its waiting period doesn't begin until all of its replica keys are deleted. This value displays that waiting period. When the last replica key in the multi-Region key is deleted, the <code>KeyState</code> of the scheduled primary key changes from <code>PendingReplicaDeletion</code> to <code>PendingDeletion</code> and the deletion date appears in the <code>DeletionDate</code> field.</p>"""
    mac_algorithms: NotRequired[
        "capo_kms.types.mac_algorithm_spec_list.MacAlgorithmSpecList"
    ]
    """<p>The message authentication code (MAC) algorithm that the HMAC KMS key supports.</p> <p>This value is present only when the <code>KeyUsage</code> of the KMS key is <code>GENERATE_VERIFY_MAC</code>.</p>"""
    xks_key_configuration: NotRequired[
        "capo_kms.types.xks_key_configuration_type.XksKeyConfigurationType"
    ]
    """<p>Information about the external key that is associated with a KMS key in an external key store.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-external-key">External key</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    current_key_material_id: NotRequired[
        "capo_kms.types.backing_key_id_type.BackingKeyIdType"
    ]
    """<p>Identifies the current key material. This value is present for symmetric encryption keys with <code>AWS_KMS</code> or <code>EXTERNAL</code> origin. These KMS keys support automatic or on-demand key rotation and can have multiple key materials associated with them. KMS uses the current key material for both encryption and decryption, and the non-current key material for decryption operations only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyMetadata) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["AWSAccountId"] = value["aws_account_id"]
    out["KeyId"] = value["key_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_date" in value:
        import capo_kms.types.date_type

        out["CreationDate"] = capo_kms.types.date_type.serialize_aws_json_1_1(
            value["creation_date"]
        )
    out["Enabled"] = value.get("enabled", False)
    if "description" in value:
        out["Description"] = value["description"]
    if "key_usage" in value:
        import capo_kms.types.key_usage_type

        out["KeyUsage"] = capo_kms.types.key_usage_type.serialize_aws_json_1_1(
            value["key_usage"]
        )
    if "key_state" in value:
        import capo_kms.types.key_state

        out["KeyState"] = capo_kms.types.key_state.serialize_aws_json_1_1(
            value["key_state"]
        )
    if "deletion_date" in value:
        import capo_kms.types.date_type

        out["DeletionDate"] = capo_kms.types.date_type.serialize_aws_json_1_1(
            value["deletion_date"]
        )
    if "valid_to" in value:
        import capo_kms.types.date_type

        out["ValidTo"] = capo_kms.types.date_type.serialize_aws_json_1_1(
            value["valid_to"]
        )
    if "origin" in value:
        import capo_kms.types.origin_type

        out["Origin"] = capo_kms.types.origin_type.serialize_aws_json_1_1(
            value["origin"]
        )
    if "custom_key_store_id" in value:
        out["CustomKeyStoreId"] = value["custom_key_store_id"]
    if "cloud_hsm_cluster_id" in value:
        out["CloudHsmClusterId"] = value["cloud_hsm_cluster_id"]
    if "expiration_model" in value:
        import capo_kms.types.expiration_model_type

        out["ExpirationModel"] = (
            capo_kms.types.expiration_model_type.serialize_aws_json_1_1(
                value["expiration_model"]
            )
        )
    if "key_manager" in value:
        import capo_kms.types.key_manager_type

        out["KeyManager"] = capo_kms.types.key_manager_type.serialize_aws_json_1_1(
            value["key_manager"]
        )
    if "customer_master_key_spec" in value:
        import capo_kms.types.customer_master_key_spec

        out["CustomerMasterKeySpec"] = (
            capo_kms.types.customer_master_key_spec.serialize_aws_json_1_1(
                value["customer_master_key_spec"]
            )
        )
    if "key_spec" in value:
        import capo_kms.types.key_spec

        out["KeySpec"] = capo_kms.types.key_spec.serialize_aws_json_1_1(
            value["key_spec"]
        )
    if "encryption_algorithms" in value:
        import capo_kms.types.encryption_algorithm_spec_list

        out["EncryptionAlgorithms"] = (
            capo_kms.types.encryption_algorithm_spec_list.serialize_aws_json_1_1(
                value["encryption_algorithms"]
            )
        )
    if "signing_algorithms" in value:
        import capo_kms.types.signing_algorithm_spec_list

        out["SigningAlgorithms"] = (
            capo_kms.types.signing_algorithm_spec_list.serialize_aws_json_1_1(
                value["signing_algorithms"]
            )
        )
    if "key_agreement_algorithms" in value:
        import capo_kms.types.key_agreement_algorithm_spec_list

        out["KeyAgreementAlgorithms"] = (
            capo_kms.types.key_agreement_algorithm_spec_list.serialize_aws_json_1_1(
                value["key_agreement_algorithms"]
            )
        )
    if "multi_region" in value:
        out["MultiRegion"] = value["multi_region"]
    if "multi_region_configuration" in value:
        import capo_kms.types.multi_region_configuration

        out["MultiRegionConfiguration"] = (
            capo_kms.types.multi_region_configuration.serialize_aws_json_1_1(
                value["multi_region_configuration"]
            )
        )
    if "pending_deletion_window_in_days" in value:
        out["PendingDeletionWindowInDays"] = value["pending_deletion_window_in_days"]
    if "mac_algorithms" in value:
        import capo_kms.types.mac_algorithm_spec_list

        out["MacAlgorithms"] = (
            capo_kms.types.mac_algorithm_spec_list.serialize_aws_json_1_1(
                value["mac_algorithms"]
            )
        )
    if "xks_key_configuration" in value:
        import capo_kms.types.xks_key_configuration_type

        out["XksKeyConfiguration"] = (
            capo_kms.types.xks_key_configuration_type.serialize_aws_json_1_1(
                value["xks_key_configuration"]
            )
        )
    if "current_key_material_id" in value:
        out["CurrentKeyMaterialId"] = value["current_key_material_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyMetadata:
    out: KeyMetadata = {}  # type: ignore[typeddict-item]
    if data.get("AWSAccountId") is not None:
        out["aws_account_id"] = data["AWSAccountId"]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("KeyMetadata.key_id required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreationDate") is not None:
        import capo_kms.types.date_type

        out["creation_date"] = capo_kms.types.date_type.deserialize_aws_json_1_1(
            data["CreationDate"]
        )
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("KeyUsage") is not None:
        import capo_kms.types.key_usage_type

        out["key_usage"] = capo_kms.types.key_usage_type.deserialize_aws_json_1_1(
            data["KeyUsage"]
        )
    if data.get("KeyState") is not None:
        import capo_kms.types.key_state

        out["key_state"] = capo_kms.types.key_state.deserialize_aws_json_1_1(
            data["KeyState"]
        )
    if data.get("DeletionDate") is not None:
        import capo_kms.types.date_type

        out["deletion_date"] = capo_kms.types.date_type.deserialize_aws_json_1_1(
            data["DeletionDate"]
        )
    if data.get("ValidTo") is not None:
        import capo_kms.types.date_type

        out["valid_to"] = capo_kms.types.date_type.deserialize_aws_json_1_1(
            data["ValidTo"]
        )
    if data.get("Origin") is not None:
        import capo_kms.types.origin_type

        out["origin"] = capo_kms.types.origin_type.deserialize_aws_json_1_1(
            data["Origin"]
        )
    if data.get("CustomKeyStoreId") is not None:
        out["custom_key_store_id"] = data["CustomKeyStoreId"]
    if data.get("CloudHsmClusterId") is not None:
        out["cloud_hsm_cluster_id"] = data["CloudHsmClusterId"]
    if data.get("ExpirationModel") is not None:
        import capo_kms.types.expiration_model_type

        out["expiration_model"] = (
            capo_kms.types.expiration_model_type.deserialize_aws_json_1_1(
                data["ExpirationModel"]
            )
        )
    if data.get("KeyManager") is not None:
        import capo_kms.types.key_manager_type

        out["key_manager"] = capo_kms.types.key_manager_type.deserialize_aws_json_1_1(
            data["KeyManager"]
        )
    if data.get("CustomerMasterKeySpec") is not None:
        import capo_kms.types.customer_master_key_spec

        out["customer_master_key_spec"] = (
            capo_kms.types.customer_master_key_spec.deserialize_aws_json_1_1(
                data["CustomerMasterKeySpec"]
            )
        )
    if data.get("KeySpec") is not None:
        import capo_kms.types.key_spec

        out["key_spec"] = capo_kms.types.key_spec.deserialize_aws_json_1_1(
            data["KeySpec"]
        )
    if data.get("EncryptionAlgorithms") is not None:
        import capo_kms.types.encryption_algorithm_spec_list

        out["encryption_algorithms"] = (
            capo_kms.types.encryption_algorithm_spec_list.deserialize_aws_json_1_1(
                data["EncryptionAlgorithms"]
            )
        )
    if data.get("SigningAlgorithms") is not None:
        import capo_kms.types.signing_algorithm_spec_list

        out["signing_algorithms"] = (
            capo_kms.types.signing_algorithm_spec_list.deserialize_aws_json_1_1(
                data["SigningAlgorithms"]
            )
        )
    if data.get("KeyAgreementAlgorithms") is not None:
        import capo_kms.types.key_agreement_algorithm_spec_list

        out["key_agreement_algorithms"] = (
            capo_kms.types.key_agreement_algorithm_spec_list.deserialize_aws_json_1_1(
                data["KeyAgreementAlgorithms"]
            )
        )
    if data.get("MultiRegion") is not None:
        out["multi_region"] = data["MultiRegion"]
    if data.get("MultiRegionConfiguration") is not None:
        import capo_kms.types.multi_region_configuration

        out["multi_region_configuration"] = (
            capo_kms.types.multi_region_configuration.deserialize_aws_json_1_1(
                data["MultiRegionConfiguration"]
            )
        )
    if data.get("PendingDeletionWindowInDays") is not None:
        out["pending_deletion_window_in_days"] = data["PendingDeletionWindowInDays"]
    if data.get("MacAlgorithms") is not None:
        import capo_kms.types.mac_algorithm_spec_list

        out["mac_algorithms"] = (
            capo_kms.types.mac_algorithm_spec_list.deserialize_aws_json_1_1(
                data["MacAlgorithms"]
            )
        )
    if data.get("XksKeyConfiguration") is not None:
        import capo_kms.types.xks_key_configuration_type

        out["xks_key_configuration"] = (
            capo_kms.types.xks_key_configuration_type.deserialize_aws_json_1_1(
                data["XksKeyConfiguration"]
            )
        )
    if data.get("CurrentKeyMaterialId") is not None:
        out["current_key_material_id"] = data["CurrentKeyMaterialId"]
    return out
