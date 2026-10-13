"""Generated from Smithy shape ``com.amazonaws.chime#ResetPersonalPINResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.user


class ResetPersonalPINResponse(TypedDict, closed=True):
    user: NotRequired["capo_chime.types.user.User"]
    """<p>The user details and new personal meeting PIN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetPersonalPINResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_chime.types.user

        out["User"] = capo_chime.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> ResetPersonalPINResponse:
    out: ResetPersonalPINResponse = {}  # type: ignore[typeddict-item]
    if data.get("User") is not None:
        import capo_chime.types.user

        out["user"] = capo_chime.types.user.deserialize_json(data["User"])
    return out


def redact_sensitive(value: ResetPersonalPINResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user" in value:
        import capo_chime.types.user

        out["user"] = capo_chime.types.user.redact_sensitive(value["user"])
    return out
