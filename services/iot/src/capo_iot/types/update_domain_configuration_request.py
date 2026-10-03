"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDomainConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.application_protocol
    import capo_iot.types.authentication_type
    import capo_iot.types.authorizer_config
    import capo_iot.types.client_certificate_config
    import capo_iot.types.domain_configuration_status
    import capo_iot.types.remove_authorizer_config
    import capo_iot.types.reserved_domain_configuration_name
    import capo_iot.types.server_certificate_config
    import capo_iot.types.tls_config


class UpdateDomainConfigurationRequest(TypedDict, closed=True):
    domain_configuration_name: "capo_iot.types.reserved_domain_configuration_name.ReservedDomainConfigurationName"
    """<p>The name of the domain configuration to be updated.</p>"""
    authorizer_config: NotRequired["capo_iot.types.authorizer_config.AuthorizerConfig"]
    """<p>An object that specifies the authorization service for a domain.</p>"""
    domain_configuration_status: NotRequired[
        "capo_iot.types.domain_configuration_status.DomainConfigurationStatus"
    ]
    """<p>The status to which the domain configuration should be updated.</p>"""
    remove_authorizer_config: (
        "capo_iot.types.remove_authorizer_config.RemoveAuthorizerConfig"
    )
    """<p>Removes the authorization configuration from a domain.</p>"""
    tls_config: NotRequired["capo_iot.types.tls_config.TlsConfig"]
    """<p>An object that specifies the TLS configuration for a domain.</p>"""
    server_certificate_config: NotRequired[
        "capo_iot.types.server_certificate_config.ServerCertificateConfig"
    ]
    """<p>The server certificate configuration.</p>"""
    authentication_type: NotRequired[
        "capo_iot.types.authentication_type.AuthenticationType"
    ]
    """<p>An enumerated string that speciﬁes the authentication type.</p> <ul> <li> <p> <code>CUSTOM_AUTH_X509</code> - Use custom authentication and authorization with additional details from the X.509 client certificate.</p> </li> </ul> <ul> <li> <p> <code>CUSTOM_AUTH</code> - Use custom authentication and authorization. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html">Custom authentication and authorization</a>.</p> </li> </ul> <ul> <li> <p> <code>AWS_X509</code> - Use X.509 client certificates without custom authentication and authorization. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html">X.509 client certificates</a>.</p> </li> </ul> <ul> <li> <p> <code>AWS_SIGV4</code> - Use Amazon Web Services Signature Version 4. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html">IAM users, groups, and roles</a>.</p> </li> </ul> <ul> <li> <p> <code>DEFAULT </code> - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify authentication type. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html">Device communication protocols</a>.</p> </li> </ul>"""
    application_protocol: NotRequired[
        "capo_iot.types.application_protocol.ApplicationProtocol"
    ]
    """<p>An enumerated string that speciﬁes the application-layer protocol.</p> <ul> <li> <p> <code>SECURE_MQTT</code> - MQTT over TLS.</p> </li> </ul> <ul> <li> <p> <code>MQTT_WSS</code> - MQTT over WebSocket.</p> </li> </ul> <ul> <li> <p> <code>HTTPS</code> - HTTP over TLS.</p> </li> </ul> <ul> <li> <p> <code>DEFAULT</code> - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify application_layer protocol. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html">Device communication protocols</a>.</p> </li> </ul>"""
    client_certificate_config: NotRequired[
        "capo_iot.types.client_certificate_config.ClientCertificateConfig"
    ]
    """<p>An object that speciﬁes the client certificate conﬁguration for a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainConfigurationRequest) -> dict:
    out: dict = {}
    if "authorizer_config" in value:
        import capo_iot.types.authorizer_config

        out["authorizerConfig"] = capo_iot.types.authorizer_config.serialize_json(
            value["authorizer_config"]
        )
    if "domain_configuration_status" in value:
        import capo_iot.types.domain_configuration_status

        out["domainConfigurationStatus"] = (
            capo_iot.types.domain_configuration_status.serialize_json(
                value["domain_configuration_status"]
            )
        )
    out["removeAuthorizerConfig"] = value.get("remove_authorizer_config", False)
    if "tls_config" in value:
        import capo_iot.types.tls_config

        out["tlsConfig"] = capo_iot.types.tls_config.serialize_json(value["tls_config"])
    if "server_certificate_config" in value:
        import capo_iot.types.server_certificate_config

        out["serverCertificateConfig"] = (
            capo_iot.types.server_certificate_config.serialize_json(
                value["server_certificate_config"]
            )
        )
    if "authentication_type" in value:
        import capo_iot.types.authentication_type

        out["authenticationType"] = capo_iot.types.authentication_type.serialize_json(
            value["authentication_type"]
        )
    if "application_protocol" in value:
        import capo_iot.types.application_protocol

        out["applicationProtocol"] = capo_iot.types.application_protocol.serialize_json(
            value["application_protocol"]
        )
    if "client_certificate_config" in value:
        import capo_iot.types.client_certificate_config

        out["clientCertificateConfig"] = (
            capo_iot.types.client_certificate_config.serialize_json(
                value["client_certificate_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDomainConfigurationRequest:
    out: UpdateDomainConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("authorizerConfig") is not None:
        import capo_iot.types.authorizer_config

        out["authorizer_config"] = capo_iot.types.authorizer_config.deserialize_json(
            data["authorizerConfig"]
        )
    if data.get("domainConfigurationStatus") is not None:
        import capo_iot.types.domain_configuration_status

        out["domain_configuration_status"] = (
            capo_iot.types.domain_configuration_status.deserialize_json(
                data["domainConfigurationStatus"]
            )
        )
    if data.get("removeAuthorizerConfig") is not None:
        out["remove_authorizer_config"] = data["removeAuthorizerConfig"]
    else:
        out["remove_authorizer_config"] = False
    if data.get("tlsConfig") is not None:
        import capo_iot.types.tls_config

        out["tls_config"] = capo_iot.types.tls_config.deserialize_json(
            data["tlsConfig"]
        )
    if data.get("serverCertificateConfig") is not None:
        import capo_iot.types.server_certificate_config

        out["server_certificate_config"] = (
            capo_iot.types.server_certificate_config.deserialize_json(
                data["serverCertificateConfig"]
            )
        )
    if data.get("authenticationType") is not None:
        import capo_iot.types.authentication_type

        out["authentication_type"] = (
            capo_iot.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    if data.get("applicationProtocol") is not None:
        import capo_iot.types.application_protocol

        out["application_protocol"] = (
            capo_iot.types.application_protocol.deserialize_json(
                data["applicationProtocol"]
            )
        )
    if data.get("clientCertificateConfig") is not None:
        import capo_iot.types.client_certificate_config

        out["client_certificate_config"] = (
            capo_iot.types.client_certificate_config.deserialize_json(
                data["clientCertificateConfig"]
            )
        )
    return out
