"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.server_side_string


class CoreNetworkPolicyError(TypedDict, closed=True):
    error_code: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The error code associated with a core network policy error.</p>"""
    message: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The message associated with a core network policy error code.</p>"""
    path: NotRequired["capo_networkmanager.types.server_side_string.ServerSideString"]
    """<p>The JSON path where the error was discovered in the policy document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicyError) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    out["Message"] = value["message"]
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_json(data: dict) -> CoreNetworkPolicyError:
    out: CoreNetworkPolicyError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        out["error_code"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    return out
