"""Generated from Smithy shape ``com.amazonaws.connect#ReleasePhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.phone_number_id


class ReleasePhoneNumberRequest(TypedDict, closed=True):
    phone_number_id: "capo_connect.types.phone_number_id.PhoneNumberId"
    """<p>A unique identifier for the phone number.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReleasePhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ReleasePhoneNumberRequest:
    out: ReleasePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out
