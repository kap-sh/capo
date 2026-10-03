"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeEthereumAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.string


class NodeEthereumAttributes(TypedDict, closed=True):
    http_endpoint: NotRequired["capo_managedblockchain.types.string.String"]
    """<p>The endpoint on which the Ethereum node listens to run Ethereum API methods over HTTP connections from a client. Use this endpoint in client code for smart contracts when using an HTTP connection. Connections to this endpoint are authenticated using <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4</a>.</p>"""
    web_socket_endpoint: NotRequired["capo_managedblockchain.types.string.String"]
    """<p>The endpoint on which the Ethereum node listens to run Ethereum JSON-RPC methods over WebSocket connections from a client. Use this endpoint in client code for smart contracts when using a WebSocket connection. Connections to this endpoint are authenticated using <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeEthereumAttributes) -> dict:
    out: dict = {}
    if "http_endpoint" in value:
        out["HttpEndpoint"] = value["http_endpoint"]
    if "web_socket_endpoint" in value:
        out["WebSocketEndpoint"] = value["web_socket_endpoint"]
    return out


def deserialize_json(data: dict) -> NodeEthereumAttributes:
    out: NodeEthereumAttributes = {}  # type: ignore[typeddict-item]
    if data.get("HttpEndpoint") is not None:
        out["http_endpoint"] = data["HttpEndpoint"]
    if data.get("WebSocketEndpoint") is not None:
        out["web_socket_endpoint"] = data["WebSocketEndpoint"]
    return out
