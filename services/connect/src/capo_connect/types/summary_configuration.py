"""Generated from Smithy shape ``com.amazonaws.connect#SummaryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.summary_modes


class SummaryConfiguration(TypedDict, closed=True):
    summary_modes: "capo_connect.types.summary_modes.SummaryModes"
    """<p>The summary modes that determine what type of summarization is generated. Valid values: <code>PostContact</code> | <code>AutomatedInteraction</code> | <code>ContactChain</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummaryConfiguration) -> dict:
    out: dict = {}
    import capo_connect.types.summary_modes

    out["SummaryModes"] = capo_connect.types.summary_modes.serialize_json(
        value["summary_modes"]
    )
    return out


def deserialize_json(data: dict) -> SummaryConfiguration:
    out: SummaryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SummaryModes") is not None:
        import capo_connect.types.summary_modes

        out["summary_modes"] = capo_connect.types.summary_modes.deserialize_json(
            data["SummaryModes"]
        )
    else:
        out["summary_modes"] = []
    return out
