"""Generated from Smithy shape ``com.amazonaws.signer#SigningImageFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signer.types.image_format
    import capo_signer.types.image_formats


class SigningImageFormat(TypedDict, closed=True):
    supported_formats: "capo_signer.types.image_formats.ImageFormats"
    """<p>The supported formats of a signing image.</p>"""
    default_format: "capo_signer.types.image_format.ImageFormat"
    """<p>The default format of a signing image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningImageFormat) -> dict:
    out: dict = {}
    import capo_signer.types.image_formats

    out["supportedFormats"] = capo_signer.types.image_formats.serialize_json(
        value["supported_formats"]
    )
    import capo_signer.types.image_format

    out["defaultFormat"] = capo_signer.types.image_format.serialize_json(
        value["default_format"]
    )
    return out


def deserialize_json(data: dict) -> SigningImageFormat:
    out: SigningImageFormat = {}  # type: ignore[typeddict-item]
    if data.get("supportedFormats") is not None:
        import capo_signer.types.image_formats

        out["supported_formats"] = capo_signer.types.image_formats.deserialize_json(
            data["supportedFormats"]
        )
    else:
        out["supported_formats"] = []
    if data.get("defaultFormat") is not None:
        import capo_signer.types.image_format

        out["default_format"] = capo_signer.types.image_format.deserialize_json(
            data["defaultFormat"]
        )
    else:
        import typing

        out["default_format"] = typing.cast(
            "capo_signer.types.image_format.ImageFormat", ""
        )
    return out
