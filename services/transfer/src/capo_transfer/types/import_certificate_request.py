"""Generated from Smithy shape ``com.amazonaws.transfer#ImportCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.cert_date
    import capo_transfer.types.certificate_body_type
    import capo_transfer.types.certificate_chain_type
    import capo_transfer.types.certificate_usage_type
    import capo_transfer.types.description
    import capo_transfer.types.private_key_type
    import capo_transfer.types.tags


class ImportCertificateRequest(TypedDict, closed=True):
    usage: "capo_transfer.types.certificate_usage_type.CertificateUsageType"
    """<p>Specifies how this certificate is used. It can be used in the following ways:</p> <ul> <li> <p> <code>SIGNING</code>: For signing AS2 messages</p> </li> <li> <p> <code>ENCRYPTION</code>: For encrypting AS2 messages</p> </li> <li> <p> <code>TLS</code>: For securing AS2 communications sent over HTTPS</p> </li> </ul>"""
    certificate: "capo_transfer.types.certificate_body_type.CertificateBodyType"
    """<ul> <li> <p>For the CLI, provide a file path for a certificate in URI format. For example, <code>--certificate file://encryption-cert.pem</code>. Alternatively, you can provide the raw content.</p> </li> <li> <p>For the SDK, specify the raw content of a certificate file. For example, <code>--certificate "`cat encryption-cert.pem`"</code>.</p> </li> </ul> <note> <p>You can provide both the certificate and its chain in this parameter, without needing to use the <code>CertificateChain</code> parameter. If you use this parameter for both the certificate and its chain, do not use the <code>CertificateChain</code> parameter.</p> </note>"""
    certificate_chain: NotRequired[
        "capo_transfer.types.certificate_chain_type.CertificateChainType"
    ]
    """<p>An optional list of certificates that make up the chain for the certificate that's being imported.</p>"""
    private_key: NotRequired["capo_transfer.types.private_key_type.PrivateKeyType"]
    """<ul> <li> <p>For the CLI, provide a file path for a private key in URI format. For example, <code>--private-key file://encryption-key.pem</code>. Alternatively, you can provide the raw content of the private key file.</p> </li> <li> <p>For the SDK, specify the raw content of a private key file. For example, <code>--private-key "`cat encryption-key.pem`"</code> </p> </li> </ul>"""
    active_date: NotRequired["capo_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>"""
    inactive_date: NotRequired["capo_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>"""
    description: NotRequired["capo_transfer.types.description.Description"]
    """<p>A short description that helps identify the certificate. </p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for certificates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCertificateRequest) -> dict:
    out: dict = {}
    import capo_transfer.types.certificate_usage_type

    out["Usage"] = capo_transfer.types.certificate_usage_type.serialize_aws_json_1_1(
        value["usage"]
    )
    out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
    if "private_key" in value:
        out["PrivateKey"] = value["private_key"]
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
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCertificateRequest:
    out: ImportCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("Usage") is not None:
        import capo_transfer.types.certificate_usage_type

        out["usage"] = (
            capo_transfer.types.certificate_usage_type.deserialize_aws_json_1_1(
                data["Usage"]
            )
        )
    else:
        raise DeserializationError("ImportCertificateRequest.usage required")
    if data.get("Certificate") is not None:
        out["certificate"] = data["Certificate"]
    else:
        raise DeserializationError("ImportCertificateRequest.certificate required")
    if data.get("CertificateChain") is not None:
        out["certificate_chain"] = data["CertificateChain"]
    if data.get("PrivateKey") is not None:
        out["private_key"] = data["PrivateKey"]
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
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
