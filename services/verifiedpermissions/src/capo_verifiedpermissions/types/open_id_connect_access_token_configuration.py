"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdConnectAccessTokenConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.audiences
    import capo_verifiedpermissions.types.claim


class OpenIdConnectAccessTokenConfiguration(TypedDict, closed=True):
    principal_id_claim: "capo_verifiedpermissions.types.claim.Claim"
    """<p>The claim that determines the principal in OIDC access tokens. For example, <code>sub</code>.</p>"""
    audiences: NotRequired["capo_verifiedpermissions.types.audiences.Audiences"]
    """<p>The access token <code>aud</code> claim values that you want to accept in your policy store. For example, <code>https://myapp.example.com, https://myapp2.example.com</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenIdConnectAccessTokenConfiguration) -> dict:
    out: dict = {}
    out["principalIdClaim"] = value.get("principal_id_claim", "sub")
    if "audiences" in value:
        import capo_verifiedpermissions.types.audiences

        out["audiences"] = (
            capo_verifiedpermissions.types.audiences.serialize_aws_json_1_0(
                value["audiences"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpenIdConnectAccessTokenConfiguration:
    out: OpenIdConnectAccessTokenConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("principalIdClaim") is not None:
        out["principal_id_claim"] = data["principalIdClaim"]
    else:
        out["principal_id_claim"] = "sub"
    if data.get("audiences") is not None:
        import capo_verifiedpermissions.types.audiences

        out["audiences"] = (
            capo_verifiedpermissions.types.audiences.deserialize_aws_json_1_0(
                data["audiences"]
            )
        )
    return out


def redact_sensitive(value: OpenIdConnectAccessTokenConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "principal_id_claim" in value:
        out["principal_id_claim"] = "*** Sensitive Data Redacted ***"
    return out
