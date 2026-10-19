"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.cert_date
    import capo_transfer.types.certificate_id
    import capo_transfer.types.description


class UpdateCertificateRequest(TypedDict, closed=True):
    certificate_id: "capo_transfer.types.certificate_id.CertificateId"
    """<p>The identifier of the certificate object that you are updating.</p>"""
    active_date: NotRequired["capo_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>"""
    inactive_date: NotRequired["capo_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>"""
    description: NotRequired["capo_transfer.types.description.Description"]
    """<p>A short description to help identify the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateId"] = value["certificate_id"]
    if "active_date" in value:
        import capo_transfer.types.cert_date

        out["ActiveDate"] = capo_transfer.types.cert_date.serialize_aws_json_1_1(
            value["active_date"]
        )
    if "inactive_date" in value:
        import capo_transfer.types.cert_date

        out["InactiveDate"] = capo_transfer.types.cert_date.serialize_aws_json_1_1(
            value["inactive_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCertificateRequest:
    out: UpdateCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    else:
        out["certificate_id"] = ""
    if data.get("ActiveDate") is not None:
        import capo_transfer.types.cert_date

        out["active_date"] = capo_transfer.types.cert_date.deserialize_aws_json_1_1(
            data["ActiveDate"]
        )
    if data.get("InactiveDate") is not None:
        import capo_transfer.types.cert_date

        out["inactive_date"] = capo_transfer.types.cert_date.deserialize_aws_json_1_1(
            data["InactiveDate"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
