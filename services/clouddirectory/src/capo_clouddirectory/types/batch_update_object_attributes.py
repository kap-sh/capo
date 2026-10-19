"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchUpdateObjectAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_attribute_update_list
    import capo_clouddirectory.types.object_reference


class BatchUpdateObjectAttributes(TypedDict, closed=True):
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>Reference that identifies the object.</p>"""
    attribute_updates: "capo_clouddirectory.types.object_attribute_update_list.ObjectAttributeUpdateList"
    """<p>Attributes update structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateObjectAttributes) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    import capo_clouddirectory.types.object_attribute_update_list

    out["AttributeUpdates"] = (
        capo_clouddirectory.types.object_attribute_update_list.serialize_json(
            value["attribute_updates"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateObjectAttributes:
    out: BatchUpdateObjectAttributes = {}  # type: ignore[typeddict-item]
    if data.get("ObjectReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateObjectAttributes.object_reference required"
        )
    if data.get("AttributeUpdates") is not None:
        import capo_clouddirectory.types.object_attribute_update_list

        out["attribute_updates"] = (
            capo_clouddirectory.types.object_attribute_update_list.deserialize_json(
                data["AttributeUpdates"]
            )
        )
    else:
        out["attribute_updates"] = []
    return out
