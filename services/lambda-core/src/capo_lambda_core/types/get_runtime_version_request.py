"""Generated from Smithy shape ``com.amazonaws.lambdacore#GetRuntimeVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_version_name


class GetRuntimeVersionRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime."""
    name: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
    """The name of the runtime version to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuntimeVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRuntimeVersionRequest:
    out: GetRuntimeVersionRequest = {}  # type: ignore[typeddict-item]
    return out
