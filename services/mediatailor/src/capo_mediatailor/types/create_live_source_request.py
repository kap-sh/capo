"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateLiveSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.http_package_configurations


class CreateLiveSourceRequest(TypedDict, closed=True):
    http_package_configurations: (
        "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations"
    )
    """<p>A list of HTTP package configuration parameters for this live source.</p>"""
    live_source_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the live source.</p>"""
    source_location_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the source location.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLiveSourceRequest) -> dict:
    out: dict = {}
    import capo_mediatailor.types.http_package_configurations

    out["HttpPackageConfigurations"] = (
        capo_mediatailor.types.http_package_configurations.serialize_json(
            value["http_package_configurations"]
        )
    )
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateLiveSourceRequest:
    out: CreateLiveSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("HttpPackageConfigurations") is not None:
        import capo_mediatailor.types.http_package_configurations

        out["http_package_configurations"] = (
            capo_mediatailor.types.http_package_configurations.deserialize_json(
                data["HttpPackageConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLiveSourceRequest.http_package_configurations required"
        )
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
