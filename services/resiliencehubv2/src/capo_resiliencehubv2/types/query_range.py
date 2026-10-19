"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#QueryRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.query_data_point_list
    import capo_resiliencehubv2.types.query_granularity


class QueryRange(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start time of the query range.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time of the query range.</p>"""
    granularity: "capo_resiliencehubv2.types.query_granularity.QueryGranularity"
    """<p>The granularity of the query range data points.</p>"""
    data_points: "capo_resiliencehubv2.types.query_data_point_list.QueryDataPointList"
    """<p>The data points within the query range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryRange) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types._prelude.timestamp

    out["startTime"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_resiliencehubv2.types._prelude.timestamp

    out["endTime"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    import capo_resiliencehubv2.types.query_granularity

    out["granularity"] = capo_resiliencehubv2.types.query_granularity.serialize_json(
        value["granularity"]
    )
    import capo_resiliencehubv2.types.query_data_point_list

    out["dataPoints"] = capo_resiliencehubv2.types.query_data_point_list.serialize_json(
        value["data_points"]
    )
    return out


def deserialize_json(data: dict) -> QueryRange:
    out: QueryRange = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["start_time"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["end_time"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("granularity") is not None:
        import capo_resiliencehubv2.types.query_granularity

        out["granularity"] = (
            capo_resiliencehubv2.types.query_granularity.deserialize_json(
                data["granularity"]
            )
        )
    else:
        import typing

        out["granularity"] = typing.cast(
            "capo_resiliencehubv2.types.query_granularity.QueryGranularity", ""
        )
    if data.get("dataPoints") is not None:
        import capo_resiliencehubv2.types.query_data_point_list

        out["data_points"] = (
            capo_resiliencehubv2.types.query_data_point_list.deserialize_json(
                data["dataPoints"]
            )
        )
    else:
        out["data_points"] = []
    return out
