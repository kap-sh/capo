"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#DeleteMicrovmImageVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.non_blank_string


class DeleteMicrovmImageVersionInput(TypedDict, closed=True):
    image_identifier: (
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    )
    """<p>The unique identifier (ARN or ID) of the MicroVM image.</p>"""
    image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The version of the MicroVM image to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMicrovmImageVersionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMicrovmImageVersionInput:
    out: DeleteMicrovmImageVersionInput = {}  # type: ignore[typeddict-item]
    return out
