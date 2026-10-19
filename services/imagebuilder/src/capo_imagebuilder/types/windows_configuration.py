"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WindowsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.windows_configuration_image_index


class WindowsConfiguration(TypedDict, closed=True):
    image_index: "capo_imagebuilder.types.windows_configuration_image_index.WindowsConfigurationImageIndex"
    """<p>The 1-based index that specifies which Windows edition to install from a multi-edition Windows ISO file. A Windows ISO can contain a <code>.wim</code> file with multiple image indexes, each representing a different edition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WindowsConfiguration) -> dict:
    out: dict = {}
    out["imageIndex"] = value["image_index"]
    return out


def deserialize_json(data: dict) -> WindowsConfiguration:
    out: WindowsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("imageIndex") is not None:
        out["image_index"] = data["imageIndex"]
    else:
        out["image_index"] = 0
    return out
