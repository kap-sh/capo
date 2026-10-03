"""Generated from Smithy shape ``com.amazonaws.servicediscovery#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.attributes
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.resource_id


class Instance(TypedDict, closed=True):
    id: "capo_servicediscovery.types.resource_id.ResourceId"
    """<p>An identifier that you want to associate with the instance. Note the following:</p> <ul> <li> <p>If the service that's specified by <code>ServiceId</code> includes settings for an <code>SRV</code> record, the value of <code>InstanceId</code> is automatically included as part of the value for the <code>SRV</code> record. For more information, see <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsRecord.html#cloudmap-Type-DnsRecord-Type">DnsRecord > Type</a>.</p> </li> <li> <p>You can use this value to update an existing instance.</p> </li> <li> <p>To register a new instance, you must specify a value that's unique among instances that you register by using the same service. </p> </li> <li> <p>If you specify an existing <code>InstanceId</code> and <code>ServiceId</code>, Cloud Map updates the existing DNS records. If there's also an existing health check, Cloud Map deletes the old health check and creates a new one. </p> <note> <p>The health check isn't deleted immediately, so it will still appear for a while if you submit a <code>ListHealthChecks</code> request, for example.</p> </note> </li> </ul>"""
    creator_request_id: NotRequired[
        "capo_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>A unique string that identifies the request and that allows failed <code>RegisterInstance</code> requests to be retried without the risk of executing the operation twice. You must use a unique <code>CreatorRequestId</code> string every time you submit a <code>RegisterInstance</code> request if you're registering additional instances for the same namespace and service. <code>CreatorRequestId</code> can be any unique string (for example, a date/time stamp).</p>"""
    attributes: NotRequired["capo_servicediscovery.types.attributes.Attributes"]
    """<p>A string map that contains the following information for the service that you specify in <code>ServiceId</code>:</p> <ul> <li> <p>The attributes that apply to the records that are defined in the service. </p> </li> <li> <p>For each attribute, the applicable value.</p> </li> </ul> <note> <p>Do not include sensitive information in the attributes if the namespace is discoverable by public DNS queries.</p> </note> <p>Supported attribute keys include the following:</p> <dl> <dt>AWS_ALIAS_DNS_NAME</dt> <dd> <p>If you want Cloud Map to create a Route 53 alias record that routes traffic to an Elastic Load Balancing load balancer, specify the DNS name that's associated with the load balancer. For information about how to get the DNS name, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-DNSName">AliasTarget->DNSName</a> in the <i>Route 53 API Reference</i>.</p> <p>Note the following:</p> <ul> <li> <p>The configuration for the service that's specified by <code>ServiceId</code> must include settings for an <code>A</code> record, an <code>AAAA</code> record, or both.</p> </li> <li> <p>In the service that's specified by <code>ServiceId</code>, the value of <code>RoutingPolicy</code> must be <code>WEIGHTED</code>.</p> </li> <li> <p>If the service that's specified by <code>ServiceId</code> includes <code>HealthCheckConfig</code> settings, Cloud Map creates the health check, but it won't associate the health check with the alias record.</p> </li> <li> <p>Auto naming currently doesn't support creating alias records that route traffic to Amazon Web Services resources other than ELB load balancers.</p> </li> <li> <p>If you specify a value for <code>AWS_ALIAS_DNS_NAME</code>, don't specify values for any of the <code>AWS_INSTANCE</code> attributes.</p> </li> </ul> </dd> <dt>AWS_EC2_INSTANCE_ID</dt> <dd> <p> <i>HTTP namespaces only.</i> The Amazon EC2 instance ID for the instance. The <code>AWS_INSTANCE_IPV4</code> attribute contains the primary private IPv4 address.</p> </dd> <dt>AWS_INIT_HEALTH_STATUS</dt> <dd> <p>If the service configuration includes <code>HealthCheckCustomConfig</code>, you can optionally use <code>AWS_INIT_HEALTH_STATUS</code> to specify the initial status of the custom health check, <code>HEALTHY</code> or <code>UNHEALTHY</code>. If you don't specify a value for <code>AWS_INIT_HEALTH_STATUS</code>, the initial status is <code>HEALTHY</code>.</p> </dd> <dt>AWS_INSTANCE_CNAME</dt> <dd> <p>If the service configuration includes a <code>CNAME</code> record, the domain name that you want Route 53 to return in response to DNS queries (for example, <code>example.com</code>).</p> <p>This value is required if the service specified by <code>ServiceId</code> includes settings for an <code>CNAME</code> record.</p> </dd> <dt>AWS_INSTANCE_IPV4</dt> <dd> <p>If the service configuration includes an <code>A</code> record, the IPv4 address that you want Route 53 to return in response to DNS queries (for example, <code>192.0.2.44</code>).</p> <p>This value is required if the service specified by <code>ServiceId</code> includes settings for an <code>A</code> record. If the service includes settings for an <code>SRV</code> record, you must specify a value for <code>AWS_INSTANCE_IPV4</code>, <code>AWS_INSTANCE_IPV6</code>, or both.</p> </dd> <dt>AWS_INSTANCE_IPV6</dt> <dd> <p>If the service configuration includes an <code>AAAA</code> record, the IPv6 address that you want Route 53 to return in response to DNS queries (for example, <code>2001:0db8:85a3:0000:0000:abcd:0001:2345</code>).</p> <p>This value is required if the service specified by <code>ServiceId</code> includes settings for an <code>AAAA</code> record. If the service includes settings for an <code>SRV</code> record, you must specify a value for <code>AWS_INSTANCE_IPV4</code>, <code>AWS_INSTANCE_IPV6</code>, or both.</p> </dd> <dt>AWS_INSTANCE_PORT</dt> <dd> <p>If the service includes an <code>SRV</code> record, the value that you want Route 53 to return for the port.</p> <p>If the service includes <code>HealthCheckConfig</code>, the port on the endpoint that you want Route 53 to send requests to. </p> <p>This value is required if you specified settings for an <code>SRV</code> record or a Route 53 health check when you created the service.</p> </dd> </dl>"""
    created_by_account: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that registered the instance. If this isn't your account ID, it's the ID of the account that shared the namespace with your account or the ID of another account with which the namespace has been shared. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Instance) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "attributes" in value:
        import capo_servicediscovery.types.attributes

        out["Attributes"] = (
            capo_servicediscovery.types.attributes.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "created_by_account" in value:
        out["CreatedByAccount"] = value["created_by_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Instance.id required")
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("Attributes") is not None:
        import capo_servicediscovery.types.attributes

        out["attributes"] = (
            capo_servicediscovery.types.attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if data.get("CreatedByAccount") is not None:
        out["created_by_account"] = data["CreatedByAccount"]
    return out
