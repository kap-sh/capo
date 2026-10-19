"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetQueryStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.query_status


class GetQueryStatusOutput(TypedDict, closed=True):
    status: "capo_internetmonitor.types.query_status.QueryStatus"
    """<p>The current status for a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStatusOutput) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> GetQueryStatusOutput:
    out: GetQueryStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
