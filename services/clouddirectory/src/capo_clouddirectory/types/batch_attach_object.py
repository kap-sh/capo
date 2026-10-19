"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchAttachObject``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.link_name
    import capo_clouddirectory.types.object_reference


class BatchAttachObject(TypedDict, closed=True):
    parent_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>The parent object reference.</p>"""
    child_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>The child object reference that is to be attached to the object.</p>"""
    link_name: "capo_clouddirectory.types.link_name.LinkName"
    """<p>The name of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAttachObject) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["ParentReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["parent_reference"]
    )
    import capo_clouddirectory.types.object_reference

    out["ChildReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["child_reference"]
    )
    out["LinkName"] = value["link_name"]
    return out


def deserialize_json(data: dict) -> BatchAttachObject:
    out: BatchAttachObject = {}  # type: ignore[typeddict-item]
    if data.get("ParentReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["parent_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ParentReference"]
            )
        )
    else:
        raise DeserializationError("BatchAttachObject.parent_reference required")
    if data.get("ChildReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["child_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ChildReference"]
            )
        )
    else:
        raise DeserializationError("BatchAttachObject.child_reference required")
    if data.get("LinkName") is not None:
        out["link_name"] = data["LinkName"]
    else:
        out["link_name"] = ""
    return out
