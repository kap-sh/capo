"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.selector_object_reference


class ObjectReference(TypedDict, closed=True):
    selector: NotRequired[
        "capo_clouddirectory.types.selector_object_reference.SelectorObjectReference"
    ]
    """<p>A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html">Access Objects</a>. You can identify an object in one of the following ways:</p> <ul> <li> <p> <i>$ObjectIdentifier</i> - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier. To identify an object with ObjectIdentifier, the ObjectIdentifier must be wrapped in double quotes. </p> </li> <li> <p> <i>/some/path</i> - Identifies the object based on path</p> </li> <li> <p> <i>#SomeBatchReference</i> - Identifies the object in a batch call</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectReference) -> dict:
    out: dict = {}
    if "selector" in value:
        out["Selector"] = value["selector"]
    return out


def deserialize_json(data: dict) -> ObjectReference:
    out: ObjectReference = {}  # type: ignore[typeddict-item]
    if data.get("Selector") is not None:
        out["selector"] = data["Selector"]
    return out
