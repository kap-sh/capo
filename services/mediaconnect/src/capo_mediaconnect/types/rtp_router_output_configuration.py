"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtpRouterOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.forward_error_correction_state


class RtpRouterOutputConfiguration(TypedDict, closed=True):
    destination_address: "str"
    """<p>The destination IP address for the RTP protocol in the router output configuration.</p>"""
    destination_port: "int"
    """<p>The destination port number for the RTP protocol in the router output configuration.</p>"""
    forward_error_correction: NotRequired[
        "capo_mediaconnect.types.forward_error_correction_state.ForwardErrorCorrectionState"
    ]
    """<p>The state of forward error correction for the RTP protocol in the router output configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtpRouterOutputConfiguration) -> dict:
    out: dict = {}
    out["destinationAddress"] = value["destination_address"]
    out["destinationPort"] = value["destination_port"]
    if "forward_error_correction" in value:
        import capo_mediaconnect.types.forward_error_correction_state

        out["forwardErrorCorrection"] = (
            capo_mediaconnect.types.forward_error_correction_state.serialize_json(
                value["forward_error_correction"]
            )
        )
    return out


def deserialize_json(data: dict) -> RtpRouterOutputConfiguration:
    out: RtpRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destinationAddress") is not None:
        out["destination_address"] = data["destinationAddress"]
    else:
        out["destination_address"] = ""
    if data.get("destinationPort") is not None:
        out["destination_port"] = data["destinationPort"]
    else:
        out["destination_port"] = 0
    if data.get("forwardErrorCorrection") is not None:
        import capo_mediaconnect.types.forward_error_correction_state

        out["forward_error_correction"] = (
            capo_mediaconnect.types.forward_error_correction_state.deserialize_json(
                data["forwardErrorCorrection"]
            )
        )
    return out
