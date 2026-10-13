"""Generated from Smithy shape ``com.amazonaws.account#GetPrimaryEmailResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account.types.primary_email_address


class GetPrimaryEmailResponse(TypedDict, closed=True):
    primary_email: NotRequired[
        "capo_account.types.primary_email_address.PrimaryEmailAddress"
    ]
    """<p>Retrieves the primary email address associated with the specified account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPrimaryEmailResponse) -> dict:
    out: dict = {}
    if "primary_email" in value:
        out["PrimaryEmail"] = value["primary_email"]
    return out


def deserialize_json(data: dict) -> GetPrimaryEmailResponse:
    out: GetPrimaryEmailResponse = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryEmail") is not None:
        out["primary_email"] = data["PrimaryEmail"]
    return out


def redact_sensitive(value: GetPrimaryEmailResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_email" in value:
        out["primary_email"] = "*** Sensitive Data Redacted ***"
    return out
