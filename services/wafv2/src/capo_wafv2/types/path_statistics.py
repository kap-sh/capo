"""Generated from Smithy shape ``com.amazonaws.wafv2#PathStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.bot_statistics_list
    import capo_wafv2.types.filter_source
    import capo_wafv2.types.path_string
    import capo_wafv2.types.percentage_value
    import capo_wafv2.types.request_count


class PathStatistics(TypedDict, closed=True):
    source: NotRequired["capo_wafv2.types.filter_source.FilterSource"]
    """<p>Information about the bot filter that was applied to generate these statistics. This field is only populated when you filter by bot category, organization, or name.</p>"""
    path: "capo_wafv2.types.path_string.PathString"
    """<p>The URI path. For example, <code>/api/</code> or <code>/api/v1/users</code>.</p>"""
    request_count: "capo_wafv2.types.request_count.RequestCount"
    """<p>The number of requests to this path within the specified time window.</p>"""
    percentage: "capo_wafv2.types.percentage_value.PercentageValue"
    """<p>The percentage of total requests that were made to this path.</p>"""
    top_bots: NotRequired["capo_wafv2.types.bot_statistics_list.BotStatisticsList"]
    """<p>The list of top bots accessing this path, ordered by request count. The number of bots included is determined by the <code>NumberOfTopTrafficBotsPerPath</code> parameter in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PathStatistics) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_wafv2.types.filter_source

        out["Source"] = capo_wafv2.types.filter_source.serialize_aws_json_1_1(
            value["source"]
        )
    out["Path"] = value["path"]
    out["RequestCount"] = value.get("request_count", 0)
    out["Percentage"] = (
        "NaN"
        if value.get("percentage", 0) != value.get("percentage", 0)
        else "Infinity"
        if value.get("percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("percentage", 0) == float("-inf")
        else value.get("percentage", 0)
    )
    if "top_bots" in value:
        import capo_wafv2.types.bot_statistics_list

        out["TopBots"] = capo_wafv2.types.bot_statistics_list.serialize_aws_json_1_1(
            value["top_bots"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PathStatistics:
    out: PathStatistics = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        import capo_wafv2.types.filter_source

        out["source"] = capo_wafv2.types.filter_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    else:
        out["path"] = ""
    if data.get("RequestCount") is not None:
        out["request_count"] = data["RequestCount"]
    else:
        out["request_count"] = 0
    if data.get("Percentage") is not None:
        out["percentage"] = float(data["Percentage"])
    else:
        out["percentage"] = 0
    if data.get("TopBots") is not None:
        import capo_wafv2.types.bot_statistics_list

        out["top_bots"] = capo_wafv2.types.bot_statistics_list.deserialize_aws_json_1_1(
            data["TopBots"]
        )
    return out
