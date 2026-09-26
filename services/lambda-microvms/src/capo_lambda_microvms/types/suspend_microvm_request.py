"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#SuspendMicrovmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_identifier


class SuspendMicrovmRequest(TypedDict, closed=True):
    microvm_identifier: (
        "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier"
    )
    """<p>The ID of the MicroVM to suspend.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuspendMicrovmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SuspendMicrovmRequest:
    out: SuspendMicrovmRequest = {}  # type: ignore[typeddict-item]
    return out
