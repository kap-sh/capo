"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateOpenIdConnectIdentityTokenConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.claim
    import capo_verifiedpermissions.types.client_ids


class UpdateOpenIdConnectIdentityTokenConfiguration(TypedDict, closed=True):
    principal_id_claim: "capo_verifiedpermissions.types.claim.Claim"
    """<p>The claim that determines the principal in OIDC access tokens. For example, <code>sub</code>.</p>"""
    client_ids: NotRequired["capo_verifiedpermissions.types.client_ids.ClientIds"]
    """<p>The ID token audience, or client ID, claim values that you want to accept in your policy store from an OIDC identity provider. For example, <code>1example23456789, 2example10111213</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateOpenIdConnectIdentityTokenConfiguration,
) -> dict:
    out: dict = {}
    out["principalIdClaim"] = value.get("principal_id_claim", "sub")
    if "client_ids" in value:
        import capo_verifiedpermissions.types.client_ids

        out["clientIds"] = (
            capo_verifiedpermissions.types.client_ids.serialize_aws_json_1_0(
                value["client_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateOpenIdConnectIdentityTokenConfiguration:
    out: UpdateOpenIdConnectIdentityTokenConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("principalIdClaim") is not None:
        out["principal_id_claim"] = data["principalIdClaim"]
    else:
        out["principal_id_claim"] = "sub"
    if data.get("clientIds") is not None:
        import capo_verifiedpermissions.types.client_ids

        out["client_ids"] = (
            capo_verifiedpermissions.types.client_ids.deserialize_aws_json_1_0(
                data["clientIds"]
            )
        )
    return out


def redact_sensitive(
    value: UpdateOpenIdConnectIdentityTokenConfiguration,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "principal_id_claim" in value:
        out["principal_id_claim"] = "*** Sensitive Data Redacted ***"
    if "client_ids" in value:
        import capo_verifiedpermissions.types.client_ids

        out["client_ids"] = capo_verifiedpermissions.types.client_ids.redact_sensitive(
            value["client_ids"]
        )
    return out
