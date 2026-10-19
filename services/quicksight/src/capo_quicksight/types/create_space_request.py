"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateSpaceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.public_space_id
    import capo_quicksight.types.space_description
    import capo_quicksight.types.space_name


class CreateSpaceRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the space.</p>"""
    space_id: "capo_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    name: "capo_quicksight.types.space_name.SpaceName"
    """<p>A display name for the space.</p>"""
    description: NotRequired["capo_quicksight.types.space_description.SpaceDescription"]
    """<p>A description of the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSpaceRequest) -> dict:
    out: dict = {}
    out["SpaceId"] = value["space_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateSpaceRequest:
    out: CreateSpaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("SpaceId") is not None:
        out["space_id"] = data["SpaceId"]
    else:
        out["space_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: CreateSpaceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
