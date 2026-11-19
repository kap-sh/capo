"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorTopContributorsRow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.additional_flow_info
    import capo_networkflowmonitor.types.availability_zone
    import capo_networkflowmonitor.types.aws_region
    import capo_networkflowmonitor.types.destination_category
    import capo_networkflowmonitor.types.instance_arn
    import capo_networkflowmonitor.types.instance_id
    import capo_networkflowmonitor.types.kubernetes_metadata
    import capo_networkflowmonitor.types.subnet_arn
    import capo_networkflowmonitor.types.subnet_id
    import capo_networkflowmonitor.types.traversed_constructs_list
    import capo_networkflowmonitor.types.vpc_arn
    import capo_networkflowmonitor.types.vpc_id


class MonitorTopContributorsRow(TypedDict, closed=True):
    local_ip: NotRequired["str"]
    """<p>The IP address of the local resource for a top contributor network flow.</p>"""
    snat_ip: NotRequired["str"]
    """<p>The secure network address translation (SNAT) IP address for a top contributor network flow.</p>"""
    local_instance_id: NotRequired[
        "capo_networkflowmonitor.types.instance_id.InstanceId"
    ]
    """<p>The instance identifier for the local resource for a top contributor network flow.</p>"""
    local_vpc_id: NotRequired["capo_networkflowmonitor.types.vpc_id.VpcId"]
    """<p>The VPC ID for a top contributor network flow for the local resource.</p>"""
    local_region: NotRequired["capo_networkflowmonitor.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region for the local resource for a top contributor network flow.</p>"""
    local_az: NotRequired[
        "capo_networkflowmonitor.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone for the local resource for a top contributor network flow.</p>"""
    local_subnet_id: NotRequired["capo_networkflowmonitor.types.subnet_id.SubnetId"]
    """<p>The subnet ID for the local resource for a top contributor network flow.</p>"""
    target_port: NotRequired["int"]
    """<p>The target port.</p>"""
    destination_category: NotRequired[
        "capo_networkflowmonitor.types.destination_category.DestinationCategory"
    ]
    """<p>The destination category for a top contributors row. Destination categories can be one of the following: </p> <ul> <li> <p> <code>INTRA_AZ</code>: Top contributor network flows within a single Availability Zone</p> </li> <li> <p> <code>INTER_AZ</code>: Top contributor network flows between Availability Zones</p> </li> <li> <p> <code>INTER_REGION</code>: Top contributor network flows between Regions (to the edge of another Region)</p> </li> <li> <p> <code>INTER_VPC</code>: Top contributor network flows between VPCs</p> </li> <li> <p> <code>AWS_SERVICES</code>: Top contributor network flows to or from Amazon Web Services services</p> </li> <li> <p> <code>UNCLASSIFIED</code>: Top contributor network flows that do not have a bucket classification</p> </li> </ul>"""
    remote_vpc_id: NotRequired["capo_networkflowmonitor.types.vpc_id.VpcId"]
    """<p>The VPC ID for a top contributor network flow for the remote resource.</p>"""
    remote_region: NotRequired["capo_networkflowmonitor.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region for the remote resource for a top contributor network flow.</p>"""
    remote_az: NotRequired[
        "capo_networkflowmonitor.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone for the remote resource for a top contributor network flow.</p>"""
    remote_subnet_id: NotRequired["capo_networkflowmonitor.types.subnet_id.SubnetId"]
    """<p>The subnet ID for the remote resource for a top contributor network flow.</p>"""
    remote_instance_id: NotRequired[
        "capo_networkflowmonitor.types.instance_id.InstanceId"
    ]
    """<p>The instance identifier for the remote resource for a top contributor network flow.</p>"""
    remote_ip: NotRequired["str"]
    """<p>The IP address of the remote resource for a top contributor network flow.</p>"""
    dnat_ip: NotRequired["str"]
    """<p>The destination network address translation (DNAT) IP address for a top contributor network flow.</p>"""
    value: NotRequired["int"]
    """<p>The value of the metric for a top contributor network flow.</p>"""
    traversed_constructs: NotRequired[
        "capo_networkflowmonitor.types.traversed_constructs_list.TraversedConstructsList"
    ]
    """<p>The constructs traversed by a network flow.</p>"""
    kubernetes_metadata: NotRequired[
        "capo_networkflowmonitor.types.kubernetes_metadata.KubernetesMetadata"
    ]
    """<p>Meta data about Kubernetes resources.</p>"""
    local_instance_arn: NotRequired[
        "capo_networkflowmonitor.types.instance_arn.InstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a local resource.</p>"""
    local_subnet_arn: NotRequired["capo_networkflowmonitor.types.subnet_arn.SubnetArn"]
    """<p>The Amazon Resource Name (ARN) of a local subnet.</p>"""
    local_vpc_arn: NotRequired["capo_networkflowmonitor.types.vpc_arn.VpcArn"]
    """<p>The Amazon Resource Name (ARN) of a local VPC.</p>"""
    remote_instance_arn: NotRequired[
        "capo_networkflowmonitor.types.instance_arn.InstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a remote resource.</p>"""
    remote_subnet_arn: NotRequired["capo_networkflowmonitor.types.subnet_arn.SubnetArn"]
    """<p>The Amazon Resource Name (ARN) of a remote subnet.</p>"""
    remote_vpc_arn: NotRequired["capo_networkflowmonitor.types.vpc_arn.VpcArn"]
    """<p>The Amazon Resource Name (ARN) of a remote VPC.</p>"""
    additional_flow_info: NotRequired[
        "capo_networkflowmonitor.types.additional_flow_info.AdditionalFlowInfo"
    ]
    """<p>Additional information about the network flow, such as the network that the remote address belongs to and the location of the client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorTopContributorsRow) -> dict:
    out: dict = {}
    if "local_ip" in value:
        out["localIp"] = value["local_ip"]
    if "snat_ip" in value:
        out["snatIp"] = value["snat_ip"]
    if "local_instance_id" in value:
        out["localInstanceId"] = value["local_instance_id"]
    if "local_vpc_id" in value:
        out["localVpcId"] = value["local_vpc_id"]
    if "local_region" in value:
        out["localRegion"] = value["local_region"]
    if "local_az" in value:
        out["localAz"] = value["local_az"]
    if "local_subnet_id" in value:
        out["localSubnetId"] = value["local_subnet_id"]
    if "target_port" in value:
        out["targetPort"] = value["target_port"]
    if "destination_category" in value:
        import capo_networkflowmonitor.types.destination_category

        out["destinationCategory"] = (
            capo_networkflowmonitor.types.destination_category.serialize_json(
                value["destination_category"]
            )
        )
    if "remote_vpc_id" in value:
        out["remoteVpcId"] = value["remote_vpc_id"]
    if "remote_region" in value:
        out["remoteRegion"] = value["remote_region"]
    if "remote_az" in value:
        out["remoteAz"] = value["remote_az"]
    if "remote_subnet_id" in value:
        out["remoteSubnetId"] = value["remote_subnet_id"]
    if "remote_instance_id" in value:
        out["remoteInstanceId"] = value["remote_instance_id"]
    if "remote_ip" in value:
        out["remoteIp"] = value["remote_ip"]
    if "dnat_ip" in value:
        out["dnatIp"] = value["dnat_ip"]
    if "value" in value:
        out["value"] = value["value"]
    if "traversed_constructs" in value:
        import capo_networkflowmonitor.types.traversed_constructs_list

        out["traversedConstructs"] = (
            capo_networkflowmonitor.types.traversed_constructs_list.serialize_json(
                value["traversed_constructs"]
            )
        )
    if "kubernetes_metadata" in value:
        import capo_networkflowmonitor.types.kubernetes_metadata

        out["kubernetesMetadata"] = (
            capo_networkflowmonitor.types.kubernetes_metadata.serialize_json(
                value["kubernetes_metadata"]
            )
        )
    if "local_instance_arn" in value:
        out["localInstanceArn"] = value["local_instance_arn"]
    if "local_subnet_arn" in value:
        out["localSubnetArn"] = value["local_subnet_arn"]
    if "local_vpc_arn" in value:
        out["localVpcArn"] = value["local_vpc_arn"]
    if "remote_instance_arn" in value:
        out["remoteInstanceArn"] = value["remote_instance_arn"]
    if "remote_subnet_arn" in value:
        out["remoteSubnetArn"] = value["remote_subnet_arn"]
    if "remote_vpc_arn" in value:
        out["remoteVpcArn"] = value["remote_vpc_arn"]
    if "additional_flow_info" in value:
        import capo_networkflowmonitor.types.additional_flow_info

        out["additionalFlowInfo"] = (
            capo_networkflowmonitor.types.additional_flow_info.serialize_json(
                value["additional_flow_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> MonitorTopContributorsRow:
    out: MonitorTopContributorsRow = {}  # type: ignore[typeddict-item]
    if data.get("localIp") is not None:
        out["local_ip"] = data["localIp"]
    if data.get("snatIp") is not None:
        out["snat_ip"] = data["snatIp"]
    if data.get("localInstanceId") is not None:
        out["local_instance_id"] = data["localInstanceId"]
    if data.get("localVpcId") is not None:
        out["local_vpc_id"] = data["localVpcId"]
    if data.get("localRegion") is not None:
        out["local_region"] = data["localRegion"]
    if data.get("localAz") is not None:
        out["local_az"] = data["localAz"]
    if data.get("localSubnetId") is not None:
        out["local_subnet_id"] = data["localSubnetId"]
    if data.get("targetPort") is not None:
        out["target_port"] = data["targetPort"]
    if data.get("destinationCategory") is not None:
        import capo_networkflowmonitor.types.destination_category

        out["destination_category"] = (
            capo_networkflowmonitor.types.destination_category.deserialize_json(
                data["destinationCategory"]
            )
        )
    if data.get("remoteVpcId") is not None:
        out["remote_vpc_id"] = data["remoteVpcId"]
    if data.get("remoteRegion") is not None:
        out["remote_region"] = data["remoteRegion"]
    if data.get("remoteAz") is not None:
        out["remote_az"] = data["remoteAz"]
    if data.get("remoteSubnetId") is not None:
        out["remote_subnet_id"] = data["remoteSubnetId"]
    if data.get("remoteInstanceId") is not None:
        out["remote_instance_id"] = data["remoteInstanceId"]
    if data.get("remoteIp") is not None:
        out["remote_ip"] = data["remoteIp"]
    if data.get("dnatIp") is not None:
        out["dnat_ip"] = data["dnatIp"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("traversedConstructs") is not None:
        import capo_networkflowmonitor.types.traversed_constructs_list

        out["traversed_constructs"] = (
            capo_networkflowmonitor.types.traversed_constructs_list.deserialize_json(
                data["traversedConstructs"]
            )
        )
    if data.get("kubernetesMetadata") is not None:
        import capo_networkflowmonitor.types.kubernetes_metadata

        out["kubernetes_metadata"] = (
            capo_networkflowmonitor.types.kubernetes_metadata.deserialize_json(
                data["kubernetesMetadata"]
            )
        )
    if data.get("localInstanceArn") is not None:
        out["local_instance_arn"] = data["localInstanceArn"]
    if data.get("localSubnetArn") is not None:
        out["local_subnet_arn"] = data["localSubnetArn"]
    if data.get("localVpcArn") is not None:
        out["local_vpc_arn"] = data["localVpcArn"]
    if data.get("remoteInstanceArn") is not None:
        out["remote_instance_arn"] = data["remoteInstanceArn"]
    if data.get("remoteSubnetArn") is not None:
        out["remote_subnet_arn"] = data["remoteSubnetArn"]
    if data.get("remoteVpcArn") is not None:
        out["remote_vpc_arn"] = data["remoteVpcArn"]
    if data.get("additionalFlowInfo") is not None:
        import capo_networkflowmonitor.types.additional_flow_info

        out["additional_flow_info"] = (
            capo_networkflowmonitor.types.additional_flow_info.deserialize_json(
                data["additionalFlowInfo"]
            )
        )
    return out
