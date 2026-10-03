"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetInterpolatedAssetPropertyValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.interpolation_type
    import capo_iotsitewise.types.interval_in_seconds
    import capo_iotsitewise.types.interval_window_in_seconds
    import capo_iotsitewise.types.max_interpolated_results
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.offset_in_nanos
    import capo_iotsitewise.types.quality
    import capo_iotsitewise.types.time_in_seconds


class GetInterpolatedAssetPropertyValuesRequest(TypedDict, closed=True):
    asset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset, in UUID format.</p>"""
    property_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset property, in UUID format.</p>"""
    property_alias: NotRequired[
        "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    start_time_in_seconds: "capo_iotsitewise.types.time_in_seconds.TimeInSeconds"
    """<p>The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time.</p>"""
    start_time_offset_in_nanos: NotRequired[
        "capo_iotsitewise.types.offset_in_nanos.OffsetInNanos"
    ]
    """<p>The nanosecond offset converted from <code>startTimeInSeconds</code>.</p>"""
    end_time_in_seconds: "capo_iotsitewise.types.time_in_seconds.TimeInSeconds"
    """<p>The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time.</p>"""
    end_time_offset_in_nanos: NotRequired[
        "capo_iotsitewise.types.offset_in_nanos.OffsetInNanos"
    ]
    """<p>The nanosecond offset converted from <code>endTimeInSeconds</code>.</p>"""
    quality: "capo_iotsitewise.types.quality.Quality"
    """<p>The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality.</p>"""
    interval_in_seconds: "capo_iotsitewise.types.interval_in_seconds.IntervalInSeconds"
    """<p>The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired[
        "capo_iotsitewise.types.max_interpolated_results.MaxInterpolatedResults"
    ]
    """<p>The maximum number of results to return for each paginated request. If not specified, the default value is 10.</p>"""
    type: "capo_iotsitewise.types.interpolation_type.InterpolationType"
    """<p>The interpolation type.</p> <p>Valid values: <code>LINEAR_INTERPOLATION | LOCF_INTERPOLATION</code> </p> <ul> <li> <p> <code>LINEAR_INTERPOLATION</code> – Estimates missing data using <a href="https://en.wikipedia.org/wiki/Linear_interpolation">linear interpolation</a>.</p> <p>For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.</p> </li> <li> <p> <code>LOCF_INTERPOLATION</code> – Estimates missing data using last observation carried forward interpolation</p> <p>If no data point is found for an interval, IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found.</p> <p>For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isn't found after 9 AM on July 2, 2021, IoT SiteWise uses the same interpolated value for the rest of the days.</p> </li> </ul>"""
    interval_window_in_seconds: NotRequired[
        "capo_iotsitewise.types.interval_window_in_seconds.IntervalWindowInSeconds"
    ]
    """<p>The query interval for the window, in seconds. IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.</p> <note> <ul> <li> <p>If you specify a value for the <code>intervalWindowInSeconds</code> parameter, the value for the <code>type</code> parameter must be <code>LINEAR_INTERPOLATION</code>.</p> </li> <li> <p>If a data point isn't found during the specified query window, IoT SiteWise won't return an interpolated value for the interval. This indicates that there's a gap in the ingested data points.</p> </li> </ul> </note> <p>For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInterpolatedAssetPropertyValuesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInterpolatedAssetPropertyValuesRequest:
    out: GetInterpolatedAssetPropertyValuesRequest = {}  # type: ignore[typeddict-item]
    return out
