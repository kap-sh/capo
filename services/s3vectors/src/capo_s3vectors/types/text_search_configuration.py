"""Generated from Smithy shape ``com.amazonaws.s3vectors#TextSearchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.analyzer_status
    import capo_s3vectors.types.language_code
    import capo_s3vectors.types.metadata_key


class TextSearchConfiguration(TypedDict, closed=True):
    metadata_key: "capo_s3vectors.types.metadata_key.MetadataKey"
    """<p>The metadata key to make full-text searchable.</p>"""
    language: NotRequired["capo_s3vectors.types.language_code.LanguageCode"]
    """<p>The language that the text search analyzer uses. Valid values are <code>en</code> (English), <code>fr</code> (French), <code>es</code> (Spanish), <code>pt</code> (Portuguese), <code>it</code> (Italian), <code>de</code> (German), <code>nl</code> (Dutch), <code>zh</code> (Chinese), <code>ja</code> (Japanese), and <code>ko</code> (Korean). If you don't specify a language, Amazon S3 Vectors uses the default standard analyzer.</p>"""
    status: NotRequired["capo_s3vectors.types.analyzer_status.AnalyzerStatus"]
    """<p>The backfill status of the text search configuration. Valid values are <code>ACTIVE</code>, which indicates that the analyzer is built and serving queries, and <code>BUILDING</code>, which indicates that the analyzer is being backfilled and isn't yet serving queries. This field is returned by <code>GetIndex</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextSearchConfiguration) -> dict:
    out: dict = {}
    out["metadataKey"] = value["metadata_key"]
    if "language" in value:
        import capo_s3vectors.types.language_code

        out["language"] = capo_s3vectors.types.language_code.serialize_json(
            value["language"]
        )
    if "status" in value:
        import capo_s3vectors.types.analyzer_status

        out["status"] = capo_s3vectors.types.analyzer_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> TextSearchConfiguration:
    out: TextSearchConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("metadataKey") is not None:
        out["metadata_key"] = data["metadataKey"]
    else:
        out["metadata_key"] = ""
    if data.get("language") is not None:
        import capo_s3vectors.types.language_code

        out["language"] = capo_s3vectors.types.language_code.deserialize_json(
            data["language"]
        )
    if data.get("status") is not None:
        import capo_s3vectors.types.analyzer_status

        out["status"] = capo_s3vectors.types.analyzer_status.deserialize_json(
            data["status"]
        )
    return out
