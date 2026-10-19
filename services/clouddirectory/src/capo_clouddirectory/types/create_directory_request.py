"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.directory_name


class CreateDirectoryRequest(TypedDict, closed=True):
    name: "capo_clouddirectory.types.directory_name.DirectoryName"
    """<p>The name of the <a>Directory</a>. Should be unique per account, per region.</p>"""
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the published schema that will be copied into the data <a>Directory</a>. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDirectoryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateDirectoryRequest:
    out: CreateDirectoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
