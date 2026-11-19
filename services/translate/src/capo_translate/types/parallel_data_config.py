"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.parallel_data_format
    import capo_translate.types.s3_uri


class ParallelDataConfig(TypedDict, closed=True):
    s3_uri: NotRequired["capo_translate.types.s3_uri.S3Uri"]
    """<p>The URI of the Amazon S3 folder that contains the parallel data input file. The folder must be in the same Region as the API endpoint you are calling.</p>"""
    format: NotRequired["capo_translate.types.parallel_data_format.ParallelDataFormat"]
    """<p>The format of the parallel data input file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelDataConfig) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "format" in value:
        import capo_translate.types.parallel_data_format

        out["Format"] = (
            capo_translate.types.parallel_data_format.serialize_aws_json_1_1(
                value["format"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParallelDataConfig:
    out: ParallelDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    if data.get("Format") is not None:
        import capo_translate.types.parallel_data_format

        out["format"] = (
            capo_translate.types.parallel_data_format.deserialize_aws_json_1_1(
                data["Format"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ParallelDataConfig) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "format" in value:
        import capo_translate.types.parallel_data_format

        out["Format"] = capo_translate.types.parallel_data_format.serialize_cbor(
            value["format"]
        )
    return out


def deserialize_cbor(data: dict) -> ParallelDataConfig:
    out: ParallelDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    if data.get("Format") is not None:
        import capo_translate.types.parallel_data_format

        out["format"] = capo_translate.types.parallel_data_format.deserialize_cbor(
            data["Format"]
        )
    return out
