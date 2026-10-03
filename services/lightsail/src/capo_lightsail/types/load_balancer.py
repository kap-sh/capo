"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.instance_health_summary_list
    import capo_lightsail.types.integer
    import capo_lightsail.types.ip_address_type
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.load_balancer_configuration_options
    import capo_lightsail.types.load_balancer_protocol
    import capo_lightsail.types.load_balancer_state
    import capo_lightsail.types.load_balancer_tls_certificate_summary_list
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.port_list
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class LoadBalancer(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the load balancer (<code>my-load-balancer</code>).</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The date when your load balancer was created.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>The AWS Region where your load balancer was created (<code>us-east-2a</code>). Lightsail automatically creates your load balancer across Availability Zones.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The resource type (<code>LoadBalancer</code>.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    dns_name: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The DNS name of your Lightsail load balancer.</p>"""
    state: NotRequired["capo_lightsail.types.load_balancer_state.LoadBalancerState"]
    """<p>The status of your load balancer. Valid values are below.</p>"""
    protocol: NotRequired[
        "capo_lightsail.types.load_balancer_protocol.LoadBalancerProtocol"
    ]
    """<p>The protocol you have enabled for your load balancer. Valid values are below.</p> <p>You can't just have <code>HTTP_HTTPS</code>, but you can have just <code>HTTP</code>.</p>"""
    public_ports: NotRequired["capo_lightsail.types.port_list.PortList"]
    """<p>An array of public port settings for your load balancer. For HTTP, use port 80. For HTTPS, use port 443.</p>"""
    health_check_path: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.</p>"""
    instance_port: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The port where the load balancer will direct traffic to your Lightsail instances. For HTTP traffic, it's port 80. For HTTPS traffic, it's port 443.</p>"""
    instance_health_summary: NotRequired[
        "capo_lightsail.types.instance_health_summary_list.InstanceHealthSummaryList"
    ]
    """<p>An array of InstanceHealthSummary objects describing the health of the load balancer.</p>"""
    tls_certificate_summaries: NotRequired[
        "capo_lightsail.types.load_balancer_tls_certificate_summary_list.LoadBalancerTlsCertificateSummaryList"
    ]
    """<p>An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the SSL/TLS certificates. For example, if <code>true</code>, the certificate is attached to the load balancer.</p>"""
    configuration_options: NotRequired[
        "capo_lightsail.types.load_balancer_configuration_options.LoadBalancerConfigurationOptions"
    ]
    """<p>A string to string map of the configuration options for your load balancer. Valid values are listed below.</p>"""
    ip_address_type: NotRequired["capo_lightsail.types.ip_address_type.IpAddressType"]
    """<p>The IP address type of the load balancer.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p>"""
    https_redirection_enabled: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.</p>"""
    tls_policy_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the TLS security policy for the load balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancer) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "dns_name" in value:
        out["dnsName"] = value["dns_name"]
    if "state" in value:
        import capo_lightsail.types.load_balancer_state

        out["state"] = capo_lightsail.types.load_balancer_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "protocol" in value:
        import capo_lightsail.types.load_balancer_protocol

        out["protocol"] = (
            capo_lightsail.types.load_balancer_protocol.serialize_aws_json_1_1(
                value["protocol"]
            )
        )
    if "public_ports" in value:
        import capo_lightsail.types.port_list

        out["publicPorts"] = capo_lightsail.types.port_list.serialize_aws_json_1_1(
            value["public_ports"]
        )
    if "health_check_path" in value:
        out["healthCheckPath"] = value["health_check_path"]
    if "instance_port" in value:
        out["instancePort"] = value["instance_port"]
    if "instance_health_summary" in value:
        import capo_lightsail.types.instance_health_summary_list

        out["instanceHealthSummary"] = (
            capo_lightsail.types.instance_health_summary_list.serialize_aws_json_1_1(
                value["instance_health_summary"]
            )
        )
    if "tls_certificate_summaries" in value:
        import capo_lightsail.types.load_balancer_tls_certificate_summary_list

        out["tlsCertificateSummaries"] = (
            capo_lightsail.types.load_balancer_tls_certificate_summary_list.serialize_aws_json_1_1(
                value["tls_certificate_summaries"]
            )
        )
    if "configuration_options" in value:
        import capo_lightsail.types.load_balancer_configuration_options

        out["configurationOptions"] = (
            capo_lightsail.types.load_balancer_configuration_options.serialize_aws_json_1_1(
                value["configuration_options"]
            )
        )
    if "ip_address_type" in value:
        import capo_lightsail.types.ip_address_type

        out["ipAddressType"] = (
            capo_lightsail.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "https_redirection_enabled" in value:
        out["httpsRedirectionEnabled"] = value["https_redirection_enabled"]
    if "tls_policy_name" in value:
        out["tlsPolicyName"] = value["tls_policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LoadBalancer:
    out: LoadBalancer = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("supportCode") is not None:
        out["support_code"] = data["supportCode"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("dnsName") is not None:
        out["dns_name"] = data["dnsName"]
    if data.get("state") is not None:
        import capo_lightsail.types.load_balancer_state

        out["state"] = (
            capo_lightsail.types.load_balancer_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    if data.get("protocol") is not None:
        import capo_lightsail.types.load_balancer_protocol

        out["protocol"] = (
            capo_lightsail.types.load_balancer_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    if data.get("publicPorts") is not None:
        import capo_lightsail.types.port_list

        out["public_ports"] = capo_lightsail.types.port_list.deserialize_aws_json_1_1(
            data["publicPorts"]
        )
    if data.get("healthCheckPath") is not None:
        out["health_check_path"] = data["healthCheckPath"]
    if data.get("instancePort") is not None:
        out["instance_port"] = data["instancePort"]
    if data.get("instanceHealthSummary") is not None:
        import capo_lightsail.types.instance_health_summary_list

        out["instance_health_summary"] = (
            capo_lightsail.types.instance_health_summary_list.deserialize_aws_json_1_1(
                data["instanceHealthSummary"]
            )
        )
    if data.get("tlsCertificateSummaries") is not None:
        import capo_lightsail.types.load_balancer_tls_certificate_summary_list

        out["tls_certificate_summaries"] = (
            capo_lightsail.types.load_balancer_tls_certificate_summary_list.deserialize_aws_json_1_1(
                data["tlsCertificateSummaries"]
            )
        )
    if data.get("configurationOptions") is not None:
        import capo_lightsail.types.load_balancer_configuration_options

        out["configuration_options"] = (
            capo_lightsail.types.load_balancer_configuration_options.deserialize_aws_json_1_1(
                data["configurationOptions"]
            )
        )
    if data.get("ipAddressType") is not None:
        import capo_lightsail.types.ip_address_type

        out["ip_address_type"] = (
            capo_lightsail.types.ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    if data.get("httpsRedirectionEnabled") is not None:
        out["https_redirection_enabled"] = data["httpsRedirectionEnabled"]
    if data.get("tlsPolicyName") is not None:
        out["tls_policy_name"] = data["tlsPolicyName"]
    return out
