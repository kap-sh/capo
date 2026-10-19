"""Generated from Smithy shape ``com.amazonaws.iot#GetV2LoggingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.verbose_flag


class GetV2LoggingOptionsRequest(TypedDict, closed=True):
    verbose: NotRequired["capo_iot.types.verbose_flag.VerboseFlag"]
    """<p> The flag is used to get all the event types and their respective configuration that event-based logging supports. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetV2LoggingOptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetV2LoggingOptionsRequest:
    out: GetV2LoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    return out
