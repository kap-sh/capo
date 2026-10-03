"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHealthCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.alarm_identifier
    import capo_route_53.types.child_health_check_list
    import capo_route_53.types.disabled
    import capo_route_53.types.enable_sni
    import capo_route_53.types.failure_threshold
    import capo_route_53.types.fully_qualified_domain_name
    import capo_route_53.types.health_check_id
    import capo_route_53.types.health_check_region_list
    import capo_route_53.types.health_check_version
    import capo_route_53.types.health_threshold
    import capo_route_53.types.insufficient_data_health_status
    import capo_route_53.types.inverted
    import capo_route_53.types.ip_address
    import capo_route_53.types.port
    import capo_route_53.types.resettable_element_name_list
    import capo_route_53.types.resource_path
    import capo_route_53.types.search_string


class UpdateHealthCheckRequest(TypedDict, closed=True):
    health_check_id: "capo_route_53.types.health_check_id.HealthCheckId"
    """<p>The ID for the health check for which you want detailed information. When you created the health check, <code>CreateHealthCheck</code> returned the ID in the response, in the <code>HealthCheckId</code> element.</p>"""
    health_check_version: NotRequired[
        "capo_route_53.types.health_check_version.HealthCheckVersion"
    ]
    """<p>A sequential counter that Amazon Route 53 sets to <code>1</code> when you create a health check and increments by 1 each time you update settings for the health check.</p> <p>We recommend that you use <code>GetHealthCheck</code> or <code>ListHealthChecks</code> to get the current value of <code>HealthCheckVersion</code> for the health check that you want to update, and that you include that value in your <code>UpdateHealthCheck</code> request. This prevents Route 53 from overwriting an intervening update:</p> <ul> <li> <p>If the value in the <code>UpdateHealthCheck</code> request matches the value of <code>HealthCheckVersion</code> in the health check, Route 53 updates the health check with the new settings.</p> </li> <li> <p>If the value of <code>HealthCheckVersion</code> in the health check is greater, the health check was changed after you got the version number. Route 53 does not update the health check, and it returns a <code>HealthCheckVersionMismatch</code> error.</p> </li> </ul>"""
    ip_address: NotRequired["capo_route_53.types.ip_address.IPAddress"]
    """<p>The IPv4 or IPv6 IP address for the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for <code>IPAddress</code>, Route 53 sends a DNS request to resolve the domain name that you specify in <code>FullyQualifiedDomainName</code> at the interval that you specify in <code>RequestInterval</code>. Using an IP address that is returned by DNS, Route 53 then checks the health of the endpoint.</p> <p>Use one of the following formats for the value of <code>IPAddress</code>: </p> <ul> <li> <p> <b>IPv4 address</b>: four values between 0 and 255, separated by periods (.), for example, <code>192.0.2.44</code>.</p> </li> <li> <p> <b>IPv6 address</b>: eight groups of four hexadecimal values, separated by colons (:), for example, <code>2001:0db8:85a3:0000:0000:abcd:0001:2345</code>. You can also shorten IPv6 addresses as described in RFC 5952, for example, <code>2001:db8:85a3::abcd:1:2345</code>.</p> </li> </ul> <p>If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for <code>IPAddress</code>. This ensures that the IP address of your instance never changes. For more information, see the applicable documentation:</p> <ul> <li> <p>Linux: <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html">Elastic IP Addresses (EIP)</a> in the <i>Amazon EC2 User Guide for Linux Instances</i> </p> </li> <li> <p>Windows: <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-ip-addresses-eip.html">Elastic IP Addresses (EIP)</a> in the <i>Amazon EC2 User Guide for Windows Instances</i> </p> </li> </ul> <note> <p>If a health check already has a value for <code>IPAddress</code>, you can change the value. However, you can't update an existing health check to add or remove the value of <code>IPAddress</code>. </p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName">FullyQualifiedDomainName</a>. </p> <p>Constraints: Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:</p> <ul> <li> <p> <a href="https://tools.ietf.org/html/rfc5735">RFC 5735, Special Use IPv4 Addresses</a> </p> </li> <li> <p> <a href="https://tools.ietf.org/html/rfc6598">RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space</a> </p> </li> <li> <p> <a href="https://tools.ietf.org/html/rfc5156">RFC 5156, Special-Use IPv6 Addresses</a> </p> </li> </ul>"""
    port: NotRequired["capo_route_53.types.port.Port"]
    """<p>The port on the endpoint that you want Amazon Route 53 to perform health checks on.</p> <note> <p>Don't specify a value for <code>Port</code> when you specify a value for <code>Type</code> of <code>CLOUDWATCH_METRIC</code> or <code>CALCULATED</code>.</p> </note>"""
    resource_path: NotRequired["capo_route_53.types.resource_path.ResourcePath"]
    """<p>The path that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example the file /docs/route53-health-check.html. You can also include query string parameters, for example, <code>/welcome.html?language=jp&login=y</code>. </p> <p>Specify this value only if you want to change it.</p>"""
    fully_qualified_domain_name: NotRequired[
        "capo_route_53.types.fully_qualified_domain_name.FullyQualifiedDomainName"
    ]
    """<p>Amazon Route 53 behavior depends on whether you specify a value for <code>IPAddress</code>.</p> <note> <p>If a health check already has a value for <code>IPAddress</code>, you can change the value. However, you can't update an existing health check to add or remove the value of <code>IPAddress</code>. </p> </note> <p> <b>If you specify a value for</b> <code>IPAddress</code>:</p> <p>Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of <code>FullyQualifiedDomainName</code> in the <code>Host</code> header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.</p> <p>When Route 53 checks the health of an endpoint, here is how it constructs the <code>Host</code> header:</p> <ul> <li> <p>If you specify a value of <code>80</code> for <code>Port</code> and <code>HTTP</code> or <code>HTTP_STR_MATCH</code> for <code>Type</code>, Route 53 passes the value of <code>FullyQualifiedDomainName</code> to the endpoint in the <code>Host</code> header.</p> </li> <li> <p>If you specify a value of <code>443</code> for <code>Port</code> and <code>HTTPS</code> or <code>HTTPS_STR_MATCH</code> for <code>Type</code>, Route 53 passes the value of <code>FullyQualifiedDomainName</code> to the endpoint in the <code>Host</code> header.</p> </li> <li> <p>If you specify another value for <code>Port</code> and any value except <code>TCP</code> for <code>Type</code>, Route 53 passes <i> <code>FullyQualifiedDomainName</code>:<code>Port</code> </i> to the endpoint in the <code>Host</code> header.</p> </li> </ul> <p>If you don't specify a value for <code>FullyQualifiedDomainName</code>, Route 53 substitutes the value of <code>IPAddress</code> in the <code>Host</code> header in each of the above cases.</p> <p> <b>If you don't specify a value for</b> <code>IPAddress</code>:</p> <p>If you don't specify a value for <code>IPAddress</code>, Route 53 sends a DNS request to the domain that you specify in <code>FullyQualifiedDomainName</code> at the interval you specify in <code>RequestInterval</code>. Using an IPv4 address that is returned by DNS, Route 53 then checks the health of the endpoint.</p> <p>If you don't specify a value for <code>IPAddress</code>, you can’t update the health check to remove the <code>FullyQualifiedDomainName</code>; if you don’t specify a value for <code>IPAddress</code> on creation, a <code>FullyQualifiedDomainName</code> is required.</p> <note> <p>If you don't specify a value for <code>IPAddress</code>, Route 53 uses only IPv4 to send health checks to the endpoint. If there's no resource record set with a type of A for the name that you specify for <code>FullyQualifiedDomainName</code>, the health check fails with a "DNS resolution failed" error.</p> </note> <p>If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by <code>FullyQualifiedDomainName</code>, we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of <code>FullyQualifiedDomainName</code>, specify the domain name of the server (such as <code>us-east-2-www.example.com</code>), not the name of the resource record sets (www.example.com).</p> <important> <p>In this configuration, if the value of <code>FullyQualifiedDomainName</code> matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.</p> </important> <p>In addition, if the value of <code>Type</code> is <code>HTTP</code>, <code>HTTPS</code>, <code>HTTP_STR_MATCH</code>, or <code>HTTPS_STR_MATCH</code>, Route 53 passes the value of <code>FullyQualifiedDomainName</code> in the <code>Host</code> header, as it does when you specify a value for <code>IPAddress</code>. If the value of <code>Type</code> is <code>TCP</code>, Route 53 doesn't pass a <code>Host</code> header.</p>"""
    search_string: NotRequired["capo_route_53.types.search_string.SearchString"]
    """<p>If the value of <code>Type</code> is <code>HTTP_STR_MATCH</code> or <code>HTTPS_STR_MATCH</code>, the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy. (You can't change the value of <code>Type</code> when you update a health check.)</p>"""
    failure_threshold: NotRequired[
        "capo_route_53.types.failure_threshold.FailureThreshold"
    ]
    """<p>The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html">How Amazon Route 53 Determines Whether an Endpoint Is Healthy</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>Otherwise, if you don't specify a value for <code>FailureThreshold</code>, the default value is three health checks.</p>"""
    inverted: NotRequired["capo_route_53.types.inverted.Inverted"]
    """<p>Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.</p>"""
    disabled: NotRequired["capo_route_53.types.disabled.Disabled"]
    """<p>Stops Route 53 from performing health checks. When you disable a health check, here's what happens:</p> <ul> <li> <p> <b>Health checks that check the health of endpoints:</b> Route 53 stops submitting requests to your application, server, or other resource.</p> </li> <li> <p> <b>Calculated health checks:</b> Route 53 stops aggregating the status of the referenced health checks.</p> </li> <li> <p> <b>Health checks that monitor CloudWatch alarms:</b> Route 53 stops monitoring the corresponding CloudWatch metrics.</p> </li> </ul> <p>After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. Additionally, in disabled state, you can also invert the status of the health check to route traffic differently. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted">Inverted</a>. </p> <p>Charges for a health check still apply when the health check is disabled. For more information, see <a href="http://aws.amazon.com/route53/pricing/">Amazon Route 53 Pricing</a>.</p>"""
    health_threshold: NotRequired[
        "capo_route_53.types.health_threshold.HealthThreshold"
    ]
    """<p>The number of child health checks that are associated with a <code>CALCULATED</code> health that Amazon Route 53 must consider healthy for the <code>CALCULATED</code> health check to be considered healthy. To specify the child health checks that you want to associate with a <code>CALCULATED</code> health check, use the <code>ChildHealthChecks</code> and <code>ChildHealthCheck</code> elements.</p> <p>Note the following:</p> <ul> <li> <p>If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.</p> </li> <li> <p>If you specify <code>0</code>, Route 53 always considers this health check to be healthy.</p> </li> </ul>"""
    child_health_checks: NotRequired[
        "capo_route_53.types.child_health_check_list.ChildHealthCheckList"
    ]
    """<p>A complex type that contains one <code>ChildHealthCheck</code> element for each health check that you want to associate with a <code>CALCULATED</code> health check.</p>"""
    enable_sni: NotRequired["capo_route_53.types.enable_sni.EnableSNI"]
    """<p>Specify whether you want Amazon Route 53 to send the value of <code>FullyQualifiedDomainName</code> to the endpoint in the <code>client_hello</code> message during <code>TLS</code> negotiation. This allows the endpoint to respond to <code>HTTPS</code> health check requests with the applicable SSL/TLS certificate.</p> <p>Some endpoints require that HTTPS requests include the host name in the <code>client_hello</code> message. If you don't enable SNI, the status of the health check will be SSL alert <code>handshake_failure</code>. A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.</p> <p>The SSL/TLS certificate on your endpoint includes a domain name in the <code>Common Name</code> field and possibly several more in the <code>Subject Alternative Names</code> field. One of the domain names in the certificate should match the value that you specify for <code>FullyQualifiedDomainName</code>. If the endpoint responds to the <code>client_hello</code> message with a certificate that does not include the domain name that you specified in <code>FullyQualifiedDomainName</code>, a health checker will retry the handshake. In the second attempt, the health checker will omit <code>FullyQualifiedDomainName</code> from the <code>client_hello</code> message.</p>"""
    regions: NotRequired[
        "capo_route_53.types.health_check_region_list.HealthCheckRegionList"
    ]
    """<p>A complex type that contains one <code>Region</code> element for each region that you want Amazon Route 53 health checkers to check the specified endpoint from.</p>"""
    alarm_identifier: NotRequired[
        "capo_route_53.types.alarm_identifier.AlarmIdentifier"
    ]
    """<p>A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.</p>"""
    insufficient_data_health_status: NotRequired[
        "capo_route_53.types.insufficient_data_health_status.InsufficientDataHealthStatus"
    ]
    """<p>When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:</p> <ul> <li> <p> <code>Healthy</code>: Route 53 considers the health check to be healthy.</p> </li> <li> <p> <code>Unhealthy</code>: Route 53 considers the health check to be unhealthy.</p> </li> <li> <p> <code>LastKnownStatus</code>: By default, Route 53 uses the status of the health check from the last time CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the status for the health check is healthy.</p> </li> </ul>"""
    reset_elements: NotRequired[
        "capo_route_53.types.resettable_element_name_list.ResettableElementNameList"
    ]
    """<p>A complex type that contains one <code>ResettableElementName</code> element for each element that you want to reset to the default value. Valid values for <code>ResettableElementName</code> include the following:</p> <ul> <li> <p> <code>ChildHealthChecks</code>: Amazon Route 53 resets <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-ChildHealthChecks">ChildHealthChecks</a> to null.</p> </li> <li> <p> <code>FullyQualifiedDomainName</code>: Route 53 resets <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName">FullyQualifiedDomainName</a>. to null.</p> </li> <li> <p> <code>Regions</code>: Route 53 resets the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions">Regions</a> list to the default set of regions. </p> </li> <li> <p> <code>ResourcePath</code>: Route 53 resets <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-ResourcePath">ResourcePath</a> to null.</p> </li> </ul>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateHealthCheckRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "health_check_version" in value:
        SubElement(el, "HealthCheckVersion").text = str(value["health_check_version"])
    if "ip_address" in value:
        SubElement(el, "IPAddress").text = str(value["ip_address"])
    if "port" in value:
        SubElement(el, "Port").text = str(value["port"])
    if "resource_path" in value:
        SubElement(el, "ResourcePath").text = str(value["resource_path"])
    if "fully_qualified_domain_name" in value:
        SubElement(el, "FullyQualifiedDomainName").text = str(
            value["fully_qualified_domain_name"]
        )
    if "search_string" in value:
        SubElement(el, "SearchString").text = str(value["search_string"])
    if "failure_threshold" in value:
        SubElement(el, "FailureThreshold").text = str(value["failure_threshold"])
    if "inverted" in value:
        SubElement(el, "Inverted").text = "true" if value["inverted"] else "false"
    if "disabled" in value:
        SubElement(el, "Disabled").text = "true" if value["disabled"] else "false"
    if "health_threshold" in value:
        SubElement(el, "HealthThreshold").text = str(value["health_threshold"])
    if "child_health_checks" in value:
        import capo_route_53.types.child_health_check_list

        capo_route_53.types.child_health_check_list.serialize_xml(
            value["child_health_checks"], el, "ChildHealthChecks"
        )
    if "enable_sni" in value:
        SubElement(el, "EnableSNI").text = "true" if value["enable_sni"] else "false"
    if "regions" in value:
        import capo_route_53.types.health_check_region_list

        capo_route_53.types.health_check_region_list.serialize_xml(
            value["regions"], el, "Regions"
        )
    if "alarm_identifier" in value:
        import capo_route_53.types.alarm_identifier

        capo_route_53.types.alarm_identifier.serialize_xml(
            value["alarm_identifier"], el, "AlarmIdentifier"
        )
    if "insufficient_data_health_status" in value:
        import capo_route_53.types.insufficient_data_health_status

        capo_route_53.types.insufficient_data_health_status.serialize_xml(
            value["insufficient_data_health_status"], el, "InsufficientDataHealthStatus"
        )
    if "reset_elements" in value:
        import capo_route_53.types.resettable_element_name_list

        capo_route_53.types.resettable_element_name_list.serialize_xml(
            value["reset_elements"], el, "ResetElements"
        )


def deserialize_xml(el: Element) -> UpdateHealthCheckRequest:
    out: UpdateHealthCheckRequest = {}  # type: ignore[typeddict-item]
    child_health_check_version = el.find("HealthCheckVersion")
    if child_health_check_version is not None:
        out["health_check_version"] = int(child_health_check_version.text or "")
    child_ip_address = el.find("IPAddress")
    if child_ip_address is not None:
        out["ip_address"] = str(child_ip_address.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_resource_path = el.find("ResourcePath")
    if child_resource_path is not None:
        out["resource_path"] = str(child_resource_path.text or "")
    child_fully_qualified_domain_name = el.find("FullyQualifiedDomainName")
    if child_fully_qualified_domain_name is not None:
        out["fully_qualified_domain_name"] = str(
            child_fully_qualified_domain_name.text or ""
        )
    child_search_string = el.find("SearchString")
    if child_search_string is not None:
        out["search_string"] = str(child_search_string.text or "")
    child_failure_threshold = el.find("FailureThreshold")
    if child_failure_threshold is not None:
        out["failure_threshold"] = int(child_failure_threshold.text or "")
    child_inverted = el.find("Inverted")
    if child_inverted is not None:
        out["inverted"] = (child_inverted.text or "").lower() == "true"
    child_disabled = el.find("Disabled")
    if child_disabled is not None:
        out["disabled"] = (child_disabled.text or "").lower() == "true"
    child_health_threshold = el.find("HealthThreshold")
    if child_health_threshold is not None:
        out["health_threshold"] = int(child_health_threshold.text or "")
    child_child_health_checks = el.find("ChildHealthChecks")
    if child_child_health_checks is not None:
        import capo_route_53.types.child_health_check_list

        out["child_health_checks"] = (
            capo_route_53.types.child_health_check_list.deserialize_xml(
                child_child_health_checks
            )
        )
    child_enable_sni = el.find("EnableSNI")
    if child_enable_sni is not None:
        out["enable_sni"] = (child_enable_sni.text or "").lower() == "true"
    child_regions = el.find("Regions")
    if child_regions is not None:
        import capo_route_53.types.health_check_region_list

        out["regions"] = capo_route_53.types.health_check_region_list.deserialize_xml(
            child_regions
        )
    child_alarm_identifier = el.find("AlarmIdentifier")
    if child_alarm_identifier is not None:
        import capo_route_53.types.alarm_identifier

        out["alarm_identifier"] = capo_route_53.types.alarm_identifier.deserialize_xml(
            child_alarm_identifier
        )
    child_insufficient_data_health_status = el.find("InsufficientDataHealthStatus")
    if child_insufficient_data_health_status is not None:
        import capo_route_53.types.insufficient_data_health_status

        out["insufficient_data_health_status"] = (
            capo_route_53.types.insufficient_data_health_status.deserialize_xml(
                child_insufficient_data_health_status
            )
        )
    child_reset_elements = el.find("ResetElements")
    if child_reset_elements is not None:
        import capo_route_53.types.resettable_element_name_list

        out["reset_elements"] = (
            capo_route_53.types.resettable_element_name_list.deserialize_xml(
                child_reset_elements
            )
        )
    return out
