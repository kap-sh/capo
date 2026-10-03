"""Generated from Smithy shape ``com.amazonaws.glue#XMLClassifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.classification
    import capo_glue.types.name_string
    import capo_glue.types.row_tag
    import capo_glue.types.timestamp
    import capo_glue.types.version_id


class XMLClassifier(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    classification: "capo_glue.types.classification.Classification"
    """<p>An identifier of the data format that the classifier matches.</p>"""
    creation_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was registered.</p>"""
    last_updated: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was last updated.</p>"""
    version: "capo_glue.types.version_id.VersionId"
    """<p>The version of this classifier.</p>"""
    row_tag: NotRequired["capo_glue.types.row_tag.RowTag"]
    """<p>The XML tag designating the element that contains each record in an XML document being parsed. This can't identify a self-closing element (closed by <code>/></code>). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <code><row item_a="A" item_b="B"></row></code> is okay, but <code><row item_a="A" item_b="B" /></code> is not).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XMLClassifier) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Classification"] = value["classification"]
    if "creation_time" in value:
        import capo_glue.types.timestamp

        out["CreationTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated" in value:
        import capo_glue.types.timestamp

        out["LastUpdated"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    out["Version"] = value.get("version", 0)
    if "row_tag" in value:
        out["RowTag"] = value["row_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> XMLClassifier:
    out: XMLClassifier = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("XMLClassifier.name required")
    if data.get("Classification") is not None:
        out["classification"] = data["Classification"]
    else:
        raise DeserializationError("XMLClassifier.classification required")
    if data.get("CreationTime") is not None:
        import capo_glue.types.timestamp

        out["creation_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastUpdated") is not None:
        import capo_glue.types.timestamp

        out["last_updated"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastUpdated"]
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if data.get("RowTag") is not None:
        out["row_tag"] = data["RowTag"]
    return out
