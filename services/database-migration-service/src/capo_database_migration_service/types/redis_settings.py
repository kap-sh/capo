"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RedisSettings``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer
    import capo_database_migration_service.types.redis_auth_type_value
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.ssl_security_protocol_value
    import capo_database_migration_service.types.string


class RedisSettings(TypedDict, closed=True):
    server_name: "capo_database_migration_service.types.string.String"
    """<p>Fully qualified domain name of the endpoint.</p>"""
    port: "capo_database_migration_service.types.integer.Integer"
    """<p>Transmission Control Protocol (TCP) port for the endpoint.</p>"""
    ssl_security_protocol: NotRequired[
        "capo_database_migration_service.types.ssl_security_protocol_value.SslSecurityProtocolValue"
    ]
    """<p>The connection to a Redis target endpoint using Transport Layer Security (TLS). Valid values include <code>plaintext</code> and <code>ssl-encryption</code>. The default is <code>ssl-encryption</code>. The <code>ssl-encryption</code> option makes an encrypted connection. Optionally, you can identify an Amazon Resource Name (ARN) for an SSL certificate authority (CA) using the <code>SslCaCertificateArn </code>setting. If an ARN isn't given for a CA, DMS uses the Amazon root CA.</p> <p>The <code>plaintext</code> option doesn't provide Transport Layer Security (TLS) encryption for traffic between endpoint and database.</p>"""
    auth_type: NotRequired[
        "capo_database_migration_service.types.redis_auth_type_value.RedisAuthTypeValue"
    ]
    """<p>The type of authentication to perform when connecting to a Redis target. Options include <code>none</code>, <code>auth-token</code>, and <code>auth-role</code>. The <code>auth-token</code> option requires an <code>AuthPassword</code> value to be provided. The <code>auth-role</code> option requires <code>AuthUserName</code> and <code>AuthPassword</code> values to be provided.</p>"""
    auth_user_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The user name provided with the <code>auth-role</code> option of the <code>AuthType</code> setting for a Redis target endpoint.</p>"""
    auth_password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>The password provided with the <code>auth-role</code> and <code>auth-token</code> options of the <code>AuthType</code> setting for a Redis target endpoint.</p>"""
    ssl_ca_certificate_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) for the certificate authority (CA) that DMS uses to connect to your Redis target endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedisSettings) -> dict:
    out: dict = {}
    out["ServerName"] = value["server_name"]
    out["Port"] = value.get("port", 0)
    if "ssl_security_protocol" in value:
        import capo_database_migration_service.types.ssl_security_protocol_value

        out["SslSecurityProtocol"] = (
            capo_database_migration_service.types.ssl_security_protocol_value.serialize_aws_json_1_1(
                value["ssl_security_protocol"]
            )
        )
    if "auth_type" in value:
        import capo_database_migration_service.types.redis_auth_type_value

        out["AuthType"] = (
            capo_database_migration_service.types.redis_auth_type_value.serialize_aws_json_1_1(
                value["auth_type"]
            )
        )
    if "auth_user_name" in value:
        out["AuthUserName"] = value["auth_user_name"]
    if "auth_password" in value:
        out["AuthPassword"] = value["auth_password"]
    if "ssl_ca_certificate_arn" in value:
        out["SslCaCertificateArn"] = value["ssl_ca_certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedisSettings:
    out: RedisSettings = {}  # type: ignore[typeddict-item]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    else:
        out["server_name"] = ""
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    if data.get("SslSecurityProtocol") is not None:
        import capo_database_migration_service.types.ssl_security_protocol_value

        out["ssl_security_protocol"] = (
            capo_database_migration_service.types.ssl_security_protocol_value.deserialize_aws_json_1_1(
                data["SslSecurityProtocol"]
            )
        )
    if data.get("AuthType") is not None:
        import capo_database_migration_service.types.redis_auth_type_value

        out["auth_type"] = (
            capo_database_migration_service.types.redis_auth_type_value.deserialize_aws_json_1_1(
                data["AuthType"]
            )
        )
    if data.get("AuthUserName") is not None:
        out["auth_user_name"] = data["AuthUserName"]
    if data.get("AuthPassword") is not None:
        out["auth_password"] = data["AuthPassword"]
    if data.get("SslCaCertificateArn") is not None:
        out["ssl_ca_certificate_arn"] = data["SslCaCertificateArn"]
    return out


def redact_sensitive(value: RedisSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_password" in value:
        out["auth_password"] = "*** Sensitive Data Redacted ***"
    return out
