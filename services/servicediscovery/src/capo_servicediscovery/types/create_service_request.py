"""Generated from Smithy shape ``com.amazonaws.servicediscovery#CreateServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.dns_config
    import capo_servicediscovery.types.health_check_config
    import capo_servicediscovery.types.health_check_custom_config
    import capo_servicediscovery.types.resource_description
    import capo_servicediscovery.types.resource_id
    import capo_servicediscovery.types.service_name
    import capo_servicediscovery.types.service_type_option
    import capo_servicediscovery.types.tag_list


class CreateServiceRequest(TypedDict, closed=True):
    name: "capo_servicediscovery.types.service_name.ServiceName"
    """<p>The name that you want to assign to the service.</p> <note> <p>Do not include sensitive information in the name if the namespace is discoverable by public DNS queries.</p> </note> <p>If you want Cloud Map to create an <code>SRV</code> record when you register an instance and you're using a system that requires a specific <code>SRV</code> format, such as <a href="http://www.haproxy.org/">HAProxy</a>, specify the following for <code>Name</code>:</p> <ul> <li> <p>Start the name with an underscore (_), such as <code>_exampleservice</code>.</p> </li> <li> <p>End the name with <i>._protocol</i>, such as <code>._tcp</code>.</p> </li> </ul> <p>When you register an instance, Cloud Map creates an <code>SRV</code> record and assigns a name to the record by concatenating the service name and the namespace name (for example,</p> <p> <code>_exampleservice._tcp.example.com</code>).</p> <note> <p>For services that are accessible by DNS queries, you can't create multiple services with names that differ only by case (such as EXAMPLE and example). Otherwise, these services have the same DNS name and can't be distinguished. However, if you use a namespace that's only accessible by API calls, then you can create services that with names that differ only by case.</p> </note>"""
    namespace_id: NotRequired["capo_servicediscovery.types.arn.Arn"]
    """<p>The ID or Amazon Resource Name (ARN) of the namespace that you want to use to create the service. For namespaces shared with your Amazon Web Services account, specify the namespace ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    creator_request_id: NotRequired[
        "capo_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>A unique string that identifies the request and that allows failed <code>CreateService</code> requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string (for example, a date/timestamp).</p>"""
    description: NotRequired[
        "capo_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>A description for the service.</p>"""
    dns_config: NotRequired["capo_servicediscovery.types.dns_config.DnsConfig"]
    """<p>A complex type that contains information about the Amazon Route 53 records that you want Cloud Map to create when you register an instance. </p>"""
    health_check_config: NotRequired[
        "capo_servicediscovery.types.health_check_config.HealthCheckConfig"
    ]
    """<p> <i>Public DNS and HTTP namespaces only.</i> A complex type that contains settings for an optional Route 53 health check. If you specify settings for a health check, Cloud Map associates the health check with all the Route 53 DNS records that you specify in <code>DnsConfig</code>.</p> <important> <p>If you specify a health check configuration, you can specify either <code>HealthCheckCustomConfig</code> or <code>HealthCheckConfig</code> but not both.</p> </important> <p>For information about the charges for health checks, see <a href="http://aws.amazon.com/cloud-map/pricing/">Cloud Map Pricing</a>.</p>"""
    health_check_custom_config: NotRequired[
        "capo_servicediscovery.types.health_check_custom_config.HealthCheckCustomConfig"
    ]
    """<p>A complex type that contains information about an optional custom health check.</p> <important> <p>If you specify a health check configuration, you can specify either <code>HealthCheckCustomConfig</code> or <code>HealthCheckConfig</code> but not both.</p> </important> <p>You can't add, update, or delete a <code>HealthCheckCustomConfig</code> configuration from an existing service.</p>"""
    tags: NotRequired["capo_servicediscovery.types.tag_list.TagList"]
    """<p>The tags to add to the service. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.</p>"""
    type: NotRequired[
        "capo_servicediscovery.types.service_type_option.ServiceTypeOption"
    ]
    """<p>If present, specifies that the service instances are only discoverable using the <code>DiscoverInstances</code> API operation. No DNS records is registered for the service instances. The only valid value is <code>HTTP</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateServiceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "namespace_id" in value:
        out["NamespaceId"] = value["namespace_id"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "dns_config" in value:
        import capo_servicediscovery.types.dns_config

        out["DnsConfig"] = (
            capo_servicediscovery.types.dns_config.serialize_aws_json_1_1(
                value["dns_config"]
            )
        )
    if "health_check_config" in value:
        import capo_servicediscovery.types.health_check_config

        out["HealthCheckConfig"] = (
            capo_servicediscovery.types.health_check_config.serialize_aws_json_1_1(
                value["health_check_config"]
            )
        )
    if "health_check_custom_config" in value:
        import capo_servicediscovery.types.health_check_custom_config

        out["HealthCheckCustomConfig"] = (
            capo_servicediscovery.types.health_check_custom_config.serialize_aws_json_1_1(
                value["health_check_custom_config"]
            )
        )
    if "tags" in value:
        import capo_servicediscovery.types.tag_list

        out["Tags"] = capo_servicediscovery.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "type" in value:
        import capo_servicediscovery.types.service_type_option

        out["Type"] = (
            capo_servicediscovery.types.service_type_option.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateServiceRequest:
    out: CreateServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateServiceRequest.name required")
    if data.get("NamespaceId") is not None:
        out["namespace_id"] = data["NamespaceId"]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DnsConfig") is not None:
        import capo_servicediscovery.types.dns_config

        out["dns_config"] = (
            capo_servicediscovery.types.dns_config.deserialize_aws_json_1_1(
                data["DnsConfig"]
            )
        )
    if data.get("HealthCheckConfig") is not None:
        import capo_servicediscovery.types.health_check_config

        out["health_check_config"] = (
            capo_servicediscovery.types.health_check_config.deserialize_aws_json_1_1(
                data["HealthCheckConfig"]
            )
        )
    if data.get("HealthCheckCustomConfig") is not None:
        import capo_servicediscovery.types.health_check_custom_config

        out["health_check_custom_config"] = (
            capo_servicediscovery.types.health_check_custom_config.deserialize_aws_json_1_1(
                data["HealthCheckCustomConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_servicediscovery.types.tag_list

        out["tags"] = capo_servicediscovery.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("Type") is not None:
        import capo_servicediscovery.types.service_type_option

        out["type"] = (
            capo_servicediscovery.types.service_type_option.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
