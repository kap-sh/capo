"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_arn
    import capo_lambda_core.types.runtime_description
    import capo_lambda_core.types.runtime_license_info
    import capo_lambda_core.types.runtime_name
    import capo_lambda_core.types.runtime_release_lifecycle
    import capo_lambda_core.types.runtime_state
    import capo_lambda_core.types.runtime_timestamp


class RuntimeInfo(TypedDict, closed=True):
    arn: "capo_lambda_core.types.runtime_arn.RuntimeArn"
    """The Amazon Resource Name (ARN) of the runtime."""
    name: "capo_lambda_core.types.runtime_name.RuntimeName"
    """The name of the runtime."""
    description: NotRequired[
        "capo_lambda_core.types.runtime_description.RuntimeDescription"
    ]
    """The description of the runtime."""
    license_info: NotRequired[
        "capo_lambda_core.types.runtime_license_info.RuntimeLicenseInfo"
    ]
    """The license information for the runtime."""
    release_lifecycle: NotRequired[
        "capo_lambda_core.types.runtime_release_lifecycle.RuntimeReleaseLifecycle"
    ]
    """The runtime lifecycle for the runtime. Used to schedule runtime deprecation."""
    state: NotRequired["capo_lambda_core.types.runtime_state.RuntimeState"]
    """The current state of the runtime."""
    pending_deletion_at: NotRequired[
        "capo_lambda_core.types.runtime_timestamp.RuntimeTimestamp"
    ]
    """Present only when State is PENDING_DELETION. The date and time at which the runtime will be permanently deleted."""
    created: "capo_lambda_core.types.runtime_timestamp.RuntimeTimestamp"
    """The date and time when the runtime was created."""
    last_modified: "capo_lambda_core.types.runtime_timestamp.RuntimeTimestamp"
    """The date and time when the runtime was last modified."""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeInfo) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
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
    if "state" in value:
        import capo_lambda_core.types.runtime_state

        out["State"] = capo_lambda_core.types.runtime_state.serialize_json(
            value["state"]
        )
    if "pending_deletion_at" in value:
        out["PendingDeletionAt"] = value["pending_deletion_at"]
    out["Created"] = value["created"]
    out["LastModified"] = value["last_modified"]
    return out


def deserialize_json(data: dict) -> RuntimeInfo:
    out: RuntimeInfo = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    if data.get("State") is not None:
        import capo_lambda_core.types.runtime_state

        out["state"] = capo_lambda_core.types.runtime_state.deserialize_json(
            data["State"]
        )
    if data.get("PendingDeletionAt") is not None:
        out["pending_deletion_at"] = data["PendingDeletionAt"]
    if data.get("Created") is not None:
        out["created"] = data["Created"]
    else:
        out["created"] = ""
    if data.get("LastModified") is not None:
        out["last_modified"] = data["LastModified"]
    else:
        out["last_modified"] = ""
    return out
