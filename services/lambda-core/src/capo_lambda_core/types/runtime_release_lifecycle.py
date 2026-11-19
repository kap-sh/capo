"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeReleaseLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_lifecycle_date
    import capo_lambda_core.types.runtime_release_state


class RuntimeReleaseLifecycle(TypedDict, closed=True):
    release_state: NotRequired[
        "capo_lambda_core.types.runtime_release_state.RuntimeReleaseState"
    ]
    """Optional, with no default applied. DEPRECATED requires a DeprecationDate on or before today (UTC); PREVIEW and GA require a later one, or none. Reads report DEPRECATED once DeprecationDate is reached."""
    deprecation_date: NotRequired[
        "capo_lambda_core.types.runtime_lifecycle_date.RuntimeLifecycleDate"
    ]
    """The date (UTC) on which the runtime or alias becomes deprecated."""
    function_create_block_date: NotRequired[
        "capo_lambda_core.types.runtime_lifecycle_date.RuntimeLifecycleDate"
    ]
    """The date (UTC) on which creating new functions that use this runtime or alias is blocked."""
    function_update_block_date: NotRequired[
        "capo_lambda_core.types.runtime_lifecycle_date.RuntimeLifecycleDate"
    ]
    """The date (UTC) on which updating existing functions that use this runtime or alias is blocked."""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeReleaseLifecycle) -> dict:
    out: dict = {}
    if "release_state" in value:
        import capo_lambda_core.types.runtime_release_state

        out["ReleaseState"] = (
            capo_lambda_core.types.runtime_release_state.serialize_json(
                value["release_state"]
            )
        )
    if "deprecation_date" in value:
        out["DeprecationDate"] = value["deprecation_date"]
    if "function_create_block_date" in value:
        out["FunctionCreateBlockDate"] = value["function_create_block_date"]
    if "function_update_block_date" in value:
        out["FunctionUpdateBlockDate"] = value["function_update_block_date"]
    return out


def deserialize_json(data: dict) -> RuntimeReleaseLifecycle:
    out: RuntimeReleaseLifecycle = {}  # type: ignore[typeddict-item]
    if data.get("ReleaseState") is not None:
        import capo_lambda_core.types.runtime_release_state

        out["release_state"] = (
            capo_lambda_core.types.runtime_release_state.deserialize_json(
                data["ReleaseState"]
            )
        )
    if data.get("DeprecationDate") is not None:
        out["deprecation_date"] = data["DeprecationDate"]
    if data.get("FunctionCreateBlockDate") is not None:
        out["function_create_block_date"] = data["FunctionCreateBlockDate"]
    if data.get("FunctionUpdateBlockDate") is not None:
        out["function_update_block_date"] = data["FunctionUpdateBlockDate"]
    return out
