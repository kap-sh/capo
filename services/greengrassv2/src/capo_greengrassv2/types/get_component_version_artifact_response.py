"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetComponentVersionArtifactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.non_empty_string


class GetComponentVersionArtifactResponse(TypedDict, closed=True):
    pre_signed_url: "capo_greengrassv2.types.non_empty_string.NonEmptyString"
    """<p>The URL of the artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentVersionArtifactResponse) -> dict:
    out: dict = {}
    out["preSignedUrl"] = value["pre_signed_url"]
    return out


def deserialize_json(data: dict) -> GetComponentVersionArtifactResponse:
    out: GetComponentVersionArtifactResponse = {}  # type: ignore[typeddict-item]
    if data.get("preSignedUrl") is not None:
        out["pre_signed_url"] = data["preSignedUrl"]
    else:
        out["pre_signed_url"] = ""
    return out
