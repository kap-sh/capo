"""Generated from Smithy shape ``com.amazonaws.datazone#IdentityMapping``."""

from typing_extensions import NotRequired, TypedDict


class IdentityMapping(TypedDict, closed=True):
    username_attribute: "str"
    """<p>The username attribute used for the identity mapping.</p>"""
    prefix: NotRequired["str"]
    """<p>The prefix used for the identity mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityMapping) -> dict:
    out: dict = {}
    out["usernameAttribute"] = value["username_attribute"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> IdentityMapping:
    out: IdentityMapping = {}  # type: ignore[typeddict-item]
    if data.get("usernameAttribute") is not None:
        out["username_attribute"] = data["usernameAttribute"]
    else:
        out["username_attribute"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out
