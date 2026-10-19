"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AddNotificationChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.channels
    import capo_codeguruprofiler.types.profiling_group_name


class AddNotificationChannelsRequest(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group that we are setting up notifications for.</p>"""
    channels: "capo_codeguruprofiler.types.channels.Channels"
    """<p>One or 2 channels to report to when anomalies are detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddNotificationChannelsRequest) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.channels

    out["channels"] = capo_codeguruprofiler.types.channels.serialize_json(
        value["channels"]
    )
    return out


def deserialize_json(data: dict) -> AddNotificationChannelsRequest:
    out: AddNotificationChannelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("channels") is not None:
        import capo_codeguruprofiler.types.channels

        out["channels"] = capo_codeguruprofiler.types.channels.deserialize_json(
            data["channels"]
        )
    else:
        out["channels"] = []
    return out
