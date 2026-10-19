"""Generated from Smithy shape ``com.amazonaws.route53domains#Nameserver``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.glue_ip_list
    import capo_route_53_domains.types.host_name


class Nameserver(TypedDict, closed=True):
    name: "capo_route_53_domains.types.host_name.HostName"
    """<p>The fully qualified host name of the name server.</p> <p>Constraint: Maximum 255 characters</p>"""
    glue_ips: NotRequired["capo_route_53_domains.types.glue_ip_list.GlueIpList"]
    """<p>Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.</p> <p>Constraints: The list can contain only one IPv4 and one IPv6 address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Nameserver) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "glue_ips" in value:
        import capo_route_53_domains.types.glue_ip_list

        out["GlueIps"] = (
            capo_route_53_domains.types.glue_ip_list.serialize_aws_json_1_1(
                value["glue_ips"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Nameserver:
    out: Nameserver = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("GlueIps") is not None:
        import capo_route_53_domains.types.glue_ip_list

        out["glue_ips"] = (
            capo_route_53_domains.types.glue_ip_list.deserialize_aws_json_1_1(
                data["GlueIps"]
            )
        )
    return out
