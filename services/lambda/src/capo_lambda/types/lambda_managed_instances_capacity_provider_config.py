"""Generated from Smithy shape ``com.amazonaws.lambda#LambdaManagedInstancesCapacityProviderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_arn
    import capo_lambda.types.execution_environment_memory_gi_b_per_v_cpu
    import capo_lambda.types.per_execution_environment_max_concurrency


class LambdaManagedInstancesCapacityProviderConfig(TypedDict, closed=True):
    capacity_provider_arn: "capo_lambda.types.capacity_provider_arn.CapacityProviderArn"
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    per_execution_environment_max_concurrency: NotRequired[
        "capo_lambda.types.per_execution_environment_max_concurrency.PerExecutionEnvironmentMaxConcurrency"
    ]
    """<p>The maximum number of concurrent execution environments that can run on each compute instance.</p>"""
    execution_environment_memory_gi_b_per_v_cpu: NotRequired[
        "capo_lambda.types.execution_environment_memory_gi_b_per_v_cpu.ExecutionEnvironmentMemoryGiBPerVCpu"
    ]
    """<p>The amount of memory in GiB allocated per vCPU for execution environments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaManagedInstancesCapacityProviderConfig) -> dict:
    out: dict = {}
    out["CapacityProviderArn"] = value["capacity_provider_arn"]
    if "per_execution_environment_max_concurrency" in value:
        out["PerExecutionEnvironmentMaxConcurrency"] = value[
            "per_execution_environment_max_concurrency"
        ]
    if "execution_environment_memory_gi_b_per_v_cpu" in value:
        out["ExecutionEnvironmentMemoryGiBPerVCpu"] = (
            "NaN"
            if value["execution_environment_memory_gi_b_per_v_cpu"]
            != value["execution_environment_memory_gi_b_per_v_cpu"]
            else "Infinity"
            if value["execution_environment_memory_gi_b_per_v_cpu"] == float("inf")
            else "-Infinity"
            if value["execution_environment_memory_gi_b_per_v_cpu"] == float("-inf")
            else value["execution_environment_memory_gi_b_per_v_cpu"]
        )
    return out


def deserialize_json(data: dict) -> LambdaManagedInstancesCapacityProviderConfig:
    out: LambdaManagedInstancesCapacityProviderConfig = {}  # type: ignore[typeddict-item]
    if data.get("CapacityProviderArn") is not None:
        out["capacity_provider_arn"] = data["CapacityProviderArn"]
    else:
        out["capacity_provider_arn"] = ""
    if data.get("PerExecutionEnvironmentMaxConcurrency") is not None:
        out["per_execution_environment_max_concurrency"] = data[
            "PerExecutionEnvironmentMaxConcurrency"
        ]
    if data.get("ExecutionEnvironmentMemoryGiBPerVCpu") is not None:
        out["execution_environment_memory_gi_b_per_v_cpu"] = float(
            data["ExecutionEnvironmentMemoryGiBPerVCpu"]
        )
    return out
