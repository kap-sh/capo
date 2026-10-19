"""Generated from Smithy shape ``com.amazonaws.panorama#OTAJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.boolean
    import capo_panorama.types.image_version


class OTAJobConfig(TypedDict, closed=True):
    image_version: "capo_panorama.types.image_version.ImageVersion"
    """<p>The target version of the device software.</p>"""
    allow_major_version_update: "capo_panorama.types.boolean.Boolean"
    """<p>Whether to apply the update if it is a major version change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OTAJobConfig) -> dict:
    out: dict = {}
    out["ImageVersion"] = value["image_version"]
    out["AllowMajorVersionUpdate"] = value.get("allow_major_version_update", False)
    return out


def deserialize_json(data: dict) -> OTAJobConfig:
    out: OTAJobConfig = {}  # type: ignore[typeddict-item]
    if data.get("ImageVersion") is not None:
        out["image_version"] = data["ImageVersion"]
    else:
        out["image_version"] = ""
    if data.get("AllowMajorVersionUpdate") is not None:
        out["allow_major_version_update"] = data["AllowMajorVersionUpdate"]
    else:
        out["allow_major_version_update"] = False
    return out
