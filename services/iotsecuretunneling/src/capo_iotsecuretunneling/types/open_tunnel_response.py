"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#OpenTunnelResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.client_access_token
    import capo_iotsecuretunneling.types.tunnel_arn
    import capo_iotsecuretunneling.types.tunnel_id


class OpenTunnelResponse(TypedDict, closed=True):
    tunnel_id: NotRequired["capo_iotsecuretunneling.types.tunnel_id.TunnelId"]
    """<p>A unique alpha-numeric tunnel ID.</p>"""
    tunnel_arn: NotRequired["capo_iotsecuretunneling.types.tunnel_arn.TunnelArn"]
    """<p>The Amazon Resource Name for the tunnel.</p>"""
    source_access_token: NotRequired[
        "capo_iotsecuretunneling.types.client_access_token.ClientAccessToken"
    ]
    """<p>The access token the source local proxy uses to connect to IoT Secure Tunneling.</p>"""
    destination_access_token: NotRequired[
        "capo_iotsecuretunneling.types.client_access_token.ClientAccessToken"
    ]
    """<p>The access token the destination local proxy uses to connect to IoT Secure Tunneling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenTunnelResponse) -> dict:
    out: dict = {}
    if "tunnel_id" in value:
        out["tunnelId"] = value["tunnel_id"]
    if "tunnel_arn" in value:
        out["tunnelArn"] = value["tunnel_arn"]
    if "source_access_token" in value:
        out["sourceAccessToken"] = value["source_access_token"]
    if "destination_access_token" in value:
        out["destinationAccessToken"] = value["destination_access_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenTunnelResponse:
    out: OpenTunnelResponse = {}  # type: ignore[typeddict-item]
    if data.get("tunnelId") is not None:
        out["tunnel_id"] = data["tunnelId"]
    if data.get("tunnelArn") is not None:
        out["tunnel_arn"] = data["tunnelArn"]
    if data.get("sourceAccessToken") is not None:
        out["source_access_token"] = data["sourceAccessToken"]
    if data.get("destinationAccessToken") is not None:
        out["destination_access_token"] = data["destinationAccessToken"]
    return out


def redact_sensitive(value: OpenTunnelResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_access_token" in value:
        out["source_access_token"] = "*** Sensitive Data Redacted ***"
    if "destination_access_token" in value:
        out["destination_access_token"] = "*** Sensitive Data Redacted ***"
    return out
