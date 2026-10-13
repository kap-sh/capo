"""Generated from Smithy shape ``com.amazonaws.directoryservice#RadiusSettings``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.port_number
    import capo_directory_service.types.radius_authentication_protocol
    import capo_directory_service.types.radius_display_label
    import capo_directory_service.types.radius_retries
    import capo_directory_service.types.radius_shared_secret
    import capo_directory_service.types.radius_timeout
    import capo_directory_service.types.servers
    import capo_directory_service.types.use_same_username


class RadiusSettings(TypedDict, closed=True):
    radius_servers: NotRequired["capo_directory_service.types.servers.Servers"]
    """<p>The fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.</p>"""
    radius_servers_ipv6: NotRequired["capo_directory_service.types.servers.Servers"]
    """<p>The IPv6 addresses of the RADIUS server endpoints or RADIUS server load balancer.</p>"""
    radius_port: NotRequired["capo_directory_service.types.port_number.PortNumber"]
    """<p>The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the Directory Service servers.</p>"""
    radius_timeout: NotRequired[
        "capo_directory_service.types.radius_timeout.RadiusTimeout"
    ]
    """<p>The amount of time, in seconds, to wait for the RADIUS server to respond.</p>"""
    radius_retries: "capo_directory_service.types.radius_retries.RadiusRetries"
    """<p>The maximum number of times that communication with the RADIUS server is retried after the initial attempt.</p>"""
    shared_secret: NotRequired[
        "capo_directory_service.types.radius_shared_secret.RadiusSharedSecret"
    ]
    """<p>Required for enabling RADIUS on the directory.</p>"""
    authentication_protocol: NotRequired[
        "capo_directory_service.types.radius_authentication_protocol.RadiusAuthenticationProtocol"
    ]
    """<p>The protocol specified for your RADIUS endpoints.</p>"""
    display_label: NotRequired[
        "capo_directory_service.types.radius_display_label.RadiusDisplayLabel"
    ]
    """<p>Not currently used.</p>"""
    use_same_username: "capo_directory_service.types.use_same_username.UseSameUsername"
    """<p>Not currently used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RadiusSettings) -> dict:
    out: dict = {}
    if "radius_servers" in value:
        import capo_directory_service.types.servers

        out["RadiusServers"] = (
            capo_directory_service.types.servers.serialize_aws_json_1_1(
                value["radius_servers"]
            )
        )
    if "radius_servers_ipv6" in value:
        import capo_directory_service.types.servers

        out["RadiusServersIpv6"] = (
            capo_directory_service.types.servers.serialize_aws_json_1_1(
                value["radius_servers_ipv6"]
            )
        )
    if "radius_port" in value:
        out["RadiusPort"] = value["radius_port"]
    if "radius_timeout" in value:
        out["RadiusTimeout"] = value["radius_timeout"]
    out["RadiusRetries"] = value.get("radius_retries", 0)
    if "shared_secret" in value:
        out["SharedSecret"] = value["shared_secret"]
    if "authentication_protocol" in value:
        import capo_directory_service.types.radius_authentication_protocol

        out["AuthenticationProtocol"] = (
            capo_directory_service.types.radius_authentication_protocol.serialize_aws_json_1_1(
                value["authentication_protocol"]
            )
        )
    if "display_label" in value:
        out["DisplayLabel"] = value["display_label"]
    out["UseSameUsername"] = value.get("use_same_username", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RadiusSettings:
    out: RadiusSettings = {}  # type: ignore[typeddict-item]
    if data.get("RadiusServers") is not None:
        import capo_directory_service.types.servers

        out["radius_servers"] = (
            capo_directory_service.types.servers.deserialize_aws_json_1_1(
                data["RadiusServers"]
            )
        )
    if data.get("RadiusServersIpv6") is not None:
        import capo_directory_service.types.servers

        out["radius_servers_ipv6"] = (
            capo_directory_service.types.servers.deserialize_aws_json_1_1(
                data["RadiusServersIpv6"]
            )
        )
    if data.get("RadiusPort") is not None:
        out["radius_port"] = data["RadiusPort"]
    if data.get("RadiusTimeout") is not None:
        out["radius_timeout"] = data["RadiusTimeout"]
    if data.get("RadiusRetries") is not None:
        out["radius_retries"] = data["RadiusRetries"]
    else:
        out["radius_retries"] = 0
    if data.get("SharedSecret") is not None:
        out["shared_secret"] = data["SharedSecret"]
    if data.get("AuthenticationProtocol") is not None:
        import capo_directory_service.types.radius_authentication_protocol

        out["authentication_protocol"] = (
            capo_directory_service.types.radius_authentication_protocol.deserialize_aws_json_1_1(
                data["AuthenticationProtocol"]
            )
        )
    if data.get("DisplayLabel") is not None:
        out["display_label"] = data["DisplayLabel"]
    if data.get("UseSameUsername") is not None:
        out["use_same_username"] = data["UseSameUsername"]
    else:
        out["use_same_username"] = False
    return out


def redact_sensitive(value: RadiusSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "shared_secret" in value:
        out["shared_secret"] = "*** Sensitive Data Redacted ***"
    return out
