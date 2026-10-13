"""Generated from Smithy shape ``com.amazonaws.finspacedata#DatasetOwnerInfo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.email
    import capo_finspace_data.types.owner_name
    import capo_finspace_data.types.phone_number


class DatasetOwnerInfo(TypedDict, closed=True):
    name: NotRequired["capo_finspace_data.types.owner_name.OwnerName"]
    """<p>The name of the Dataset owner.</p>"""
    phone_number: NotRequired["capo_finspace_data.types.phone_number.PhoneNumber"]
    """<p>Phone number for the Dataset owner.</p>"""
    email: NotRequired["capo_finspace_data.types.email.Email"]
    """<p>Email address for the Dataset owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetOwnerInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "phone_number" in value:
        out["phoneNumber"] = value["phone_number"]
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> DatasetOwnerInfo:
    out: DatasetOwnerInfo = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("phoneNumber") is not None:
        out["phone_number"] = data["phoneNumber"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    return out


def redact_sensitive(value: DatasetOwnerInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    return out
