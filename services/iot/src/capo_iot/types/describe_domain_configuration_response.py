"""Generated from Smithy shape ``com.amazonaws.iot#DescribeDomainConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.application_protocol
    import capo_iot.types.authentication_type
    import capo_iot.types.authorizer_config
    import capo_iot.types.client_certificate_config
    import capo_iot.types.date_type
    import capo_iot.types.domain_configuration_arn
    import capo_iot.types.domain_configuration_status
    import capo_iot.types.domain_name
    import capo_iot.types.domain_type
    import capo_iot.types.reserved_domain_configuration_name
    import capo_iot.types.server_certificate_config
    import capo_iot.types.server_certificates
    import capo_iot.types.service_type
    import capo_iot.types.tls_config


class DescribeDomainConfigurationResponse(TypedDict, closed=True):
    domain_configuration_name: NotRequired[
        "capo_iot.types.reserved_domain_configuration_name.ReservedDomainConfigurationName"
    ]
    """<p>The name of the domain configuration.</p>"""
    domain_configuration_arn: NotRequired[
        "capo_iot.types.domain_configuration_arn.DomainConfigurationArn"
    ]
    """<p>The ARN of the domain configuration.</p>"""
    domain_name: NotRequired["capo_iot.types.domain_name.DomainName"]
    """<p>The name of the domain.</p>"""
    server_certificates: NotRequired[
        "capo_iot.types.server_certificates.ServerCertificates"
    ]
    """<p>A list containing summary information about the server certificate included in the domain configuration.</p>"""
    authorizer_config: NotRequired["capo_iot.types.authorizer_config.AuthorizerConfig"]
    """<p>An object that specifies the authorization service for a domain.</p>"""
    domain_configuration_status: NotRequired[
        "capo_iot.types.domain_configuration_status.DomainConfigurationStatus"
    ]
    """<p>A Boolean value that specifies the current state of the domain configuration.</p>"""
    service_type: NotRequired["capo_iot.types.service_type.ServiceType"]
    """<p>The type of service delivered by the endpoint.</p>"""
    domain_type: NotRequired["capo_iot.types.domain_type.DomainType"]
    """<p>The type of the domain.</p>"""
    last_status_change_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date and time the domain configuration's status was last changed.</p>"""
    tls_config: NotRequired["capo_iot.types.tls_config.TlsConfig"]
    """<p>An object that specifies the TLS configuration for a domain.</p>"""
    server_certificate_config: NotRequired[
        "capo_iot.types.server_certificate_config.ServerCertificateConfig"
    ]
    """<p>The server certificate configuration.</p>"""
    authentication_type: NotRequired[
        "capo_iot.types.authentication_type.AuthenticationType"
    ]
    """<p>An enumerated string that speciﬁes the authentication type.</p> <ul> <li> <p> <code>CUSTOM_AUTH_X509</code> - Use custom authentication and authorization with additional details from the X.509 client certificate.</p> </li> </ul> <ul> <li> <p> <code>CUSTOM_AUTH</code> - Use custom authentication and authorization. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html">Custom authentication and authorization</a>.</p> </li> </ul> <ul> <li> <p> <code>AWS_X509</code> - Use X.509 client certificates without custom authentication and authorization. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html">X.509 client certificates</a>.</p> </li> </ul> <ul> <li> <p> <code>AWS_SIGV4</code> - Use Amazon Web Services Signature Version 4. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html">IAM users, groups, and roles</a>.</p> </li> </ul> <ul> <li> <p> <code>DEFAULT</code> - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify authentication type. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html">Device communication protocols</a>.</p> </li> </ul>"""
    application_protocol: NotRequired[
        "capo_iot.types.application_protocol.ApplicationProtocol"
    ]
    """<p>An enumerated string that speciﬁes the application-layer protocol.</p> <ul> <li> <p> <code>SECURE_MQTT</code> - MQTT over TLS.</p> </li> </ul> <ul> <li> <p> <code>MQTT_WSS</code> - MQTT over WebSocket.</p> </li> </ul> <ul> <li> <p> <code>HTTPS</code> - HTTP over TLS.</p> </li> </ul> <ul> <li> <p> <code>DEFAULT</code> - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify application_layer protocol. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html">Device communication protocols</a>.</p> </li> </ul>"""
    client_certificate_config: NotRequired[
        "capo_iot.types.client_certificate_config.ClientCertificateConfig"
    ]
    """<p>An object that speciﬁes the client certificate conﬁguration for a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainConfigurationResponse) -> dict:
    out: dict = {}
    if "domain_configuration_name" in value:
        out["domainConfigurationName"] = value["domain_configuration_name"]
    if "domain_configuration_arn" in value:
        out["domainConfigurationArn"] = value["domain_configuration_arn"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "server_certificates" in value:
        import capo_iot.types.server_certificates

        out["serverCertificates"] = capo_iot.types.server_certificates.serialize_json(
            value["server_certificates"]
        )
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
    if "service_type" in value:
        import capo_iot.types.service_type

        out["serviceType"] = capo_iot.types.service_type.serialize_json(
            value["service_type"]
        )
    if "domain_type" in value:
        import capo_iot.types.domain_type

        out["domainType"] = capo_iot.types.domain_type.serialize_json(
            value["domain_type"]
        )
    if "last_status_change_date" in value:
        import capo_iot.types.date_type

        out["lastStatusChangeDate"] = capo_iot.types.date_type.serialize_json(
            value["last_status_change_date"]
        )
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


def deserialize_json(data: dict) -> DescribeDomainConfigurationResponse:
    out: DescribeDomainConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("domainConfigurationName") is not None:
        out["domain_configuration_name"] = data["domainConfigurationName"]
    if data.get("domainConfigurationArn") is not None:
        out["domain_configuration_arn"] = data["domainConfigurationArn"]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("serverCertificates") is not None:
        import capo_iot.types.server_certificates

        out["server_certificates"] = (
            capo_iot.types.server_certificates.deserialize_json(
                data["serverCertificates"]
            )
        )
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
    if data.get("serviceType") is not None:
        import capo_iot.types.service_type

        out["service_type"] = capo_iot.types.service_type.deserialize_json(
            data["serviceType"]
        )
    if data.get("domainType") is not None:
        import capo_iot.types.domain_type

        out["domain_type"] = capo_iot.types.domain_type.deserialize_json(
            data["domainType"]
        )
    if data.get("lastStatusChangeDate") is not None:
        import capo_iot.types.date_type

        out["last_status_change_date"] = capo_iot.types.date_type.deserialize_json(
            data["lastStatusChangeDate"]
        )
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
