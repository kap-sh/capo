"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtpStandardDestinationEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.forward_error_correction_state


class RtpStandardDestinationEndpointConfiguration(TypedDict, closed=True):
    destination_address: "str"
    """<p>The IP address on which the destination endpoint receives content.</p>"""
    destination_ingest_port: "int"
    """<p>The port on which the destination endpoint receives content. The valid range is 1024 to 65531.</p>"""
    forward_error_correction_state: "capo_mediaconnect.types.forward_error_correction_state.ForwardErrorCorrectionState"
    """<p>Indicates whether forward error correction (FEC) is enabled for the destination endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtpStandardDestinationEndpointConfiguration) -> dict:
    out: dict = {}
    out["destinationAddress"] = value["destination_address"]
    out["destinationIngestPort"] = value["destination_ingest_port"]
    import capo_mediaconnect.types.forward_error_correction_state

    out["forwardErrorCorrectionState"] = (
        capo_mediaconnect.types.forward_error_correction_state.serialize_json(
            value["forward_error_correction_state"]
        )
    )
    return out


def deserialize_json(data: dict) -> RtpStandardDestinationEndpointConfiguration:
    out: RtpStandardDestinationEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destinationAddress") is not None:
        out["destination_address"] = data["destinationAddress"]
    else:
        out["destination_address"] = ""
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
