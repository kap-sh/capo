"""Generated from Smithy shape ``com.amazonaws.inspector2#Usage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cloud_provider
    import capo_inspector2.types.currency
    import capo_inspector2.types.monthly_cost_estimate
    import capo_inspector2.types.usage_type
    import capo_inspector2.types.usage_value


class Usage(TypedDict, closed=True):
    type: NotRequired["capo_inspector2.types.usage_type.UsageType"]
    """<p>The type of scan. Valid values:</p> <ul> <li> <p>Amazon Web Services – <code>EC2_INSTANCE_HOURS</code>, <code>EC2_AGENTLESS_INSTANCE_HOURS</code>, <code>EC2_AMI_HOURS</code>, <code>EC2_AMI_ONE_SHOT_SCAN</code>, <code>ECR_INITIAL_SCAN</code>, <code>ECR_RESCAN</code>, <code>LAMBDA_FUNCTION_HOURS</code>, <code>LAMBDA_FUNCTION_CODE_HOURS</code>, <code>CODE_REPOSITORY_SAST</code>, <code>CODE_REPOSITORY_IAC</code>, or <code>CODE_REPOSITORY_SCA</code>.</p> </li> <li> <p>Microsoft Azure – <code>AZURE_VM_AGENT_BASED_INSTANCE_HOURS</code>, <code>AZURE_CONTAINER_IMAGE_INITIAL_SCAN</code>, <code>AZURE_CONTAINER_IMAGE_RESCAN</code>, or <code>AZURE_SERVERLESS_FUNCTION_HOURS</code>.</p> </li> <li> <p>Google Cloud Platform (GCP) – <code>GCP_VM_AGENT_BASED_INSTANCE_HOURS</code>, <code>GCP_CONTAINER_IMAGE_INITIAL_SCAN</code>, <code>GCP_CONTAINER_IMAGE_RESCAN</code>, or <code>GCP_CLOUD_RUN_HOURS</code> (Cloud Run functions).</p> </li> </ul>"""
    total: "capo_inspector2.types.usage_value.UsageValue"
    """<p>The total of usage.</p>"""
    estimated_monthly_cost: (
        "capo_inspector2.types.monthly_cost_estimate.MonthlyCostEstimate"
    )
    """<p>The estimated monthly cost of Amazon Inspector.</p>"""
    currency: NotRequired["capo_inspector2.types.currency.Currency"]
    """<p>The currency type used when calculating usage data.</p>"""
    cloud_provider: NotRequired["capo_inspector2.types.cloud_provider.CloudProvider"]
    """<p>The cloud provider associated with the usage information. Valid values:</p> <ul> <li> <p> <code>AWS</code> – Amazon Web Services resources.</p> </li> <li> <p> <code>AZURE</code> – Microsoft Azure resources.</p> </li> <li> <p> <code>GCP</code> – Google Cloud Platform (GCP) resources.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Usage) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    out["total"] = (
        "NaN"
        if value.get("total", 0) != value.get("total", 0)
        else "Infinity"
        if value.get("total", 0) == float("inf")
        else "-Infinity"
        if value.get("total", 0) == float("-inf")
        else value.get("total", 0)
    )
    out["estimatedMonthlyCost"] = (
        "NaN"
        if value.get("estimated_monthly_cost", 0)
        != value.get("estimated_monthly_cost", 0)
        else "Infinity"
        if value.get("estimated_monthly_cost", 0) == float("inf")
        else "-Infinity"
        if value.get("estimated_monthly_cost", 0) == float("-inf")
        else value.get("estimated_monthly_cost", 0)
    )
    if "currency" in value:
        out["currency"] = value["currency"]
    if "cloud_provider" in value:
        out["cloudProvider"] = value["cloud_provider"]
    return out


def deserialize_json(data: dict) -> Usage:
    out: Usage = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("total") is not None:
        out["total"] = float(data["total"])
    else:
        out["total"] = 0
    if data.get("estimatedMonthlyCost") is not None:
        out["estimated_monthly_cost"] = float(data["estimatedMonthlyCost"])
    else:
        out["estimated_monthly_cost"] = 0
    if data.get("currency") is not None:
        out["currency"] = data["currency"]
    if data.get("cloudProvider") is not None:
        out["cloud_provider"] = data["cloudProvider"]
    return out
