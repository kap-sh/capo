"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of_list_of__string


class EndpointUser(TypedDict, closed=True):
    user_attributes: NotRequired[
        "capo_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    r"""<p>One or more custom attributes that describe the user by associating a name with an array of values. For example, the value of an attribute named Interests might be: ["Science", "Music", "Travel"]. You can use these attributes as filter criteria when you create segments. Attribute names are case sensitive.</p> <p>An attribute name can contain up to 50 characters. An attribute value can contain up to 100 characters. When you define the name of a custom attribute, avoid using the following characters: number sign (#), colon (:), question mark (?), backslash (\), and slash (/). The Amazon Pinpoint console can't display attribute names that contain these characters. This restriction doesn't apply to attribute values.</p>"""
    user_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointUser) -> dict:
    out: dict = {}
    if "user_attributes" in value:
        import capo_pinpoint.types.map_of_list_of__string

        out["UserAttributes"] = (
            capo_pinpoint.types.map_of_list_of__string.serialize_json(
                value["user_attributes"]
            )
        )
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> EndpointUser:
    out: EndpointUser = {}  # type: ignore[typeddict-item]
    if data.get("UserAttributes") is not None:
        import capo_pinpoint.types.map_of_list_of__string

        out["user_attributes"] = (
            capo_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["UserAttributes"]
            )
        )
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    return out
