"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UpdateTrustedTokenIssuerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.trusted_token_issuer_arn
    import capo_sso_admin.types.trusted_token_issuer_name
    import capo_sso_admin.types.trusted_token_issuer_update_configuration


class UpdateTrustedTokenIssuerRequest(TypedDict, closed=True):
    trusted_token_issuer_arn: (
        "capo_sso_admin.types.trusted_token_issuer_arn.TrustedTokenIssuerArn"
    )
    """<p>Specifies the ARN of the trusted token issuer configuration that you want to update.</p>"""
    name: NotRequired[
        "capo_sso_admin.types.trusted_token_issuer_name.TrustedTokenIssuerName"
    ]
    """<p>Specifies the updated name to be applied to the trusted token issuer configuration.</p>"""
    trusted_token_issuer_configuration: NotRequired[
        "capo_sso_admin.types.trusted_token_issuer_update_configuration.TrustedTokenIssuerUpdateConfiguration"
    ]
    """<p>Specifies a structure with settings to apply to the specified trusted token issuer. The settings that you can provide are determined by the type of the trusted token issuer that you are updating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrustedTokenIssuerRequest) -> dict:
    out: dict = {}
    out["TrustedTokenIssuerArn"] = value["trusted_token_issuer_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "trusted_token_issuer_configuration" in value:
        import capo_sso_admin.types.trusted_token_issuer_update_configuration

        out["TrustedTokenIssuerConfiguration"] = (
            capo_sso_admin.types.trusted_token_issuer_update_configuration.serialize_aws_json_1_1(
                value["trusted_token_issuer_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrustedTokenIssuerRequest:
    out: UpdateTrustedTokenIssuerRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrustedTokenIssuerArn") is not None:
        out["trusted_token_issuer_arn"] = data["TrustedTokenIssuerArn"]
    else:
        out["trusted_token_issuer_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("TrustedTokenIssuerConfiguration") is not None:
        import capo_sso_admin.types.trusted_token_issuer_update_configuration

        out["trusted_token_issuer_configuration"] = (
            capo_sso_admin.types.trusted_token_issuer_update_configuration.deserialize_aws_json_1_1(
                data["TrustedTokenIssuerConfiguration"]
            )
        )
    return out
