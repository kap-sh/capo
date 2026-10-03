"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StorageConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.s3_storage_configuration
    import capo_ivs_realtime.types.storage_configuration_arn
    import capo_ivs_realtime.types.storage_configuration_name
    import capo_ivs_realtime.types.tags


class StorageConfigurationSummary(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.storage_configuration_arn.StorageConfigurationArn"
    """<p>ARN of the storage configuration.</p>"""
    name: NotRequired[
        "capo_ivs_realtime.types.storage_configuration_name.StorageConfigurationName"
    ]
    """<p>Name of the storage configuration.</p>"""
    s3: NotRequired[
        "capo_ivs_realtime.types.s3_storage_configuration.S3StorageConfiguration"
    ]
    """<p>An S3 destination configuration where recorded videos will be stored.</p>"""
    tags: NotRequired["capo_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfigurationSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "s3" in value:
        import capo_ivs_realtime.types.s3_storage_configuration

        out["s3"] = capo_ivs_realtime.types.s3_storage_configuration.serialize_json(
            value["s3"]
        )
    if "tags" in value:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StorageConfigurationSummary:
    out: StorageConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("StorageConfigurationSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("s3") is not None:
        import capo_ivs_realtime.types.s3_storage_configuration

        out["s3"] = capo_ivs_realtime.types.s3_storage_configuration.deserialize_json(
            data["s3"]
        )
    if data.get("tags") is not None:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
