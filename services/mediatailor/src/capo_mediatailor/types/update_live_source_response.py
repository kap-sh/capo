"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateLiveSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.http_package_configurations


class UpdateLiveSourceResponse(TypedDict, closed=True):
    arn: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) associated with this live source.</p>"""
    creation_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the live source was created.</p>"""
    http_package_configurations: NotRequired[
        "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations"
    ]
    """<p>A list of HTTP package configurations for the live source on this account.</p>"""
    last_modified_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the live source was last modified.</p>"""
    live_source_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the live source.</p>"""
    source_location_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the source location associated with the live source.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLiveSourceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["CreationTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    if "http_package_configurations" in value:
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
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateLiveSourceResponse:
    out: UpdateLiveSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
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
    if data.get("LastModifiedTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            capo_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if data.get("LiveSourceName") is not None:
        out["live_source_name"] = data["LiveSourceName"]
    if data.get("SourceLocationName") is not None:
        out["source_location_name"] = data["SourceLocationName"]
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
