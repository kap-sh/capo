"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateHostedConfigurationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appconfig.types.blob
    import capo_appconfig.types.description
    import capo_appconfig.types.integer
    import capo_appconfig.types.long_name
    import capo_appconfig.types.name
    import capo_appconfig.types.string_with_length_between1_and255
    import capo_appconfig.types.version_label


class CreateHostedConfigurationVersionRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.name.Name"
    """<p>The application ID.</p>"""
    configuration_profile_id: "capo_appconfig.types.long_name.LongName"
    """<p>The configuration profile ID.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the configuration.</p> <note> <p>Due to HTTP limitations, this field only supports ASCII characters.</p> </note>"""
    content: "capo_appconfig.types.blob.Blob"
    """<p>The configuration data, as bytes.</p> <note> <p>AppConfig accepts any type of data, including text formats like JSON or TOML, or binary formats like protocol buffers or compressed data.</p> </note>"""
    content_type: "capo_appconfig.types.string_with_length_between1_and255.StringWithLengthBetween1And255"
    """<p>A standard MIME type describing the format of the configuration content. For more information, see <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17">Content-Type</a>.</p>"""
    latest_version_number: NotRequired["capo_appconfig.types.integer.Integer"]
    """<p>An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.</p>"""
    version_label: NotRequired["capo_appconfig.types.version_label.VersionLabel"]
    """<p>An optional, user-defined label for the AppConfig hosted configuration version. This value must contain at least one non-numeric character. For example, "v2.2.0".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHostedConfigurationVersionRequest) -> dict:
    out: dict = {}
    import capo_appconfig.types.blob

    out["Content"] = capo_appconfig.types.blob.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> CreateHostedConfigurationVersionRequest:
    out: CreateHostedConfigurationVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        import capo_appconfig.types.blob

        out["content"] = capo_appconfig.types.blob.deserialize_json(data["Content"])
    else:
        raise DeserializationError(
            "CreateHostedConfigurationVersionRequest.content required"
        )
    return out
