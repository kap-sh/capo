"""Generated from Smithy shape ``com.amazonaws.lambdacore#CreateRuntimeAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_alias_description
    import capo_lambda_core.types.runtime_alias_name
    import capo_lambda_core.types.runtime_alias_state
    import capo_lambda_core.types.runtime_arn
    import capo_lambda_core.types.runtime_release_lifecycle
    import capo_lambda_core.types.runtime_timestamp
    import capo_lambda_core.types.runtime_version_name


class CreateRuntimeAliasResponse(TypedDict, closed=True):
    name: "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName"
    """The name of the runtime alias."""
    arn: "capo_lambda_core.types.runtime_arn.RuntimeArn"
    """The Amazon Resource Name (ARN) of the runtime alias."""
    runtime_version: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
    """The name of the runtime version the alias points to."""
    runtime_version_arn: "capo_lambda_core.types.runtime_arn.RuntimeArn"
    """The Amazon Resource Name (ARN) of the runtime version the alias points to."""
    state: "capo_lambda_core.types.runtime_alias_state.RuntimeAliasState"
    """The current state of the runtime alias."""
    description: NotRequired[
        "capo_lambda_core.types.runtime_alias_description.RuntimeAliasDescription"
    ]
    """A description of the runtime alias."""
    release_lifecycle: NotRequired[
        "capo_lambda_core.types.runtime_release_lifecycle.RuntimeReleaseLifecycle"
    ]
    """The runtime lifecycle for the alias. By default, this is inherited from the runtime lifecycle. Optionally, you can override the lifecycle information at the alias level, if required."""
    created: "capo_lambda_core.types.runtime_timestamp.RuntimeTimestamp"
    """The date and time when the runtime alias was created."""
    last_modified: "capo_lambda_core.types.runtime_timestamp.RuntimeTimestamp"
    """The date and time when the runtime alias was last modified."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuntimeAliasResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    out["RuntimeVersion"] = value["runtime_version"]
    out["RuntimeVersionArn"] = value["runtime_version_arn"]
    import capo_lambda_core.types.runtime_alias_state

    out["State"] = capo_lambda_core.types.runtime_alias_state.serialize_json(
        value["state"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "release_lifecycle" in value:
        import capo_lambda_core.types.runtime_release_lifecycle

        out["ReleaseLifecycle"] = (
            capo_lambda_core.types.runtime_release_lifecycle.serialize_json(
                value["release_lifecycle"]
            )
        )
    out["Created"] = value["created"]
    out["LastModified"] = value["last_modified"]
    return out


def deserialize_json(data: dict) -> CreateRuntimeAliasResponse:
    out: CreateRuntimeAliasResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("RuntimeVersion") is not None:
        out["runtime_version"] = data["RuntimeVersion"]
    else:
        out["runtime_version"] = ""
    if data.get("RuntimeVersionArn") is not None:
        out["runtime_version_arn"] = data["RuntimeVersionArn"]
    else:
        out["runtime_version_arn"] = ""
    if data.get("State") is not None:
        import capo_lambda_core.types.runtime_alias_state

        out["state"] = capo_lambda_core.types.runtime_alias_state.deserialize_json(
            data["State"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_lambda_core.types.runtime_alias_state.RuntimeAliasState", ""
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ReleaseLifecycle") is not None:
        import capo_lambda_core.types.runtime_release_lifecycle

        out["release_lifecycle"] = (
            capo_lambda_core.types.runtime_release_lifecycle.deserialize_json(
                data["ReleaseLifecycle"]
            )
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
