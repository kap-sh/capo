"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainEndpointOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.boolean
    import capo_opensearch.types.domain_name_fqdn
    import capo_opensearch.types.tls_security_policy


class DomainEndpointOptions(TypedDict, closed=True):
    enforce_https: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>True to require that all traffic to the domain arrive over HTTPS.</p>"""
    tls_security_policy: NotRequired[
        "capo_opensearch.types.tls_security_policy.TLSSecurityPolicy"
    ]
    """<p>Specify the TLS security policy to apply to the HTTPS endpoint of the domain. The policy can be one of the following values:</p> <ul> <li> <p> <b>Policy-Min-TLS-1-0-2019-07:</b> TLS security policy that supports TLS version 1.0 to TLS version 1.2</p> </li> <li> <p> <b>Policy-Min-TLS-1-2-2019-07:</b> TLS security policy that supports only TLS version 1.2</p> </li> <li> <p> <b>Policy-Min-TLS-1-2-PFS-2023-10:</b> TLS security policy that supports TLS version 1.2 to TLS version 1.3 with perfect forward secrecy cipher suites</p> </li> <li> <p> <b>Policy-Min-TLS-1-2-RFC9151-FIPS-2024-08:</b> TLS security policy that supports TLS version 1.3 with FIPS</p> </li> <li> <p> <b>Policy-Min-TLS-1-2-FIPS-PQ-2026-10:</b> TLS security policy that supports TLS version 1.2 to TLS version 1.3 with FIPS and post-quantum cipher suites</p> </li> </ul>"""
    custom_endpoint_enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Whether to enable a custom endpoint for the domain.</p>"""
    custom_endpoint: NotRequired[
        "capo_opensearch.types.domain_name_fqdn.DomainNameFqdn"
    ]
    """<p>The fully qualified URL for the custom endpoint.</p>"""
    custom_endpoint_certificate_arn: NotRequired["capo_opensearch.types.arn.ARN"]
    """<p>The ARN for your security certificate, managed in Amazon Web Services Certificate Manager (ACM).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainEndpointOptions) -> dict:
    out: dict = {}
    if "enforce_https" in value:
        out["EnforceHTTPS"] = value["enforce_https"]
    if "tls_security_policy" in value:
        import capo_opensearch.types.tls_security_policy

        out["TLSSecurityPolicy"] = (
            capo_opensearch.types.tls_security_policy.serialize_json(
                value["tls_security_policy"]
            )
        )
    if "custom_endpoint_enabled" in value:
        out["CustomEndpointEnabled"] = value["custom_endpoint_enabled"]
    if "custom_endpoint" in value:
        out["CustomEndpoint"] = value["custom_endpoint"]
    if "custom_endpoint_certificate_arn" in value:
        out["CustomEndpointCertificateArn"] = value["custom_endpoint_certificate_arn"]
    return out


def deserialize_json(data: dict) -> DomainEndpointOptions:
    out: DomainEndpointOptions = {}  # type: ignore[typeddict-item]
    if data.get("EnforceHTTPS") is not None:
        out["enforce_https"] = data["EnforceHTTPS"]
    if data.get("TLSSecurityPolicy") is not None:
        import capo_opensearch.types.tls_security_policy

        out["tls_security_policy"] = (
            capo_opensearch.types.tls_security_policy.deserialize_json(
                data["TLSSecurityPolicy"]
            )
        )
    if data.get("CustomEndpointEnabled") is not None:
        out["custom_endpoint_enabled"] = data["CustomEndpointEnabled"]
    if data.get("CustomEndpoint") is not None:
        out["custom_endpoint"] = data["CustomEndpoint"]
    if data.get("CustomEndpointCertificateArn") is not None:
        out["custom_endpoint_certificate_arn"] = data["CustomEndpointCertificateArn"]
    return out
