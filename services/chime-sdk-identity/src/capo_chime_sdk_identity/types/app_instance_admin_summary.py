"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceAdminSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.identity


class AppInstanceAdminSummary(TypedDict, closed=True):
    admin: NotRequired["capo_chime_sdk_identity.types.identity.Identity"]
    """<p>The details of the <code>AppInstanceAdmin</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceAdminSummary) -> dict:
    out: dict = {}
    if "admin" in value:
        import capo_chime_sdk_identity.types.identity

        out["Admin"] = capo_chime_sdk_identity.types.identity.serialize_json(
            value["admin"]
        )
    return out


def deserialize_json(data: dict) -> AppInstanceAdminSummary:
    out: AppInstanceAdminSummary = {}  # type: ignore[typeddict-item]
    if data.get("Admin") is not None:
        import capo_chime_sdk_identity.types.identity

        out["admin"] = capo_chime_sdk_identity.types.identity.deserialize_json(
            data["Admin"]
        )
    return out


def redact_sensitive(value: AppInstanceAdminSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "admin" in value:
        import capo_chime_sdk_identity.types.identity

        out["admin"] = capo_chime_sdk_identity.types.identity.redact_sensitive(
            value["admin"]
        )
    return out
