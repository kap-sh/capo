"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#EfsFileSystemConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.efs_file_system_policy


class EfsFileSystemConfiguration(TypedDict, closed=True):
    file_system_policy: NotRequired[
        "capo_accessanalyzer.types.efs_file_system_policy.EfsFileSystemPolicy"
    ]
    """<p>The JSON policy definition to apply to the Amazon EFS file system. For more information on the elements that make up a file system policy, see <a href="https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-manage-access-intro-resource-policies">Amazon EFS Resource-based policies</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EfsFileSystemConfiguration) -> dict:
    out: dict = {}
    if "file_system_policy" in value:
        out["fileSystemPolicy"] = value["file_system_policy"]
    return out


def deserialize_json(data: dict) -> EfsFileSystemConfiguration:
    out: EfsFileSystemConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fileSystemPolicy") is not None:
        out["file_system_policy"] = data["fileSystemPolicy"]
    return out
