"""Generated from Smithy shape ``com.amazonaws.s3vectors#MetadataConfigurationAdd``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.text_search_configurations


class MetadataConfigurationAdd(TypedDict, closed=True):
    text_search_configurations: NotRequired[
        "capo_s3vectors.types.text_search_configurations.TextSearchConfigurations"
    ]
    """<p>Text search configurations to add. Amazon S3 Vectors begins building the corresponding full-text indexes after the update is accepted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfigurationAdd) -> dict:
    out: dict = {}
    if "text_search_configurations" in value:
        import capo_s3vectors.types.text_search_configurations

        out["textSearchConfigurations"] = (
            capo_s3vectors.types.text_search_configurations.serialize_json(
                value["text_search_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataConfigurationAdd:
    out: MetadataConfigurationAdd = {}  # type: ignore[typeddict-item]
    if data.get("textSearchConfigurations") is not None:
        import capo_s3vectors.types.text_search_configurations

        out["text_search_configurations"] = (
            capo_s3vectors.types.text_search_configurations.deserialize_json(
                data["textSearchConfigurations"]
            )
        )
    return out
