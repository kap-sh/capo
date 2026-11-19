"""Generated from Smithy shape ``com.amazonaws.appstream#ApplicationSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.boolean
    import capo_appstream.types.settings_group
    import capo_appstream.types.string


class ApplicationSettingsResponse(TypedDict, closed=True):
    enabled: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Specifies whether persistent application settings are enabled for users during their streaming sessions.</p>"""
    settings_group: NotRequired["capo_appstream.types.settings_group.SettingsGroup"]
    """<p>The path prefix for the S3 bucket where users’ persistent application settings are stored.</p>"""
    s3_bucket_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The S3 bucket where users’ persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSettingsResponse) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "settings_group" in value:
        out["SettingsGroup"] = value["settings_group"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSettingsResponse:
    out: ApplicationSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("SettingsGroup") is not None:
        out["settings_group"] = data["SettingsGroup"]
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationSettingsResponse) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "settings_group" in value:
        out["SettingsGroup"] = value["settings_group"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    return out


def deserialize_cbor(data: dict) -> ApplicationSettingsResponse:
    out: ApplicationSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("SettingsGroup") is not None:
        out["settings_group"] = data["SettingsGroup"]
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    return out
