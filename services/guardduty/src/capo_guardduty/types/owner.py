"""Generated from Smithy shape ``com.amazonaws.guardduty#Owner``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class Owner(TypedDict, closed=True):
    id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The canonical user ID of the bucket owner. For information about locating your canonical user ID see <a href="https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html#FindingCanonicalId">Finding Your Account Canonical User ID.</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Owner) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> Owner:
    out: Owner = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    return out
