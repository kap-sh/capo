"""Generated from Smithy shape ``com.amazonaws.acmpca#DeletePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.account_id
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.principal


class DeletePermissionRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Number (ARN) of the private CA that issued the permissions. You can find the CA's ARN by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action. This must have the following form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>"""
    principal: "capo_acm_pca.types.principal.Principal"
    """<p>The Amazon Web Services service or identity that will have its CA permissions revoked. At this time, the only valid service principal is <code>acm.amazonaws.com</code> </p>"""
    source_account: NotRequired["capo_acm_pca.types.account_id.AccountId"]
    """<p>The Amazon Web Services account that calls this action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePermissionRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    out["Principal"] = value["principal"]
    if "source_account" in value:
        out["SourceAccount"] = value["source_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePermissionRequest:
    out: DeletePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "DeletePermissionRequest.certificate_authority_arn required"
        )
    if data.get("Principal") is not None:
        out["principal"] = data["Principal"]
    else:
        raise DeserializationError("DeletePermissionRequest.principal required")
    if data.get("SourceAccount") is not None:
        out["source_account"] = data["SourceAccount"]
    return out
