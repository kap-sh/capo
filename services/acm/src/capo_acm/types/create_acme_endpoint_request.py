"""Generated from Smithy shape ``com.amazonaws.acm#CreateAcmeEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_authorization_behavior
    import capo_acm.types.acme_contact
    import capo_acm.types.certificate_authority
    import capo_acm.types.tag_list


class CreateAcmeEndpointRequest(TypedDict, closed=True):
    idempotency_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    authorization_behavior: (
        "capo_acm.types.acme_authorization_behavior.AcmeAuthorizationBehavior"
    )
    """<p>The authorization behavior for the ACME endpoint.</p>"""
    contact: NotRequired["capo_acm.types.acme_contact.AcmeContact"]
    """<p>Specifies whether ACME clients must provide contact information during account registration.</p>"""
    certificate_authority: "capo_acm.types.certificate_authority.CertificateAuthority"
    """<p>The type of certificate authority to use for issuing certificates through this ACME endpoint.</p>"""
    tags: NotRequired["capo_acm.types.tag_list.TagList"]
    """<p>One or more tags to associate with the ACME endpoint.</p>"""
    certificate_tags: NotRequired["capo_acm.types.tag_list.TagList"]
    """<p>Tags to apply to certificates issued through this ACME endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAcmeEndpointRequest) -> dict:
    out: dict = {}
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
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
    import capo_acm.types.certificate_authority

    out["CertificateAuthority"] = (
        capo_acm.types.certificate_authority.serialize_aws_json_1_1(
            value["certificate_authority"]
        )
    )
    if "tags" in value:
        import capo_acm.types.tag_list

        out["Tags"] = capo_acm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "certificate_tags" in value:
        import capo_acm.types.tag_list

        out["CertificateTags"] = capo_acm.types.tag_list.serialize_aws_json_1_1(
            value["certificate_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAcmeEndpointRequest:
    out: CreateAcmeEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("AuthorizationBehavior") is not None:
        import capo_acm.types.acme_authorization_behavior

        out["authorization_behavior"] = (
            capo_acm.types.acme_authorization_behavior.deserialize_aws_json_1_1(
                data["AuthorizationBehavior"]
            )
        )
    else:
        import typing

        out["authorization_behavior"] = typing.cast(
            "capo_acm.types.acme_authorization_behavior.AcmeAuthorizationBehavior", ""
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
    else:
        import capo_acm.types._unknown

        out["certificate_authority"] = capo_acm.types._unknown.UnknownUnionMember("")
    if data.get("Tags") is not None:
        import capo_acm.types.tag_list

        out["tags"] = capo_acm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("CertificateTags") is not None:
        import capo_acm.types.tag_list

        out["certificate_tags"] = capo_acm.types.tag_list.deserialize_aws_json_1_1(
            data["CertificateTags"]
        )
    return out
