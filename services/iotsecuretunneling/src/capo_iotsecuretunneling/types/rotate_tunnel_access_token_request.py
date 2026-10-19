"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#RotateTunnelAccessTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.client_mode
    import capo_iotsecuretunneling.types.destination_config
    import capo_iotsecuretunneling.types.tunnel_id


class RotateTunnelAccessTokenRequest(TypedDict, closed=True):
    tunnel_id: "capo_iotsecuretunneling.types.tunnel_id.TunnelId"
    """<p>The tunnel for which you want to rotate the access tokens.</p>"""
    client_mode: "capo_iotsecuretunneling.types.client_mode.ClientMode"
    """<p>The mode of the client that will use the client token, which can be either the source or destination, or both source and destination.</p>"""
    destination_config: NotRequired[
        "capo_iotsecuretunneling.types.destination_config.DestinationConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotateTunnelAccessTokenRequest) -> dict:
    out: dict = {}
    out["tunnelId"] = value["tunnel_id"]
    import capo_iotsecuretunneling.types.client_mode

    out["clientMode"] = (
        capo_iotsecuretunneling.types.client_mode.serialize_aws_json_1_1(
            value["client_mode"]
        )
    )
    if "destination_config" in value:
        import capo_iotsecuretunneling.types.destination_config

        out["destinationConfig"] = (
            capo_iotsecuretunneling.types.destination_config.serialize_aws_json_1_1(
                value["destination_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RotateTunnelAccessTokenRequest:
    out: RotateTunnelAccessTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("tunnelId") is not None:
        out["tunnel_id"] = data["tunnelId"]
    else:
        out["tunnel_id"] = ""
    if data.get("clientMode") is not None:
        import capo_iotsecuretunneling.types.client_mode

        out["client_mode"] = (
            capo_iotsecuretunneling.types.client_mode.deserialize_aws_json_1_1(
                data["clientMode"]
            )
        )
    else:
        import typing

        out["client_mode"] = typing.cast(
            "capo_iotsecuretunneling.types.client_mode.ClientMode", ""
        )
    if data.get("destinationConfig") is not None:
        import capo_iotsecuretunneling.types.destination_config

        out["destination_config"] = (
            capo_iotsecuretunneling.types.destination_config.deserialize_aws_json_1_1(
                data["destinationConfig"]
            )
        )
    return out
