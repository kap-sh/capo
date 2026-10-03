"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.port_number
    import capo_ecs.types.service_connect_client_alias_list
    import capo_ecs.types.service_connect_tls_configuration
    import capo_ecs.types.string
    import capo_ecs.types.timeout_configuration


class ServiceConnectService(TypedDict, closed=True):
    port_name: "capo_ecs.types.string.String"
    """<p>The <code>portName</code> must match the name of one of the <code>portMappings</code> from all the containers in the task definition of this Amazon ECS service.</p>"""
    discovery_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>discoveryName</code> is the name of the new Cloud Map service that Amazon ECS creates for this Amazon ECS service. This must be unique within the Cloud Map namespace. The name can contain up to 64 characters. The name can include lowercase letters, numbers, underscores (_), and hyphens (-). The name can't start with a hyphen.</p> <p>If the <code>discoveryName</code> isn't specified, the port mapping name from the task definition is used in <code>portName.namespace</code>.</p>"""
    client_aliases: NotRequired[
        "capo_ecs.types.service_connect_client_alias_list.ServiceConnectClientAliasList"
    ]
    """<p>The list of client aliases for this Service Connect service. You use these to assign names that can be used by client applications. The maximum number of client aliases that you can have in this list is 1.</p> <p>Each alias ("endpoint") is a fully-qualified name and port number that other Amazon ECS tasks ("clients") can use to connect to this service.</p> <p>Each name and port mapping must be unique within the namespace.</p> <p>For each <code>ServiceConnectService</code>, you must provide at least one <code>clientAlias</code> with one <code>port</code>.</p>"""
    ingress_port_override: NotRequired["capo_ecs.types.port_number.PortNumber"]
    """<p>The port number for the Service Connect proxy to listen on.</p> <p>Use the value of this field to bypass the proxy for traffic on the port number specified in the named <code>portMapping</code> in the task definition of this application, and then use it in your VPC security groups to allow traffic into the proxy for this Amazon ECS service.</p> <p>In <code>awsvpc</code> mode and Fargate, the default value is the container port number. The container port number is in the <code>portMapping</code> in the task definition. In bridge mode, the default value is the ephemeral port of the Service Connect proxy.</p>"""
    timeout: NotRequired["capo_ecs.types.timeout_configuration.TimeoutConfiguration"]
    """<p>A reference to an object that represents the configured timeouts for Service Connect.</p>"""
    tls: NotRequired[
        "capo_ecs.types.service_connect_tls_configuration.ServiceConnectTlsConfiguration"
    ]
    """<p>A reference to an object that represents a Transport Layer Security (TLS) configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectService) -> dict:
    out: dict = {}
    out["portName"] = value["port_name"]
    if "discovery_name" in value:
        out["discoveryName"] = value["discovery_name"]
    if "client_aliases" in value:
        import capo_ecs.types.service_connect_client_alias_list

        out["clientAliases"] = (
            capo_ecs.types.service_connect_client_alias_list.serialize_aws_json_1_1(
                value["client_aliases"]
            )
        )
    if "ingress_port_override" in value:
        out["ingressPortOverride"] = value["ingress_port_override"]
    if "timeout" in value:
        import capo_ecs.types.timeout_configuration

        out["timeout"] = capo_ecs.types.timeout_configuration.serialize_aws_json_1_1(
            value["timeout"]
        )
    if "tls" in value:
        import capo_ecs.types.service_connect_tls_configuration

        out["tls"] = (
            capo_ecs.types.service_connect_tls_configuration.serialize_aws_json_1_1(
                value["tls"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectService:
    out: ServiceConnectService = {}  # type: ignore[typeddict-item]
    if data.get("portName") is not None:
        out["port_name"] = data["portName"]
    else:
        raise DeserializationError("ServiceConnectService.port_name required")
    if data.get("discoveryName") is not None:
        out["discovery_name"] = data["discoveryName"]
    if data.get("clientAliases") is not None:
        import capo_ecs.types.service_connect_client_alias_list

        out["client_aliases"] = (
            capo_ecs.types.service_connect_client_alias_list.deserialize_aws_json_1_1(
                data["clientAliases"]
            )
        )
    if data.get("ingressPortOverride") is not None:
        out["ingress_port_override"] = data["ingressPortOverride"]
    if data.get("timeout") is not None:
        import capo_ecs.types.timeout_configuration

        out["timeout"] = capo_ecs.types.timeout_configuration.deserialize_aws_json_1_1(
            data["timeout"]
        )
    if data.get("tls") is not None:
        import capo_ecs.types.service_connect_tls_configuration

        out["tls"] = (
            capo_ecs.types.service_connect_tls_configuration.deserialize_aws_json_1_1(
                data["tls"]
            )
        )
    return out
