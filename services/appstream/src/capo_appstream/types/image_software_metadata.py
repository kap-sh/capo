"""Generated from Smithy shape ``com.amazonaws.appstream#ImageSoftwareMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.nvidia_grid_driver_version


class ImageSoftwareMetadata(TypedDict, closed=True):
    nvidia_grid_driver_version: NotRequired[
        "capo_appstream.types.nvidia_grid_driver_version.NvidiaGridDriverVersion"
    ]
    """<p>The version of the NVIDIA GRID driver installed on the image. This field is empty if no NVIDIA GRID driver is installed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageSoftwareMetadata) -> dict:
    out: dict = {}
    if "nvidia_grid_driver_version" in value:
        out["nvidiaGridDriverVersion"] = value["nvidia_grid_driver_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageSoftwareMetadata:
    out: ImageSoftwareMetadata = {}  # type: ignore[typeddict-item]
    if data.get("nvidiaGridDriverVersion") is not None:
        out["nvidia_grid_driver_version"] = data["nvidiaGridDriverVersion"]
    return out
