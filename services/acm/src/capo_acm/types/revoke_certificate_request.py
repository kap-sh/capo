"""Generated from Smithy shape ``com.amazonaws.acm#RevokeCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.revocation_reason


class RevokeCertificateRequest(TypedDict, closed=True):
    certificate_arn: "capo_acm.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the public or private certificate that will be revoked. The ARN must have the following form: </p> <p> <code>arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012</code> </p>"""
    revocation_reason: "capo_acm.types.revocation_reason.RevocationReason"
    """<p>Specifies why you revoked the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    import capo_acm.types.revocation_reason

    out["RevocationReason"] = capo_acm.types.revocation_reason.serialize_aws_json_1_1(
        value["revocation_reason"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeCertificateRequest:
    out: RevokeCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        out["certificate_arn"] = ""
    if data.get("RevocationReason") is not None:
        import capo_acm.types.revocation_reason

        out["revocation_reason"] = (
            capo_acm.types.revocation_reason.deserialize_aws_json_1_1(
                data["RevocationReason"]
            )
        )
    else:
        import typing

        out["revocation_reason"] = typing.cast(
            "capo_acm.types.revocation_reason.RevocationReason", ""
        )
    return out
