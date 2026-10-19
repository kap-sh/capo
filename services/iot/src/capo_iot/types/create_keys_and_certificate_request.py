"""Generated from Smithy shape ``com.amazonaws.iot#CreateKeysAndCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.set_as_active


class CreateKeysAndCertificateRequest(TypedDict, closed=True):
    set_as_active: NotRequired["capo_iot.types.set_as_active.SetAsActive"]
    """<p>Specifies whether the certificate is active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKeysAndCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateKeysAndCertificateRequest:
    out: CreateKeysAndCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
