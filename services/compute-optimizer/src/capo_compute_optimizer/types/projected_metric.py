"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ProjectedMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.metric_name
    import capo_compute_optimizer.types.metric_values
    import capo_compute_optimizer.types.timestamps


class ProjectedMetric(TypedDict, closed=True):
    name: NotRequired["capo_compute_optimizer.types.metric_name.MetricName"]
    """<p>The name of the projected utilization metric.</p> <p>The following projected utilization metrics are returned:</p> <ul> <li> <p> <code>Cpu</code> - The projected percentage of allocated EC2 compute units that would be in use on the recommendation option had you used that resource during the analyzed period. This metric identifies the processing power required to run an application on the recommendation option.</p> <p>Depending on the instance type, tools in your operating system can show a lower percentage than CloudWatch when the instance is not allocated a full processor core.</p> </li> <li> <p> <code>Memory</code> - The percentage of memory that would be in use on the recommendation option had you used that resource during the analyzed period. This metric identifies the amount of memory required to run an application on the recommendation option.</p> <p>Units: Percent</p> <note> <p>The <code>Memory</code> metric is only returned for resources with the unified CloudWatch agent installed on them. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent">Enabling Memory Utilization with the CloudWatch Agent</a>.</p> </note> </li> <li> <p> <code>GPU</code> - The projected percentage of allocated GPUs if you adjust your configurations to Compute Optimizer's recommendation option.</p> </li> <li> <p> <code>GPU_MEMORY</code> - The projected percentage of total GPU memory if you adjust your configurations to Compute Optimizer's recommendation option.</p> <note> <p>The <code>GPU</code> and <code>GPU_MEMORY</code> metrics are only returned for resources with the unified CloudWatch Agent installed on them. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#nvidia-cw-agent">Enabling NVIDIA GPU utilization with the CloudWatch Agent</a>.</p> </note> </li> </ul>"""
    timestamps: NotRequired["capo_compute_optimizer.types.timestamps.Timestamps"]
    """<p>The timestamps of the projected utilization metric.</p>"""
    values: NotRequired["capo_compute_optimizer.types.metric_values.MetricValues"]
    """<p>The values of the projected utilization metrics.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProjectedMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.metric_name

        out["name"] = capo_compute_optimizer.types.metric_name.serialize_aws_json_1_0(
            value["name"]
        )
    if "timestamps" in value:
        import capo_compute_optimizer.types.timestamps

        out["timestamps"] = (
            capo_compute_optimizer.types.timestamps.serialize_aws_json_1_0(
                value["timestamps"]
            )
        )
    if "values" in value:
        import capo_compute_optimizer.types.metric_values

        out["values"] = (
            capo_compute_optimizer.types.metric_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProjectedMetric:
    out: ProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.metric_name

        out["name"] = capo_compute_optimizer.types.metric_name.deserialize_aws_json_1_0(
            data["name"]
        )
    if data.get("timestamps") is not None:
        import capo_compute_optimizer.types.timestamps

        out["timestamps"] = (
            capo_compute_optimizer.types.timestamps.deserialize_aws_json_1_0(
                data["timestamps"]
            )
        )
    if data.get("values") is not None:
        import capo_compute_optimizer.types.metric_values

        out["values"] = (
            capo_compute_optimizer.types.metric_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out
