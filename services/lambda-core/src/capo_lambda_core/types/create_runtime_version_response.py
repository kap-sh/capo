"""Generated from Smithy shape ``com.amazonaws.lambdacore#CreateRuntimeVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.compatibility
    import capo_lambda_core.types.platform_list
    import capo_lambda_core.types.runtime_arn
    import capo_lambda_core.types.runtime_timestamp
    import capo_lambda_core.types.runtime_version_name
    import capo_lambda_core.types.runtime_version_state


class CreateRuntimeVersionResponse(TypedDict, closed=True):
    name: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
    """The name of the runtime version."""
    arn: "capo_lambda_core.types.runtime_arn.RuntimeArn"
    """The Amazon Resource Name (ARN) of the runtime version."""
    resolved_uri: "str"
    """The resolved image URI of the runtime version."""
    state: "capo_lambda_core.types.runtime_version_state.RuntimeVersionState"
    """The current state of the runtime version."""
    release_notes: NotRequired["str"]
    """The release notes associated with the runtime version."""
    platforms: NotRequired["capo_lambda_core.types.platform_list.PlatformList"]
    """The platforms (architecture and OS combinations) available for the runtime version."""
    compatibility: NotRequired["capo_lambda_core.types.compatibility.Compatibility"]
    """The compatibility matrix of the runtime version."""
    created: "capo_lambda_core.types.runtime_timestamp.RuntimeTimestamp"
    """The date and time when the runtime version was created."""
    last_modified: "capo_lambda_core.types.runtime_timestamp.RuntimeTimestamp"
    """The date and time when the runtime version was last modified."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuntimeVersionResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    out["ResolvedUri"] = value["resolved_uri"]
    import capo_lambda_core.types.runtime_version_state

    out["State"] = capo_lambda_core.types.runtime_version_state.serialize_json(
        value["state"]
    )
    if "release_notes" in value:
        out["ReleaseNotes"] = value["release_notes"]
    if "platforms" in value:
        import capo_lambda_core.types.platform_list

        out["Platforms"] = capo_lambda_core.types.platform_list.serialize_json(
            value["platforms"]
        )
    if "compatibility" in value:
        import capo_lambda_core.types.compatibility

        out["Compatibility"] = capo_lambda_core.types.compatibility.serialize_json(
            value["compatibility"]
        )
    out["Created"] = value["created"]
    out["LastModified"] = value["last_modified"]
    return out


def deserialize_json(data: dict) -> CreateRuntimeVersionResponse:
    out: CreateRuntimeVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ResolvedUri") is not None:
        out["resolved_uri"] = data["ResolvedUri"]
    else:
        out["resolved_uri"] = ""
    if data.get("State") is not None:
        import capo_lambda_core.types.runtime_version_state

        out["state"] = capo_lambda_core.types.runtime_version_state.deserialize_json(
            data["State"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_lambda_core.types.runtime_version_state.RuntimeVersionState", ""
        )
    if data.get("ReleaseNotes") is not None:
        out["release_notes"] = data["ReleaseNotes"]
    if data.get("Platforms") is not None:
        import capo_lambda_core.types.platform_list

        out["platforms"] = capo_lambda_core.types.platform_list.deserialize_json(
            data["Platforms"]
        )
    if data.get("Compatibility") is not None:
        import capo_lambda_core.types.compatibility

        out["compatibility"] = capo_lambda_core.types.compatibility.deserialize_json(
            data["Compatibility"]
        )
    if data.get("Created") is not None:
        out["created"] = data["Created"]
    else:
        out["created"] = ""
    if data.get("LastModified") is not None:
        out["last_modified"] = data["LastModified"]
    else:
        out["last_modified"] = ""
    return out
