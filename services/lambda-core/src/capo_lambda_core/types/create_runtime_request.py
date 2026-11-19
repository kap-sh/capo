"""Generated from Smithy shape ``com.amazonaws.lambdacore#CreateRuntimeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_description
    import capo_lambda_core.types.runtime_license_info
    import capo_lambda_core.types.runtime_name
    import capo_lambda_core.types.runtime_release_lifecycle
    import capo_lambda_core.types.tag_map


class CreateRuntimeRequest(TypedDict, closed=True):
    name: "capo_lambda_core.types.runtime_name.RuntimeName"
    """The name of the runtime to create."""
    tags: NotRequired["capo_lambda_core.types.tag_map.TagMap"]
    """A map of tag keys and values to associate with the runtime."""
    description: NotRequired[
        "capo_lambda_core.types.runtime_description.RuntimeDescription"
    ]
    """A description of the runtime."""
    license_info: NotRequired[
        "capo_lambda_core.types.runtime_license_info.RuntimeLicenseInfo"
    ]
    """The license information for the runtime."""
    release_lifecycle: NotRequired[
        "capo_lambda_core.types.runtime_release_lifecycle.RuntimeReleaseLifecycle"
    ]
    """The runtime lifecycle for the runtime (optional). Use this to schedule runtime deprecation."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuntimeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "tags" in value:
        import capo_lambda_core.types.tag_map

        out["Tags"] = capo_lambda_core.types.tag_map.serialize_json(value["tags"])
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


def deserialize_json(data: dict) -> CreateRuntimeRequest:
    out: CreateRuntimeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Tags") is not None:
        import capo_lambda_core.types.tag_map

        out["tags"] = capo_lambda_core.types.tag_map.deserialize_json(data["Tags"])
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
