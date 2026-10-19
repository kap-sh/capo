"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DisableDirectoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn


class DisableDirectoryResponse(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory that has been disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableDirectoryResponse) -> dict:
    out: dict = {}
    out["DirectoryArn"] = value["directory_arn"]
    return out


def deserialize_json(data: dict) -> DisableDirectoryResponse:
    out: DisableDirectoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryArn") is not None:
        out["directory_arn"] = data["DirectoryArn"]
    else:
        out["directory_arn"] = ""
    return out
