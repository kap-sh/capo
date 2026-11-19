"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ScalarCrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.crl_identifier


class ScalarCrlRequest(TypedDict, closed=True):
    crl_id: "capo_rolesanywhere.types.crl_identifier.CrlIdentifier"
    """<p>The certificate revocation list (CRL) to act on. You can specify one of the following:</p> <ul> <li> <p>The CRL ID.</p> </li> <li> <p>The CRL ARN.</p> </li> <li> <p>The alias ARN of the CRL.</p> </li> </ul> <p>An ARN must be for a CRL in your account and Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalarCrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ScalarCrlRequest:
    out: ScalarCrlRequest = {}  # type: ignore[typeddict-item]
    return out
