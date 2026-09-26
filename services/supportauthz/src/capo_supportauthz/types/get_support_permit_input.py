"""Generated from Smithy shape ``com.amazonaws.supportauthz#GetSupportPermitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supportauthz.types.support_permit_identifier


class GetSupportPermitInput(TypedDict, closed=True):
    support_permit_identifier: (
        "capo_supportauthz.types.support_permit_identifier.SupportPermitIdentifier"
    )
    """<p>The ARN or name of the support permit to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSupportPermitInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSupportPermitInput:
    out: GetSupportPermitInput = {}  # type: ignore[typeddict-item]
    return out
