"""Generated from Smithy shape ``com.amazonaws.workdocs#ActivateUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.user


class ActivateUserResponse(TypedDict, closed=True):
    user: NotRequired["capo_workdocs.types.user.User"]
    """<p>The user information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_workdocs.types.user

        out["User"] = capo_workdocs.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> ActivateUserResponse:
    out: ActivateUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("User") is not None:
        import capo_workdocs.types.user

        out["user"] = capo_workdocs.types.user.deserialize_json(data["User"])
    return out


def redact_sensitive(value: ActivateUserResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user" in value:
        import capo_workdocs.types.user

        out["user"] = capo_workdocs.types.user.redact_sensitive(value["user"])
    return out
