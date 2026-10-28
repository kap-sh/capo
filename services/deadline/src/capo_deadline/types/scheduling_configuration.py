"""Generated from Smithy shape ``com.amazonaws.deadline#SchedulingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.priority_balanced_scheduling_configuration
    import capo_deadline.types.priority_fifo_scheduling_configuration
    import capo_deadline.types.weighted_balanced_scheduling_configuration


class SchedulingConfigurationPriorityFifoMember(TypedDict, closed=True):
    priorityFifo: "capo_deadline.types.priority_fifo_scheduling_configuration.PriorityFifoSchedulingConfiguration"


class SchedulingConfigurationPriorityBalancedMember(TypedDict, closed=True):
    priorityBalanced: "capo_deadline.types.priority_balanced_scheduling_configuration.PriorityBalancedSchedulingConfiguration"


class SchedulingConfigurationWeightedBalancedMember(TypedDict, closed=True):
    weightedBalanced: "capo_deadline.types.weighted_balanced_scheduling_configuration.WeightedBalancedSchedulingConfiguration"


SchedulingConfiguration: TypeAlias = (
    SchedulingConfigurationPriorityFifoMember
    | SchedulingConfigurationPriorityBalancedMember
    | SchedulingConfigurationWeightedBalancedMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SchedulingConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "priorityFifo" in value:
        import capo_deadline.types.priority_fifo_scheduling_configuration

        return {
            "priorityFifo": capo_deadline.types.priority_fifo_scheduling_configuration.serialize_json(
                value["priorityFifo"]
            )
        }
    elif "priorityBalanced" in value:
        import capo_deadline.types.priority_balanced_scheduling_configuration

        return {
            "priorityBalanced": capo_deadline.types.priority_balanced_scheduling_configuration.serialize_json(
                value["priorityBalanced"]
            )
        }
    elif "weightedBalanced" in value:
        import capo_deadline.types.weighted_balanced_scheduling_configuration

        return {
            "weightedBalanced": capo_deadline.types.weighted_balanced_scheduling_configuration.serialize_json(
                value["weightedBalanced"]
            )
        }
    else:
        raise SerializationError("SchedulingConfiguration: no variant present")


def deserialize_json(data: dict) -> SchedulingConfiguration:
    if data.get("priorityFifo") is not None:
        import capo_deadline.types.priority_fifo_scheduling_configuration

        return {
            "priorityFifo": capo_deadline.types.priority_fifo_scheduling_configuration.deserialize_json(
                data["priorityFifo"]
            )
        }
    elif data.get("priorityBalanced") is not None:
        import capo_deadline.types.priority_balanced_scheduling_configuration

        return {
            "priorityBalanced": capo_deadline.types.priority_balanced_scheduling_configuration.deserialize_json(
                data["priorityBalanced"]
            )
        }
    elif data.get("weightedBalanced") is not None:
        import capo_deadline.types.weighted_balanced_scheduling_configuration

        return {
            "weightedBalanced": capo_deadline.types.weighted_balanced_scheduling_configuration.deserialize_json(
                data["weightedBalanced"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SchedulingConfiguration: no recognized variant key")
