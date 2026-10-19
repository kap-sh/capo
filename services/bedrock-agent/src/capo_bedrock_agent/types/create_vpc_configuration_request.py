"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateVpcConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.host_header
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.port
    import capo_bedrock_agent.types.resource_target
    import capo_bedrock_agent.types.subnet_id_list
    import capo_bedrock_agent.types.tls_server_name
    import capo_bedrock_agent.types.vpc_configuration_description
    import capo_bedrock_agent.types.vpc_configuration_name
    import capo_bedrock_agent.types.vpc_id
    import capo_bedrock_agent.types.vpc_protocol
    import capo_bedrock_agent.types.vpc_resolution_mode


class CreateVpcConfigurationRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to associate this VPC configuration with.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>"""
    vpc_id: "capo_bedrock_agent.types.vpc_id.VpcId"
    """<p>The identifier of the VPC that the knowledge base connects through to reach the resource.</p>"""
    subnet_ids: "capo_bedrock_agent.types.subnet_id_list.SubnetIdList"
    """<p>The subnets, in the VPC identified by <code>vpcId</code>, that the knowledge base uses to connect to the resource.</p>"""
    resource_target: "capo_bedrock_agent.types.resource_target.ResourceTarget"
    """<p>The private IPv4 address or DNS name of the resource you want the knowledge base to reach. The target must be privately reachable from inside your VPC, such as an internal load balancer or a private IP. The following are not supported:</p> <ul> <li> <p>Internet-facing endpoints</p> </li> <li> <p>Loopback addresses</p> </li> <li> <p>Link-local addresses</p> </li> <li> <p>Wildcard addresses</p> </li> <li> <p>Multicast addresses</p> </li> <li> <p>IPv6 literals</p> </li> </ul>"""
    port: "capo_bedrock_agent.types.port.Port"
    """<p>The port on which to reach the resource.</p>"""
    protocol: "capo_bedrock_agent.types.vpc_protocol.VpcProtocol"
    """<p>The protocol used to connect to the resource. Specify <code>HTTP</code> for plaintext or <code>HTTPS</code> for TLS. When you specify <code>HTTPS</code>, you must also provide <code>tlsServerName</code>.</p>"""
    resolution_mode: "capo_bedrock_agent.types.vpc_resolution_mode.VpcResolutionMode"
    """<p>Controls how a domain-name <code>resourceTarget</code> is resolved. This applies only when the target is a domain name; it has no effect for IP-address targets, which have no name to resolve. In all cases the resolved address must be reachable from inside your VPC. Valid values:</p> <ul> <li> <p> <code>IN_VPC</code> (default, recommended) – The target domain name is resolved privately, using the DNS resolvers of the VPC, such as private Route 53 hosted zones or on-premises DNS reachable from the VPC. Use this for targets that are private to your VPC, such as internal load balancers, private hosted-zone names, or on-premises hosts.</p> </li> <li> <p> <code>PUBLIC</code> – The target domain name is resolved against public DNS resolvers. Select this only when the target's domain name must be resolved through public DNS and the resulting address is still reachable from the VPC, an uncommon split-horizon configuration. If you are unsure, use <code>IN_VPC</code>.</p> </li> </ul>"""
    host_header: NotRequired["capo_bedrock_agent.types.host_header.HostHeader"]
    """<p>An optional HTTP <code>Host</code> header value to send when invoking the resource. Set this only if your resource (or an upstream router or ingress) routes by the <code>Host</code> header and that host differs from the target. This setting is independent of <code>tlsServerName</code>.</p>"""
    tls_server_name: NotRequired[
        "capo_bedrock_agent.types.tls_server_name.TlsServerName"
    ]
    """<p>The expected TLS server name. The service matches this value against the Subject Alternative Names on your resource's TLS certificate during invocation. This field is required when <code>protocol</code> is <code>HTTPS</code>. Set it to a hostname on your certificate, such as <code>app.internal.example.com</code>. You can use a single leftmost wildcard, such as <code>*.example.com</code>. The value must be a hostname without a port.</p>"""
    name: NotRequired[
        "capo_bedrock_agent.types.vpc_configuration_name.VpcConfigurationName"
    ]
    """<p>An optional human-readable name for the VPC configuration. If you don't specify a name, the VPC configuration has no name.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.vpc_configuration_description.VpcConfigurationDescription"
    ]
    """<p>An optional description of the VPC configuration. If you don't specify a description, the VPC configuration has no description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["vpcId"] = value["vpc_id"]
    import capo_bedrock_agent.types.subnet_id_list

    out["subnetIds"] = capo_bedrock_agent.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    out["resourceTarget"] = value["resource_target"]
    out["port"] = value["port"]
    import capo_bedrock_agent.types.vpc_protocol

    out["protocol"] = capo_bedrock_agent.types.vpc_protocol.serialize_json(
        value["protocol"]
    )
    import capo_bedrock_agent.types.vpc_resolution_mode

    out["resolutionMode"] = capo_bedrock_agent.types.vpc_resolution_mode.serialize_json(
        value["resolution_mode"]
    )
    if "host_header" in value:
        out["hostHeader"] = value["host_header"]
    if "tls_server_name" in value:
        out["tlsServerName"] = value["tls_server_name"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateVpcConfigurationRequest:
    out: CreateVpcConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("subnetIds") is not None:
        import capo_bedrock_agent.types.subnet_id_list

        out["subnet_ids"] = capo_bedrock_agent.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("resourceTarget") is not None:
        out["resource_target"] = data["resourceTarget"]
    else:
        out["resource_target"] = ""
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    if data.get("protocol") is not None:
        import capo_bedrock_agent.types.vpc_protocol

        out["protocol"] = capo_bedrock_agent.types.vpc_protocol.deserialize_json(
            data["protocol"]
        )
    else:
        import typing

        out["protocol"] = typing.cast(
            "capo_bedrock_agent.types.vpc_protocol.VpcProtocol", ""
        )
    if data.get("resolutionMode") is not None:
        import capo_bedrock_agent.types.vpc_resolution_mode

        out["resolution_mode"] = (
            capo_bedrock_agent.types.vpc_resolution_mode.deserialize_json(
                data["resolutionMode"]
            )
        )
    else:
        import typing

        out["resolution_mode"] = typing.cast(
            "capo_bedrock_agent.types.vpc_resolution_mode.VpcResolutionMode", ""
        )
    if data.get("hostHeader") is not None:
        out["host_header"] = data["hostHeader"]
    if data.get("tlsServerName") is not None:
        out["tls_server_name"] = data["tlsServerName"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
