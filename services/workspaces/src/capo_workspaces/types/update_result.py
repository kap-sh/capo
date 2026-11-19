"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.boolean_object
    import capo_workspaces.types.update_description


class UpdateResult(TypedDict, closed=True):
    update_available: NotRequired["capo_workspaces.types.boolean_object.BooleanObject"]
    """<p>Indicates whether updated drivers or other components are available for the specified WorkSpace image.</p>"""
    description: NotRequired[
        "capo_workspaces.types.update_description.UpdateDescription"
    ]
    """<p>A description of whether updates for the WorkSpace image are pending or available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResult) -> dict:
    out: dict = {}
    if "update_available" in value:
        out["UpdateAvailable"] = value["update_available"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResult:
    out: UpdateResult = {}  # type: ignore[typeddict-item]
    if data.get("UpdateAvailable") is not None:
        out["update_available"] = data["UpdateAvailable"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateResult) -> dict:
    out: dict = {}
    if "update_available" in value:
        out["UpdateAvailable"] = value["update_available"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> UpdateResult:
    out: UpdateResult = {}  # type: ignore[typeddict-item]
    if data.get("UpdateAvailable") is not None:
        out["update_available"] = data["UpdateAvailable"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
