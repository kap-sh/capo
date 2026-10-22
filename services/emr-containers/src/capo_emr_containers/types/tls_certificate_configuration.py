"""Generated from Smithy shape ``com.amazonaws.emrcontainers#TLSCertificateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.certificate_provider_type
    import capo_emr_containers.types.secrets_manager_arn


class TLSCertificateConfiguration(TypedDict, closed=True):
    certificate_provider_type: NotRequired[
        "capo_emr_containers.types.certificate_provider_type.CertificateProviderType"
    ]
    """<p>The TLS certificate type. Acceptable values: <code>PEM</code> or <code>Custom</code>.</p>"""
    public_certificate_secret_arn: NotRequired[
        "capo_emr_containers.types.secrets_manager_arn.SecretsManagerArn"
    ]
    """<p> Secrets Manager ARN that contains the public TLS certificate contents, used for communication between the user job and the system job.</p>"""
    private_certificate_secret_arn: NotRequired[
        "capo_emr_containers.types.secrets_manager_arn.SecretsManagerArn"
    ]
    """<p> Secrets Manager ARN that contains the private TLS certificate contents, used for communication between the user job and the system job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TLSCertificateConfiguration) -> dict:
    out: dict = {}
    if "certificate_provider_type" in value:
        import capo_emr_containers.types.certificate_provider_type

        out["certificateProviderType"] = (
            capo_emr_containers.types.certificate_provider_type.serialize_json(
                value["certificate_provider_type"]
            )
        )
    if "public_certificate_secret_arn" in value:
        out["publicCertificateSecretArn"] = value["public_certificate_secret_arn"]
    if "private_certificate_secret_arn" in value:
        out["privateCertificateSecretArn"] = value["private_certificate_secret_arn"]
    return out


def deserialize_json(data: dict) -> TLSCertificateConfiguration:
    out: TLSCertificateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("certificateProviderType") is not None:
        import capo_emr_containers.types.certificate_provider_type

        out["certificate_provider_type"] = (
            capo_emr_containers.types.certificate_provider_type.deserialize_json(
                data["certificateProviderType"]
            )
        )
    if data.get("publicCertificateSecretArn") is not None:
        out["public_certificate_secret_arn"] = data["publicCertificateSecretArn"]
    if data.get("privateCertificateSecretArn") is not None:
        out["private_certificate_secret_arn"] = data["privateCertificateSecretArn"]
    return out
