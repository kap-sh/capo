"""Generated from Smithy shape ``com.amazonaws.iotsitewise#QuerySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.query_id
    import capo_iotsitewise.types.query_status


class QuerySummary(TypedDict, closed=True):
    query_id: "capo_iotsitewise.types.query_id.QueryId"
    """<p>The unique identifier for the query execution.</p>"""
    status: "capo_iotsitewise.types.query_status.QueryStatus"
    """<p>The current query status.</p>"""
    submitted_at: "datetime.datetime"
    """<p>The date and time when the query was submitted, in Unix epoch time.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the query reached a terminal state, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuerySummary) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    import capo_iotsitewise.types.query_status

    out["status"] = capo_iotsitewise.types.query_status.serialize_json(value["status"])
    import capo_iotsitewise.types._prelude.timestamp

    out["submittedAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
        value["submitted_at"]
    )
    if "completed_at" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["completedAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["completed_at"]
        )
    return out


def deserialize_json(data: dict) -> QuerySummary:
    out: QuerySummary = {}  # type: ignore[typeddict-item]
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
    if data.get("submittedAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["submitted_at"] = (
            capo_iotsitewise.types._prelude.timestamp.deserialize_json(
                data["submittedAt"]
            )
        )
    else:
        import datetime

        out["submitted_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("completedAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["completed_at"] = (
            capo_iotsitewise.types._prelude.timestamp.deserialize_json(
                data["completedAt"]
            )
        )
    return out
