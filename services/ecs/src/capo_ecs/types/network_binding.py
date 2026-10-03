"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkBinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string
    import capo_ecs.types.transport_protocol


class NetworkBinding(TypedDict, closed=True):
    bind_ip: NotRequired["capo_ecs.types.string.String"]
    """<p>The IP address that the container is bound to on the container instance.</p>"""
    container_port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port number on the container that's used with the network binding.</p>"""
    host_port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port number on the host that's used with the network binding.</p>"""
    protocol: NotRequired["capo_ecs.types.transport_protocol.TransportProtocol"]
    """<p>The protocol used for the network binding.</p>"""
    container_port_range: NotRequired["capo_ecs.types.string.String"]
    """<p>The port number range on the container that's bound to the dynamically mapped host port range.</p> <p>The following rules apply when you specify a <code>containerPortRange</code>:</p> <ul> <li> <p>You must use either the <code>bridge</code> network mode or the <code>awsvpc</code> network mode.</p> </li> <li> <p>This parameter is available for both the EC2 and Fargate launch types.</p> </li> <li> <p>This parameter is available for both the Linux and Windows operating systems.</p> </li> <li> <p>The container instance must have at least version 1.67.0 of the container agent and at least version 1.67.0-1 of the <code>ecs-init</code> package </p> </li> <li> <p>You can specify a maximum of 100 port ranges per container.</p> </li> <li> <p>You do not specify a <code>hostPortRange</code>. The value of the <code>hostPortRange</code> is set as follows:</p> <ul> <li> <p>For containers in a task with the <code>awsvpc</code> network mode, the <code>hostPortRange</code> is set to the same value as the <code>containerPortRange</code>. This is a static mapping strategy.</p> </li> <li> <p>For containers in a task with the <code>bridge</code> network mode, the Amazon ECS agent finds open host ports from the default ephemeral range and passes it to docker to bind them to the container ports.</p> </li> </ul> </li> <li> <p>The <code>containerPortRange</code> valid values are between 1 and 65535.</p> </li> <li> <p>A port can only be included in one port mapping per container.</p> </li> <li> <p>You cannot specify overlapping port ranges.</p> </li> <li> <p>The first port in the range must be less than last port in the range.</p> </li> <li> <p>Docker recommends that you turn off the docker-proxy in the Docker daemon config file when you have a large number of ports.</p> <p>For more information, see <a href="https://github.com/moby/moby/issues/11185"> Issue #11185</a> on the Github website.</p> <p>For information about how to turn off the docker-proxy in the Docker daemon config file, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bootstrap_container_instance.html#bootstrap_docker_daemon">Docker daemon</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> </ul> <p>You can call <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html"> <code>DescribeTasks</code> </a> to view the <code>hostPortRange</code> which are the host ports that are bound to the container ports.</p>"""
    host_port_range: NotRequired["capo_ecs.types.string.String"]
    """<p>The port number range on the host that's used with the network binding. This is assigned is assigned by Docker and delivered by the Amazon ECS agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkBinding) -> dict:
    out: dict = {}
    if "bind_ip" in value:
        out["bindIP"] = value["bind_ip"]
    if "container_port" in value:
        out["containerPort"] = value["container_port"]
    if "host_port" in value:
        out["hostPort"] = value["host_port"]
    if "protocol" in value:
        import capo_ecs.types.transport_protocol

        out["protocol"] = capo_ecs.types.transport_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "container_port_range" in value:
        out["containerPortRange"] = value["container_port_range"]
    if "host_port_range" in value:
        out["hostPortRange"] = value["host_port_range"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkBinding:
    out: NetworkBinding = {}  # type: ignore[typeddict-item]
    if data.get("bindIP") is not None:
        out["bind_ip"] = data["bindIP"]
    if data.get("containerPort") is not None:
        out["container_port"] = data["containerPort"]
    if data.get("hostPort") is not None:
        out["host_port"] = data["hostPort"]
    if data.get("protocol") is not None:
        import capo_ecs.types.transport_protocol

        out["protocol"] = capo_ecs.types.transport_protocol.deserialize_aws_json_1_1(
            data["protocol"]
        )
    if data.get("containerPortRange") is not None:
        out["container_port_range"] = data["containerPortRange"]
    if data.get("hostPortRange") is not None:
        out["host_port_range"] = data["hostPortRange"]
    return out
