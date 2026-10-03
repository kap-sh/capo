"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.max_depth
    import capo_codeguruprofiler.types.period
    import capo_codeguruprofiler.types.profiling_group_name
    import capo_codeguruprofiler.types.timestamp


class GetProfileRequest(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group to get.</p>"""
    start_time: NotRequired["capo_codeguruprofiler.types.timestamp.Timestamp"]
    """<p>The start time of the profile to get. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p> <p> If you specify <code>startTime</code>, then you must also specify <code>period</code> or <code>endTime</code>, but not both. </p>"""
    period: NotRequired["capo_codeguruprofiler.types.period.Period"]
    """<p> Used with <code>startTime</code> or <code>endTime</code> to specify the time range for the returned aggregated profile. Specify using the ISO 8601 format. For example, <code>P1DT1H1M1S</code>. </p> <p> To get the latest aggregated profile, specify only <code>period</code>. </p>"""
    end_time: NotRequired["capo_codeguruprofiler.types.timestamp.Timestamp"]
    """<p> The end time of the requested profile. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p> <p> If you specify <code>endTime</code>, then you must also specify <code>period</code> or <code>startTime</code>, but not both. </p>"""
    max_depth: NotRequired["capo_codeguruprofiler.types.max_depth.MaxDepth"]
    """<p> The maximum depth of the stacks in the code that is represented in the aggregated profile. For example, if CodeGuru Profiler finds a method <code>A</code>, which calls method <code>B</code>, which calls method <code>C</code>, which calls method <code>D</code>, then the depth is 4. If the <code>maxDepth</code> is set to 2, then the aggregated profile contains representations of methods <code>A</code> and <code>B</code>. </p>"""
    accept: NotRequired["str"]
    """<p> The format of the returned profiling data. The format maps to the <code>Accept</code> and <code>Content-Type</code> headers of the HTTP request. You can specify one of the following: or the default . </p> <ul> <li> <p> <code>application/json</code> — standard JSON format </p> </li> <li> <p> <code>application/x-amzn-ion</code> — the Amazon Ion data format. For more information, see <a href="http://amzn.github.io/ion-docs/">Amazon Ion</a>. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProfileRequest:
    out: GetProfileRequest = {}  # type: ignore[typeddict-item]
    return out
