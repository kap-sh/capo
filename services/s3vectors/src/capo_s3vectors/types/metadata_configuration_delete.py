"""Generated from Smithy shape ``com.amazonaws.s3vectors#MetadataConfigurationDelete``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.text_search_configuration_keys


class MetadataConfigurationDelete(TypedDict, closed=True):
    text_search_configurations: NotRequired[
        "capo_s3vectors.types.text_search_configuration_keys.TextSearchConfigurationKeys"
    ]
    """<p>Searchable metadata keys whose text search configurations to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfigurationDelete) -> dict:
    out: dict = {}
    if "text_search_configurations" in value:
        import capo_s3vectors.types.text_search_configuration_keys

        out["textSearchConfigurations"] = (
            capo_s3vectors.types.text_search_configuration_keys.serialize_json(
                value["text_search_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataConfigurationDelete:
    out: MetadataConfigurationDelete = {}  # type: ignore[typeddict-item]
    if data.get("textSearchConfigurations") is not None:
        import capo_s3vectors.types.text_search_configuration_keys

        out["text_search_configurations"] = (
            capo_s3vectors.types.text_search_configuration_keys.deserialize_json(
                data["textSearchConfigurations"]
            )
        )
    return out
