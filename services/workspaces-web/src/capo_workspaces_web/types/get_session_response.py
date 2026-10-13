"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetSessionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.session


class GetSessionResponse(TypedDict, closed=True):
    session: NotRequired["capo_workspaces_web.types.session.Session"]
    """<p>The sessions in a list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    if "session" in value:
        import capo_workspaces_web.types.session

        out["session"] = capo_workspaces_web.types.session.serialize_json(
            value["session"]
        )
    return out


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("session") is not None:
        import capo_workspaces_web.types.session

        out["session"] = capo_workspaces_web.types.session.deserialize_json(
            data["session"]
        )
    return out


def redact_sensitive(value: GetSessionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "session" in value:
        import capo_workspaces_web.types.session

        out["session"] = capo_workspaces_web.types.session.redact_sensitive(
            value["session"]
        )
    return out
