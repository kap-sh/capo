"""Generated from Smithy shape ``com.amazonaws.supportauthz#DeleteSupportPermitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supportauthz.types.arn


class DeleteSupportPermitInput(TypedDict, closed=True):
    support_permit_identifier: "capo_supportauthz.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) or name of the support permit to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSupportPermitInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSupportPermitInput:
    out: DeleteSupportPermitInput = {}  # type: ignore[typeddict-item]
    return out
