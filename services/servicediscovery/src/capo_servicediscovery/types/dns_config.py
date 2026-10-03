"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DnsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.dns_record_list
    import capo_servicediscovery.types.resource_id
    import capo_servicediscovery.types.routing_policy


class DnsConfig(TypedDict, closed=True):
    namespace_id: NotRequired["capo_servicediscovery.types.resource_id.ResourceId"]
    """<p> <i>Use NamespaceId in <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_Service.html">Service</a> instead.</i> </p> <p>The ID of the namespace to use for DNS configuration.</p>"""
    routing_policy: NotRequired[
        "capo_servicediscovery.types.routing_policy.RoutingPolicy"
    ]
    """<p>The routing policy that you want to apply to all Route 53 DNS records that Cloud Map creates when you register an instance and specify this service.</p> <note> <p>If you want to use this service to register instances that create alias records, specify <code>WEIGHTED</code> for the routing policy.</p> </note> <p>You can specify the following values:</p> <dl> <dt>MULTIVALUE</dt> <dd> <p>If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.</p> <p>For example, suppose that the service includes configurations for one <code>A</code> record and a health check. You use the service to register 10 instances. Route 53 responds to DNS queries with IP addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route 53 responds to every DNS query with the IP addresses for all of the healthy instances.</p> <p>If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the values for up to eight instances.</p> <p>For more information about the multivalue routing policy, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue">Multivalue Answer Routing</a> in the <i>Route 53 Developer Guide</i>.</p> </dd> <dt>WEIGHTED</dt> <dd> <p>Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service. Currently, all records have the same weight, so you can't route more or less traffic to any instances.</p> <p>For example, suppose that the service includes configurations for one <code>A</code> record and a health check. You use the service to register 10 instances. Route 53 responds to DNS queries with the IP address for one randomly selected instance from among the healthy instances. If no instances are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.</p> <p>If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the applicable value for one randomly selected instance.</p> <p>For more information about the weighted routing policy, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted">Weighted Routing</a> in the <i>Route 53 Developer Guide</i>.</p> </dd> </dl>"""
    dns_records: "capo_servicediscovery.types.dns_record_list.DnsRecordList"
    """<p>An array that contains one <code>DnsRecord</code> object for each Route 53 DNS record that you want Cloud Map to create when you register an instance.</p> <important> <p>The record type of a service specified in a <code>DnsRecord</code> object can't be updated. To change a record type, you need to delete the service and recreate it with a new <code>DnsConfig</code>.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsConfig) -> dict:
    out: dict = {}
    if "namespace_id" in value:
        out["NamespaceId"] = value["namespace_id"]
    if "routing_policy" in value:
        import capo_servicediscovery.types.routing_policy

        out["RoutingPolicy"] = (
            capo_servicediscovery.types.routing_policy.serialize_aws_json_1_1(
                value["routing_policy"]
            )
        )
    import capo_servicediscovery.types.dns_record_list

    out["DnsRecords"] = (
        capo_servicediscovery.types.dns_record_list.serialize_aws_json_1_1(
            value["dns_records"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsConfig:
    out: DnsConfig = {}  # type: ignore[typeddict-item]
    if data.get("NamespaceId") is not None:
        out["namespace_id"] = data["NamespaceId"]
    if data.get("RoutingPolicy") is not None:
        import capo_servicediscovery.types.routing_policy

        out["routing_policy"] = (
            capo_servicediscovery.types.routing_policy.deserialize_aws_json_1_1(
                data["RoutingPolicy"]
            )
        )
    if data.get("DnsRecords") is not None:
        import capo_servicediscovery.types.dns_record_list

        out["dns_records"] = (
            capo_servicediscovery.types.dns_record_list.deserialize_aws_json_1_1(
                data["DnsRecords"]
            )
        )
    else:
        raise DeserializationError("DnsConfig.dns_records required")
    return out
