"""Generated from Smithy shape ``com.amazonaws.ecs#PortMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.application_protocol
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string
    import capo_ecs.types.transport_protocol


class PortMapping(TypedDict, closed=True):
    container_port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port number on the container that's bound to the user-specified or automatically assigned host port.</p> <p>If you use containers in a task with the <code>awsvpc</code> or <code>host</code> network mode, specify the exposed ports using <code>containerPort</code>.</p> <p>If you use containers in a task with the <code>bridge</code> network mode and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range. For more information, see <code>hostPort</code>. Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.</p>"""
    host_port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port number on the container instance to reserve for your container.</p> <p>If you specify a <code>containerPortRange</code>, leave this field empty and the value of the <code>hostPort</code> is set as follows:</p> <ul> <li> <p>For containers in a task with the <code>awsvpc</code> network mode, the <code>hostPort</code> is set to the same value as the <code>containerPort</code>. This is a static mapping strategy.</p> </li> <li> <p>For containers in a task with the <code>bridge</code> network mode, the Amazon ECS agent finds open ports on the host and automatically binds them to the container ports. This is a dynamic mapping strategy.</p> </li> </ul> <p>If you use containers in a task with the <code>awsvpc</code> or <code>host</code> network mode, the <code>hostPort</code> can either be left blank or set to the same value as the <code>containerPort</code>.</p> <p>If you use containers in a task with the <code>bridge</code> network mode, you can specify a non-reserved host port for your container port mapping, or you can omit the <code>hostPort</code> (or set it to <code>0</code>) while specifying a <code>containerPort</code> and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.</p> <p>The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under <code>/proc/sys/net/ipv4/ip_local_port_range</code>. If this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 (Linux) or 49152 through 65535 (Windows) is used. Do not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.</p> <p>The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678-51680. Any host port that was previously specified in a running task is also reserved while the task is running. That is, after a task stops, the host port is released. The current reserved ports are displayed in the <code>remainingResources</code> of <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeContainerInstances.html">DescribeContainerInstances</a> output. A container instance can have up to 100 reserved ports at a time. This number includes the default reserved ports. Automatically assigned ports aren't included in the 100 reserved ports quota.</p>"""
    protocol: NotRequired["capo_ecs.types.transport_protocol.TransportProtocol"]
    """<p>The protocol that's used for the port mapping. Valid values are <code>tcp</code> and <code>udp</code> (case-sensitive). The default is <code>tcp</code>. Amazon ECS treats any other specified value as <code>tcp</code>. <code>protocol</code> is immutable in a Service Connect service. To update this field, you must delete and redeploy the service. </p>"""
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name that's used for the port mapping. This parameter is the name that you use in the <code>serviceConnectConfiguration</code> and the <code>vpcLatticeConfigurations</code> of a service. The name can include up to 64 characters. The characters can include lowercase letters, numbers, underscores (_), and hyphens (-). The name can't start with a hyphen.</p>"""
    app_protocol: NotRequired["capo_ecs.types.application_protocol.ApplicationProtocol"]
    """<p>The application protocol that's used for the port mapping. This parameter only applies to Service Connect. We recommend that you set this parameter to be consistent with the protocol that your application uses. If you set this parameter, Amazon ECS adds protocol-specific connection handling to the Service Connect proxy. If you set this parameter, Amazon ECS adds protocol-specific telemetry in the Amazon ECS console and CloudWatch.</p> <p>If you don't set a value for this parameter, then TCP is used. However, Amazon ECS doesn't add protocol-specific telemetry for TCP.</p> <p> <code>appProtocol</code> is immutable in a Service Connect service. Updating this field requires a service deletion and redeployment.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    container_port_range: NotRequired["capo_ecs.types.string.String"]
    """<p>The port number range on the container that's bound to the dynamically mapped host port range. </p> <p>The following rules apply when you specify a <code>containerPortRange</code>:</p> <ul> <li> <p>You must use either the <code>bridge</code> network mode or the <code>awsvpc</code> network mode.</p> </li> <li> <p>This parameter is available for both the EC2 and Fargate launch types.</p> </li> <li> <p>This parameter is available for both the Linux and Windows operating systems.</p> </li> <li> <p>The container instance must have at least version 1.67.0 of the container agent and at least version 1.67.0-1 of the <code>ecs-init</code> package </p> </li> <li> <p>You can specify a maximum of 100 port ranges per container.</p> </li> <li> <p>You do not specify a <code>hostPortRange</code>. The value of the <code>hostPortRange</code> is set as follows:</p> <ul> <li> <p>For containers in a task with the <code>awsvpc</code> network mode, the <code>hostPortRange</code> is set to the same value as the <code>containerPortRange</code>. This is a static mapping strategy.</p> </li> <li> <p>For containers in a task with the <code>bridge</code> network mode, the Amazon ECS agent finds open host ports from the default ephemeral range and passes it to docker to bind them to the container ports.</p> </li> </ul> </li> <li> <p>The <code>containerPortRange</code> valid values are between 1 and 65535.</p> </li> <li> <p>A port can only be included in one port mapping per container.</p> </li> <li> <p>You cannot specify overlapping port ranges.</p> </li> <li> <p>The first port in the range must be less than last port in the range.</p> </li> <li> <p>Docker recommends that you turn off the docker-proxy in the Docker daemon config file when you have a large number of ports.</p> <p>For more information, see <a href="https://github.com/moby/moby/issues/11185"> Issue #11185</a> on the Github website.</p> <p>For information about how to turn off the docker-proxy in the Docker daemon config file, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bootstrap_container_instance.html#bootstrap_docker_daemon">Docker daemon</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> </ul> <p>You can call <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html"> <code>DescribeTasks</code> </a> to view the <code>hostPortRange</code> which are the host ports that are bound to the container ports.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortMapping) -> dict:
    out: dict = {}
    if "container_port" in value:
        out["containerPort"] = value["container_port"]
    if "host_port" in value:
        out["hostPort"] = value["host_port"]
    if "protocol" in value:
        import capo_ecs.types.transport_protocol

        out["protocol"] = capo_ecs.types.transport_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "app_protocol" in value:
        import capo_ecs.types.application_protocol

        out["appProtocol"] = capo_ecs.types.application_protocol.serialize_aws_json_1_1(
            value["app_protocol"]
        )
    if "container_port_range" in value:
        out["containerPortRange"] = value["container_port_range"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PortMapping:
    out: PortMapping = {}  # type: ignore[typeddict-item]
    if data.get("containerPort") is not None:
        out["container_port"] = data["containerPort"]
    if data.get("hostPort") is not None:
        out["host_port"] = data["hostPort"]
    if data.get("protocol") is not None:
        import capo_ecs.types.transport_protocol

        out["protocol"] = capo_ecs.types.transport_protocol.deserialize_aws_json_1_1(
            data["protocol"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("appProtocol") is not None:
        import capo_ecs.types.application_protocol

        out["app_protocol"] = (
            capo_ecs.types.application_protocol.deserialize_aws_json_1_1(
                data["appProtocol"]
            )
        )
    if data.get("containerPortRange") is not None:
        out["container_port_range"] = data["containerPortRange"]
    return out
