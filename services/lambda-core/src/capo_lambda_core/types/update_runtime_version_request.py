"""Generated from Smithy shape ``com.amazonaws.lambdacore#UpdateRuntimeVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_version_name


class UpdateRuntimeVersionRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime."""
    name: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
    """The name of the runtime version to update."""
    release_notes: "str"
    """The release notes to associate with the runtime version."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuntimeVersionRequest) -> dict:
    out: dict = {}
    out["ReleaseNotes"] = value["release_notes"]
    return out


def deserialize_json(data: dict) -> UpdateRuntimeVersionRequest:
    out: UpdateRuntimeVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReleaseNotes") is not None:
        out["release_notes"] = data["ReleaseNotes"]
    else:
        out["release_notes"] = ""
    return out
