"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterNetworkInterfaceError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_network_interface_arn


class BatchGetRouterNetworkInterfaceError(TypedDict, closed=True):
    arn: (
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the router network interface for which the error occurred.</p>"""
    code: "str"
    """<p>The error code associated with the error.</p>"""
    message: "str"
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterNetworkInterfaceError) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetRouterNetworkInterfaceError:
    out: BatchGetRouterNetworkInterfaceError = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
