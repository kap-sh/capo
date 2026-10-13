"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DetectedProfileObjectType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.field_map
    import capo_customer_profiles.types.key_map
    import capo_customer_profiles.types.string1_to255


class DetectedProfileObjectType(TypedDict, closed=True):
    source_last_updated_timestamp_format: NotRequired[
        "capo_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The format of <code>sourceLastUpdatedTimestamp</code> that was detected in fields.</p>"""
    fields: NotRequired["capo_customer_profiles.types.field_map.FieldMap"]
    """<p>A map of the name and the <code>ObjectType</code> field.</p>"""
    keys: NotRequired["capo_customer_profiles.types.key_map.KeyMap"]
    """<p>A list of unique keys that can be used to map data to a profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectedProfileObjectType) -> dict:
    out: dict = {}
    if "source_last_updated_timestamp_format" in value:
        out["SourceLastUpdatedTimestampFormat"] = value[
            "source_last_updated_timestamp_format"
        ]
    if "fields" in value:
        import capo_customer_profiles.types.field_map

        out["Fields"] = capo_customer_profiles.types.field_map.serialize_json(
            value["fields"]
        )
    if "keys" in value:
        import capo_customer_profiles.types.key_map

        out["Keys"] = capo_customer_profiles.types.key_map.serialize_json(value["keys"])
    return out


def deserialize_json(data: dict) -> DetectedProfileObjectType:
    out: DetectedProfileObjectType = {}  # type: ignore[typeddict-item]
    if data.get("SourceLastUpdatedTimestampFormat") is not None:
        out["source_last_updated_timestamp_format"] = data[
            "SourceLastUpdatedTimestampFormat"
        ]
    if data.get("Fields") is not None:
        import capo_customer_profiles.types.field_map

        out["fields"] = capo_customer_profiles.types.field_map.deserialize_json(
            data["Fields"]
        )
    if data.get("Keys") is not None:
        import capo_customer_profiles.types.key_map

        out["keys"] = capo_customer_profiles.types.key_map.deserialize_json(
            data["Keys"]
        )
    return out


def redact_sensitive(value: DetectedProfileObjectType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fields" in value:
        out["fields"] = "*** Sensitive Data Redacted ***"
    if "keys" in value:
        out["keys"] = "*** Sensitive Data Redacted ***"
    return out
