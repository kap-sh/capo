"""Generated from Smithy shape ``com.amazonaws.lambdacore#GetRuntimeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_identifier


class GetRuntimeRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuntimeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRuntimeRequest:
    out: GetRuntimeRequest = {}  # type: ignore[typeddict-item]
    return out
