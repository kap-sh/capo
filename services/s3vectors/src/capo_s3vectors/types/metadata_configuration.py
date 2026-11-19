"""Generated from Smithy shape ``com.amazonaws.s3vectors#MetadataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.non_filterable_metadata_keys
    import capo_s3vectors.types.text_search_configurations


class MetadataConfiguration(TypedDict, closed=True):
    non_filterable_metadata_keys: (
        "capo_s3vectors.types.non_filterable_metadata_keys.NonFilterableMetadataKeys"
    )
    """<p>Non-filterable metadata keys allow you to enrich vectors with additional context during storage and retrieval. You can't use these keys in metadata filters. You can still make a non-filterable key full-text searchable by configuring it separately in <code>textSearchConfigurations</code>. You can retrieve non-filterable metadata keys after finding the vectors. For more information about non-filterable metadata keys, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-vectors.html">Vectors</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-limitations.html">Limitations and restrictions</a> in the <i>Amazon S3 User Guide</i>. </p>"""
    text_search_configurations: (
        "capo_s3vectors.types.text_search_configurations.TextSearchConfigurations"
    )
    """<p>Full-text search configurations for searchable metadata keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfiguration) -> dict:
    out: dict = {}
    import capo_s3vectors.types.non_filterable_metadata_keys

    out["nonFilterableMetadataKeys"] = (
        capo_s3vectors.types.non_filterable_metadata_keys.serialize_json(
            value.get("non_filterable_metadata_keys", [])
        )
    )
    import capo_s3vectors.types.text_search_configurations

    out["textSearchConfigurations"] = (
        capo_s3vectors.types.text_search_configurations.serialize_json(
            value.get("text_search_configurations", [])
        )
    )
    return out


def deserialize_json(data: dict) -> MetadataConfiguration:
    out: MetadataConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("nonFilterableMetadataKeys") is not None:
        import capo_s3vectors.types.non_filterable_metadata_keys

        out["non_filterable_metadata_keys"] = (
            capo_s3vectors.types.non_filterable_metadata_keys.deserialize_json(
                data["nonFilterableMetadataKeys"]
            )
        )
    else:
        out["non_filterable_metadata_keys"] = []
    if data.get("textSearchConfigurations") is not None:
        import capo_s3vectors.types.text_search_configurations

        out["text_search_configurations"] = (
            capo_s3vectors.types.text_search_configurations.deserialize_json(
                data["textSearchConfigurations"]
            )
        )
    else:
        out["text_search_configurations"] = []
    return out
