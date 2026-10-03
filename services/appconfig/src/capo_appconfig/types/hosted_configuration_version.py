"""Generated from Smithy shape ``com.amazonaws.appconfig#HostedConfigurationVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.arn
    import capo_appconfig.types.blob
    import capo_appconfig.types.description
    import capo_appconfig.types.id
    import capo_appconfig.types.integer
    import capo_appconfig.types.string_with_length_between1_and255
    import capo_appconfig.types.version_label


class HostedConfigurationVersion(TypedDict, closed=True):
    application_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    configuration_profile_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The configuration profile ID.</p>"""
    version_number: "capo_appconfig.types.integer.Integer"
    """<p>The configuration version.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the configuration.</p>"""
    content: NotRequired["capo_appconfig.types.blob.Blob"]
    """<p>The content of the configuration or the configuration data.</p>"""
    content_type: NotRequired[
        "capo_appconfig.types.string_with_length_between1_and255.StringWithLengthBetween1And255"
    ]
    """<p>A standard MIME type describing the format of the configuration content. For more information, see <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17">Content-Type</a>.</p>"""
    version_label: NotRequired["capo_appconfig.types.version_label.VersionLabel"]
    """<p>A user-defined label for an AppConfig hosted configuration version.</p>"""
    kms_key_arn: NotRequired["capo_appconfig.types.arn.Arn"]
    """<p>The Amazon Resource Name of the Key Management Service key that was used to encrypt this specific version of the configuration data in the AppConfig hosted configuration store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostedConfigurationVersion) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_appconfig.types.blob

        out["Content"] = capo_appconfig.types.blob.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> HostedConfigurationVersion:
    out: HostedConfigurationVersion = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        import capo_appconfig.types.blob

        out["content"] = capo_appconfig.types.blob.deserialize_json(data["Content"])
    return out
