"""Generated from Smithy shape ``com.amazonaws.acmpca#DeleteCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.permanent_deletion_time_in_days


class DeleteCertificateAuthorityRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must have the following form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>"""
    permanent_deletion_time_in_days: NotRequired[
        "capo_acm_pca.types.permanent_deletion_time_in_days.PermanentDeletionTimeInDays"
    ]
    """<p>The number of days to make a CA restorable after it has been deleted. This can be anywhere from 7 to 30 days, with 30 being the default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCertificateAuthorityRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "permanent_deletion_time_in_days" in value:
        out["PermanentDeletionTimeInDays"] = value["permanent_deletion_time_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCertificateAuthorityRequest:
    out: DeleteCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "DeleteCertificateAuthorityRequest.certificate_authority_arn required"
        )
    if data.get("PermanentDeletionTimeInDays") is not None:
        out["permanent_deletion_time_in_days"] = data["PermanentDeletionTimeInDays"]
    return out
