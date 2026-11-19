"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ScalarTrustAnchorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.trust_anchor_identifier


class ScalarTrustAnchorRequest(TypedDict, closed=True):
    trust_anchor_id: (
        "capo_rolesanywhere.types.trust_anchor_identifier.TrustAnchorIdentifier"
    )
    """<p>The trust anchor to act on. You can specify one of the following:</p> <ul> <li> <p>The trust anchor ID.</p> </li> <li> <p>The trust anchor ARN.</p> </li> <li> <p>The alias ARN of the trust anchor.</p> </li> </ul> <p>An ARN must be for a trust anchor in your account and Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalarTrustAnchorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ScalarTrustAnchorRequest:
    out: ScalarTrustAnchorRequest = {}  # type: ignore[typeddict-item]
    return out
