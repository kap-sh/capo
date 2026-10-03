"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.certificate_arn
    import capo_ec2.types.create_verified_access_endpoint_cidr_options
    import capo_ec2.types.create_verified_access_endpoint_eni_options
    import capo_ec2.types.create_verified_access_endpoint_load_balancer_options
    import capo_ec2.types.create_verified_access_endpoint_rds_options
    import capo_ec2.types.security_group_id_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.verified_access_endpoint_attachment_type
    import capo_ec2.types.verified_access_endpoint_type
    import capo_ec2.types.verified_access_group_id
    import capo_ec2.types.verified_access_sse_specification_request


class CreateVerifiedAccessEndpointRequest(TypedDict, closed=True):
    verified_access_group_id: NotRequired[
        "capo_ec2.types.verified_access_group_id.VerifiedAccessGroupId"
    ]
    """<p>The ID of the Verified Access group to associate the endpoint with.</p>"""
    endpoint_type: NotRequired[
        "capo_ec2.types.verified_access_endpoint_type.VerifiedAccessEndpointType"
    ]
    """<p>The type of Verified Access endpoint to create.</p>"""
    attachment_type: NotRequired[
        "capo_ec2.types.verified_access_endpoint_attachment_type.VerifiedAccessEndpointAttachmentType"
    ]
    """<p>The type of attachment.</p>"""
    domain_certificate_arn: NotRequired["capo_ec2.types.certificate_arn.CertificateArn"]
    """<p>The ARN of the public TLS/SSL certificate in Amazon Web Services Certificate Manager to associate with the endpoint. The CN in the certificate must match the DNS name your end users will use to reach your application.</p>"""
    application_domain: NotRequired["capo_ec2.types.string.String"]
    """<p>The DNS name for users to reach your application.</p>"""
    endpoint_domain_prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>A custom identifier that is prepended to the DNS name that is generated for the endpoint.</p>"""
    security_group_ids: NotRequired[
        "capo_ec2.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The IDs of the security groups to associate with the Verified Access endpoint. Required if <code>AttachmentType</code> is set to <code>vpc</code>.</p>"""
    load_balancer_options: NotRequired[
        "capo_ec2.types.create_verified_access_endpoint_load_balancer_options.CreateVerifiedAccessEndpointLoadBalancerOptions"
    ]
    """<p>The load balancer details. This parameter is required if the endpoint type is <code>load-balancer</code>.</p>"""
    network_interface_options: NotRequired[
        "capo_ec2.types.create_verified_access_endpoint_eni_options.CreateVerifiedAccessEndpointEniOptions"
    ]
    """<p>The network interface details. This parameter is required if the endpoint type is <code>network-interface</code>.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the Verified Access endpoint.</p>"""
    policy_document: NotRequired["capo_ec2.types.string.String"]
    """<p>The Verified Access policy document.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Verified Access endpoint.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    sse_specification: NotRequired[
        "capo_ec2.types.verified_access_sse_specification_request.VerifiedAccessSseSpecificationRequest"
    ]
    """<p>The options for server side encryption.</p>"""
    rds_options: NotRequired[
        "capo_ec2.types.create_verified_access_endpoint_rds_options.CreateVerifiedAccessEndpointRdsOptions"
    ]
    """<p>The RDS details. This parameter is required if the endpoint type is <code>rds</code>.</p>"""
    cidr_options: NotRequired[
        "capo_ec2.types.create_verified_access_endpoint_cidr_options.CreateVerifiedAccessEndpointCidrOptions"
    ]
    """<p>The CIDR options. This parameter is required if the endpoint type is <code>cidr</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessEndpointRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_group_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessGroupId",
                str(value["verified_access_group_id"]),
            )
        )
    if "endpoint_type" in value:
        import capo_ec2.types.verified_access_endpoint_type

        capo_ec2.types.verified_access_endpoint_type.serialize_ec2_query(
            value["endpoint_type"], pairs, f"{key_prefix}EndpointType"
        )
    if "attachment_type" in value:
        import capo_ec2.types.verified_access_endpoint_attachment_type

        capo_ec2.types.verified_access_endpoint_attachment_type.serialize_ec2_query(
            value["attachment_type"], pairs, f"{key_prefix}AttachmentType"
        )
    if "domain_certificate_arn" in value:
        pairs.append(
            (f"{key_prefix}DomainCertificateArn", str(value["domain_certificate_arn"]))
        )
    if "application_domain" in value:
        pairs.append(
            (f"{key_prefix}ApplicationDomain", str(value["application_domain"]))
        )
    if "endpoint_domain_prefix" in value:
        pairs.append(
            (f"{key_prefix}EndpointDomainPrefix", str(value["endpoint_domain_prefix"]))
        )
    if "security_group_ids" in value:
        import capo_ec2.types.security_group_id_list

        capo_ec2.types.security_group_id_list.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupId"
        )
    if "load_balancer_options" in value:
        import capo_ec2.types.create_verified_access_endpoint_load_balancer_options

        capo_ec2.types.create_verified_access_endpoint_load_balancer_options.serialize_ec2_query(
            value["load_balancer_options"], pairs, f"{key_prefix}LoadBalancerOptions"
        )
    if "network_interface_options" in value:
        import capo_ec2.types.create_verified_access_endpoint_eni_options

        capo_ec2.types.create_verified_access_endpoint_eni_options.serialize_ec2_query(
            value["network_interface_options"],
            pairs,
            f"{key_prefix}NetworkInterfaceOptions",
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "policy_document" in value:
        pairs.append((f"{key_prefix}PolicyDocument", str(value["policy_document"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "sse_specification" in value:
        import capo_ec2.types.verified_access_sse_specification_request

        capo_ec2.types.verified_access_sse_specification_request.serialize_ec2_query(
            value["sse_specification"], pairs, f"{key_prefix}SseSpecification"
        )
    if "rds_options" in value:
        import capo_ec2.types.create_verified_access_endpoint_rds_options

        capo_ec2.types.create_verified_access_endpoint_rds_options.serialize_ec2_query(
            value["rds_options"], pairs, f"{key_prefix}RdsOptions"
        )
    if "cidr_options" in value:
        import capo_ec2.types.create_verified_access_endpoint_cidr_options

        capo_ec2.types.create_verified_access_endpoint_cidr_options.serialize_ec2_query(
            value["cidr_options"], pairs, f"{key_prefix}CidrOptions"
        )


def deserialize_ec2_query(el: Element) -> CreateVerifiedAccessEndpointRequest:
    out: CreateVerifiedAccessEndpointRequest = {}  # type: ignore[typeddict-item]
    child_verified_access_group_id = el.find("VerifiedAccessGroupId")
    if child_verified_access_group_id is not None:
        out["verified_access_group_id"] = str(child_verified_access_group_id.text or "")
    child_endpoint_type = el.find("EndpointType")
    if child_endpoint_type is not None:
        import capo_ec2.types.verified_access_endpoint_type

        out["endpoint_type"] = (
            capo_ec2.types.verified_access_endpoint_type.deserialize_ec2_query(
                child_endpoint_type
            )
        )
    child_attachment_type = el.find("AttachmentType")
    if child_attachment_type is not None:
        import capo_ec2.types.verified_access_endpoint_attachment_type

        out["attachment_type"] = (
            capo_ec2.types.verified_access_endpoint_attachment_type.deserialize_ec2_query(
                child_attachment_type
            )
        )
    child_domain_certificate_arn = el.find("DomainCertificateArn")
    if child_domain_certificate_arn is not None:
        out["domain_certificate_arn"] = str(child_domain_certificate_arn.text or "")
    child_application_domain = el.find("ApplicationDomain")
    if child_application_domain is not None:
        out["application_domain"] = str(child_application_domain.text or "")
    child_endpoint_domain_prefix = el.find("EndpointDomainPrefix")
    if child_endpoint_domain_prefix is not None:
        out["endpoint_domain_prefix"] = str(child_endpoint_domain_prefix.text or "")
    child_security_group_ids = el.find("SecurityGroupId")
    if child_security_group_ids is not None:
        import capo_ec2.types.security_group_id_list

        out["security_group_ids"] = (
            capo_ec2.types.security_group_id_list.deserialize_ec2_query(
                child_security_group_ids
            )
        )
    child_load_balancer_options = el.find("LoadBalancerOptions")
    if child_load_balancer_options is not None:
        import capo_ec2.types.create_verified_access_endpoint_load_balancer_options

        out["load_balancer_options"] = (
            capo_ec2.types.create_verified_access_endpoint_load_balancer_options.deserialize_ec2_query(
                child_load_balancer_options
            )
        )
    child_network_interface_options = el.find("NetworkInterfaceOptions")
    if child_network_interface_options is not None:
        import capo_ec2.types.create_verified_access_endpoint_eni_options

        out["network_interface_options"] = (
            capo_ec2.types.create_verified_access_endpoint_eni_options.deserialize_ec2_query(
                child_network_interface_options
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_sse_specification = el.find("SseSpecification")
    if child_sse_specification is not None:
        import capo_ec2.types.verified_access_sse_specification_request

        out["sse_specification"] = (
            capo_ec2.types.verified_access_sse_specification_request.deserialize_ec2_query(
                child_sse_specification
            )
        )
    child_rds_options = el.find("RdsOptions")
    if child_rds_options is not None:
        import capo_ec2.types.create_verified_access_endpoint_rds_options

        out["rds_options"] = (
            capo_ec2.types.create_verified_access_endpoint_rds_options.deserialize_ec2_query(
                child_rds_options
            )
        )
    child_cidr_options = el.find("CidrOptions")
    if child_cidr_options is not None:
        import capo_ec2.types.create_verified_access_endpoint_cidr_options

        out["cidr_options"] = (
            capo_ec2.types.create_verified_access_endpoint_cidr_options.deserialize_ec2_query(
                child_cidr_options
            )
        )
    return out
