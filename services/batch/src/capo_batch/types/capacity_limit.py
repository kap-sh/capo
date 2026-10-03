"""Generated from Smithy shape ``com.amazonaws.batch#CapacityLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.string


class CapacityLimit(TypedDict, closed=True):
    max_capacity: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum capacity available for the service environment. For a quota management enabled service environment, this value represents the maximum quantity of a particular resource type (specified by <code>capacityUnit</code>) that can be allocated to service jobs. For other service environments, this value represents the maximum quantity of all resources that can be allocated to service jobs.</p> <p>For example, if <code>maxCapacity=50</code> and <code>capacityUnit=NUM_INSTANCES</code>, you can run up to 50 instances concurrently. If you run 5 SageMaker Training jobs that each use 10 instances, a subsequent job requiring 10 instances waits in the queue until capacity is available. In a quota management enabled service environment with <code>capacityUnit=ml.m5.large</code>, only <code>ml.m5.large</code> instances count against this limit, and jobs requiring other instance types wait until a matching capacity limit is configured.</p>"""
    capacity_unit: NotRequired["capo_batch.types.string.String"]
    """<p>The unit of measure for the capacity limit, which defines how <code>maxCapacity</code> is interpreted. For <code>SAGEMAKER_TRAINING</code> jobs in a quota management enabled service environment, specify the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceConfig.html#sagemaker-Type-ResourceConfig-InstanceType">instance type</a> (for example, <code>ml.m5.large</code>). Otherwise, use <code>NUM_INSTANCES</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityLimit) -> dict:
    out: dict = {}
    if "max_capacity" in value:
        out["maxCapacity"] = value["max_capacity"]
    if "capacity_unit" in value:
        out["capacityUnit"] = value["capacity_unit"]
    return out


def deserialize_json(data: dict) -> CapacityLimit:
    out: CapacityLimit = {}  # type: ignore[typeddict-item]
    if data.get("maxCapacity") is not None:
        out["max_capacity"] = data["maxCapacity"]
    if data.get("capacityUnit") is not None:
        out["capacity_unit"] = data["capacityUnit"]
    return out
