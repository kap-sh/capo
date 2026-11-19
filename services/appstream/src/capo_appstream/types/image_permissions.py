"""Generated from Smithy shape ``com.amazonaws.appstream#ImagePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.boolean_object


class ImagePermissions(TypedDict, closed=True):
    allow_fleet: NotRequired["capo_appstream.types.boolean_object.BooleanObject"]
    """<p>Indicates whether the image can be used for a fleet.</p>"""
    allow_image_builder: NotRequired[
        "capo_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether the image can be used for an image builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImagePermissions) -> dict:
    out: dict = {}
    if "allow_fleet" in value:
        out["allowFleet"] = value["allow_fleet"]
    if "allow_image_builder" in value:
        out["allowImageBuilder"] = value["allow_image_builder"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImagePermissions:
    out: ImagePermissions = {}  # type: ignore[typeddict-item]
    if data.get("allowFleet") is not None:
        out["allow_fleet"] = data["allowFleet"]
    if data.get("allowImageBuilder") is not None:
        out["allow_image_builder"] = data["allowImageBuilder"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImagePermissions) -> dict:
    out: dict = {}
    if "allow_fleet" in value:
        out["allowFleet"] = value["allow_fleet"]
    if "allow_image_builder" in value:
        out["allowImageBuilder"] = value["allow_image_builder"]
    return out


def deserialize_cbor(data: dict) -> ImagePermissions:
    out: ImagePermissions = {}  # type: ignore[typeddict-item]
    if data.get("allowFleet") is not None:
        out["allow_fleet"] = data["allowFleet"]
    if data.get("allowImageBuilder") is not None:
        out["allow_image_builder"] = data["allowImageBuilder"]
    return out
