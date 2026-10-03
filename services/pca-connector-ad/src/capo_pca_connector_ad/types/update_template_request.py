"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#UpdateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.template_arn
    import capo_pca_connector_ad.types.template_definition


class UpdateTemplateRequest(TypedDict, closed=True):
    template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>"""
    definition: NotRequired[
        "capo_pca_connector_ad.types.template_definition.TemplateDefinition"
    ]
    """<p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>"""
    reenroll_all_certificate_holders: NotRequired["bool"]
    """<p>This setting allows the major version of a template to be increased automatically. All members of Active Directory groups that are allowed to enroll with a template will receive a new certificate issued using that template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateRequest) -> dict:
    out: dict = {}
    if "definition" in value:
        import capo_pca_connector_ad.types.template_definition

        out["Definition"] = (
            capo_pca_connector_ad.types.template_definition.serialize_json(
                value["definition"]
            )
        )
    if "reenroll_all_certificate_holders" in value:
        out["ReenrollAllCertificateHolders"] = value["reenroll_all_certificate_holders"]
    return out


def deserialize_json(data: dict) -> UpdateTemplateRequest:
    out: UpdateTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("Definition") is not None:
        import capo_pca_connector_ad.types.template_definition

        out["definition"] = (
            capo_pca_connector_ad.types.template_definition.deserialize_json(
                data["Definition"]
            )
        )
    if data.get("ReenrollAllCertificateHolders") is not None:
        out["reenroll_all_certificate_holders"] = data["ReenrollAllCertificateHolders"]
    return out
