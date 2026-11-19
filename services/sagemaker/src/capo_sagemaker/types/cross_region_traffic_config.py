"""Generated from Smithy shape ``com.amazonaws.sagemaker#CrossRegionTrafficConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cross_region_max_invocations_per_second_per_instance
    import capo_sagemaker.types.cross_region_percent_per_endpoint


class CrossRegionTrafficConfig(TypedDict, closed=True):
    max_invocations_per_second_per_instance: NotRequired[
        "capo_sagemaker.types.cross_region_max_invocations_per_second_per_instance.CrossRegionMaxInvocationsPerSecondPerInstance"
    ]
    """<p>The number of invocations per second that you expect one <code>InService</code> instance to serve. One value applies to every production variant, whatever its instance type.</p>"""
    max_cross_region_percent_per_endpoint: NotRequired[
        "capo_sagemaker.types.cross_region_percent_per_endpoint.CrossRegionPercentPerEndpoint"
    ]
    """<p>The percentage of the endpoint's capacity that requests from inference routers in other Amazon Web Services Regions can use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossRegionTrafficConfig) -> dict:
    out: dict = {}
    if "max_invocations_per_second_per_instance" in value:
        out["MaxInvocationsPerSecondPerInstance"] = value[
            "max_invocations_per_second_per_instance"
        ]
    if "max_cross_region_percent_per_endpoint" in value:
        out["MaxCrossRegionPercentPerEndpoint"] = value[
            "max_cross_region_percent_per_endpoint"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CrossRegionTrafficConfig:
    out: CrossRegionTrafficConfig = {}  # type: ignore[typeddict-item]
    if data.get("MaxInvocationsPerSecondPerInstance") is not None:
        out["max_invocations_per_second_per_instance"] = data[
            "MaxInvocationsPerSecondPerInstance"
        ]
    if data.get("MaxCrossRegionPercentPerEndpoint") is not None:
        out["max_cross_region_percent_per_endpoint"] = data[
            "MaxCrossRegionPercentPerEndpoint"
        ]
    return out
