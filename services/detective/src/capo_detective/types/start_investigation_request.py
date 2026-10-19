"""Generated from Smithy shape ``com.amazonaws.detective#StartInvestigationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.entity_arn
    import capo_detective.types.graph_arn
    import capo_detective.types.timestamp


class StartInvestigationRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The Amazon Resource Name (ARN) of the behavior graph.</p>"""
    entity_arn: "capo_detective.types.entity_arn.EntityArn"
    """<p>The unique Amazon Resource Name (ARN) of the IAM user and IAM role.</p>"""
    scope_start_time: "capo_detective.types.timestamp.Timestamp"
    """<p>The data and time when the investigation began. The value is an UTC ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""
    scope_end_time: "capo_detective.types.timestamp.Timestamp"
    """<p>The data and time when the investigation ended. The value is an UTC ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartInvestigationRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    out["EntityArn"] = value["entity_arn"]
    import capo_detective.types.timestamp

    out["ScopeStartTime"] = capo_detective.types.timestamp.serialize_json(
        value["scope_start_time"]
    )
    import capo_detective.types.timestamp

    out["ScopeEndTime"] = capo_detective.types.timestamp.serialize_json(
        value["scope_end_time"]
    )
    return out


def deserialize_json(data: dict) -> StartInvestigationRequest:
    out: StartInvestigationRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("EntityArn") is not None:
        out["entity_arn"] = data["EntityArn"]
    else:
        out["entity_arn"] = ""
    if data.get("ScopeStartTime") is not None:
        import capo_detective.types.timestamp

        out["scope_start_time"] = capo_detective.types.timestamp.deserialize_json(
            data["ScopeStartTime"]
        )
    else:
        import datetime

        out["scope_start_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ScopeEndTime") is not None:
        import capo_detective.types.timestamp

        out["scope_end_time"] = capo_detective.types.timestamp.deserialize_json(
            data["ScopeEndTime"]
        )
    else:
        import datetime

        out["scope_end_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
