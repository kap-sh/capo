"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthority``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.account_id
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.certificate_authority_configuration
    import capo_acm_pca.types.certificate_authority_status
    import capo_acm_pca.types.certificate_authority_type
    import capo_acm_pca.types.certificate_authority_usage_mode
    import capo_acm_pca.types.failure_reason
    import capo_acm_pca.types.key_storage_security_standard
    import capo_acm_pca.types.revocation_configuration
    import capo_acm_pca.types.string
    import capo_acm_pca.types.t_stamp


class CertificateAuthority(TypedDict, closed=True):
    arn: NotRequired["capo_acm_pca.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) for your private certificate authority (CA). The format is <code> <i>12345678-1234-1234-1234-123456789012</i> </code>.</p>"""
    owner_account: NotRequired["capo_acm_pca.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the certificate authority.</p>"""
    created_at: NotRequired["capo_acm_pca.types.t_stamp.TStamp"]
    """<p>Date and time at which your private CA was created.</p>"""
    last_state_change_at: NotRequired["capo_acm_pca.types.t_stamp.TStamp"]
    """<p>Date and time at which your private CA was last updated.</p>"""
    type: NotRequired[
        "capo_acm_pca.types.certificate_authority_type.CertificateAuthorityType"
    ]
    """<p>Type of your private CA.</p>"""
    serial: NotRequired["capo_acm_pca.types.string.String"]
    """<p>Serial number of your private CA.</p>"""
    status: NotRequired[
        "capo_acm_pca.types.certificate_authority_status.CertificateAuthorityStatus"
    ]
    """<p>Status of your private CA.</p>"""
    not_before: NotRequired["capo_acm_pca.types.t_stamp.TStamp"]
    """<p>Date and time before which your private CA certificate is not valid.</p>"""
    not_after: NotRequired["capo_acm_pca.types.t_stamp.TStamp"]
    """<p>Date and time after which your private CA certificate is not valid.</p>"""
    failure_reason: NotRequired["capo_acm_pca.types.failure_reason.FailureReason"]
    """<p>Reason the request to create your private CA failed.</p>"""
    certificate_authority_configuration: NotRequired[
        "capo_acm_pca.types.certificate_authority_configuration.CertificateAuthorityConfiguration"
    ]
    """<p>Your private CA configuration.</p>"""
    revocation_configuration: NotRequired[
        "capo_acm_pca.types.revocation_configuration.RevocationConfiguration"
    ]
    """<p>Information about the Online Certificate Status Protocol (OCSP) configuration or certificate revocation list (CRL) created and maintained by your private CA. </p>"""
    restorable_until: NotRequired["capo_acm_pca.types.t_stamp.TStamp"]
    """<p>The period during which a deleted CA can be restored. For more information, see the <code>PermanentDeletionTimeInDays</code> parameter of the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthorityRequest.html">DeleteCertificateAuthorityRequest</a> action. </p>"""
    key_storage_security_standard: NotRequired[
        "capo_acm_pca.types.key_storage_security_standard.KeyStorageSecurityStandard"
    ]
    """<p>Defines a cryptographic key management compliance standard for handling and protecting CA keys.</p> <p>Default: FIPS_140_2_LEVEL_3_OR_HIGHER</p> <note> <p>Starting January 26, 2023, Amazon Web Services Private CA protects all CA private keys in non-China regions using hardware security modules (HSMs) that comply with FIPS PUB 140-2 Level 3.</p> <p>For information about security standard support in different Amazon Web Services Regions, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html#private-keys">Storage and security compliance of Amazon Web Services Private CA private keys</a>.</p> </note>"""
    usage_mode: NotRequired[
        "capo_acm_pca.types.certificate_authority_usage_mode.CertificateAuthorityUsageMode"
    ]
    """<p>Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days.</p> <p>The default value is GENERAL_PURPOSE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthority) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    if "created_at" in value:
        import capo_acm_pca.types.t_stamp

        out["CreatedAt"] = capo_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "last_state_change_at" in value:
        import capo_acm_pca.types.t_stamp

        out["LastStateChangeAt"] = capo_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["last_state_change_at"]
        )
    if "type" in value:
        import capo_acm_pca.types.certificate_authority_type

        out["Type"] = (
            capo_acm_pca.types.certificate_authority_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "serial" in value:
        out["Serial"] = value["serial"]
    if "status" in value:
        import capo_acm_pca.types.certificate_authority_status

        out["Status"] = (
            capo_acm_pca.types.certificate_authority_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "not_before" in value:
        import capo_acm_pca.types.t_stamp

        out["NotBefore"] = capo_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["not_before"]
        )
    if "not_after" in value:
        import capo_acm_pca.types.t_stamp

        out["NotAfter"] = capo_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["not_after"]
        )
    if "failure_reason" in value:
        import capo_acm_pca.types.failure_reason

        out["FailureReason"] = capo_acm_pca.types.failure_reason.serialize_aws_json_1_1(
            value["failure_reason"]
        )
    if "certificate_authority_configuration" in value:
        import capo_acm_pca.types.certificate_authority_configuration

        out["CertificateAuthorityConfiguration"] = (
            capo_acm_pca.types.certificate_authority_configuration.serialize_aws_json_1_1(
                value["certificate_authority_configuration"]
            )
        )
    if "revocation_configuration" in value:
        import capo_acm_pca.types.revocation_configuration

        out["RevocationConfiguration"] = (
            capo_acm_pca.types.revocation_configuration.serialize_aws_json_1_1(
                value["revocation_configuration"]
            )
        )
    if "restorable_until" in value:
        import capo_acm_pca.types.t_stamp

        out["RestorableUntil"] = capo_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["restorable_until"]
        )
    if "key_storage_security_standard" in value:
        import capo_acm_pca.types.key_storage_security_standard

        out["KeyStorageSecurityStandard"] = (
            capo_acm_pca.types.key_storage_security_standard.serialize_aws_json_1_1(
                value["key_storage_security_standard"]
            )
        )
    if "usage_mode" in value:
        import capo_acm_pca.types.certificate_authority_usage_mode

        out["UsageMode"] = (
            capo_acm_pca.types.certificate_authority_usage_mode.serialize_aws_json_1_1(
                value["usage_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateAuthority:
    out: CertificateAuthority = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("OwnerAccount") is not None:
        out["owner_account"] = data["OwnerAccount"]
    if data.get("CreatedAt") is not None:
        import capo_acm_pca.types.t_stamp

        out["created_at"] = capo_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("LastStateChangeAt") is not None:
        import capo_acm_pca.types.t_stamp

        out["last_state_change_at"] = (
            capo_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
                data["LastStateChangeAt"]
            )
        )
    if data.get("Type") is not None:
        import capo_acm_pca.types.certificate_authority_type

        out["type"] = (
            capo_acm_pca.types.certificate_authority_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Serial") is not None:
        out["serial"] = data["Serial"]
    if data.get("Status") is not None:
        import capo_acm_pca.types.certificate_authority_status

        out["status"] = (
            capo_acm_pca.types.certificate_authority_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("NotBefore") is not None:
        import capo_acm_pca.types.t_stamp

        out["not_before"] = capo_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["NotBefore"]
        )
    if data.get("NotAfter") is not None:
        import capo_acm_pca.types.t_stamp

        out["not_after"] = capo_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["NotAfter"]
        )
    if data.get("FailureReason") is not None:
        import capo_acm_pca.types.failure_reason

        out["failure_reason"] = (
            capo_acm_pca.types.failure_reason.deserialize_aws_json_1_1(
                data["FailureReason"]
            )
        )
    if data.get("CertificateAuthorityConfiguration") is not None:
        import capo_acm_pca.types.certificate_authority_configuration

        out["certificate_authority_configuration"] = (
            capo_acm_pca.types.certificate_authority_configuration.deserialize_aws_json_1_1(
                data["CertificateAuthorityConfiguration"]
            )
        )
    if data.get("RevocationConfiguration") is not None:
        import capo_acm_pca.types.revocation_configuration

        out["revocation_configuration"] = (
            capo_acm_pca.types.revocation_configuration.deserialize_aws_json_1_1(
                data["RevocationConfiguration"]
            )
        )
    if data.get("RestorableUntil") is not None:
        import capo_acm_pca.types.t_stamp

        out["restorable_until"] = capo_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["RestorableUntil"]
        )
    if data.get("KeyStorageSecurityStandard") is not None:
        import capo_acm_pca.types.key_storage_security_standard

        out["key_storage_security_standard"] = (
            capo_acm_pca.types.key_storage_security_standard.deserialize_aws_json_1_1(
                data["KeyStorageSecurityStandard"]
            )
        )
    if data.get("UsageMode") is not None:
        import capo_acm_pca.types.certificate_authority_usage_mode

        out["usage_mode"] = (
            capo_acm_pca.types.certificate_authority_usage_mode.deserialize_aws_json_1_1(
                data["UsageMode"]
            )
        )
    return out
