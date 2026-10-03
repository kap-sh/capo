"""Generated from Smithy shape ``com.amazonaws.s3vectors#MetadataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3vectors.types.non_filterable_metadata_keys


class MetadataConfiguration(TypedDict, closed=True):
    non_filterable_metadata_keys: (
        "capo_s3vectors.types.non_filterable_metadata_keys.NonFilterableMetadataKeys"
    )
    """<p>Non-filterable metadata keys allow you to enrich vectors with additional context during storage and retrieval. Unlike default metadata keys, these keys can’t be used as query filters. Non-filterable metadata keys can be retrieved but can’t be searched, queried, or filtered. You can access non-filterable metadata keys of your vectors after finding the vectors. For more information about non-filterable metadata keys, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-vectors.html">Vectors</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-limitations.html">Limitations and restrictions</a> in the <i>Amazon S3 User Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfiguration) -> dict:
    out: dict = {}
    import capo_s3vectors.types.non_filterable_metadata_keys

    out["nonFilterableMetadataKeys"] = (
        capo_s3vectors.types.non_filterable_metadata_keys.serialize_json(
            value["non_filterable_metadata_keys"]
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
        raise DeserializationError(
            "MetadataConfiguration.non_filterable_metadata_keys required"
        )
    return out
