"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryptionProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.field_level_encryption_profile_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class FieldLevelEncryptionProfile(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The ID for a field-level encryption profile configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The last time the field-level encryption profile was updated.</p>"""
    field_level_encryption_profile_config: "capo_cloudfront.types.field_level_encryption_profile_config.FieldLevelEncryptionProfileConfig"
    """<p>A complex data type that includes the profile name and the encryption entities for the field-level encryption profile.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: FieldLevelEncryptionProfile, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    import capo_cloudfront.types.field_level_encryption_profile_config

    capo_cloudfront.types.field_level_encryption_profile_config.serialize_xml(
        value["field_level_encryption_profile_config"],
        el,
        "FieldLevelEncryptionProfileConfig",
    )


def deserialize_xml(el: Element) -> FieldLevelEncryptionProfile:
    out: FieldLevelEncryptionProfile = {}  # type: ignore[typeddict-item]
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
    child_field_level_encryption_profile_config = el.find(
        "FieldLevelEncryptionProfileConfig"
    )
    if child_field_level_encryption_profile_config is not None:
        import capo_cloudfront.types.field_level_encryption_profile_config

        out["field_level_encryption_profile_config"] = (
            capo_cloudfront.types.field_level_encryption_profile_config.deserialize_xml(
                child_field_level_encryption_profile_config
            )
        )
    else:
        raise DeserializationError(
            "FieldLevelEncryptionProfile.field_level_encryption_profile_config required"
        )
    return out
