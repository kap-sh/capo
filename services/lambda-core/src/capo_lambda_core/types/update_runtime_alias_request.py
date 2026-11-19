"""Generated from Smithy shape ``com.amazonaws.lambdacore#UpdateRuntimeAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_alias_description
    import capo_lambda_core.types.runtime_alias_name
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_release_lifecycle
    import capo_lambda_core.types.runtime_version_name


class UpdateRuntimeAliasRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime."""
    name: "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName"
    """The name of the runtime alias to update."""
    runtime_version: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
    """The name of the runtime version the alias should point to."""
    description: NotRequired[
        "capo_lambda_core.types.runtime_alias_description.RuntimeAliasDescription"
    ]
    """A description of the runtime alias."""
    release_lifecycle: NotRequired[
        "capo_lambda_core.types.runtime_release_lifecycle.RuntimeReleaseLifecycle"
    ]
    """The lifecycle for the alias. By default, this is inherited from the runtime lifecycle. Optionally, you can override the lifecycle information at the alias level, if required. Omitting or providing an empty object removes the existing lifecycle override."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuntimeAliasRequest) -> dict:
    out: dict = {}
    out["RuntimeVersion"] = value["runtime_version"]
    if "description" in value:
        out["Description"] = value["description"]
    if "release_lifecycle" in value:
        import capo_lambda_core.types.runtime_release_lifecycle

        out["ReleaseLifecycle"] = (
            capo_lambda_core.types.runtime_release_lifecycle.serialize_json(
                value["release_lifecycle"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRuntimeAliasRequest:
    out: UpdateRuntimeAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuntimeVersion") is not None:
        out["runtime_version"] = data["RuntimeVersion"]
    else:
        out["runtime_version"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ReleaseLifecycle") is not None:
        import capo_lambda_core.types.runtime_release_lifecycle

        out["release_lifecycle"] = (
            capo_lambda_core.types.runtime_release_lifecycle.deserialize_json(
                data["ReleaseLifecycle"]
            )
        )
    return out
