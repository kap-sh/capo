"""Generated from Smithy shape ``com.amazonaws.acm#UpdateAcmeEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_authorization_behavior
    import capo_acm.types.acme_contact
    import capo_acm.types.acme_endpoint_arn
    import capo_acm.types.certificate_authority


class UpdateAcmeEndpointRequest(TypedDict, closed=True):
    acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the ACME endpoint to update.</p>"""
    authorization_behavior: NotRequired[
        "capo_acm.types.acme_authorization_behavior.AcmeAuthorizationBehavior"
    ]
    """<p>The updated authorization behavior.</p>"""
    contact: NotRequired["capo_acm.types.acme_contact.AcmeContact"]
    """<p>The updated contact requirement.</p>"""
    certificate_authority: NotRequired[
        "capo_acm.types.certificate_authority.CertificateAuthority"
    ]
    """<p>The updated certificate authority configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAcmeEndpointRequest) -> dict:
    out: dict = {}
    out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    if "authorization_behavior" in value:
        import capo_acm.types.acme_authorization_behavior

        out["AuthorizationBehavior"] = (
            capo_acm.types.acme_authorization_behavior.serialize_aws_json_1_1(
                value["authorization_behavior"]
            )
        )
    if "contact" in value:
        import capo_acm.types.acme_contact

        out["Contact"] = capo_acm.types.acme_contact.serialize_aws_json_1_1(
            value["contact"]
        )
    if "certificate_authority" in value:
        import capo_acm.types.certificate_authority

        out["CertificateAuthority"] = (
            capo_acm.types.certificate_authority.serialize_aws_json_1_1(
                value["certificate_authority"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAcmeEndpointRequest:
    out: UpdateAcmeEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    else:
        out["acme_endpoint_arn"] = ""
    if data.get("AuthorizationBehavior") is not None:
        import capo_acm.types.acme_authorization_behavior

        out["authorization_behavior"] = (
            capo_acm.types.acme_authorization_behavior.deserialize_aws_json_1_1(
                data["AuthorizationBehavior"]
            )
        )
    if data.get("Contact") is not None:
        import capo_acm.types.acme_contact

        out["contact"] = capo_acm.types.acme_contact.deserialize_aws_json_1_1(
            data["Contact"]
        )
    if data.get("CertificateAuthority") is not None:
        import capo_acm.types.certificate_authority

        out["certificate_authority"] = (
            capo_acm.types.certificate_authority.deserialize_aws_json_1_1(
                data["CertificateAuthority"]
            )
        )
    return out
