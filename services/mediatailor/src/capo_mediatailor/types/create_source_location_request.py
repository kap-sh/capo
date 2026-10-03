"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateSourceLocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of_segment_delivery_configuration
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.access_configuration
    import capo_mediatailor.types.default_segment_delivery_configuration
    import capo_mediatailor.types.http_configuration


class CreateSourceLocationRequest(TypedDict, closed=True):
    access_configuration: NotRequired[
        "capo_mediatailor.types.access_configuration.AccessConfiguration"
    ]
    """<p>Access configuration parameters. Configures the type of authentication used to access content from your source location.</p>"""
    default_segment_delivery_configuration: NotRequired[
        "capo_mediatailor.types.default_segment_delivery_configuration.DefaultSegmentDeliveryConfiguration"
    ]
    """<p>The optional configuration for the server that serves segments.</p>"""
    http_configuration: "capo_mediatailor.types.http_configuration.HttpConfiguration"
    """<p>The source's HTTP package configurations.</p>"""
    segment_delivery_configurations: NotRequired[
        "capo_mediatailor.types.__list_of_segment_delivery_configuration.__listOfSegmentDeliveryConfiguration"
    ]
    """<p>A list of the segment delivery configurations associated with this resource.</p>"""
    source_location_name: "capo_mediatailor.types.__string.__string"
    """<p>The name associated with the source location.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSourceLocationRequest) -> dict:
    out: dict = {}
    if "access_configuration" in value:
        import capo_mediatailor.types.access_configuration

        out["AccessConfiguration"] = (
            capo_mediatailor.types.access_configuration.serialize_json(
                value["access_configuration"]
            )
        )
    if "default_segment_delivery_configuration" in value:
        import capo_mediatailor.types.default_segment_delivery_configuration

        out["DefaultSegmentDeliveryConfiguration"] = (
            capo_mediatailor.types.default_segment_delivery_configuration.serialize_json(
                value["default_segment_delivery_configuration"]
            )
        )
    import capo_mediatailor.types.http_configuration

    out["HttpConfiguration"] = capo_mediatailor.types.http_configuration.serialize_json(
        value["http_configuration"]
    )
    if "segment_delivery_configurations" in value:
        import capo_mediatailor.types.__list_of_segment_delivery_configuration

        out["SegmentDeliveryConfigurations"] = (
            capo_mediatailor.types.__list_of_segment_delivery_configuration.serialize_json(
                value["segment_delivery_configurations"]
            )
        )
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateSourceLocationRequest:
    out: CreateSourceLocationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessConfiguration") is not None:
        import capo_mediatailor.types.access_configuration

        out["access_configuration"] = (
            capo_mediatailor.types.access_configuration.deserialize_json(
                data["AccessConfiguration"]
            )
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
    else:
        raise DeserializationError(
            "CreateSourceLocationRequest.http_configuration required"
        )
    if data.get("SegmentDeliveryConfigurations") is not None:
        import capo_mediatailor.types.__list_of_segment_delivery_configuration

        out["segment_delivery_configurations"] = (
            capo_mediatailor.types.__list_of_segment_delivery_configuration.deserialize_json(
                data["SegmentDeliveryConfigurations"]
            )
        )
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
