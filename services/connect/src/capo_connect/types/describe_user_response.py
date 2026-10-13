"""Generated from Smithy shape ``com.amazonaws.connect#DescribeUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.user


class DescribeUserResponse(TypedDict, closed=True):
    user: NotRequired["capo_connect.types.user.User"]
    """<p>Information about the user account and configuration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_connect.types.user

        out["User"] = capo_connect.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> DescribeUserResponse:
    out: DescribeUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("User") is not None:
        import capo_connect.types.user

        out["user"] = capo_connect.types.user.deserialize_json(data["User"])
    return out


def redact_sensitive(value: DescribeUserResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user" in value:
        import capo_connect.types.user

        out["user"] = capo_connect.types.user.redact_sensitive(value["user"])
    return out
