"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ResumeMicrovmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_identifier


class ResumeMicrovmRequest(TypedDict, closed=True):
    microvm_identifier: (
        "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier"
    )
    """<p>The ID of the MicroVM to resume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResumeMicrovmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ResumeMicrovmRequest:
    out: ResumeMicrovmRequest = {}  # type: ignore[typeddict-item]
    return out
