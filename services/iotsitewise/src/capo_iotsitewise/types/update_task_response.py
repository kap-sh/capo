"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_status
    import capo_iotsitewise.types.version


class UpdateTaskResponse(TypedDict, closed=True):
    version: "capo_iotsitewise.types.version.Version"
    """<p>The new version of the task created by this update.</p>"""
    status: "capo_iotsitewise.types.resource_status.ResourceStatus"
    """<p>The current lifecycle status of the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTaskResponse) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    import capo_iotsitewise.types.resource_status

    out["status"] = capo_iotsitewise.types.resource_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateTaskResponse:
    out: UpdateTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.resource_status

        out["status"] = capo_iotsitewise.types.resource_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateTaskResponse.status required")
    return out
