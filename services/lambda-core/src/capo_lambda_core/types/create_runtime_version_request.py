"""Generated from Smithy shape ``com.amazonaws.lambdacore#CreateRuntimeVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_version_name


class CreateRuntimeVersionRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime to create a version for."""
    image_uri: "str"
    """The URI of the container image used to define the function execution environment for this runtime version."""
    name: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
    """The name to assign to the new runtime version."""
    release_notes: NotRequired["str"]
    """The release notes to associate with the runtime version."""
    dry_run: NotRequired["bool"]
    """When set to true, the request is validated without creating a new runtime version. Use this to check that the request would succeed. No runtime version is created and no changes are made."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuntimeVersionRequest) -> dict:
    out: dict = {}
    out["ImageUri"] = value["image_uri"]
    out["Name"] = value["name"]
    if "release_notes" in value:
        out["ReleaseNotes"] = value["release_notes"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_json(data: dict) -> CreateRuntimeVersionRequest:
    out: CreateRuntimeVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageUri") is not None:
        out["image_uri"] = data["ImageUri"]
    else:
        out["image_uri"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ReleaseNotes") is not None:
        out["release_notes"] = data["ReleaseNotes"]
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
