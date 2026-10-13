"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CookieSpecification``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.cookie_domain
    import capo_workspaces_web.types.cookie_name
    import capo_workspaces_web.types.cookie_path


class CookieSpecification(TypedDict, closed=True):
    domain: "capo_workspaces_web.types.cookie_domain.CookieDomain"
    """<p>The domain of the cookie.</p>"""
    name: NotRequired["capo_workspaces_web.types.cookie_name.CookieName"]
    """<p>The name of the cookie.</p>"""
    path: NotRequired["capo_workspaces_web.types.cookie_path.CookiePath"]
    """<p>The path of the cookie.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CookieSpecification) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    if "name" in value:
        out["name"] = value["name"]
    if "path" in value:
        out["path"] = value["path"]
    return out


def deserialize_json(data: dict) -> CookieSpecification:
    out: CookieSpecification = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("CookieSpecification.domain required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    return out


def redact_sensitive(value: CookieSpecification) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "domain" in value:
        out["domain"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "path" in value:
        out["path"] = "*** Sensitive Data Redacted ***"
    return out
