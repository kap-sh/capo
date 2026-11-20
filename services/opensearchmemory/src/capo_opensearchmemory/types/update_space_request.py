"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#UpdateSpaceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_expiry_days
    import capo_opensearchmemory.types.extraction_model_id
    import capo_opensearchmemory.types.memory_expiry_days
    import capo_opensearchmemory.types.memory_strategy_list
    import capo_opensearchmemory.types.space_id


class UpdateSpaceRequest(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space to update.</p>"""
    memory_strategies: NotRequired[
        "capo_opensearchmemory.types.memory_strategy_list.MemoryStrategyList"
    ]
    """<p>The complete new list of memory strategies. The service removes strategies that aren't in the list from the space. Removing a strategy stops extraction for it but doesn't delete its memories: they're kept, until they expire if the space sets <code>memoryExpiryDays</code>, and they're available again if you later add a strategy with the same <code>type</code> and <code>name</code>. To delete them, use <code>DeleteMemory</code> before you remove the strategy, or delete the space.</p> <p>To keep a strategy, include it with the same <code>type</code> and <code>name</code> that <code>GetSpace</code> returns. For a kept strategy, any <code>configuration</code> member you omit keeps its current value. It doesn't return to the default, and you can't clear a member once it's set. Omit this field to leave the strategies unchanged. The list must name at least one strategy. You can't remove every strategy from a space with <code>UpdateSpace</code>.</p> <p>The serialized list can be at most 384 KiB.</p>"""
    event_expiry_days: NotRequired[
        "capo_opensearchmemory.types.event_expiry_days.EventExpiryDays"
    ]
    """<p>How many days the space keeps each event, from 1 to 365. Omit it to leave the current value unchanged. Events already stored keep the expiry they were written with.</p>"""
    memory_expiry_days: NotRequired[
        "capo_opensearchmemory.types.memory_expiry_days.MemoryExpiryDays"
    ]
    """<p>How many days the space keeps each memory, from 0 to 3650. 0 means memories never expire. Omit it to leave the current value unchanged. You can't clear the setting. To make memories written from then on never expire, send 0. <code>GetSpace</code> then returns 0.</p> <p>A change applies to memories written after it. Memories already stored keep the expiry they were written with. A memory the service rewrites later, such as a summary it keeps up to date, takes the setting in force at that rewrite. A change moves the space to <code>UPDATING</code>. Sending the value that the space has stored doesn't.</p>"""
    extraction_model_id: NotRequired[
        "capo_opensearchmemory.types.extraction_model_id.ExtractionModelId"
    ]
    """<p>The model that extracts and consolidates memories for every strategy in the space: <code>anthropic.claude-opus-5-5</code> or <code>anthropic.claude-haiku-5-5</code>. Omit it to leave the current value unchanged. Once set, it can't be cleared back to the service default.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSpaceRequest) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "memory_strategies" in value:
        import capo_opensearchmemory.types.memory_strategy_list

        out["memoryStrategies"] = (
            capo_opensearchmemory.types.memory_strategy_list.serialize_aws_json_1_0(
                value["memory_strategies"]
            )
        )
    if "event_expiry_days" in value:
        out["eventExpiryDays"] = value["event_expiry_days"]
    if "memory_expiry_days" in value:
        out["memoryExpiryDays"] = value["memory_expiry_days"]
    if "extraction_model_id" in value:
        out["extractionModelId"] = value["extraction_model_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSpaceRequest:
    out: UpdateSpaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("memoryStrategies") is not None:
        import capo_opensearchmemory.types.memory_strategy_list

        out["memory_strategies"] = (
            capo_opensearchmemory.types.memory_strategy_list.deserialize_aws_json_1_0(
                data["memoryStrategies"]
            )
        )
    if data.get("eventExpiryDays") is not None:
        out["event_expiry_days"] = data["eventExpiryDays"]
    if data.get("memoryExpiryDays") is not None:
        out["memory_expiry_days"] = data["memoryExpiryDays"]
    if data.get("extractionModelId") is not None:
        out["extraction_model_id"] = data["extractionModelId"]
    return out


def redact_sensitive(value: UpdateSpaceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memory_strategies" in value:
        import capo_opensearchmemory.types.memory_strategy_list

        out["memory_strategies"] = (
            capo_opensearchmemory.types.memory_strategy_list.redact_sensitive(
                value["memory_strategies"]
            )
        )
    return out
