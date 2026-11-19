"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.filter_name
    import capo_compute_optimizer.types.filter_values


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_compute_optimizer.types.filter_name.FilterName"]
    """<p>The name of the filter.</p> <p>Specify <code>Finding</code> to return recommendations with a specific finding classification. For example, <code>Underprovisioned</code>.</p> <p>Specify <code>RecommendationSourceType</code> to return recommendations of a specific resource type. For example, <code>Ec2Instance</code>.</p> <p>Specify <code>FindingReasonCodes</code> to return recommendations with a specific finding reason code. For example, <code>CPUUnderprovisioned</code>.</p> <p>Specify <code>InferredWorkloadTypes</code> to return recommendations of a specific inferred workload. For example, <code>Redis</code>.</p> <p>You can filter your EC2 instance recommendations by <code>tag:key</code> and <code>tag-key</code> tags.</p> <p>A <code>tag:key</code> is a key and value combination of a tag assigned to your recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all recommendations that have a tag with the key of <code>Owner</code> and the value of <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> <p>A <code>tag-key</code> is the key of a tag assigned to your recommendations. Use this filter to find all of your recommendations that have a tag with a specific key. This doesn’t consider the tag value. For example, you can find your recommendations with a tag key value of <code>Owner</code> or without any tag keys assigned.</p>"""
    values: NotRequired["capo_compute_optimizer.types.filter_values.FilterValues"]
    """<p>The value of the filter.</p> <p>The valid values for this parameter are as follows, depending on what you specify for the <code>name</code> parameter and the resource type that you wish to filter results for:</p> <ul> <li> <p>Specify <code>Optimized</code> or <code>NotOptimized</code> if you specify the <code>name</code> parameter as <code>Finding</code> and you want to filter results for Auto Scaling groups.</p> </li> <li> <p>Specify <code>Underprovisioned</code>, <code>Overprovisioned</code>, or <code>Optimized</code> if you specify the <code>name</code> parameter as <code>Finding</code> and you want to filter results for EC2 instances.</p> </li> <li> <p>Specify <code>Ec2Instance</code> or <code>AutoScalingGroup</code> if you specify the <code>name</code> parameter as <code>RecommendationSourceType</code>.</p> </li> <li> <p>Specify one of the following options if you specify the <code>name</code> parameter as <code>FindingReasonCodes</code>:</p> <ul> <li> <p> <b> <code>CPUOverprovisioned</code> </b> — The instance’s CPU configuration can be sized down while still meeting the performance requirements of your workload.</p> </li> <li> <p> <b> <code>CPUUnderprovisioned</code> </b> — The instance’s CPU configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better CPU performance.</p> </li> <li> <p> <b> <code>MemoryOverprovisioned</code> </b> — The instance’s memory configuration can be sized down while still meeting the performance requirements of your workload.</p> </li> <li> <p> <b> <code>MemoryUnderprovisioned</code> </b> — The instance’s memory configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better memory performance.</p> </li> <li> <p> <b> <code>EBSThroughputOverprovisioned</code> </b> — The instance’s EBS throughput configuration can be sized down while still meeting the performance requirements of your workload.</p> </li> <li> <p> <b> <code>EBSThroughputUnderprovisioned</code> </b> — The instance’s EBS throughput configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance.</p> </li> <li> <p> <b> <code>EBSIOPSOverprovisioned</code> </b> — The instance’s EBS IOPS configuration can be sized down while still meeting the performance requirements of your workload.</p> </li> <li> <p> <b> <code>EBSIOPSUnderprovisioned</code> </b> — The instance’s EBS IOPS configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS IOPS performance.</p> </li> <li> <p> <b> <code>NetworkBandwidthOverprovisioned</code> </b> — The instance’s network bandwidth configuration can be sized down while still meeting the performance requirements of your workload.</p> </li> <li> <p> <b> <code>NetworkBandwidthUnderprovisioned</code> </b> — The instance’s network bandwidth configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better network bandwidth performance. This finding reason happens when the <code>NetworkIn</code> or <code>NetworkOut</code> performance of an instance is impacted.</p> </li> <li> <p> <b> <code>NetworkPPSOverprovisioned</code> </b> — The instance’s network PPS (packets per second) configuration can be sized down while still meeting the performance requirements of your workload.</p> </li> <li> <p> <b> <code>NetworkPPSUnderprovisioned</code> </b> — The instance’s network PPS (packets per second) configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better network PPS performance.</p> </li> <li> <p> <b> <code>DiskIOPSOverprovisioned</code> </b> — The instance’s disk IOPS configuration can be sized down while still meeting the performance requirements of your workload.</p> </li> <li> <p> <b> <code>DiskIOPSUnderprovisioned</code> </b> — The instance’s disk IOPS configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better disk IOPS performance.</p> </li> <li> <p> <b> <code>DiskThroughputOverprovisioned</code> </b> — The instance’s disk throughput configuration can be sized down while still meeting the performance requirements of your workload.</p> </li> <li> <p> <b> <code>DiskThroughputUnderprovisioned</code> </b> — The instance’s disk throughput configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better disk throughput performance.</p> </li> </ul> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.filter_name

        out["name"] = capo_compute_optimizer.types.filter_name.serialize_aws_json_1_0(
            value["name"]
        )
    if "values" in value:
        import capo_compute_optimizer.types.filter_values

        out["values"] = (
            capo_compute_optimizer.types.filter_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.filter_name

        out["name"] = capo_compute_optimizer.types.filter_name.deserialize_aws_json_1_0(
            data["name"]
        )
    if data.get("values") is not None:
        import capo_compute_optimizer.types.filter_values

        out["values"] = (
            capo_compute_optimizer.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.filter_name

        out["name"] = capo_compute_optimizer.types.filter_name.serialize_cbor(
            value["name"]
        )
    if "values" in value:
        import capo_compute_optimizer.types.filter_values

        out["values"] = capo_compute_optimizer.types.filter_values.serialize_cbor(
            value["values"]
        )
    return out


def deserialize_cbor(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.filter_name

        out["name"] = capo_compute_optimizer.types.filter_name.deserialize_cbor(
            data["name"]
        )
    if data.get("values") is not None:
        import capo_compute_optimizer.types.filter_values

        out["values"] = capo_compute_optimizer.types.filter_values.deserialize_cbor(
            data["values"]
        )
    return out
