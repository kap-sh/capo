"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedCertificate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.cert_date
    import capo_transfer.types.cert_serial
    import capo_transfer.types.certificate_body_type
    import capo_transfer.types.certificate_chain_type
    import capo_transfer.types.certificate_id
    import capo_transfer.types.certificate_status_type
    import capo_transfer.types.certificate_type
    import capo_transfer.types.certificate_usage_type
    import capo_transfer.types.description
    import capo_transfer.types.tags


class DescribedCertificate(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>The unique Amazon Resource Name (ARN) for the certificate.</p>"""
    certificate_id: NotRequired["capo_transfer.types.certificate_id.CertificateId"]
    """<p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>"""
    usage: NotRequired[
        "capo_transfer.types.certificate_usage_type.CertificateUsageType"
    ]
    """<p>Specifies how this certificate is used. It can be used in the following ways:</p> <ul> <li> <p> <code>SIGNING</code>: For signing AS2 messages</p> </li> <li> <p> <code>ENCRYPTION</code>: For encrypting AS2 messages</p> </li> <li> <p> <code>TLS</code>: For securing AS2 communications sent over HTTPS</p> </li> </ul>"""
    status: NotRequired[
        "capo_transfer.types.certificate_status_type.CertificateStatusType"
    ]
    """<p>A certificate's status can be either <code>ACTIVE</code> or <code>INACTIVE</code>.</p> <p>You can set <code>ActiveDate</code> and <code>InactiveDate</code> in the <code>UpdateCertificate</code> call. If you set values for these parameters, those values are used to determine whether the certificate has a status of <code>ACTIVE</code> or <code>INACTIVE</code>.</p> <p>If you don't set values for <code>ActiveDate</code> and <code>InactiveDate</code>, we use the <code>NotBefore</code> and <code>NotAfter</code> date as specified on the X509 certificate to determine when a certificate is active and when it is inactive.</p>"""
    certificate: NotRequired[
        "capo_transfer.types.certificate_body_type.CertificateBodyType"
    ]
    """<p>The file name for the certificate.</p>"""
    certificate_chain: NotRequired[
        "capo_transfer.types.certificate_chain_type.CertificateChainType"
    ]
    """<p>The list of certificates that make up the chain for the certificate.</p>"""
    active_date: NotRequired["capo_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>"""
    inactive_date: NotRequired["capo_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>"""
    serial: NotRequired["capo_transfer.types.cert_serial.CertSerial"]
    """<p>The serial number for the certificate.</p>"""
    not_before_date: NotRequired["capo_transfer.types.cert_date.CertDate"]
    """<p>The earliest date that the certificate is valid.</p>"""
    not_after_date: NotRequired["capo_transfer.types.cert_date.CertDate"]
    """<p>The final date that the certificate is valid.</p>"""
    type: NotRequired["capo_transfer.types.certificate_type.CertificateType"]
    """<p>If a private key has been specified for the certificate, its type is <code>CERTIFICATE_WITH_PRIVATE_KEY</code>. If there is no private key, the type is <code>CERTIFICATE</code>.</p>"""
    description: NotRequired["capo_transfer.types.description.Description"]
    """<p>The name or description that's used to identity the certificate. </p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for certificates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedCertificate) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    if "usage" in value:
        import capo_transfer.types.certificate_usage_type

        out["Usage"] = (
            capo_transfer.types.certificate_usage_type.serialize_aws_json_1_1(
                value["usage"]
            )
        )
    if "status" in value:
        import capo_transfer.types.certificate_status_type

        out["Status"] = (
            capo_transfer.types.certificate_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
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
    if "serial" in value:
        out["Serial"] = value["serial"]
    if "not_before_date" in value:
        import capo_transfer.types.cert_date

        out["NotBeforeDate"] = capo_transfer.types.cert_date.serialize_aws_json_1_1(
            value["not_before_date"]
        )
    if "not_after_date" in value:
        import capo_transfer.types.cert_date

        out["NotAfterDate"] = capo_transfer.types.cert_date.serialize_aws_json_1_1(
            value["not_after_date"]
        )
    if "type" in value:
        import capo_transfer.types.certificate_type

        out["Type"] = capo_transfer.types.certificate_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedCertificate:
    out: DescribedCertificate = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    if data.get("Usage") is not None:
        import capo_transfer.types.certificate_usage_type

        out["usage"] = (
            capo_transfer.types.certificate_usage_type.deserialize_aws_json_1_1(
                data["Usage"]
            )
        )
    if data.get("Status") is not None:
        import capo_transfer.types.certificate_status_type

        out["status"] = (
            capo_transfer.types.certificate_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Certificate") is not None:
        out["certificate"] = data["Certificate"]
    if data.get("CertificateChain") is not None:
        out["certificate_chain"] = data["CertificateChain"]
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
    if data.get("Serial") is not None:
        out["serial"] = data["Serial"]
    if data.get("NotBeforeDate") is not None:
        import capo_transfer.types.cert_date

        out["not_before_date"] = capo_transfer.types.cert_date.deserialize_aws_json_1_1(
            data["NotBeforeDate"]
        )
    if data.get("NotAfterDate") is not None:
        import capo_transfer.types.cert_date

        out["not_after_date"] = capo_transfer.types.cert_date.deserialize_aws_json_1_1(
            data["NotAfterDate"]
        )
    if data.get("Type") is not None:
        import capo_transfer.types.certificate_type

        out["type"] = capo_transfer.types.certificate_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out


def redact_sensitive(value: DescribedCertificate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "certificate" in value:
        out["certificate"] = "*** Sensitive Data Redacted ***"
    if "certificate_chain" in value:
        out["certificate_chain"] = "*** Sensitive Data Redacted ***"
    return out
