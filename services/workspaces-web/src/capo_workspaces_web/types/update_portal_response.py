"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdatePortalResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.portal


class UpdatePortalResponse(TypedDict, closed=True):
    portal: NotRequired["capo_workspaces_web.types.portal.Portal"]
    """<p>The web portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePortalResponse) -> dict:
    out: dict = {}
    if "portal" in value:
        import capo_workspaces_web.types.portal

        out["portal"] = capo_workspaces_web.types.portal.serialize_json(value["portal"])
    return out


def deserialize_json(data: dict) -> UpdatePortalResponse:
    out: UpdatePortalResponse = {}  # type: ignore[typeddict-item]
    if data.get("portal") is not None:
        import capo_workspaces_web.types.portal

        out["portal"] = capo_workspaces_web.types.portal.deserialize_json(
            data["portal"]
        )
    return out


def redact_sensitive(value: UpdatePortalResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "portal" in value:
        import capo_workspaces_web.types.portal

        out["portal"] = capo_workspaces_web.types.portal.redact_sensitive(
            value["portal"]
        )
    return out
