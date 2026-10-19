"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.key_group_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class KeyGroup(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier for the key group.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the key group was last modified.</p>"""
    key_group_config: "capo_cloudfront.types.key_group_config.KeyGroupConfig"
    """<p>The key group configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeyGroup, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    import capo_cloudfront.types.key_group_config

    capo_cloudfront.types.key_group_config.serialize_xml(
        value["key_group_config"], el, "KeyGroupConfig"
    )


def deserialize_xml(el: Element) -> KeyGroup:
    out: KeyGroup = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_key_group_config = el.find("KeyGroupConfig")
    if child_key_group_config is not None:
        import capo_cloudfront.types.key_group_config

        out["key_group_config"] = (
            capo_cloudfront.types.key_group_config.deserialize_xml(
                child_key_group_config
            )
        )
    else:
        raise DeserializationError("KeyGroup.key_group_config required")
    return out
