"""Generated from Smithy shape ``com.amazonaws.omics#VersionDeleteError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.version_name


class VersionDeleteError(TypedDict, closed=True):
    version_name: "capo_omics.types.version_name.VersionName"
    """<p> The name given to an annotation store version. </p>"""
    message: "str"
    """<p> The message explaining the error in annotation store deletion. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionDeleteError) -> dict:
    out: dict = {}
    out["versionName"] = value["version_name"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> VersionDeleteError:
    out: VersionDeleteError = {}  # type: ignore[typeddict-item]
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    else:
        out["version_name"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
