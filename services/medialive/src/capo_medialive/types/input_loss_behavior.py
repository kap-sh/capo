"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossBehavior``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max1000000
    import capo_medialive.types.__string_min6_max6
    import capo_medialive.types.input_location
    import capo_medialive.types.input_loss_image_type


class InputLossBehavior(TypedDict, closed=True):
    black_frame_msec: NotRequired[
        "capo_medialive.types.__integer_min0_max1000000.__integerMin0Max1000000"
    ]
    """Documentation update needed"""
    input_loss_image_color: NotRequired[
        "capo_medialive.types.__string_min6_max6.__stringMin6Max6"
    ]
    """When input loss image type is "color" this field specifies the color to use. Value: 6 hex characters representing the values of RGB."""
    input_loss_image_slate: NotRequired[
        "capo_medialive.types.input_location.InputLocation"
    ]
    """When input loss image type is "slate" these fields specify the parameters for accessing the slate."""
    input_loss_image_type: NotRequired[
        "capo_medialive.types.input_loss_image_type.InputLossImageType"
    ]
    """Indicates whether to substitute a solid color or a slate into the output after input loss exceeds blackFrameMsec."""
    repeat_frame_msec: NotRequired[
        "capo_medialive.types.__integer_min0_max1000000.__integerMin0Max1000000"
    ]
    """Documentation update needed"""


# --- restJson1 ser/de ---
def serialize_json(value: InputLossBehavior) -> dict:
    out: dict = {}
    if "black_frame_msec" in value:
        out["blackFrameMsec"] = value["black_frame_msec"]
    if "input_loss_image_color" in value:
        out["inputLossImageColor"] = value["input_loss_image_color"]
    if "input_loss_image_slate" in value:
        import capo_medialive.types.input_location

        out["inputLossImageSlate"] = capo_medialive.types.input_location.serialize_json(
            value["input_loss_image_slate"]
        )
    if "input_loss_image_type" in value:
        import capo_medialive.types.input_loss_image_type

        out["inputLossImageType"] = (
            capo_medialive.types.input_loss_image_type.serialize_json(
                value["input_loss_image_type"]
            )
        )
    if "repeat_frame_msec" in value:
        out["repeatFrameMsec"] = value["repeat_frame_msec"]
    return out


def deserialize_json(data: dict) -> InputLossBehavior:
    out: InputLossBehavior = {}  # type: ignore[typeddict-item]
    if data.get("blackFrameMsec") is not None:
        out["black_frame_msec"] = data["blackFrameMsec"]
    if data.get("inputLossImageColor") is not None:
        out["input_loss_image_color"] = data["inputLossImageColor"]
    if data.get("inputLossImageSlate") is not None:
        import capo_medialive.types.input_location

        out["input_loss_image_slate"] = (
            capo_medialive.types.input_location.deserialize_json(
                data["inputLossImageSlate"]
            )
        )
    if data.get("inputLossImageType") is not None:
        import capo_medialive.types.input_loss_image_type

        out["input_loss_image_type"] = (
            capo_medialive.types.input_loss_image_type.deserialize_json(
                data["inputLossImageType"]
            )
        )
    if data.get("repeatFrameMsec") is not None:
        out["repeat_frame_msec"] = data["repeatFrameMsec"]
    return out
