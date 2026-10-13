"""Generated from Smithy shape ``com.amazonaws.pipes#PlacementStrategy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.placement_strategy_field
    import capo_pipes.types.placement_strategy_type


class PlacementStrategy(TypedDict, closed=True):
    type: NotRequired["capo_pipes.types.placement_strategy_type.PlacementStrategyType"]
    """<p>The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task). </p>"""
    field: NotRequired[
        "capo_pipes.types.placement_strategy_field.PlacementStrategyField"
    ]
    """<p>The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are cpu and memory. For the random placement strategy, this field is not used. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlacementStrategy) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "field" in value:
        out["field"] = value["field"]
    return out


def deserialize_json(data: dict) -> PlacementStrategy:
    out: PlacementStrategy = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("field") is not None:
        out["field"] = data["field"]
    return out


def redact_sensitive(value: PlacementStrategy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field" in value:
        out["field"] = "*** Sensitive Data Redacted ***"
    return out
