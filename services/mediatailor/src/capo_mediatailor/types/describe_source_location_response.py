"""Generated from Smithy shape ``com.amazonaws.mediatailor#DescribeSourceLocationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of_segment_delivery_configuration
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.access_configuration
    import capo_mediatailor.types.default_segment_delivery_configuration
    import capo_mediatailor.types.http_configuration


class DescribeSourceLocationResponse(TypedDict, closed=True):
    access_configuration: NotRequired[
        "capo_mediatailor.types.access_configuration.AccessConfiguration"
    ]
    """<p>The access configuration for the source location.</p>"""
    arn: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The ARN of the source location.</p>"""
    creation_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the source location was created.</p>"""
    default_segment_delivery_configuration: NotRequired[
        "capo_mediatailor.types.default_segment_delivery_configuration.DefaultSegmentDeliveryConfiguration"
    ]
    """<p>The default segment delivery configuration settings.</p>"""
    http_configuration: NotRequired[
        "capo_mediatailor.types.http_configuration.HttpConfiguration"
    ]
    """<p>The HTTP package configuration settings for the source location.</p>"""
    last_modified_time: NotRequired[
        "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the source location was last modified.</p>"""
    segment_delivery_configurations: NotRequired[
        "capo_mediatailor.types.__list_of_segment_delivery_configuration.__listOfSegmentDeliveryConfiguration"
    ]
    """<p>A list of the segment delivery configurations associated with this resource.</p>"""
    source_location_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name of the source location.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags assigned to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceLocationResponse) -> dict:
    out: dict = {}
    if "access_configuration" in value:
        import capo_mediatailor.types.access_configuration

        out["AccessConfiguration"] = (
            capo_mediatailor.types.access_configuration.serialize_json(
                value["access_configuration"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["CreationTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    if "default_segment_delivery_configuration" in value:
        import capo_mediatailor.types.default_segment_delivery_configuration

        out["DefaultSegmentDeliveryConfiguration"] = (
            capo_mediatailor.types.default_segment_delivery_configuration.serialize_json(
                value["default_segment_delivery_configuration"]
            )
        )
    if "http_configuration" in value:
        import capo_mediatailor.types.http_configuration

        out["HttpConfiguration"] = (
            capo_mediatailor.types.http_configuration.serialize_json(
                value["http_configuration"]
            )
        )
    if "last_modified_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["LastModifiedTime"] = (
            capo_mediatailor.types.__timestamp_unix.serialize_json(
                value["last_modified_time"]
            )
        )
    if "segment_delivery_configurations" in value:
        import capo_mediatailor.types.__list_of_segment_delivery_configuration

        out["SegmentDeliveryConfigurations"] = (
            capo_mediatailor.types.__list_of_segment_delivery_configuration.serialize_json(
                value["segment_delivery_configurations"]
            )
        )
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> DescribeSourceLocationResponse:
    out: DescribeSourceLocationResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccessConfiguration") is not None:
        import capo_mediatailor.types.access_configuration

        out["access_configuration"] = (
            capo_mediatailor.types.access_configuration.deserialize_json(
                data["AccessConfiguration"]
            )
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreationTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["creation_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["CreationTime"]
        )
    if data.get("DefaultSegmentDeliveryConfiguration") is not None:
        import capo_mediatailor.types.default_segment_delivery_configuration

        out["default_segment_delivery_configuration"] = (
            capo_mediatailor.types.default_segment_delivery_configuration.deserialize_json(
                data["DefaultSegmentDeliveryConfiguration"]
            )
        )
    if data.get("HttpConfiguration") is not None:
        import capo_mediatailor.types.http_configuration

        out["http_configuration"] = (
            capo_mediatailor.types.http_configuration.deserialize_json(
                data["HttpConfiguration"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            capo_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if data.get("SegmentDeliveryConfigurations") is not None:
        import capo_mediatailor.types.__list_of_segment_delivery_configuration

        out["segment_delivery_configurations"] = (
            capo_mediatailor.types.__list_of_segment_delivery_configuration.deserialize_json(
                data["SegmentDeliveryConfigurations"]
            )
        )
    if data.get("SourceLocationName") is not None:
        out["source_location_name"] = data["SourceLocationName"]
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
