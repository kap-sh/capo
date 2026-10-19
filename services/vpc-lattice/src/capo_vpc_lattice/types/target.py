"""Generated from Smithy shape ``com.amazonaws.vpclattice#Target``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.port


class Target(TypedDict, closed=True):
    id: "str"
    """<p>The ID of the target. If the target group type is <code>INSTANCE</code>, this is an instance ID. If the target group type is <code>IP</code>, this is an IP address. If the target group type is <code>LAMBDA</code>, this is the ARN of a Lambda function. If the target group type is <code>ALB</code>, this is the ARN of an Application Load Balancer.</p>"""
    port: NotRequired["capo_vpc_lattice.types.port.Port"]
    """<p>The port on which the target is listening. For HTTP, the default is 80. For HTTPS, the default is 443.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Target) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("port") is not None:
        out["port"] = data["port"]
    return out
