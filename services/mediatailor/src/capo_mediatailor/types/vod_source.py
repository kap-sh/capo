"""Generated from Smithy shape ``com.amazonaws.mediatailor#VodSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.http_package_configurations


class VodSource(TypedDict, closed=True):
    arn: "capo_mediatailor.types.__string.__string"
    """<p>The ARN for the VOD source.</p>"""
    creation_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the VOD source was created.</p>"""
    http_package_configurations: (
        "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations"
    )
    """<p>The HTTP package configurations for the VOD source.</p>"""
    last_modified_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the VOD source was last modified.</p>"""
    source_location_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the source location that the VOD source is associated with.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags assigned to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    vod_source_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the VOD source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VodSource) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "creation_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["CreationTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    import capo_mediatailor.types.http_package_configurations

    out["HttpPackageConfigurations"] = (
        capo_mediatailor.types.http_package_configurations.serialize_json(
            value["http_package_configurations"]
        )
    )
    if "last_modified_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["LastModifiedTime"] = (
            capo_mediatailor.types.__timestamp_unix.serialize_json(
                value["last_modified_time"]
            )
        )
    out["SourceLocationName"] = value["source_location_name"]
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    out["VodSourceName"] = value["vod_source_name"]
    return out


def deserialize_json(data: dict) -> VodSource:
    out: VodSource = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("VodSource.arn required")
    if data.get("CreationTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["creation_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["CreationTime"]
        )
    if data.get("HttpPackageConfigurations") is not None:
        import capo_mediatailor.types.http_package_configurations

        out["http_package_configurations"] = (
            capo_mediatailor.types.http_package_configurations.deserialize_json(
                data["HttpPackageConfigurations"]
            )
        )
    else:
        raise DeserializationError("VodSource.http_package_configurations required")
    if data.get("LastModifiedTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            capo_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if data.get("SourceLocationName") is not None:
        out["source_location_name"] = data["SourceLocationName"]
    else:
        raise DeserializationError("VodSource.source_location_name required")
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if data.get("VodSourceName") is not None:
        out["vod_source_name"] = data["VodSourceName"]
    else:
        raise DeserializationError("VodSource.vod_source_name required")
    return out
