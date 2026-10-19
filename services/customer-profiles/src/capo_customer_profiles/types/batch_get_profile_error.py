"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetProfileError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.string1_to1000
    import capo_customer_profiles.types.uuid


class BatchGetProfileError(TypedDict, closed=True):
    code: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>Status code for why a specific profile failed.</p>"""
    message: "capo_customer_profiles.types.string1_to1000.string1To1000"
    """<p>Message describing why a specific profile failed.</p>"""
    profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The profile id that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetProfileError) -> dict:
    out: dict = {}
    out["Code"] = value["code"]
    out["Message"] = value["message"]
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_json(data: dict) -> BatchGetProfileError:
    out: BatchGetProfileError = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    return out
