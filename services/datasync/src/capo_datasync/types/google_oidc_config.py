"""Generated from Smithy shape ``com.amazonaws.datasync#GoogleOidcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.google_identity_federation_resource_string
    import capo_datasync.types.project_name_string
    import capo_datasync.types.project_number_string


class GoogleOidcConfig(TypedDict, closed=True):
    project_name: "capo_datasync.types.project_name_string.ProjectNameString"
    """<p>Human-readable project name (e.g. "my-project").</p>"""
    project_number: "capo_datasync.types.project_number_string.ProjectNumberString"
    """<p>Numeric project ID as a string (e.g. "123456789").</p>"""
    identity_pool_name: "capo_datasync.types.google_identity_federation_resource_string.GoogleIdentityFederationResourceString"
    """<p>Human-readable pool name (e.g. "my-pool").</p>"""
    identity_provider_name: "capo_datasync.types.google_identity_federation_resource_string.GoogleIdentityFederationResourceString"
    """<p>Human-readable provider name (e.g. "my-oidc-provider").</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GoogleOidcConfig) -> dict:
    out: dict = {}
    out["ProjectName"] = value["project_name"]
    out["ProjectNumber"] = value["project_number"]
    out["IdentityPoolName"] = value["identity_pool_name"]
    out["IdentityProviderName"] = value["identity_provider_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GoogleOidcConfig:
    out: GoogleOidcConfig = {}  # type: ignore[typeddict-item]
    if data.get("ProjectName") is not None:
        out["project_name"] = data["ProjectName"]
    else:
        out["project_name"] = ""
    if data.get("ProjectNumber") is not None:
        out["project_number"] = data["ProjectNumber"]
    else:
        out["project_number"] = ""
    if data.get("IdentityPoolName") is not None:
        out["identity_pool_name"] = data["IdentityPoolName"]
    else:
        out["identity_pool_name"] = ""
    if data.get("IdentityProviderName") is not None:
        out["identity_provider_name"] = data["IdentityProviderName"]
    else:
        out["identity_provider_name"] = ""
    return out
