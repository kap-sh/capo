"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ColorInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.video_colorimetry
    import capo_mediaconnect.types.video_matrix_coefficients
    import capo_mediaconnect.types.video_transfer_characteristics


class ColorInformation(TypedDict, closed=True):
    colorimetry: NotRequired[
        "capo_mediaconnect.types.video_colorimetry.VideoColorimetry"
    ]
    """<p>The color primaries that the video stream uses (for example, <code>BT709</code> or <code>BT2020</code>).</p>"""
    transfer_characteristics: NotRequired[
        "capo_mediaconnect.types.video_transfer_characteristics.VideoTransferCharacteristics"
    ]
    """<p>The transfer characteristics that the video stream uses (for example, <code>BT601</code>, <code>BT709</code>, <code>BT2100_PQ</code>, or <code>BT2100_HLG</code>).</p>"""
    matrix_coefficients: NotRequired[
        "capo_mediaconnect.types.video_matrix_coefficients.VideoMatrixCoefficients"
    ]
    """<p>The YCbCr matrix coefficients that the video stream uses (for example, <code>BT709</code> or <code>BT2020_NCL</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColorInformation) -> dict:
    out: dict = {}
    if "colorimetry" in value:
        import capo_mediaconnect.types.video_colorimetry

        out["colorimetry"] = capo_mediaconnect.types.video_colorimetry.serialize_json(
            value["colorimetry"]
        )
    if "transfer_characteristics" in value:
        import capo_mediaconnect.types.video_transfer_characteristics

        out["transferCharacteristics"] = (
            capo_mediaconnect.types.video_transfer_characteristics.serialize_json(
                value["transfer_characteristics"]
            )
        )
    if "matrix_coefficients" in value:
        import capo_mediaconnect.types.video_matrix_coefficients

        out["matrixCoefficients"] = (
            capo_mediaconnect.types.video_matrix_coefficients.serialize_json(
                value["matrix_coefficients"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColorInformation:
    out: ColorInformation = {}  # type: ignore[typeddict-item]
    if data.get("colorimetry") is not None:
        import capo_mediaconnect.types.video_colorimetry

        out["colorimetry"] = capo_mediaconnect.types.video_colorimetry.deserialize_json(
            data["colorimetry"]
        )
    if data.get("transferCharacteristics") is not None:
        import capo_mediaconnect.types.video_transfer_characteristics

        out["transfer_characteristics"] = (
            capo_mediaconnect.types.video_transfer_characteristics.deserialize_json(
                data["transferCharacteristics"]
            )
        )
    if data.get("matrixCoefficients") is not None:
        import capo_mediaconnect.types.video_matrix_coefficients

        out["matrix_coefficients"] = (
            capo_mediaconnect.types.video_matrix_coefficients.deserialize_json(
                data["matrixCoefficients"]
            )
        )
    return out
