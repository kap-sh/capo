"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#Key``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.derive_key_usage
    import capo_payment_cryptography.types.key_arn
    import capo_payment_cryptography.types.key_attributes
    import capo_payment_cryptography.types.key_check_value
    import capo_payment_cryptography.types.key_check_value_algorithm
    import capo_payment_cryptography.types.key_origin
    import capo_payment_cryptography.types.key_state
    import capo_payment_cryptography.types.mpa_status
    import capo_payment_cryptography.types.multi_region_key_type
    import capo_payment_cryptography.types.region
    import capo_payment_cryptography.types.replication_status
    import capo_payment_cryptography.types.timestamp


class Key(TypedDict, closed=True):
    key_arn: "capo_payment_cryptography.types.key_arn.KeyArn"
    """<p>The Amazon Resource Name (ARN) of the key.</p>"""
    key_attributes: "capo_payment_cryptography.types.key_attributes.KeyAttributes"
    """<p>The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.</p>"""
    key_check_value: "capo_payment_cryptography.types.key_check_value.KeyCheckValue"
    """<p>The key check value (KCV) is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p>"""
    key_check_value_algorithm: "capo_payment_cryptography.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
    """<p>The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.</p> <p>For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.</p>"""
    enabled: "bool"
    """<p>Specifies whether the key is enabled. </p>"""
    exportable: "bool"
    """<p>Specifies whether the key is exportable. This data is immutable after the key is created.</p>"""
    key_state: "capo_payment_cryptography.types.key_state.KeyState"
    """<p>The state of key that is being created or deleted.</p>"""
    key_origin: "capo_payment_cryptography.types.key_origin.KeyOrigin"
    """<p>The source of the key material. For keys created within Amazon Web Services Payment Cryptography, the value is <code>AWS_PAYMENT_CRYPTOGRAPHY</code>. For keys imported into Amazon Web Services Payment Cryptography, the value is <code>EXTERNAL</code>.</p>"""
    create_timestamp: "capo_payment_cryptography.types.timestamp.Timestamp"
    """<p>The date and time when the key was created.</p>"""
    usage_start_timestamp: NotRequired[
        "capo_payment_cryptography.types.timestamp.Timestamp"
    ]
    """<p>The date and time after which Amazon Web Services Payment Cryptography will start using the key material for cryptographic operations.</p>"""
    usage_stop_timestamp: NotRequired[
        "capo_payment_cryptography.types.timestamp.Timestamp"
    ]
    """<p>The date and time after which Amazon Web Services Payment Cryptography will stop using the key material for cryptographic operations.</p>"""
    delete_pending_timestamp: NotRequired[
        "capo_payment_cryptography.types.timestamp.Timestamp"
    ]
    """<p>The date and time after which Amazon Web Services Payment Cryptography will delete the key. This value is present only when <code>KeyState</code> is <code>DELETE_PENDING</code> and the key is scheduled for deletion.</p>"""
    delete_timestamp: NotRequired["capo_payment_cryptography.types.timestamp.Timestamp"]
    """<p>The date and time after which Amazon Web Services Payment Cryptography will delete the key. This value is present only when when the <code>KeyState</code> is <code>DELETE_COMPLETE</code> and the Amazon Web Services Payment Cryptography key is deleted.</p>"""
    derive_key_usage: NotRequired[
        "capo_payment_cryptography.types.derive_key_usage.DeriveKeyUsage"
    ]
    """<p>The cryptographic usage of an ECDH derived key as deﬁned in section A.5.2 of the TR-31 spec.</p>"""
    multi_region_key_type: NotRequired[
        "capo_payment_cryptography.types.multi_region_key_type.MultiRegionKeyType"
    ]
    """<p>Indicates whether this key is a Multi-Region key and its role in the Multi-Region key hierarchy.</p> <p>Multi-Region replication keys allow the same key material to be used across multiple Amazon Web Services Regions. This field specifies whether the key is a Primary Region key (PRK) (which can be replicated to other Amazon Web Services Regions) or a Replica Region key (RRK) (which is a copy of a PRK in another Region). For more information, see <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html">Multi-Region key replication</a>.</p>"""
    primary_region: NotRequired["capo_payment_cryptography.types.region.Region"]
    replication_status: NotRequired[
        "capo_payment_cryptography.types.replication_status.ReplicationStatus"
    ]
    """<p>Information about the replication status of the key across different Amazon Web Services Regions.</p> <p>This field provides details about the current state of key replication, including any status messages or operational information. It helps track the progress and health of key replication operations.</p>"""
    using_default_replication_regions: NotRequired["bool"]
    """<p>Indicates whether this key is using the account's default replication regions configuration for <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html">Multi-Region key replication</a>.</p> <p>When set to <code>true</code>, the key automatically replicates to the regions specified in the account's default replication settings. When set to <code>false</code>, the key has a custom replication configuration that overrides the account defaults.</p>"""
    mpa_status: NotRequired["capo_payment_cryptography.types.mpa_status.MpaStatus"]
    """<p>The Multi-Party Approval (MPA) status for the key, if applicable.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Key) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    import capo_payment_cryptography.types.key_attributes

    out["KeyAttributes"] = (
        capo_payment_cryptography.types.key_attributes.serialize_aws_json_1_0(
            value["key_attributes"]
        )
    )
    out["KeyCheckValue"] = value["key_check_value"]
    out["KeyCheckValueAlgorithm"] = value["key_check_value_algorithm"]
    out["Enabled"] = value["enabled"]
    out["Exportable"] = value["exportable"]
    out["KeyState"] = value["key_state"]
    out["KeyOrigin"] = value["key_origin"]
    import capo_payment_cryptography.types.timestamp

    out["CreateTimestamp"] = (
        capo_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
            value["create_timestamp"]
        )
    )
    if "usage_start_timestamp" in value:
        import capo_payment_cryptography.types.timestamp

        out["UsageStartTimestamp"] = (
            capo_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
                value["usage_start_timestamp"]
            )
        )
    if "usage_stop_timestamp" in value:
        import capo_payment_cryptography.types.timestamp

        out["UsageStopTimestamp"] = (
            capo_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
                value["usage_stop_timestamp"]
            )
        )
    if "delete_pending_timestamp" in value:
        import capo_payment_cryptography.types.timestamp

        out["DeletePendingTimestamp"] = (
            capo_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
                value["delete_pending_timestamp"]
            )
        )
    if "delete_timestamp" in value:
        import capo_payment_cryptography.types.timestamp

        out["DeleteTimestamp"] = (
            capo_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
                value["delete_timestamp"]
            )
        )
    if "derive_key_usage" in value:
        out["DeriveKeyUsage"] = value["derive_key_usage"]
    if "multi_region_key_type" in value:
        out["MultiRegionKeyType"] = value["multi_region_key_type"]
    if "primary_region" in value:
        out["PrimaryRegion"] = value["primary_region"]
    if "replication_status" in value:
        import capo_payment_cryptography.types.replication_status

        out["ReplicationStatus"] = (
            capo_payment_cryptography.types.replication_status.serialize_aws_json_1_0(
                value["replication_status"]
            )
        )
    if "using_default_replication_regions" in value:
        out["UsingDefaultReplicationRegions"] = value[
            "using_default_replication_regions"
        ]
    if "mpa_status" in value:
        import capo_payment_cryptography.types.mpa_status

        out["MpaStatus"] = (
            capo_payment_cryptography.types.mpa_status.serialize_aws_json_1_0(
                value["mpa_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Key:
    out: Key = {}  # type: ignore[typeddict-item]
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        raise DeserializationError("Key.key_arn required")
    if data.get("KeyAttributes") is not None:
        import capo_payment_cryptography.types.key_attributes

        out["key_attributes"] = (
            capo_payment_cryptography.types.key_attributes.deserialize_aws_json_1_0(
                data["KeyAttributes"]
            )
        )
    else:
        raise DeserializationError("Key.key_attributes required")
    if data.get("KeyCheckValue") is not None:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        raise DeserializationError("Key.key_check_value required")
    if data.get("KeyCheckValueAlgorithm") is not None:
        out["key_check_value_algorithm"] = data["KeyCheckValueAlgorithm"]
    else:
        raise DeserializationError("Key.key_check_value_algorithm required")
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("Key.enabled required")
    if data.get("Exportable") is not None:
        out["exportable"] = data["Exportable"]
    else:
        raise DeserializationError("Key.exportable required")
    if data.get("KeyState") is not None:
        out["key_state"] = data["KeyState"]
    else:
        raise DeserializationError("Key.key_state required")
    if data.get("KeyOrigin") is not None:
        out["key_origin"] = data["KeyOrigin"]
    else:
        raise DeserializationError("Key.key_origin required")
    if data.get("CreateTimestamp") is not None:
        import capo_payment_cryptography.types.timestamp

        out["create_timestamp"] = (
            capo_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["CreateTimestamp"]
            )
        )
    else:
        raise DeserializationError("Key.create_timestamp required")
    if data.get("UsageStartTimestamp") is not None:
        import capo_payment_cryptography.types.timestamp

        out["usage_start_timestamp"] = (
            capo_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["UsageStartTimestamp"]
            )
        )
    if data.get("UsageStopTimestamp") is not None:
        import capo_payment_cryptography.types.timestamp

        out["usage_stop_timestamp"] = (
            capo_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["UsageStopTimestamp"]
            )
        )
    if data.get("DeletePendingTimestamp") is not None:
        import capo_payment_cryptography.types.timestamp

        out["delete_pending_timestamp"] = (
            capo_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["DeletePendingTimestamp"]
            )
        )
    if data.get("DeleteTimestamp") is not None:
        import capo_payment_cryptography.types.timestamp

        out["delete_timestamp"] = (
            capo_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["DeleteTimestamp"]
            )
        )
    if data.get("DeriveKeyUsage") is not None:
        out["derive_key_usage"] = data["DeriveKeyUsage"]
    if data.get("MultiRegionKeyType") is not None:
        out["multi_region_key_type"] = data["MultiRegionKeyType"]
    if data.get("PrimaryRegion") is not None:
        out["primary_region"] = data["PrimaryRegion"]
    if data.get("ReplicationStatus") is not None:
        import capo_payment_cryptography.types.replication_status

        out["replication_status"] = (
            capo_payment_cryptography.types.replication_status.deserialize_aws_json_1_0(
                data["ReplicationStatus"]
            )
        )
    if data.get("UsingDefaultReplicationRegions") is not None:
        out["using_default_replication_regions"] = data[
            "UsingDefaultReplicationRegions"
        ]
    if data.get("MpaStatus") is not None:
        import capo_payment_cryptography.types.mpa_status

        out["mpa_status"] = (
            capo_payment_cryptography.types.mpa_status.deserialize_aws_json_1_0(
                data["MpaStatus"]
            )
        )
    return out
