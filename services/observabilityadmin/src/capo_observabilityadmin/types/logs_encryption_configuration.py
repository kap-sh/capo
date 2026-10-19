"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LogsEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.encryption_conflict_resolution_strategy
    import capo_observabilityadmin.types.encryption_scope
    import capo_observabilityadmin.types.encryption_strategy
    import capo_observabilityadmin.types.resource_arn


class LogsEncryptionConfiguration(TypedDict, closed=True):
    encryption_strategy: (
        "capo_observabilityadmin.types.encryption_strategy.EncryptionStrategy"
    )
    """<p>Configuration that determines the encryption strategy of the destination log groups. CUSTOMER_MANAGED uses the configured KmsKeyArn to encrypt newly created destination log groups.</p>"""
    kms_key_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>KMS Key ARN belonging to the primary destination account and region, to encrypt newly created central log groups in the primary destination.</p>"""
    encryption_conflict_resolution_strategy: NotRequired[
        "capo_observabilityadmin.types.encryption_conflict_resolution_strategy.EncryptionConflictResolutionStrategy"
    ]
    """<p>Conflict resolution strategy for centralization if the encryption strategy is set to CUSTOMER_MANAGED and the destination log group is encrypted with an AWS_OWNED KMS Key. ALLOW lets centralization go through while SKIP prevents centralization into the destination log group.</p>"""
    encryption_scope: NotRequired[
        "capo_observabilityadmin.types.encryption_scope.EncryptionScope"
    ]
    """<p>Determines which newly created destination log groups are encrypted with the configured <code>KmsKeyArn</code> when <code>EncryptionStrategy</code> is <code>CUSTOMER_MANAGED</code>.</p> <p>If you set this to <code>ENCRYPTED_SOURCE_ONLY</code> (the default), only destination log groups whose source log group is encrypted with a customer managed KMS key use the configured <code>KmsKeyArn</code>. Destination log groups derived from Amazon Web Services owned encrypted source log groups remain Amazon Web Services owned encrypted.</p> <p>If you set this to <code>NEW_DESTINATION_LOG_GROUPS</code>, every new destination log group created by this rule uses the configured <code>KmsKeyArn</code>, regardless of the source log group's encryption posture.</p> <p>This field is not valid when <code>EncryptionStrategy</code> is <code>AWS_OWNED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogsEncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.encryption_strategy

    out["EncryptionStrategy"] = (
        capo_observabilityadmin.types.encryption_strategy.serialize_json(
            value["encryption_strategy"]
        )
    )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "encryption_conflict_resolution_strategy" in value:
        import capo_observabilityadmin.types.encryption_conflict_resolution_strategy

        out["EncryptionConflictResolutionStrategy"] = (
            capo_observabilityadmin.types.encryption_conflict_resolution_strategy.serialize_json(
                value["encryption_conflict_resolution_strategy"]
            )
        )
    if "encryption_scope" in value:
        import capo_observabilityadmin.types.encryption_scope

        out["EncryptionScope"] = (
            capo_observabilityadmin.types.encryption_scope.serialize_json(
                value["encryption_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogsEncryptionConfiguration:
    out: LogsEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EncryptionStrategy") is not None:
        import capo_observabilityadmin.types.encryption_strategy

        out["encryption_strategy"] = (
            capo_observabilityadmin.types.encryption_strategy.deserialize_json(
                data["EncryptionStrategy"]
            )
        )
    else:
        import typing

        out["encryption_strategy"] = typing.cast(
            "capo_observabilityadmin.types.encryption_strategy.EncryptionStrategy", ""
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("EncryptionConflictResolutionStrategy") is not None:
        import capo_observabilityadmin.types.encryption_conflict_resolution_strategy

        out["encryption_conflict_resolution_strategy"] = (
            capo_observabilityadmin.types.encryption_conflict_resolution_strategy.deserialize_json(
                data["EncryptionConflictResolutionStrategy"]
            )
        )
    if data.get("EncryptionScope") is not None:
        import capo_observabilityadmin.types.encryption_scope

        out["encryption_scope"] = (
            capo_observabilityadmin.types.encryption_scope.deserialize_json(
                data["EncryptionScope"]
            )
        )
    return out
