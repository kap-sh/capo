"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemoryStrategy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_strategy_configuration
    import capo_opensearchmemory.types.memory_strategy_description
    import capo_opensearchmemory.types.memory_strategy_name
    import capo_opensearchmemory.types.memory_strategy_type


class MemoryStrategy(TypedDict, closed=True):
    type: "capo_opensearchmemory.types.memory_strategy_type.MemoryStrategyType"
    """<p>The type of memory the strategy extracts.</p>"""
    name: NotRequired[
        "capo_opensearchmemory.types.memory_strategy_name.MemoryStrategyName"
    ]
    """<p>A name for the strategy, unique within the space. Omit it to have the service generate one from the type, for example <code>semantic_1</code>. The name must be 1 to 64 characters: letters, digits, periods, hyphens, and underscores, starting with a letter or digit. A strategy's name can't be changed, and the strategy's memories are stored under it: a strategy added under a new name starts with no memories.</p>"""
    description: NotRequired[
        "capo_opensearchmemory.types.memory_strategy_description.MemoryStrategyDescription"
    ]
    """<p>A description of the strategy.</p>"""
    configuration: NotRequired[
        "capo_opensearchmemory.types.memory_strategy_configuration.MemoryStrategyConfiguration"
    ]
    """<p>Settings for the strategy. When you create a strategy, omit it to use the defaults for the strategy's type.</p> <p>A <code>CUSTOM</code> strategy must set <code>extractionPrompt</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemoryStrategy) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.memory_strategy_type

    out["type"] = (
        capo_opensearchmemory.types.memory_strategy_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "configuration" in value:
        import capo_opensearchmemory.types.memory_strategy_configuration

        out["configuration"] = (
            capo_opensearchmemory.types.memory_strategy_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MemoryStrategy:
    out: MemoryStrategy = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_opensearchmemory.types.memory_strategy_type

        out["type"] = (
            capo_opensearchmemory.types.memory_strategy_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_opensearchmemory.types.memory_strategy_type.MemoryStrategyType", ""
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("configuration") is not None:
        import capo_opensearchmemory.types.memory_strategy_configuration

        out["configuration"] = (
            capo_opensearchmemory.types.memory_strategy_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    return out


def redact_sensitive(value: MemoryStrategy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_opensearchmemory.types.memory_strategy_configuration

        out["configuration"] = (
            capo_opensearchmemory.types.memory_strategy_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
