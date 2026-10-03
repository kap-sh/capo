"""Generated from Smithy shape ``com.amazonaws.pi#ResponseResourceMetricKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pi.types.dimension_map
    import capo_pi.types.string


class ResponseResourceMetricKey(TypedDict, closed=True):
    metric: "capo_pi.types.string.String"
    """<p>The name of a Performance Insights metric to be measured.</p> <p>Valid values for <code>Metric</code> are:</p> <ul> <li> <p> <code>db.load.avg</code> - A scaled representation of the number of active sessions for the database engine.</p> </li> <li> <p> <code>db.sampledload.avg</code> - The raw number of active sessions for the database engine.</p> </li> <li> <p>The counter metrics listed in <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS">Performance Insights operating system counters</a> in the <i>Amazon Aurora User Guide</i>.</p> </li> <li> <p>The counter metrics listed in <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS">Performance Insights operating system counters</a> in the <i>Amazon RDS User Guide</i>.</p> </li> </ul> <p>If the number of active sessions is less than an internal Performance Insights threshold, <code>db.load.avg</code> and <code>db.sampledload.avg</code> are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with <code>db.load.avg</code> showing the scaled values, <code>db.sampledload.avg</code> showing the raw values, and <code>db.sampledload.avg</code> less than <code>db.load.avg</code>. For most use cases, you can query <code>db.load.avg</code> only. </p>"""
    dimensions: NotRequired["capo_pi.types.dimension_map.DimensionMap"]
    """<p>The valid dimensions for the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseResourceMetricKey) -> dict:
    out: dict = {}
    out["Metric"] = value["metric"]
    if "dimensions" in value:
        import capo_pi.types.dimension_map

        out["Dimensions"] = capo_pi.types.dimension_map.serialize_aws_json_1_1(
            value["dimensions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseResourceMetricKey:
    out: ResponseResourceMetricKey = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    else:
        raise DeserializationError("ResponseResourceMetricKey.metric required")
    if data.get("Dimensions") is not None:
        import capo_pi.types.dimension_map

        out["dimensions"] = capo_pi.types.dimension_map.deserialize_aws_json_1_1(
            data["Dimensions"]
        )
    return out
