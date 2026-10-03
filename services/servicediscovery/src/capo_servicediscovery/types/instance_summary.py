"""Generated from Smithy shape ``com.amazonaws.servicediscovery#InstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.attributes
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.resource_id


class InstanceSummary(TypedDict, closed=True):
    id: NotRequired["capo_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID for an instance that you created by using a specified service.</p>"""
    attributes: NotRequired["capo_servicediscovery.types.attributes.Attributes"]
    """<p>A string map that contains the following information:</p> <ul> <li> <p>The attributes that are associated with the instance. </p> </li> <li> <p>For each attribute, the applicable value.</p> </li> </ul> <p>Supported attribute keys include the following:</p> <dl> <dt>AWS_ALIAS_DNS_NAME</dt> <dd> <p>For an alias record that routes traffic to an Elastic Load Balancing load balancer, the DNS name that's associated with the load balancer. </p> </dd> <dt>AWS_EC2_INSTANCE_ID (HTTP namespaces only)</dt> <dd> <p>The Amazon EC2 instance ID for the instance. When the <code>AWS_EC2_INSTANCE_ID</code> attribute is specified, then the <code>AWS_INSTANCE_IPV4</code> attribute contains the primary private IPv4 address.</p> </dd> <dt>AWS_INIT_HEALTH_STATUS</dt> <dd> <p>If the service configuration includes <code>HealthCheckCustomConfig</code>, you can optionally use <code>AWS_INIT_HEALTH_STATUS</code> to specify the initial status of the custom health check, <code>HEALTHY</code> or <code>UNHEALTHY</code>. If you don't specify a value for <code>AWS_INIT_HEALTH_STATUS</code>, the initial status is <code>HEALTHY</code>.</p> </dd> <dt>AWS_INSTANCE_CNAME</dt> <dd> <p>For a <code>CNAME</code> record, the domain name that Route 53 returns in response to DNS queries (for example, <code>example.com</code>).</p> </dd> <dt>AWS_INSTANCE_IPV4</dt> <dd> <p>For an <code>A</code> record, the IPv4 address that Route 53 returns in response to DNS queries (for example, <code>192.0.2.44</code>).</p> </dd> <dt>AWS_INSTANCE_IPV6</dt> <dd> <p>For an <code>AAAA</code> record, the IPv6 address that Route 53 returns in response to DNS queries (for example, <code>2001:0db8:85a3:0000:0000:abcd:0001:2345</code>).</p> </dd> <dt>AWS_INSTANCE_PORT</dt> <dd> <p>For an <code>SRV</code> record, the value that Route 53 returns for the port. In addition, if the service includes <code>HealthCheckConfig</code>, the port on the endpoint that Route 53 sends requests to.</p> </dd> </dl>"""
    created_by_account: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that registered the instance. If this isn't your account ID, it's the ID of the account that shared the namespace with your account or the ID of another account with which the namespace has been shared. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
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


def deserialize_aws_json_1_1(data: dict) -> InstanceSummary:
    out: InstanceSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
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
