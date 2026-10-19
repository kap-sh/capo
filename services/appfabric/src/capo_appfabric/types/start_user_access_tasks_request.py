"""Generated from Smithy shape ``com.amazonaws.appfabric#StartUserAccessTasksRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.email
    import capo_appfabric.types.identifier


class StartUserAccessTasksRequest(TypedDict, closed=True):
    app_bundle_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    email: "capo_appfabric.types.email.Email"
    """<p>The email address of the target user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartUserAccessTasksRequest) -> dict:
    out: dict = {}
    out["appBundleIdentifier"] = value["app_bundle_identifier"]
    out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> StartUserAccessTasksRequest:
    out: StartUserAccessTasksRequest = {}  # type: ignore[typeddict-item]
    if data.get("appBundleIdentifier") is not None:
        out["app_bundle_identifier"] = data["appBundleIdentifier"]
    else:
        out["app_bundle_identifier"] = ""
    if data.get("email") is not None:
        out["email"] = data["email"]
    else:
        out["email"] = ""
    return out


def redact_sensitive(value: StartUserAccessTasksRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    return out
