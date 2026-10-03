"""Generated from Smithy shape ``com.amazonaws.firehose#Serializer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.orc_ser_de
    import capo_firehose.types.parquet_ser_de


class Serializer(TypedDict, closed=True):
    parquet_ser_de: NotRequired["capo_firehose.types.parquet_ser_de.ParquetSerDe"]
    """<p>A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see <a href="https://parquet.apache.org/docs/contribution-guidelines/">Apache Parquet</a>.</p>"""
    orc_ser_de: NotRequired["capo_firehose.types.orc_ser_de.OrcSerDe"]
    """<p>A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see <a href="https://orc.apache.org/docs/">Apache ORC</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Serializer) -> dict:
    out: dict = {}
    if "parquet_ser_de" in value:
        import capo_firehose.types.parquet_ser_de

        out["ParquetSerDe"] = capo_firehose.types.parquet_ser_de.serialize_aws_json_1_1(
            value["parquet_ser_de"]
        )
    if "orc_ser_de" in value:
        import capo_firehose.types.orc_ser_de

        out["OrcSerDe"] = capo_firehose.types.orc_ser_de.serialize_aws_json_1_1(
            value["orc_ser_de"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Serializer:
    out: Serializer = {}  # type: ignore[typeddict-item]
    if data.get("ParquetSerDe") is not None:
        import capo_firehose.types.parquet_ser_de

        out["parquet_ser_de"] = (
            capo_firehose.types.parquet_ser_de.deserialize_aws_json_1_1(
                data["ParquetSerDe"]
            )
        )
    if data.get("OrcSerDe") is not None:
        import capo_firehose.types.orc_ser_de

        out["orc_ser_de"] = capo_firehose.types.orc_ser_de.deserialize_aws_json_1_1(
            data["OrcSerDe"]
        )
    return out
