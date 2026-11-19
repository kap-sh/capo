"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.cpu_vendor_architectures


class RecommendationPreferences(TypedDict, closed=True):
    cpu_vendor_architectures: NotRequired[
        "capo_compute_optimizer.types.cpu_vendor_architectures.CpuVendorArchitectures"
    ]
    """<p>Specifies the CPU vendor and architecture for Amazon EC2 instance and Auto Scaling group recommendations.</p> <p>For example, when you specify <code>AWS_ARM64</code> with:</p> <ul> <li> <p>A <a>GetEC2InstanceRecommendations</a> or <a>GetAutoScalingGroupRecommendations</a> request, Compute Optimizer returns recommendations that consist of Graviton instance types only.</p> </li> <li> <p>A <a>GetEC2RecommendationProjectedMetrics</a> request, Compute Optimizer returns projected utilization metrics for Graviton instance type recommendations only.</p> </li> <li> <p>A <a>ExportEC2InstanceRecommendations</a> or <a>ExportAutoScalingGroupRecommendations</a> request, Compute Optimizer exports recommendations that consist of Graviton instance types only.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationPreferences) -> dict:
    out: dict = {}
    if "cpu_vendor_architectures" in value:
        import capo_compute_optimizer.types.cpu_vendor_architectures

        out["cpuVendorArchitectures"] = (
            capo_compute_optimizer.types.cpu_vendor_architectures.serialize_aws_json_1_0(
                value["cpu_vendor_architectures"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationPreferences:
    out: RecommendationPreferences = {}  # type: ignore[typeddict-item]
    if data.get("cpuVendorArchitectures") is not None:
        import capo_compute_optimizer.types.cpu_vendor_architectures

        out["cpu_vendor_architectures"] = (
            capo_compute_optimizer.types.cpu_vendor_architectures.deserialize_aws_json_1_0(
                data["cpuVendorArchitectures"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationPreferences) -> dict:
    out: dict = {}
    if "cpu_vendor_architectures" in value:
        import capo_compute_optimizer.types.cpu_vendor_architectures

        out["cpuVendorArchitectures"] = (
            capo_compute_optimizer.types.cpu_vendor_architectures.serialize_cbor(
                value["cpu_vendor_architectures"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RecommendationPreferences:
    out: RecommendationPreferences = {}  # type: ignore[typeddict-item]
    if data.get("cpuVendorArchitectures") is not None:
        import capo_compute_optimizer.types.cpu_vendor_architectures

        out["cpu_vendor_architectures"] = (
            capo_compute_optimizer.types.cpu_vendor_architectures.deserialize_cbor(
                data["cpuVendorArchitectures"]
            )
        )
    return out
