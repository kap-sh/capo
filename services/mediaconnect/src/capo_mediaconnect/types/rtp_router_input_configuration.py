"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtpRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.forward_error_correction_state


class RtpRouterInputConfiguration(TypedDict, closed=True):
    port: "int"
    """<p>The port number used for the RTP protocol in the router input configuration.</p>"""
    forward_error_correction: NotRequired[
        "capo_mediaconnect.types.forward_error_correction_state.ForwardErrorCorrectionState"
    ]
    """<p>The state of forward error correction for the RTP protocol in the router input configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtpRouterInputConfiguration) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    if "forward_error_correction" in value:
        import capo_mediaconnect.types.forward_error_correction_state

        out["forwardErrorCorrection"] = (
            capo_mediaconnect.types.forward_error_correction_state.serialize_json(
                value["forward_error_correction"]
            )
        )
    return out


def deserialize_json(data: dict) -> RtpRouterInputConfiguration:
    out: RtpRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    if data.get("forwardErrorCorrection") is not None:
        import capo_mediaconnect.types.forward_error_correction_state

        out["forward_error_correction"] = (
            capo_mediaconnect.types.forward_error_correction_state.deserialize_json(
                data["forwardErrorCorrection"]
            )
        )
    return out
