"""Generated from Smithy shape ``com.amazonaws.glacier#Grantee``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.string
    import capo_glacier.types.type


class Grantee(TypedDict, closed=True):
    type: "capo_glacier.types.type.Type"
    """<p>Type of grantee</p>"""
    display_name: NotRequired["capo_glacier.types.string.string"]
    """<p>Screen name of the grantee.</p>"""
    uri: NotRequired["capo_glacier.types.string.string"]
    """<p>URI of the grantee group.</p>"""
    id: NotRequired["capo_glacier.types.string.string"]
    """<p>The canonical user ID of the grantee.</p>"""
    email_address: NotRequired["capo_glacier.types.string.string"]
    """<p>Email address of the grantee.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Grantee) -> dict:
    out: dict = {}
    import capo_glacier.types.type

    out["Type"] = capo_glacier.types.type.serialize_json(value["type"])
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "uri" in value:
        out["URI"] = value["uri"]
    if "id" in value:
        out["ID"] = value["id"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> Grantee:
    out: Grantee = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_glacier.types.type

        out["type"] = capo_glacier.types.type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_glacier.types.type.Type", "")
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("URI") is not None:
        out["uri"] = data["URI"]
    if data.get("ID") is not None:
        out["id"] = data["ID"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    return out
