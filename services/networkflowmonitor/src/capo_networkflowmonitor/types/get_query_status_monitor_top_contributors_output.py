"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryStatusMonitorTopContributorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.query_status


class GetQueryStatusMonitorTopContributorsOutput(TypedDict, closed=True):
    status: "capo_networkflowmonitor.types.query_status.QueryStatus"
    """<p>When you run a query, use this call to check the status of the query to make sure that the query has <code>SUCCEEDED</code> before you review the results.</p> <ul> <li> <p> <code>QUEUED</code>: The query is scheduled to run.</p> </li> <li> <p> <code>RUNNING</code>: The query is in progress but not complete.</p> </li> <li> <p> <code>SUCCEEDED</code>: The query completed sucessfully.</p> </li> <li> <p> <code>FAILED</code>: The query failed due to an error.</p> </li> <li> <p> <code>CANCELED</code>: The query was canceled.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStatusMonitorTopContributorsOutput) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.query_status

    out["status"] = capo_networkflowmonitor.types.query_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> GetQueryStatusMonitorTopContributorsOutput:
    out: GetQueryStatusMonitorTopContributorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_networkflowmonitor.types.query_status

        out["status"] = capo_networkflowmonitor.types.query_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_networkflowmonitor.types.query_status.QueryStatus", ""
        )
    return out
