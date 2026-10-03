"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.dns_config
    import capo_servicediscovery.types.health_check_config
    import capo_servicediscovery.types.health_check_custom_config
    import capo_servicediscovery.types.resource_count
    import capo_servicediscovery.types.resource_description
    import capo_servicediscovery.types.resource_id
    import capo_servicediscovery.types.service_name
    import capo_servicediscovery.types.service_type
    import capo_servicediscovery.types.timestamp


class ServiceSummary(TypedDict, closed=True):
    id: NotRequired["capo_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID that Cloud Map assigned to the service when you created it.</p>"""
    arn: NotRequired["capo_servicediscovery.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that Cloud Map assigns to the service when you create it.</p>"""
    resource_owner: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that created the namespace with which the service is associated. If this isn't your account ID, it is the ID of the account that shared the namespace with your account. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    name: NotRequired["capo_servicediscovery.types.service_name.ServiceName"]
    """<p>The name of the service.</p>"""
    type: NotRequired["capo_servicediscovery.types.service_type.ServiceType"]
    """<p>Describes the systems that can be used to discover the service instances.</p> <dl> <dt>DNS_HTTP</dt> <dd> <p>The service instances can be discovered using either DNS queries or the <code>DiscoverInstances</code> API operation.</p> </dd> <dt>HTTP</dt> <dd> <p>The service instances can only be discovered using the <code>DiscoverInstances</code> API operation.</p> </dd> <dt>DNS</dt> <dd> <p>Reserved.</p> </dd> </dl>"""
    description: NotRequired[
        "capo_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>The description that you specify when you create the service.</p>"""
    instance_count: NotRequired[
        "capo_servicediscovery.types.resource_count.ResourceCount"
    ]
    """<p>The number of instances that are currently associated with the service. Instances that were previously associated with the service but that are deleted aren't included in the count. The count might not reflect pending registrations and deregistrations.</p>"""
    dns_config: NotRequired["capo_servicediscovery.types.dns_config.DnsConfig"]
    """<p>Information about the Route 53 DNS records that you want Cloud Map to create when you register an instance.</p>"""
    health_check_config: NotRequired[
        "capo_servicediscovery.types.health_check_config.HealthCheckConfig"
    ]
    """<p> <i>Public DNS and HTTP namespaces only.</i> Settings for an optional health check. If you specify settings for a health check, Cloud Map associates the health check with the records that you specify in <code>DnsConfig</code>.</p>"""
    health_check_custom_config: NotRequired[
        "capo_servicediscovery.types.health_check_custom_config.HealthCheckCustomConfig"
    ]
    """<p>Information about an optional custom health check. A custom health check, which requires that you use a third-party health checker to evaluate the health of your resources, is useful in the following circumstances:</p> <ul> <li> <p>You can't use a health check that's defined by <code>HealthCheckConfig</code> because the resource isn't available over the internet. For example, you can use a custom health check when the instance is in an Amazon VPC. (To check the health of resources in a VPC, the health checker must also be in the VPC.)</p> </li> <li> <p>You want to use a third-party health checker regardless of where your resources are located.</p> </li> </ul> <important> <p>If you specify a health check configuration, you can specify either <code>HealthCheckCustomConfig</code> or <code>HealthCheckConfig</code> but not both.</p> </important>"""
    create_date: NotRequired["capo_servicediscovery.types.timestamp.Timestamp"]
    """<p>The date and time that the service was created.</p>"""
    created_by_account: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that created the service. If this isn't your account ID, it is the account ID of the namespace owner or of another account with which the namespace has been shared. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "resource_owner" in value:
        out["ResourceOwner"] = value["resource_owner"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_servicediscovery.types.service_type

        out["Type"] = capo_servicediscovery.types.service_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
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
    if "create_date" in value:
        import capo_servicediscovery.types.timestamp

        out["CreateDate"] = (
            capo_servicediscovery.types.timestamp.serialize_aws_json_1_1(
                value["create_date"]
            )
        )
    if "created_by_account" in value:
        out["CreatedByAccount"] = value["created_by_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceSummary:
    out: ServiceSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ResourceOwner") is not None:
        out["resource_owner"] = data["ResourceOwner"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_servicediscovery.types.service_type

        out["type"] = capo_servicediscovery.types.service_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
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
    if data.get("CreateDate") is not None:
        import capo_servicediscovery.types.timestamp

        out["create_date"] = (
            capo_servicediscovery.types.timestamp.deserialize_aws_json_1_1(
                data["CreateDate"]
            )
        )
    if data.get("CreatedByAccount") is not None:
        out["created_by_account"] = data["CreatedByAccount"]
    return out
