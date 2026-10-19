"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TumblingWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.interval
    import capo_iotsitewise.types.offset


class TumblingWindow(TypedDict, closed=True):
    interval: "capo_iotsitewise.types.interval.Interval"
    """<p>The time interval for the tumbling window. The interval time must be between 1 minute and 1 week.</p> <p>IoT SiteWise computes the <code>1w</code> interval the end of Sunday at midnight each week (UTC), the <code>1d</code> interval at the end of each day at midnight (UTC), the <code>1h</code> interval at the end of each hour, and so on. </p> <p>When IoT SiteWise aggregates data points for metric computations, the start of each interval is exclusive and the end of each interval is inclusive. IoT SiteWise places the computed data point at the end of the interval.</p>"""
    offset: NotRequired["capo_iotsitewise.types.offset.Offset"]
    """<p>The offset for the tumbling window. The <code>offset</code> parameter accepts the following:</p> <ul> <li> <p>The offset time.</p> <p>For example, if you specify <code>18h</code> for <code>offset</code> and <code>1d</code> for <code>interval</code>, IoT SiteWise aggregates data in one of the following ways:</p> <ul> <li> <p>If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric.</p> </li> <li> <p>If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day.</p> </li> </ul> </li> <li> <p>The ISO 8601 format.</p> <p>For example, if you specify <code>PT18H</code> for <code>offset</code> and <code>1d</code> for <code>interval</code>, IoT SiteWise aggregates data in one of the following ways:</p> <ul> <li> <p>If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric.</p> </li> <li> <p>If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day.</p> </li> </ul> </li> <li> <p>The 24-hour clock.</p> <p>For example, if you specify <code>00:03:00</code> for <code>offset</code>, <code>5m</code> for <code>interval</code>, and you create the metric at 2 PM (UTC), you get the first aggregation result at 2:03 PM (UTC). You get the second aggregation result at 2:08 PM (UTC). </p> </li> <li> <p>The offset time zone.</p> <p>For example, if you specify <code>2021-07-23T18:00-08</code> for <code>offset</code> and <code>1d</code> for <code>interval</code>, IoT SiteWise aggregates data in one of the following ways:</p> <ul> <li> <p>If you create the metric before or at 6 PM (PST), you get the first aggregation result at 6 PM (PST) on the day when you create the metric.</p> </li> <li> <p>If you create the metric after 6 PM (PST), you get the first aggregation result at 6 PM (PST) the next day.</p> </li> </ul> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TumblingWindow) -> dict:
    out: dict = {}
    out["interval"] = value["interval"]
    if "offset" in value:
        out["offset"] = value["offset"]
    return out


def deserialize_json(data: dict) -> TumblingWindow:
    out: TumblingWindow = {}  # type: ignore[typeddict-item]
    if data.get("interval") is not None:
        out["interval"] = data["interval"]
    else:
        out["interval"] = ""
    if data.get("offset") is not None:
        out["offset"] = data["offset"]
    return out
