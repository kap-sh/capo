"""Generated from Smithy shape ``com.amazonaws.lambdacore#RestoreRuntimeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_alias_name
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_version_name


class RestoreRuntimeRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime to restore. When RuntimeVersion or RuntimeAlias is specified, the runtime that owns the runtime version or runtime alias to restore."""
    runtime_version: NotRequired[
        "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
    ]
    """Optional. Restores the named RuntimeVersion under RuntimeName. Mutually exclusive with RuntimeAlias; supplying both is rejected with InvalidParameterValueException."""
    runtime_alias: NotRequired[
        "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName"
    ]
    """Optional. Restores the named RuntimeAlias under RuntimeName. Mutually exclusive with RuntimeVersion; supplying both is rejected with InvalidParameterValueException."""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreRuntimeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestoreRuntimeRequest:
    out: RestoreRuntimeRequest = {}  # type: ignore[typeddict-item]
    return out
