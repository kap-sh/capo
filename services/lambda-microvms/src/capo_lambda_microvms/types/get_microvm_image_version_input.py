"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#GetMicrovmImageVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.non_blank_string


class GetMicrovmImageVersionInput(TypedDict, closed=True):
    image_identifier: (
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    )
    """<p>The unique identifier (ARN or ID) of the MicroVM image.</p>"""
    image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The version of the MicroVM image to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMicrovmImageVersionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMicrovmImageVersionInput:
    out: GetMicrovmImageVersionInput = {}  # type: ignore[typeddict-item]
    return out
