"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectStorageExternalIdentityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.google_oidc_config


class ObjectStorageExternalIdentityConfig(TypedDict, closed=True):
    google_oidc: NotRequired["capo_datasync.types.google_oidc_config.GoogleOidcConfig"]
    """<p>External identity parameters for Google Cloud Storage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectStorageExternalIdentityConfig) -> dict:
    out: dict = {}
    if "google_oidc" in value:
        import capo_datasync.types.google_oidc_config

        out["GoogleOidc"] = (
            capo_datasync.types.google_oidc_config.serialize_aws_json_1_1(
                value["google_oidc"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ObjectStorageExternalIdentityConfig:
    out: ObjectStorageExternalIdentityConfig = {}  # type: ignore[typeddict-item]
    if data.get("GoogleOidc") is not None:
        import capo_datasync.types.google_oidc_config

        out["google_oidc"] = (
            capo_datasync.types.google_oidc_config.deserialize_aws_json_1_1(
                data["GoogleOidc"]
            )
        )
    return out
