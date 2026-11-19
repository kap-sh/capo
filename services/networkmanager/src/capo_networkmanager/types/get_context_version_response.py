"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetContextVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string


class GetContextVersionResponse(TypedDict, closed=True):
    version_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The current version of the context entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContextVersionResponse) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> GetContextVersionResponse:
    out: GetContextVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    return out
