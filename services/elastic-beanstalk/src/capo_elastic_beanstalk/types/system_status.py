"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SystemStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.cpu_utilization
    import capo_elastic_beanstalk.types.load_average


class SystemStatus(TypedDict, closed=True):
    cpu_utilization: NotRequired[
        "capo_elastic_beanstalk.types.cpu_utilization.CPUUtilization"
    ]
    """<p>CPU utilization metrics for the instance.</p>"""
    load_average: NotRequired["capo_elastic_beanstalk.types.load_average.LoadAverage"]
    """<p>Load average in the last 1-minute, 5-minute, and 15-minute periods. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-metrics.html#health-enhanced-metrics-os">Operating System Metrics</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SystemStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cpu_utilization" in value:
        import capo_elastic_beanstalk.types.cpu_utilization

        capo_elastic_beanstalk.types.cpu_utilization.serialize_query(
            value["cpu_utilization"], pairs, f"{key_prefix}CPUUtilization"
        )
    if "load_average" in value:
        import capo_elastic_beanstalk.types.load_average

        capo_elastic_beanstalk.types.load_average.serialize_query(
            value["load_average"], pairs, f"{key_prefix}LoadAverage"
        )


def deserialize_query(el: Element) -> SystemStatus:
    out: SystemStatus = {}  # type: ignore[typeddict-item]
    child_cpu_utilization = el.find("CPUUtilization")
    if child_cpu_utilization is not None:
        import capo_elastic_beanstalk.types.cpu_utilization

        out["cpu_utilization"] = (
            capo_elastic_beanstalk.types.cpu_utilization.deserialize_query(
                child_cpu_utilization
            )
        )
    child_load_average = el.find("LoadAverage")
    if child_load_average is not None:
        import capo_elastic_beanstalk.types.load_average

        out["load_average"] = (
            capo_elastic_beanstalk.types.load_average.deserialize_query(
                child_load_average
            )
        )
    return out
