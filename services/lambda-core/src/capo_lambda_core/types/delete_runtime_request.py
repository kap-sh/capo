"""Generated from Smithy shape ``com.amazonaws.lambdacore#DeleteRuntimeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_identifier


class DeleteRuntimeRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime to delete."""
    recovery_window_in_days: NotRequired["int"]
    """Optional. The waiting period, in days (7-30), before the runtime is permanently deleted."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRuntimeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRuntimeRequest:
    out: DeleteRuntimeRequest = {}  # type: ignore[typeddict-item]
    return out
