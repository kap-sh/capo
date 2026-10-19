"""Generated from Smithy shape ``com.amazonaws.amplify#CreateDomainAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.app_id
    import capo_amplify.types.auto_sub_domain_creation_patterns
    import capo_amplify.types.auto_sub_domain_iam_role
    import capo_amplify.types.certificate_settings
    import capo_amplify.types.domain_name
    import capo_amplify.types.enable_auto_sub_domain
    import capo_amplify.types.sub_domain_settings


class CreateDomainAssociationRequest(TypedDict, closed=True):
    app_id: "capo_amplify.types.app_id.AppId"
    """<p> The unique ID for an Amplify app. </p>"""
    domain_name: "capo_amplify.types.domain_name.DomainName"
    """<p> The domain name for the domain association. </p>"""
    enable_auto_sub_domain: NotRequired[
        "capo_amplify.types.enable_auto_sub_domain.EnableAutoSubDomain"
    ]
    """<p> Enables the automated creation of subdomains for branches. </p>"""
    sub_domain_settings: "capo_amplify.types.sub_domain_settings.SubDomainSettings"
    """<p> The setting for the subdomain. </p>"""
    auto_sub_domain_creation_patterns: NotRequired[
        "capo_amplify.types.auto_sub_domain_creation_patterns.AutoSubDomainCreationPatterns"
    ]
    """<p> Sets the branch patterns for automatic subdomain creation. </p>"""
    auto_sub_domain_iam_role: NotRequired[
        "capo_amplify.types.auto_sub_domain_iam_role.AutoSubDomainIAMRole"
    ]
    """<p> The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains. </p>"""
    certificate_settings: NotRequired[
        "capo_amplify.types.certificate_settings.CertificateSettings"
    ]
    """<p>The type of SSL/TLS certificate to use for your custom domain. If you don't specify a certificate type, Amplify uses the default certificate that it provisions and manages for you.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainAssociationRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    if "enable_auto_sub_domain" in value:
        out["enableAutoSubDomain"] = value["enable_auto_sub_domain"]
    import capo_amplify.types.sub_domain_settings

    out["subDomainSettings"] = capo_amplify.types.sub_domain_settings.serialize_json(
        value["sub_domain_settings"]
    )
    if "auto_sub_domain_creation_patterns" in value:
        import capo_amplify.types.auto_sub_domain_creation_patterns

        out["autoSubDomainCreationPatterns"] = (
            capo_amplify.types.auto_sub_domain_creation_patterns.serialize_json(
                value["auto_sub_domain_creation_patterns"]
            )
        )
    if "auto_sub_domain_iam_role" in value:
        out["autoSubDomainIAMRole"] = value["auto_sub_domain_iam_role"]
    if "certificate_settings" in value:
        import capo_amplify.types.certificate_settings

        out["certificateSettings"] = (
            capo_amplify.types.certificate_settings.serialize_json(
                value["certificate_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDomainAssociationRequest:
    out: CreateDomainAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("enableAutoSubDomain") is not None:
        out["enable_auto_sub_domain"] = data["enableAutoSubDomain"]
    if data.get("subDomainSettings") is not None:
        import capo_amplify.types.sub_domain_settings

        out["sub_domain_settings"] = (
            capo_amplify.types.sub_domain_settings.deserialize_json(
                data["subDomainSettings"]
            )
        )
    else:
        out["sub_domain_settings"] = []
    if data.get("autoSubDomainCreationPatterns") is not None:
        import capo_amplify.types.auto_sub_domain_creation_patterns

        out["auto_sub_domain_creation_patterns"] = (
            capo_amplify.types.auto_sub_domain_creation_patterns.deserialize_json(
                data["autoSubDomainCreationPatterns"]
            )
        )
    if data.get("autoSubDomainIAMRole") is not None:
        out["auto_sub_domain_iam_role"] = data["autoSubDomainIAMRole"]
    if data.get("certificateSettings") is not None:
        import capo_amplify.types.certificate_settings

        out["certificate_settings"] = (
            capo_amplify.types.certificate_settings.deserialize_json(
                data["certificateSettings"]
            )
        )
    return out
