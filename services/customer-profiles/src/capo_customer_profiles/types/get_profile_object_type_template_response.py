"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetProfileObjectTypeTemplateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.boolean
    import capo_customer_profiles.types.field_map
    import capo_customer_profiles.types.key_map
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to255


class GetProfileObjectTypeTemplateResponse(TypedDict, closed=True):
    template_id: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>A unique identifier for the object template.</p>"""
    source_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the source of the object template.</p>"""
    source_object: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The source of the object template.</p>"""
    allow_profile_creation: "capo_customer_profiles.types.boolean.boolean"
    """<p>Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is <code>FALSE</code>. If the AllowProfileCreation flag is set to <code>FALSE</code>, then the service tries to fetch a standard profile and associate this object with the profile. If it is set to <code>TRUE</code>, and if no match is found, then the service creates a new standard profile.</p>"""
    source_last_updated_timestamp_format: NotRequired[
        "capo_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The format of your <code>sourceLastUpdatedTimestamp</code> that was previously set up.</p>"""
    fields: NotRequired["capo_customer_profiles.types.field_map.FieldMap"]
    """<p>A map of the name and ObjectType field.</p>"""
    keys: NotRequired["capo_customer_profiles.types.key_map.KeyMap"]
    """<p>A list of unique keys that can be used to map data to the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileObjectTypeTemplateResponse) -> dict:
    out: dict = {}
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    if "source_object" in value:
        out["SourceObject"] = value["source_object"]
    out["AllowProfileCreation"] = value.get("allow_profile_creation", False)
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


def deserialize_json(data: dict) -> GetProfileObjectTypeTemplateResponse:
    out: GetProfileObjectTypeTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("TemplateId") is not None:
        out["template_id"] = data["TemplateId"]
    if data.get("SourceName") is not None:
        out["source_name"] = data["SourceName"]
    if data.get("SourceObject") is not None:
        out["source_object"] = data["SourceObject"]
    if data.get("AllowProfileCreation") is not None:
        out["allow_profile_creation"] = data["AllowProfileCreation"]
    else:
        out["allow_profile_creation"] = False
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


def redact_sensitive(value: GetProfileObjectTypeTemplateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fields" in value:
        out["fields"] = "*** Sensitive Data Redacted ***"
    if "keys" in value:
        out["keys"] = "*** Sensitive Data Redacted ***"
    return out
