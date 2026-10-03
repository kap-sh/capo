"""Generated from Smithy shape ``com.amazonaws.iot#AttributePayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.attributes
    import capo_iot.types.flag


class AttributePayload(TypedDict, closed=True):
    attributes: NotRequired["capo_iot.types.attributes.Attributes"]
    r"""<p>A JSON string containing up to three key-value pair in JSON format. For example:</p> <p> <code>{\"attributes\":{\"string1\":\"string2\"}}</code> </p>"""
    merge: "capo_iot.types.flag.Flag"
    """<p>Specifies whether the list of attributes provided in the <code>AttributePayload</code> is merged with the attributes stored in the registry, instead of overwriting them.</p> <p>To remove an attribute, call <code>UpdateThing</code> with an empty attribute value.</p> <note> <p>The <code>merge</code> attribute is only valid when calling <code>UpdateThing</code> or <code>UpdateThingGroup</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributePayload) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_iot.types.attributes

        out["attributes"] = capo_iot.types.attributes.serialize_json(
            value["attributes"]
        )
    out["merge"] = value.get("merge", False)
    return out


def deserialize_json(data: dict) -> AttributePayload:
    out: AttributePayload = {}  # type: ignore[typeddict-item]
    if data.get("attributes") is not None:
        import capo_iot.types.attributes

        out["attributes"] = capo_iot.types.attributes.deserialize_json(
            data["attributes"]
        )
    if data.get("merge") is not None:
        out["merge"] = data["merge"]
    else:
        out["merge"] = False
    return out
