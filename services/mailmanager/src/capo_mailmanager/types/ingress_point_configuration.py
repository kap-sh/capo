"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.secret_arn
    import capo_mailmanager.types.smtp_password
    import capo_mailmanager.types.tls_auth_configuration


class _IngressPointConfiguration_SmtpPassword(TypedDict, closed=True):
    SmtpPassword: "capo_mailmanager.types.smtp_password.SmtpPassword"


class _IngressPointConfiguration_SecretArn(TypedDict, closed=True):
    SecretArn: "capo_mailmanager.types.secret_arn.SecretArn"


class _IngressPointConfiguration_TlsAuthConfiguration(TypedDict, closed=True):
    TlsAuthConfiguration: (
        "capo_mailmanager.types.tls_auth_configuration.TlsAuthConfiguration"
    )


IngressPointConfiguration: TypeAlias = (
    _IngressPointConfiguration_SmtpPassword
    | _IngressPointConfiguration_SecretArn
    | _IngressPointConfiguration_TlsAuthConfiguration
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointConfiguration) -> dict:
    if "SmtpPassword" in value:
        return {"SmtpPassword": value["SmtpPassword"]}
    elif "SecretArn" in value:
        return {"SecretArn": value["SecretArn"]}
    elif "TlsAuthConfiguration" in value:
        import capo_mailmanager.types.tls_auth_configuration

        return {
            "TlsAuthConfiguration": capo_mailmanager.types.tls_auth_configuration.serialize_aws_json_1_0(
                value["TlsAuthConfiguration"]
            )
        }
    else:
        raise SerializationError("IngressPointConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> IngressPointConfiguration:
    if data.get("SmtpPassword") is not None:
        return {"SmtpPassword": data["SmtpPassword"]}
    elif data.get("SecretArn") is not None:
        return {"SecretArn": data["SecretArn"]}
    elif data.get("TlsAuthConfiguration") is not None:
        import capo_mailmanager.types.tls_auth_configuration

        return {
            "TlsAuthConfiguration": capo_mailmanager.types.tls_auth_configuration.deserialize_aws_json_1_0(
                data["TlsAuthConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "IngressPointConfiguration: no recognized variant key"
        )


def redact_sensitive(value: IngressPointConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "SmtpPassword" in value:
        out["SmtpPassword"] = "*** Sensitive Data Redacted ***"
    if "TlsAuthConfiguration" in value:
        import capo_mailmanager.types.tls_auth_configuration

        out["TlsAuthConfiguration"] = (
            capo_mailmanager.types.tls_auth_configuration.redact_sensitive(
                value["TlsAuthConfiguration"]
            )
        )
    return out
