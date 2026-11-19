"""Generated from Smithy shape ``com.amazonaws.lambdacore#DeleteRuntimeVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_version_name


class DeleteRuntimeVersionRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime."""
    name: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
    """The name of the runtime version to delete."""
    recovery_window_in_days: NotRequired["int"]
    """Optional. The waiting period, in days (7-30), before the runtime version is permanently deleted."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRuntimeVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRuntimeVersionRequest:
    out: DeleteRuntimeVersionRequest = {}  # type: ignore[typeddict-item]
    return out
