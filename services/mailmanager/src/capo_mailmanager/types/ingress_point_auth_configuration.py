"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointAuthConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_point_password_configuration
    import capo_mailmanager.types.secret_arn
    import capo_mailmanager.types.tls_auth_configuration


class IngressPointAuthConfiguration(TypedDict, closed=True):
    ingress_point_password_configuration: NotRequired[
        "capo_mailmanager.types.ingress_point_password_configuration.IngressPointPasswordConfiguration"
    ]
    """<p>The ingress endpoint password configuration for the ingress endpoint resource.</p>"""
    secret_arn: NotRequired["capo_mailmanager.types.secret_arn.SecretArn"]
    """<p>The ingress endpoint SecretsManager::Secret ARN configuration for the ingress endpoint resource.</p>"""
    tls_auth_configuration: NotRequired[
        "capo_mailmanager.types.tls_auth_configuration.TlsAuthConfiguration"
    ]
    """<p>The mutual TLS authentication configuration for the ingress endpoint resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointAuthConfiguration) -> dict:
    out: dict = {}
    if "ingress_point_password_configuration" in value:
        import capo_mailmanager.types.ingress_point_password_configuration

        out["IngressPointPasswordConfiguration"] = (
            capo_mailmanager.types.ingress_point_password_configuration.serialize_aws_json_1_0(
                value["ingress_point_password_configuration"]
            )
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "tls_auth_configuration" in value:
        import capo_mailmanager.types.tls_auth_configuration

        out["TlsAuthConfiguration"] = (
            capo_mailmanager.types.tls_auth_configuration.serialize_aws_json_1_0(
                value["tls_auth_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressPointAuthConfiguration:
    out: IngressPointAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("IngressPointPasswordConfiguration") is not None:
        import capo_mailmanager.types.ingress_point_password_configuration

        out["ingress_point_password_configuration"] = (
            capo_mailmanager.types.ingress_point_password_configuration.deserialize_aws_json_1_0(
                data["IngressPointPasswordConfiguration"]
            )
        )
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    if data.get("TlsAuthConfiguration") is not None:
        import capo_mailmanager.types.tls_auth_configuration

        out["tls_auth_configuration"] = (
            capo_mailmanager.types.tls_auth_configuration.deserialize_aws_json_1_0(
                data["TlsAuthConfiguration"]
            )
        )
    return out


def redact_sensitive(value: IngressPointAuthConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tls_auth_configuration" in value:
        import capo_mailmanager.types.tls_auth_configuration

        out["tls_auth_configuration"] = (
            capo_mailmanager.types.tls_auth_configuration.redact_sensitive(
                value["tls_auth_configuration"]
            )
        )
    return out
