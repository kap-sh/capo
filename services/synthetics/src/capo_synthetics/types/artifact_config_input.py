"""Generated from Smithy shape ``com.amazonaws.synthetics#ArtifactConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.s3_encryption_config


class ArtifactConfigInput(TypedDict, closed=True):
    s3_encryption: NotRequired[
        "capo_synthetics.types.s3_encryption_config.S3EncryptionConfig"
    ]
    """<p>A structure that contains the configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3. Artifact encryption functionality is available only for canaries that use Synthetics runtime version syn-nodejs-puppeteer-3.3 or later. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html">Encrypting canary artifacts</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactConfigInput) -> dict:
    out: dict = {}
    if "s3_encryption" in value:
        import capo_synthetics.types.s3_encryption_config

        out["S3Encryption"] = capo_synthetics.types.s3_encryption_config.serialize_json(
            value["s3_encryption"]
        )
    return out


def deserialize_json(data: dict) -> ArtifactConfigInput:
    out: ArtifactConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("S3Encryption") is not None:
        import capo_synthetics.types.s3_encryption_config

        out["s3_encryption"] = (
            capo_synthetics.types.s3_encryption_config.deserialize_json(
                data["S3Encryption"]
            )
        )
    return out
