"""Generated from Smithy shape ``com.amazonaws.acmpca#CreatePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.account_id
    import capo_acm_pca.types.action_list
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.principal


class CreatePermissionRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the CA that grants the permissions. You can find the ARN by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action. This must have the following form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>"""
    principal: "capo_acm_pca.types.principal.Principal"
    """<p>The Amazon Web Services service or identity that receives the permission. At this time, the only valid principal is <code>acm.amazonaws.com</code>.</p>"""
    source_account: NotRequired["capo_acm_pca.types.account_id.AccountId"]
    """<p>The ID of the calling account.</p>"""
    actions: "capo_acm_pca.types.action_list.ActionList"
    """<p>The actions that the specified Amazon Web Services service principal can use. These include <code>IssueCertificate</code>, <code>GetCertificate</code>, and <code>ListPermissions</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePermissionRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    out["Principal"] = value["principal"]
    if "source_account" in value:
        out["SourceAccount"] = value["source_account"]
    import capo_acm_pca.types.action_list

    out["Actions"] = capo_acm_pca.types.action_list.serialize_aws_json_1_1(
        value["actions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePermissionRequest:
    out: CreatePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "CreatePermissionRequest.certificate_authority_arn required"
        )
    if data.get("Principal") is not None:
        out["principal"] = data["Principal"]
    else:
        raise DeserializationError("CreatePermissionRequest.principal required")
    if data.get("SourceAccount") is not None:
        out["source_account"] = data["SourceAccount"]
    if data.get("Actions") is not None:
        import capo_acm_pca.types.action_list

        out["actions"] = capo_acm_pca.types.action_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    else:
        raise DeserializationError("CreatePermissionRequest.actions required")
    return out
