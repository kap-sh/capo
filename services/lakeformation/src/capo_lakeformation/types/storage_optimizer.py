"""Generated from Smithy shape ``com.amazonaws.lakeformation#StorageOptimizer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.message_string
    import capo_lakeformation.types.optimizer_type
    import capo_lakeformation.types.storage_optimizer_config


class StorageOptimizer(TypedDict, closed=True):
    storage_optimizer_type: NotRequired[
        "capo_lakeformation.types.optimizer_type.OptimizerType"
    ]
    """<p>The specific type of storage optimizer. The supported value is <code>compaction</code>.</p>"""
    config: NotRequired[
        "capo_lakeformation.types.storage_optimizer_config.StorageOptimizerConfig"
    ]
    """<p>A map of the storage optimizer configuration. Currently contains only one key-value pair: <code>is_enabled</code> indicates true or false for acceleration.</p>"""
    error_message: NotRequired["capo_lakeformation.types.message_string.MessageString"]
    """<p>A message that contains information about any error (if present).</p> <p>When an acceleration result has an enabled status, the error message is empty.</p> <p>When an acceleration result has a disabled status, the message describes an error or simply indicates "disabled by the user".</p>"""
    warnings: NotRequired["capo_lakeformation.types.message_string.MessageString"]
    """<p>A message that contains information about any warnings (if present).</p>"""
    last_run_details: NotRequired[
        "capo_lakeformation.types.message_string.MessageString"
    ]
    """<p>When an acceleration result has an enabled status, contains the details of the last job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageOptimizer) -> dict:
    out: dict = {}
    if "storage_optimizer_type" in value:
        import capo_lakeformation.types.optimizer_type

        out["StorageOptimizerType"] = (
            capo_lakeformation.types.optimizer_type.serialize_json(
                value["storage_optimizer_type"]
            )
        )
    if "config" in value:
        import capo_lakeformation.types.storage_optimizer_config

        out["Config"] = (
            capo_lakeformation.types.storage_optimizer_config.serialize_json(
                value["config"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "warnings" in value:
        out["Warnings"] = value["warnings"]
    if "last_run_details" in value:
        out["LastRunDetails"] = value["last_run_details"]
    return out


def deserialize_json(data: dict) -> StorageOptimizer:
    out: StorageOptimizer = {}  # type: ignore[typeddict-item]
    if data.get("StorageOptimizerType") is not None:
        import capo_lakeformation.types.optimizer_type

        out["storage_optimizer_type"] = (
            capo_lakeformation.types.optimizer_type.deserialize_json(
                data["StorageOptimizerType"]
            )
        )
    if data.get("Config") is not None:
        import capo_lakeformation.types.storage_optimizer_config

        out["config"] = (
            capo_lakeformation.types.storage_optimizer_config.deserialize_json(
                data["Config"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("Warnings") is not None:
        out["warnings"] = data["Warnings"]
    if data.get("LastRunDetails") is not None:
        out["last_run_details"] = data["LastRunDetails"]
    return out
