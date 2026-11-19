"""Generated from Smithy shape ``com.amazonaws.datasync#SourceManifestConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.s3_manifest_config


class SourceManifestConfig(TypedDict, closed=True):
    s3: "capo_datasync.types.s3_manifest_config.S3ManifestConfig"
    """<p>Specifies the S3 bucket where you're hosting your manifest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceManifestConfig) -> dict:
    out: dict = {}
    import capo_datasync.types.s3_manifest_config

    out["S3"] = capo_datasync.types.s3_manifest_config.serialize_aws_json_1_1(
        value["s3"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceManifestConfig:
    out: SourceManifestConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3") is not None:
        import capo_datasync.types.s3_manifest_config

        out["s3"] = capo_datasync.types.s3_manifest_config.deserialize_aws_json_1_1(
            data["S3"]
        )
    else:
        raise DeserializationError("SourceManifestConfig.s3 required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceManifestConfig) -> dict:
    out: dict = {}
    import capo_datasync.types.s3_manifest_config

    out["S3"] = capo_datasync.types.s3_manifest_config.serialize_cbor(value["s3"])
    return out


def deserialize_cbor(data: dict) -> SourceManifestConfig:
    out: SourceManifestConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3") is not None:
        import capo_datasync.types.s3_manifest_config

        out["s3"] = capo_datasync.types.s3_manifest_config.deserialize_cbor(data["S3"])
    else:
        raise DeserializationError("SourceManifestConfig.s3 required")
    return out
