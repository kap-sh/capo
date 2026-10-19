"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryInsights``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.query_insights_mode


class QueryInsights(TypedDict, closed=True):
    mode: "capo_timestream_query.types.query_insights_mode.QueryInsightsMode"
    """<p>Provides the following modes to enable <code>QueryInsights</code>:</p> <ul> <li> <p> <code>ENABLED_WITH_RATE_CONTROL</code> – Enables <code>QueryInsights</code> for the queries being processed. This mode also includes a rate control mechanism, which limits the <code>QueryInsights</code> feature to 1 query per second (QPS).</p> </li> <li> <p> <code>DISABLED</code> – Disables <code>QueryInsights</code>.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryInsights) -> dict:
    out: dict = {}
    import capo_timestream_query.types.query_insights_mode

    out["Mode"] = (
        capo_timestream_query.types.query_insights_mode.serialize_aws_json_1_0(
            value["mode"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryInsights:
    out: QueryInsights = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_timestream_query.types.query_insights_mode

        out["mode"] = (
            capo_timestream_query.types.query_insights_mode.deserialize_aws_json_1_0(
                data["Mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_timestream_query.types.query_insights_mode.QueryInsightsMode", ""
        )
    return out
