"""Generated from Smithy shape ``com.amazonaws.ecs#ProxyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.proxy_configuration_properties
    import capo_ecs.types.proxy_configuration_type
    import capo_ecs.types.string


class ProxyConfiguration(TypedDict, closed=True):
    type: NotRequired["capo_ecs.types.proxy_configuration_type.ProxyConfigurationType"]
    """<p>The proxy type. The only supported value is <code>APPMESH</code>.</p>"""
    container_name: "capo_ecs.types.string.String"
    """<p>The name of the container that will serve as the App Mesh proxy.</p>"""
    properties: NotRequired[
        "capo_ecs.types.proxy_configuration_properties.ProxyConfigurationProperties"
    ]
    """<p>The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified as key-value pairs.</p> <ul> <li> <p> <code>IgnoredUID</code> - (Required) The user ID (UID) of the proxy container as defined by the <code>user</code> parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If <code>IgnoredGID</code> is specified, this field can be empty.</p> </li> <li> <p> <code>IgnoredGID</code> - (Required) The group ID (GID) of the proxy container as defined by the <code>user</code> parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If <code>IgnoredUID</code> is specified, this field can be empty.</p> </li> <li> <p> <code>AppPorts</code> - (Required) The list of ports that the application uses. Network traffic to these ports is forwarded to the <code>ProxyIngressPort</code> and <code>ProxyEgressPort</code>.</p> </li> <li> <p> <code>ProxyIngressPort</code> - (Required) Specifies the port that incoming traffic to the <code>AppPorts</code> is directed to.</p> </li> <li> <p> <code>ProxyEgressPort</code> - (Required) Specifies the port that outgoing traffic from the <code>AppPorts</code> is directed to.</p> </li> <li> <p> <code>EgressIgnoredPorts</code> - (Required) The egress traffic going to the specified ports is ignored and not redirected to the <code>ProxyEgressPort</code>. It can be an empty list.</p> </li> <li> <p> <code>EgressIgnoredIPs</code> - (Required) The egress traffic going to the specified IP addresses is ignored and not redirected to the <code>ProxyEgressPort</code>. It can be an empty list.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProxyConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_ecs.types.proxy_configuration_type

        out["type"] = capo_ecs.types.proxy_configuration_type.serialize_aws_json_1_1(
            value["type"]
        )
    out["containerName"] = value["container_name"]
    if "properties" in value:
        import capo_ecs.types.proxy_configuration_properties

        out["properties"] = (
            capo_ecs.types.proxy_configuration_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProxyConfiguration:
    out: ProxyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_ecs.types.proxy_configuration_type

        out["type"] = capo_ecs.types.proxy_configuration_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    else:
        out["container_name"] = ""
    if data.get("properties") is not None:
        import capo_ecs.types.proxy_configuration_properties

        out["properties"] = (
            capo_ecs.types.proxy_configuration_properties.deserialize_aws_json_1_1(
                data["properties"]
            )
        )
    return out
