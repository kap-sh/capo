"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioLogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.s3_bucket_log_destination


class AudioLogDestination(TypedDict, closed=True):
    s3_bucket: (
        "capo_lex_models_v2.types.s3_bucket_log_destination.S3BucketLogDestination"
    )
    """<p>The Amazon S3 bucket where the audio log files are stored. The IAM role specified in the <code>roleArn</code> parameter of the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html">CreateBot</a> operation must have permission to write to this bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioLogDestination) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.s3_bucket_log_destination

    out["s3Bucket"] = capo_lex_models_v2.types.s3_bucket_log_destination.serialize_json(
        value["s3_bucket"]
    )
    return out


def deserialize_json(data: dict) -> AudioLogDestination:
    out: AudioLogDestination = {}  # type: ignore[typeddict-item]
    if data.get("s3Bucket") is not None:
        import capo_lex_models_v2.types.s3_bucket_log_destination

        out["s3_bucket"] = (
            capo_lex_models_v2.types.s3_bucket_log_destination.deserialize_json(
                data["s3Bucket"]
            )
        )
    else:
        raise DeserializationError("AudioLogDestination.s3_bucket required")
    return out
