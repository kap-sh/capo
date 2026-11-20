"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemoryStrategyConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.extraction_prompt
    import capo_opensearchmemory.types.idle_timeout_seconds
    import capo_opensearchmemory.types.seed_memory_count
    import capo_opensearchmemory.types.token_count
    import capo_opensearchmemory.types.trigger_every_n_messages


class MemoryStrategyConfiguration(TypedDict, closed=True):
    extraction_prompt: NotRequired[
        "capo_opensearchmemory.types.extraction_prompt.ExtractionPrompt"
    ]
    """<p>Instructions that define what a <code>CUSTOM</code> strategy extracts, up to 30,720 characters. Required for a <code>CUSTOM</code> strategy: <code>CreateSpace</code> and <code>UpdateSpace</code> fail with <code>ValidationException</code> if a <code>CUSTOM</code> strategy has none.</p> <p>Only <code>CUSTOM</code> strategies use it. <code>SEMANTIC</code> and <code>SUMMARY</code> strategies always extract with the service's built-in instructions: the service accepts and stores a prompt on them, and <code>GetSpace</code> returns it, but extraction doesn't use it.</p>"""
    extract_every_n_messages: NotRequired[
        "capo_opensearchmemory.types.trigger_every_n_messages.TriggerEveryNMessages"
    ]
    """<p>Extract once this many messages have accumulated, from 1 to 1000. Lower values extract more often, in smaller batches. The default is 12.</p> <p>Messages accumulate until the first of <code>extractEveryNMessages</code>, <code>extractEveryNTokens</code>, and <code>idleTimeoutSeconds</code> is reached. The service then extracts them together in one pass.</p>"""
    extract_every_n_tokens: NotRequired[
        "capo_opensearchmemory.types.token_count.TokenCount"
    ]
    """<p>Extract once this many tokens of conversation have accumulated, from 1 to 80,000, however few messages that takes. Use it to bound how much text one extraction call carries when message sizes vary widely. Omit it to bound a batch only by <code>extractEveryNMessages</code>, <code>idleTimeoutSeconds</code>, and the service's maximum batch size.</p>"""
    idle_timeout_seconds: NotRequired[
        "capo_opensearchmemory.types.idle_timeout_seconds.IdleTimeoutSeconds"
    ]
    """<p>Extract what has accumulated once the conversation has been idle for this many seconds, from 1 to 86,400. The default is 60. This is what extracts the end of a conversation that stops. Raise it when the pauses in your conversations are longer than that, so that one exchange isn't split across several extraction passes.</p>"""
    extraction_seed_top_k: NotRequired[
        "capo_opensearchmemory.types.seed_memory_count.SeedMemoryCount"
    ]
    """<p>How many of the strategy's stored memories that are most relevant to the conversation to include in the extraction prompt, from 0 to 20, to improve extraction and reduce duplicates. If you omit this or set it to 0, the service uses its default (see <code>extractionSeedRecentN</code>). When this and <code>extractionSeedRecentN</code> are both set, the two sets of memories are combined without duplicates.</p>"""
    extraction_seed_recent_n: NotRequired[
        "capo_opensearchmemory.types.seed_memory_count.SeedMemoryCount"
    ]
    """<p>How many of the strategy's most recent stored memories to include in the extraction prompt, from 0 to 20. If you omit this or set it to 0, the service uses its default: no seeding for most strategy types, and the 10 most recent memories for a <code>SUMMARY</code> strategy when neither seed setting is given. When this and <code>extractionSeedTopK</code> are both set, the two sets of memories are combined without duplicates.</p>"""
    consolidation_enabled: NotRequired["bool"]
    """<p>Specifies whether the strategy consolidates memories. With consolidation, each new memory is compared with similar stored memories, and the service adds it, updates a stored memory, or skips it, so duplicate or contradicting facts don't accumulate. Without it, every extracted memory is stored as a new memory, which costs less and keeps a full history.</p> <p>When omitted, the default depends on the strategy's type: on for <code>SEMANTIC</code> and <code>SUMMARY</code>, off for <code>CUSTOM</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemoryStrategyConfiguration) -> dict:
    out: dict = {}
    if "extraction_prompt" in value:
        out["extractionPrompt"] = value["extraction_prompt"]
    if "extract_every_n_messages" in value:
        out["extractEveryNMessages"] = value["extract_every_n_messages"]
    if "extract_every_n_tokens" in value:
        out["extractEveryNTokens"] = value["extract_every_n_tokens"]
    if "idle_timeout_seconds" in value:
        out["idleTimeoutSeconds"] = value["idle_timeout_seconds"]
    if "extraction_seed_top_k" in value:
        out["extractionSeedTopK"] = value["extraction_seed_top_k"]
    if "extraction_seed_recent_n" in value:
        out["extractionSeedRecentN"] = value["extraction_seed_recent_n"]
    if "consolidation_enabled" in value:
        out["consolidationEnabled"] = value["consolidation_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MemoryStrategyConfiguration:
    out: MemoryStrategyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("extractionPrompt") is not None:
        out["extraction_prompt"] = data["extractionPrompt"]
    if data.get("extractEveryNMessages") is not None:
        out["extract_every_n_messages"] = data["extractEveryNMessages"]
    if data.get("extractEveryNTokens") is not None:
        out["extract_every_n_tokens"] = data["extractEveryNTokens"]
    if data.get("idleTimeoutSeconds") is not None:
        out["idle_timeout_seconds"] = data["idleTimeoutSeconds"]
    if data.get("extractionSeedTopK") is not None:
        out["extraction_seed_top_k"] = data["extractionSeedTopK"]
    if data.get("extractionSeedRecentN") is not None:
        out["extraction_seed_recent_n"] = data["extractionSeedRecentN"]
    if data.get("consolidationEnabled") is not None:
        out["consolidation_enabled"] = data["consolidationEnabled"]
    return out


def redact_sensitive(value: MemoryStrategyConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "extraction_prompt" in value:
        out["extraction_prompt"] = "*** Sensitive Data Redacted ***"
    return out
