"""Generated from Smithy shape ``com.amazonaws.translate#OutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.encryption_key
    import capo_translate.types.s3_uri


class OutputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_translate.types.s3_uri.S3Uri"
    """<p>The URI of the S3 folder that contains a translation job's output file. The folder must be in the same Region as the API endpoint that you are calling.</p>"""
    encryption_key: NotRequired["capo_translate.types.encryption_key.EncryptionKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputDataConfig) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "encryption_key" in value:
        import capo_translate.types.encryption_key

        out["EncryptionKey"] = (
            capo_translate.types.encryption_key.serialize_aws_json_1_1(
                value["encryption_key"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputDataConfig:
    out: OutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("EncryptionKey") is not None:
        import capo_translate.types.encryption_key

        out["encryption_key"] = (
            capo_translate.types.encryption_key.deserialize_aws_json_1_1(
                data["EncryptionKey"]
            )
        )
    return out
