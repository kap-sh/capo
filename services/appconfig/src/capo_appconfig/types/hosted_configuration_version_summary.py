"""Generated from Smithy shape ``com.amazonaws.appconfig#HostedConfigurationVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.arn
    import capo_appconfig.types.description
    import capo_appconfig.types.id
    import capo_appconfig.types.integer
    import capo_appconfig.types.string_with_length_between1_and255
    import capo_appconfig.types.version_label


class HostedConfigurationVersionSummary(TypedDict, closed=True):
    application_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    configuration_profile_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The configuration profile ID.</p>"""
    version_number: "capo_appconfig.types.integer.Integer"
    """<p>The configuration version.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the configuration.</p>"""
    content_type: NotRequired[
        "capo_appconfig.types.string_with_length_between1_and255.StringWithLengthBetween1And255"
    ]
    """<p>A standard MIME type describing the format of the configuration content. For more information, see <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17">Content-Type</a>.</p>"""
    version_label: NotRequired["capo_appconfig.types.version_label.VersionLabel"]
    """<p>A user-defined label for an AppConfig hosted configuration version.</p>"""
    kms_key_arn: NotRequired["capo_appconfig.types.arn.Arn"]
    """<p>The Amazon Resource Name of the Key Management Service key that was used to encrypt this specific version of the configuration data in the AppConfig hosted configuration store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostedConfigurationVersionSummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "configuration_profile_id" in value:
        out["ConfigurationProfileId"] = value["configuration_profile_id"]
    out["VersionNumber"] = value.get("version_number", 0)
    if "description" in value:
        out["Description"] = value["description"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "version_label" in value:
        out["VersionLabel"] = value["version_label"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> HostedConfigurationVersionSummary:
    out: HostedConfigurationVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("ConfigurationProfileId") is not None:
        out["configuration_profile_id"] = data["ConfigurationProfileId"]
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    else:
        out["version_number"] = 0
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("VersionLabel") is not None:
        out["version_label"] = data["VersionLabel"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
