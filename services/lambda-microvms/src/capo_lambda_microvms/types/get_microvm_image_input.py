"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#GetMicrovmImageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_identifier


class GetMicrovmImageInput(TypedDict, closed=True):
    image_identifier: (
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    )
    """<p>The unique identifier (ARN or ID) of the MicroVM image to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMicrovmImageInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMicrovmImageInput:
    out: GetMicrovmImageInput = {}  # type: ignore[typeddict-item]
    return out
