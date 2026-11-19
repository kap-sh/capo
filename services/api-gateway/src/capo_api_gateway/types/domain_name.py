"""Generated from Smithy shape ``com.amazonaws.apigateway#DomainName``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.domain_name_status
    import capo_api_gateway.types.endpoint_access_mode
    import capo_api_gateway.types.endpoint_configuration
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.mutual_tls_authentication
    import capo_api_gateway.types.routing_mode
    import capo_api_gateway.types.security_policy
    import capo_api_gateway.types.string
    import capo_api_gateway.types.timestamp


class DomainName(TypedDict, closed=True):
    domain_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The custom domain name as an API host name, for example, <code>my-api.example.com</code>.</p>"""
    domain_name_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier for the domain name resource. Supported only for private custom domain names.</p>"""
    domain_name_arn: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The ARN of the domain name. </p>"""
    certificate_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of the certificate that will be used by edge-optimized endpoint or private endpoint for this domain name.</p>"""
    certificate_arn: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The reference to an Amazon Web Services-managed certificate that will be used by edge-optimized endpoint or private endpoint for this domain name. Certificate Manager is the only supported source.</p>"""
    certificate_upload_date: NotRequired["capo_api_gateway.types.timestamp.Timestamp"]
    """<p>The timestamp when the certificate that was used by edge-optimized endpoint or private endpoint for this domain name was uploaded.</p>"""
    regional_domain_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.</p>"""
    regional_hosted_zone_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see Set up a Regional Custom Domain Name and Amazon Web Services Regions and Endpoints for API Gateway. </p>"""
    regional_certificate_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of the certificate that will be used for validating the regional domain name.</p>"""
    regional_certificate_arn: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The reference to an Amazon Web Services-managed certificate that will be used for validating the regional domain name. Certificate Manager is the only supported source.</p>"""
    distribution_domain_name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the Amazon CloudFront documentation.</p>"""
    distribution_hosted_zone_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is <code>Z2FDTNDATAQYW2</code> for all the regions. For more information, see Set up a Regional Custom Domain Name and Amazon Web Services Regions and Endpoints for API Gateway. </p>"""
    endpoint_configuration: NotRequired[
        "capo_api_gateway.types.endpoint_configuration.EndpointConfiguration"
    ]
    """<p>The endpoint configuration of this DomainName showing the endpoint types and IP address types of the domain name. </p>"""
    domain_name_status: NotRequired[
        "capo_api_gateway.types.domain_name_status.DomainNameStatus"
    ]
    """<p>The status of the DomainName migration. The valid values are <code>AVAILABLE</code> and <code>UPDATING</code>. If the status is <code>UPDATING</code>, the domain cannot be modified further until the existing operation is complete. If it is <code>AVAILABLE</code>, the domain can be updated.</p>"""
    domain_name_status_message: NotRequired["capo_api_gateway.types.string.String"]
    """<p>An optional text message containing detailed information about status of the DomainName migration.</p>"""
    security_policy: NotRequired[
        "capo_api_gateway.types.security_policy.SecurityPolicy"
    ]
    """<p>The Transport Layer Security (TLS) version + cipher suite for this DomainName.</p>"""
    endpoint_access_mode: NotRequired[
        "capo_api_gateway.types.endpoint_access_mode.EndpointAccessMode"
    ]
    """<p> The endpoint access mode of the DomainName. </p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""
    mutual_tls_authentication: NotRequired[
        "capo_api_gateway.types.mutual_tls_authentication.MutualTlsAuthentication"
    ]
    """<p>The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.</p>"""
    ownership_verification_certificate_arn: NotRequired[
        "capo_api_gateway.types.string.String"
    ]
    """<p>The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn.</p>"""
    management_policy: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A stringified JSON policy document that applies to the API Gateway Management service for this DomainName. This policy document controls access for access association sources to create domain name access associations with this DomainName. Supported only for private custom domain names.</p>"""
    policy: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A stringified JSON policy document that applies to the <code>execute-api</code> service for this DomainName regardless of the caller and Method configuration. Supported only for private custom domain names.</p>"""
    routing_mode: NotRequired["capo_api_gateway.types.routing_mode.RoutingMode"]
    """<p>The routing mode for this domain name. The routing mode determines how API Gateway sends traffic from your custom domain name to your private APIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainName) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "domain_name_id" in value:
        out["domainNameId"] = value["domain_name_id"]
    if "domain_name_arn" in value:
        out["domainNameArn"] = value["domain_name_arn"]
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_upload_date" in value:
        import capo_api_gateway.types.timestamp

        out["certificateUploadDate"] = capo_api_gateway.types.timestamp.serialize_json(
            value["certificate_upload_date"]
        )
    if "regional_domain_name" in value:
        out["regionalDomainName"] = value["regional_domain_name"]
    if "regional_hosted_zone_id" in value:
        out["regionalHostedZoneId"] = value["regional_hosted_zone_id"]
    if "regional_certificate_name" in value:
        out["regionalCertificateName"] = value["regional_certificate_name"]
    if "regional_certificate_arn" in value:
        out["regionalCertificateArn"] = value["regional_certificate_arn"]
    if "distribution_domain_name" in value:
        out["distributionDomainName"] = value["distribution_domain_name"]
    if "distribution_hosted_zone_id" in value:
        out["distributionHostedZoneId"] = value["distribution_hosted_zone_id"]
    if "endpoint_configuration" in value:
        import capo_api_gateway.types.endpoint_configuration

        out["endpointConfiguration"] = (
            capo_api_gateway.types.endpoint_configuration.serialize_json(
                value["endpoint_configuration"]
            )
        )
    if "domain_name_status" in value:
        import capo_api_gateway.types.domain_name_status

        out["domainNameStatus"] = (
            capo_api_gateway.types.domain_name_status.serialize_json(
                value["domain_name_status"]
            )
        )
    if "domain_name_status_message" in value:
        out["domainNameStatusMessage"] = value["domain_name_status_message"]
    if "security_policy" in value:
        import capo_api_gateway.types.security_policy

        out["securityPolicy"] = capo_api_gateway.types.security_policy.serialize_json(
            value["security_policy"]
        )
    if "endpoint_access_mode" in value:
        import capo_api_gateway.types.endpoint_access_mode

        out["endpointAccessMode"] = (
            capo_api_gateway.types.endpoint_access_mode.serialize_json(
                value["endpoint_access_mode"]
            )
        )
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    if "mutual_tls_authentication" in value:
        import capo_api_gateway.types.mutual_tls_authentication

        out["mutualTlsAuthentication"] = (
            capo_api_gateway.types.mutual_tls_authentication.serialize_json(
                value["mutual_tls_authentication"]
            )
        )
    if "ownership_verification_certificate_arn" in value:
        out["ownershipVerificationCertificateArn"] = value[
            "ownership_verification_certificate_arn"
        ]
    if "management_policy" in value:
        out["managementPolicy"] = value["management_policy"]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "routing_mode" in value:
        import capo_api_gateway.types.routing_mode

        out["routingMode"] = capo_api_gateway.types.routing_mode.serialize_json(
            value["routing_mode"]
        )
    return out


def deserialize_json(data: dict) -> DomainName:
    out: DomainName = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("domainNameId") is not None:
        out["domain_name_id"] = data["domainNameId"]
    if data.get("domainNameArn") is not None:
        out["domain_name_arn"] = data["domainNameArn"]
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    if data.get("certificateArn") is not None:
        out["certificate_arn"] = data["certificateArn"]
    if data.get("certificateUploadDate") is not None:
        import capo_api_gateway.types.timestamp

        out["certificate_upload_date"] = (
            capo_api_gateway.types.timestamp.deserialize_json(
                data["certificateUploadDate"]
            )
        )
    if data.get("regionalDomainName") is not None:
        out["regional_domain_name"] = data["regionalDomainName"]
    if data.get("regionalHostedZoneId") is not None:
        out["regional_hosted_zone_id"] = data["regionalHostedZoneId"]
    if data.get("regionalCertificateName") is not None:
        out["regional_certificate_name"] = data["regionalCertificateName"]
    if data.get("regionalCertificateArn") is not None:
        out["regional_certificate_arn"] = data["regionalCertificateArn"]
    if data.get("distributionDomainName") is not None:
        out["distribution_domain_name"] = data["distributionDomainName"]
    if data.get("distributionHostedZoneId") is not None:
        out["distribution_hosted_zone_id"] = data["distributionHostedZoneId"]
    if data.get("endpointConfiguration") is not None:
        import capo_api_gateway.types.endpoint_configuration

        out["endpoint_configuration"] = (
            capo_api_gateway.types.endpoint_configuration.deserialize_json(
                data["endpointConfiguration"]
            )
        )
    if data.get("domainNameStatus") is not None:
        import capo_api_gateway.types.domain_name_status

        out["domain_name_status"] = (
            capo_api_gateway.types.domain_name_status.deserialize_json(
                data["domainNameStatus"]
            )
        )
    if data.get("domainNameStatusMessage") is not None:
        out["domain_name_status_message"] = data["domainNameStatusMessage"]
    if data.get("securityPolicy") is not None:
        import capo_api_gateway.types.security_policy

        out["security_policy"] = (
            capo_api_gateway.types.security_policy.deserialize_json(
                data["securityPolicy"]
            )
        )
    if data.get("endpointAccessMode") is not None:
        import capo_api_gateway.types.endpoint_access_mode

        out["endpoint_access_mode"] = (
            capo_api_gateway.types.endpoint_access_mode.deserialize_json(
                data["endpointAccessMode"]
            )
        )
    if data.get("tags") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    if data.get("mutualTlsAuthentication") is not None:
        import capo_api_gateway.types.mutual_tls_authentication

        out["mutual_tls_authentication"] = (
            capo_api_gateway.types.mutual_tls_authentication.deserialize_json(
                data["mutualTlsAuthentication"]
            )
        )
    if data.get("ownershipVerificationCertificateArn") is not None:
        out["ownership_verification_certificate_arn"] = data[
            "ownershipVerificationCertificateArn"
        ]
    if data.get("managementPolicy") is not None:
        out["management_policy"] = data["managementPolicy"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    if data.get("routingMode") is not None:
        import capo_api_gateway.types.routing_mode

        out["routing_mode"] = capo_api_gateway.types.routing_mode.deserialize_json(
            data["routingMode"]
        )
    return out
