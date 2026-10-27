"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtpStandardSourceEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.forward_error_correction_state


class RtpStandardSourceEndpointConfiguration(TypedDict, closed=True):
    destination_ingest_port: "int"
    """<p>The port on the destination that receives the content. The valid range is 3000 to 30000.</p>"""
    forward_error_correction_state: "capo_mediaconnect.types.forward_error_correction_state.ForwardErrorCorrectionState"
    """<p>Indicates whether forward error correction (FEC) is enabled for the source endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtpStandardSourceEndpointConfiguration) -> dict:
    out: dict = {}
    out["destinationIngestPort"] = value["destination_ingest_port"]
    import capo_mediaconnect.types.forward_error_correction_state

    out["forwardErrorCorrectionState"] = (
        capo_mediaconnect.types.forward_error_correction_state.serialize_json(
            value["forward_error_correction_state"]
        )
    )
    return out


def deserialize_json(data: dict) -> RtpStandardSourceEndpointConfiguration:
    out: RtpStandardSourceEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destinationIngestPort") is not None:
        out["destination_ingest_port"] = data["destinationIngestPort"]
    else:
        out["destination_ingest_port"] = 0
    if data.get("forwardErrorCorrectionState") is not None:
        import capo_mediaconnect.types.forward_error_correction_state

        out["forward_error_correction_state"] = (
            capo_mediaconnect.types.forward_error_correction_state.deserialize_json(
                data["forwardErrorCorrectionState"]
            )
        )
    else:
        import typing

        out["forward_error_correction_state"] = typing.cast(
            "capo_mediaconnect.types.forward_error_correction_state.ForwardErrorCorrectionState",
            "",
        )
    return out
