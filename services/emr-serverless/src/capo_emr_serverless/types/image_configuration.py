"""Generated from Smithy shape ``com.amazonaws.emrserverless#ImageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.image_digest
    import capo_emr_serverless.types.image_uri


class ImageConfiguration(TypedDict, closed=True):
    image_uri: "capo_emr_serverless.types.image_uri.ImageUri"
    """<p>The image URI.</p>"""
    resolved_image_digest: NotRequired[
        "capo_emr_serverless.types.image_digest.ImageDigest"
    ]
    """<p>The SHA256 digest of the image URI. This indicates which specific image the application is configured for. The image digest doesn't exist until an application has started.</p>"""
    application_level_digest_resolution: NotRequired["bool"]
    """<p>Boolean value indicating if the digest resolution is application level or workload level. If true, a custom image URI is resolved at application start time and all workloads submitted will use that image digest. If false, the custom image URI is resolved at the workload submission time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageConfiguration) -> dict:
    out: dict = {}
    out["imageUri"] = value["image_uri"]
    if "resolved_image_digest" in value:
        out["resolvedImageDigest"] = value["resolved_image_digest"]
    if "application_level_digest_resolution" in value:
        out["applicationLevelDigestResolution"] = value[
            "application_level_digest_resolution"
        ]
    return out


def deserialize_json(data: dict) -> ImageConfiguration:
    out: ImageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("imageUri") is not None:
        out["image_uri"] = data["imageUri"]
    else:
        out["image_uri"] = ""
    if data.get("resolvedImageDigest") is not None:
        out["resolved_image_digest"] = data["resolvedImageDigest"]
    if data.get("applicationLevelDigestResolution") is not None:
        out["application_level_digest_resolution"] = data[
            "applicationLevelDigestResolution"
        ]
    return out
