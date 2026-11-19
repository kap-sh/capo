"""Generated from Smithy shape ``com.amazonaws.lambdacore#GetRuntimeAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_alias_name
    import capo_lambda_core.types.runtime_identifier


class GetRuntimeAliasRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime."""
    name: "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName"
    """The name of the runtime alias to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuntimeAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRuntimeAliasRequest:
    out: GetRuntimeAliasRequest = {}  # type: ignore[typeddict-item]
    return out
