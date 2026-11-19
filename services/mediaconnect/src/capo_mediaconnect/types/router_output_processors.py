"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputProcessors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.single_program_transport_stream_pid_map_configuration


class RouterOutputProcessors(TypedDict, closed=True):
    single_program_transport_stream_pid_map: NotRequired[
        "capo_mediaconnect.types.single_program_transport_stream_pid_map_configuration.SingleProgramTransportStreamPidMapConfiguration"
    ]
    """<p>The configuration settings for remapping the identification numbers of elementary streams and program identifiers of a single-program transport stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputProcessors) -> dict:
    out: dict = {}
    if "single_program_transport_stream_pid_map" in value:
        import capo_mediaconnect.types.single_program_transport_stream_pid_map_configuration

        out["singleProgramTransportStreamPidMap"] = (
            capo_mediaconnect.types.single_program_transport_stream_pid_map_configuration.serialize_json(
                value["single_program_transport_stream_pid_map"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouterOutputProcessors:
    out: RouterOutputProcessors = {}  # type: ignore[typeddict-item]
    if data.get("singleProgramTransportStreamPidMap") is not None:
        import capo_mediaconnect.types.single_program_transport_stream_pid_map_configuration

        out["single_program_transport_stream_pid_map"] = (
            capo_mediaconnect.types.single_program_transport_stream_pid_map_configuration.deserialize_json(
                data["singleProgramTransportStreamPidMap"]
            )
        )
    return out
