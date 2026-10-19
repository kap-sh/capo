"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CancelQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.query_id
    import capo_iotsitewise.types.query_status


class CancelQueryResponse(TypedDict, closed=True):
    query_id: "capo_iotsitewise.types.query_id.QueryId"
    """<p>The unique identifier for the cancelled query.</p>"""
    status: "capo_iotsitewise.types.query_status.QueryStatus"
    """<p>The current query status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelQueryResponse) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    import capo_iotsitewise.types.query_status

    out["status"] = capo_iotsitewise.types.query_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CancelQueryResponse:
    out: CancelQueryResponse = {}  # type: ignore[typeddict-item]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    else:
        out["query_id"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.query_status

        out["status"] = capo_iotsitewise.types.query_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iotsitewise.types.query_status.QueryStatus", ""
        )
    return out
