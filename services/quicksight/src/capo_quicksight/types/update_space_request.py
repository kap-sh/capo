"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSpaceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.public_space_id
    import capo_quicksight.types.space_description
    import capo_quicksight.types.space_name


class UpdateSpaceRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the space.</p>"""
    space_id: "capo_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space that you want to update.</p>"""
    name: NotRequired["capo_quicksight.types.space_name.SpaceName"]
    """<p>A new display name for the space.</p>"""
    description: NotRequired["capo_quicksight.types.space_description.SpaceDescription"]
    """<p>A new description for the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpaceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateSpaceRequest:
    out: UpdateSpaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: UpdateSpaceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
