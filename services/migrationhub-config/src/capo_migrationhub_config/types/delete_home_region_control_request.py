"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#DeleteHomeRegionControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_migrationhub_config.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migrationhub_config.types.control_id


class DeleteHomeRegionControlRequest(TypedDict, closed=True):
    control_id: "capo_migrationhub_config.types.control_id.ControlId"
    """<p>A unique identifier that's generated for each home region control. It's always a string that begins with "hrc-" followed by 12 lowercase letters and numbers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHomeRegionControlRequest) -> dict:
    out: dict = {}
    out["ControlId"] = value["control_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHomeRegionControlRequest:
    out: DeleteHomeRegionControlRequest = {}  # type: ignore[typeddict-item]
    if data.get("ControlId") is not None:
        out["control_id"] = data["ControlId"]
    else:
        raise DeserializationError("DeleteHomeRegionControlRequest.control_id required")
    return out
