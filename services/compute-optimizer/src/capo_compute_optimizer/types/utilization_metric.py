"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#UtilizationMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.metric_name
    import capo_compute_optimizer.types.metric_statistic
    import capo_compute_optimizer.types.metric_value


class UtilizationMetric(TypedDict, closed=True):
    name: NotRequired["capo_compute_optimizer.types.metric_name.MetricName"]
    """<p>The name of the utilization metric.</p> <p>The following utilization metrics are available:</p> <ul> <li> <p> <code>Cpu</code> - The percentage of allocated EC2 compute units that are currently in use on the instance. This metric identifies the processing power required to run an application on the instance.</p> <p>Depending on the instance type, tools in your operating system can show a lower percentage than CloudWatch when the instance is not allocated a full processor core.</p> <p>Units: Percent</p> </li> <li> <p> <code>Memory</code> - The percentage of memory that is currently in use on the instance. This metric identifies the amount of memory required to run an application on the instance.</p> <p>Units: Percent</p> <note> <p>The <code>Memory</code> metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent">Enabling Memory Utilization with the CloudWatch Agent</a>.</p> </note> </li> <li> <p> <code>GPU</code> - The percentage of allocated GPUs that currently run on the instance.</p> </li> <li> <p> <code>GPU_MEMORY</code> - The percentage of total GPU memory that currently runs on the instance.</p> <note> <p>The <code>GPU</code> and <code>GPU_MEMORY</code> metrics are only returned for resources with the unified CloudWatch Agent installed on them. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#nvidia-cw-agent">Enabling NVIDIA GPU utilization with the CloudWatch Agent</a>.</p> </note> </li> <li> <p> <code>EBS_READ_OPS_PER_SECOND</code> - The completed read operations from all EBS volumes attached to the instance in a specified period of time.</p> <p>Unit: Count</p> </li> <li> <p> <code>EBS_WRITE_OPS_PER_SECOND</code> - The completed write operations to all EBS volumes attached to the instance in a specified period of time.</p> <p>Unit: Count</p> </li> <li> <p> <code>EBS_READ_BYTES_PER_SECOND</code> - The bytes read from all EBS volumes attached to the instance in a specified period of time.</p> <p>Unit: Bytes</p> </li> <li> <p> <code>EBS_WRITE_BYTES_PER_SECOND</code> - The bytes written to all EBS volumes attached to the instance in a specified period of time.</p> <p>Unit: Bytes</p> </li> <li> <p> <code>DISK_READ_OPS_PER_SECOND</code> - The completed read operations from all instance store volumes available to the instance in a specified period of time.</p> <p>If there are no instance store volumes, either the value is <code>0</code> or the metric is not reported.</p> </li> <li> <p> <code>DISK_WRITE_OPS_PER_SECOND</code> - The completed write operations from all instance store volumes available to the instance in a specified period of time.</p> <p>If there are no instance store volumes, either the value is <code>0</code> or the metric is not reported.</p> </li> <li> <p> <code>DISK_READ_BYTES_PER_SECOND</code> - The bytes read from all instance store volumes available to the instance. This metric is used to determine the volume of the data the application reads from the disk of the instance. This can be used to determine the speed of the application.</p> <p>If there are no instance store volumes, either the value is <code>0</code> or the metric is not reported.</p> </li> <li> <p> <code>DISK_WRITE_BYTES_PER_SECOND</code> - The bytes written to all instance store volumes available to the instance. This metric is used to determine the volume of the data the application writes onto the disk of the instance. This can be used to determine the speed of the application.</p> <p>If there are no instance store volumes, either the value is <code>0</code> or the metric is not reported.</p> </li> <li> <p> <code>NETWORK_IN_BYTES_PER_SECOND</code> - The number of bytes received by the instance on all network interfaces. This metric identifies the volume of incoming network traffic to a single instance.</p> </li> <li> <p> <code>NETWORK_OUT_BYTES_PER_SECOND</code> - The number of bytes sent out by the instance on all network interfaces. This metric identifies the volume of outgoing network traffic from a single instance.</p> </li> <li> <p> <code>NETWORK_PACKETS_IN_PER_SECOND</code> - The number of packets received by the instance on all network interfaces. This metric identifies the volume of incoming traffic in terms of the number of packets on a single instance.</p> </li> <li> <p> <code>NETWORK_PACKETS_OUT_PER_SECOND</code> - The number of packets sent out by the instance on all network interfaces. This metric identifies the volume of outgoing traffic in terms of the number of packets on a single instance.</p> </li> </ul>"""
    statistic: NotRequired[
        "capo_compute_optimizer.types.metric_statistic.MetricStatistic"
    ]
    """<p>The statistic of the utilization metric.</p> <p>The Compute Optimizer API, Command Line Interface (CLI), and SDKs return utilization metrics using only the <code>Maximum</code> statistic, which is the highest value observed during the specified period.</p> <p>The Compute Optimizer console displays graphs for some utilization metrics using the <code>Average</code> statistic, which is the value of <code>Sum</code> / <code>SampleCount</code> during the specified period. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html">Viewing resource recommendations</a> in the <i>Compute Optimizer User Guide</i>. You can also get averaged utilization metric data for your resources using Amazon CloudWatch. For more information, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html">Amazon CloudWatch User Guide</a>.</p>"""
    value: "capo_compute_optimizer.types.metric_value.MetricValue"
    """<p>The value of the utilization metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UtilizationMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.metric_name

        out["name"] = capo_compute_optimizer.types.metric_name.serialize_aws_json_1_0(
            value["name"]
        )
    if "statistic" in value:
        import capo_compute_optimizer.types.metric_statistic

        out["statistic"] = (
            capo_compute_optimizer.types.metric_statistic.serialize_aws_json_1_0(
                value["statistic"]
            )
        )
    out["value"] = (
        "NaN"
        if value.get("value", 0) != value.get("value", 0)
        else "Infinity"
        if value.get("value", 0) == float("inf")
        else "-Infinity"
        if value.get("value", 0) == float("-inf")
        else value.get("value", 0)
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UtilizationMetric:
    out: UtilizationMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.metric_name

        out["name"] = capo_compute_optimizer.types.metric_name.deserialize_aws_json_1_0(
            data["name"]
        )
    if data.get("statistic") is not None:
        import capo_compute_optimizer.types.metric_statistic

        out["statistic"] = (
            capo_compute_optimizer.types.metric_statistic.deserialize_aws_json_1_0(
                data["statistic"]
            )
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out
