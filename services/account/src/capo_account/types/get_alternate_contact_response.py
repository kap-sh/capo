"""Generated from Smithy shape ``com.amazonaws.account#GetAlternateContactResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account.types.alternate_contact


class GetAlternateContactResponse(TypedDict, closed=True):
    alternate_contact: NotRequired[
        "capo_account.types.alternate_contact.AlternateContact"
    ]
    """<p>A structure that contains the details for the specified alternate contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAlternateContactResponse) -> dict:
    out: dict = {}
    if "alternate_contact" in value:
        import capo_account.types.alternate_contact

        out["AlternateContact"] = capo_account.types.alternate_contact.serialize_json(
            value["alternate_contact"]
        )
    return out


def deserialize_json(data: dict) -> GetAlternateContactResponse:
    out: GetAlternateContactResponse = {}  # type: ignore[typeddict-item]
    if data.get("AlternateContact") is not None:
        import capo_account.types.alternate_contact

        out["alternate_contact"] = (
            capo_account.types.alternate_contact.deserialize_json(
                data["AlternateContact"]
            )
        )
    return out


def redact_sensitive(value: GetAlternateContactResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "alternate_contact" in value:
        import capo_account.types.alternate_contact

        out["alternate_contact"] = (
            capo_account.types.alternate_contact.redact_sensitive(
                value["alternate_contact"]
            )
        )
    return out
