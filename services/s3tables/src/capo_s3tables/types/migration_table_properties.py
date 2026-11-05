"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationTableProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.compression_codec
    import capo_s3tables.types.data_file_format


class MigrationTableProperties(TypedDict, closed=True):
    write_format: "capo_s3tables.types.data_file_format.DataFileFormat"
    """<p>The file format of the data files. The only supported format is <code>parquet</code>, the default.</p>"""
    iceberg_format_version: "int"
    """<p>The Iceberg format version of the destination table. Valid values are <code>2</code> and <code>3</code>. The default is <code>2</code>.</p>"""
    compression_codec: "capo_s3tables.types.compression_codec.CompressionCodec"
    """<p>The compression codec of the data files. The default is <code>zstd</code>.</p>"""
    dictionary_encoding: "bool"
    """<p>Specifies whether the data files use dictionary encoding. The default is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationTableProperties) -> dict:
    out: dict = {}
    import capo_s3tables.types.data_file_format

    out["writeFormat"] = capo_s3tables.types.data_file_format.serialize_json(
        value.get("write_format", "parquet")
    )
    out["icebergFormatVersion"] = value.get("iceberg_format_version", 2)
    import capo_s3tables.types.compression_codec

    out["compressionCodec"] = capo_s3tables.types.compression_codec.serialize_json(
        value.get("compression_codec", "zstd")
    )
    out["dictionaryEncoding"] = value.get("dictionary_encoding", True)
    return out


def deserialize_json(data: dict) -> MigrationTableProperties:
    out: MigrationTableProperties = {}  # type: ignore[typeddict-item]
    if data.get("writeFormat") is not None:
        import capo_s3tables.types.data_file_format

        out["write_format"] = capo_s3tables.types.data_file_format.deserialize_json(
            data["writeFormat"]
        )
    else:
        out["write_format"] = "parquet"
    if data.get("icebergFormatVersion") is not None:
        out["iceberg_format_version"] = data["icebergFormatVersion"]
    else:
        out["iceberg_format_version"] = 2
    if data.get("compressionCodec") is not None:
        import capo_s3tables.types.compression_codec

        out["compression_codec"] = (
            capo_s3tables.types.compression_codec.deserialize_json(
                data["compressionCodec"]
            )
        )
    else:
        out["compression_codec"] = "zstd"
    if data.get("dictionaryEncoding") is not None:
        out["dictionary_encoding"] = data["dictionaryEncoding"]
    else:
        out["dictionary_encoding"] = True
    return out
