"""Generated from Smithy shape ``com.amazonaws.pcs#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.endpoint_type


class Endpoint(TypedDict, closed=True):
    type: "capo_pcs.types.endpoint_type.EndpointType"
    """<p>Indicates the type of endpoint running at the specific IP address.</p>"""
    private_ip_address: "str"
    """<p>For clusters that use IPv4, this is the endpoint's private IP address.</p> <p>Example: <code>10.1.2.3</code> </p> <p>For clusters configured to use IPv6, this is an empty string.</p>"""
    public_ip_address: NotRequired["str"]
    """<p>The endpoint's public IP address.</p> <p>Example: <code>192.0.2.1</code> </p>"""
    ipv6_address: NotRequired["str"]
    """<p>The endpoint's IPv6 address.</p> <p>Example: <code>2001:db8::1</code> </p>"""
    port: "str"
    """<p>The endpoint's connection port number.</p> <p> Example: <code>1234</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Endpoint) -> dict:
    out: dict = {}
    import capo_pcs.types.endpoint_type

    out["type"] = capo_pcs.types.endpoint_type.serialize_aws_json_1_0(value["type"])
    out["privateIpAddress"] = value["private_ip_address"]
    if "public_ip_address" in value:
        out["publicIpAddress"] = value["public_ip_address"]
    if "ipv6_address" in value:
        out["ipv6Address"] = value["ipv6_address"]
    out["port"] = value["port"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_pcs.types.endpoint_type

        out["type"] = capo_pcs.types.endpoint_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_pcs.types.endpoint_type.EndpointType", "")
    if data.get("privateIpAddress") is not None:
        out["private_ip_address"] = data["privateIpAddress"]
    else:
        out["private_ip_address"] = ""
    if data.get("publicIpAddress") is not None:
        out["public_ip_address"] = data["publicIpAddress"]
    if data.get("ipv6Address") is not None:
        out["ipv6_address"] = data["ipv6Address"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = ""
    return out
