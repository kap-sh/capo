"""Generated from Smithy shape ``com.amazonaws.lambdacore#UpdateRuntimeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_description
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_license_info
    import capo_lambda_core.types.runtime_release_lifecycle


class UpdateRuntimeRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime to update."""
    description: NotRequired[
        "capo_lambda_core.types.runtime_description.RuntimeDescription"
    ]
    """The updated description of the runtime."""
    license_info: NotRequired[
        "capo_lambda_core.types.runtime_license_info.RuntimeLicenseInfo"
    ]
    """The updated license information for the runtime."""
    release_lifecycle: NotRequired[
        "capo_lambda_core.types.runtime_release_lifecycle.RuntimeReleaseLifecycle"
    ]
    """The runtime lifecycle for the runtime. Optional. Used to schedule runtime deprecation. Omitting or providing an empty object removes the existing lifecycle."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuntimeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "license_info" in value:
        out["LicenseInfo"] = value["license_info"]
    if "release_lifecycle" in value:
        import capo_lambda_core.types.runtime_release_lifecycle

        out["ReleaseLifecycle"] = (
            capo_lambda_core.types.runtime_release_lifecycle.serialize_json(
                value["release_lifecycle"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRuntimeRequest:
    out: UpdateRuntimeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LicenseInfo") is not None:
        out["license_info"] = data["LicenseInfo"]
    if data.get("ReleaseLifecycle") is not None:
        import capo_lambda_core.types.runtime_release_lifecycle

        out["release_lifecycle"] = (
            capo_lambda_core.types.runtime_release_lifecycle.deserialize_json(
                data["ReleaseLifecycle"]
            )
        )
    return out
