"""Generated from Smithy shape ``com.amazonaws.acm#ImportCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.certificate_body_blob
    import capo_acm.types.certificate_chain_blob
    import capo_acm.types.private_key_blob
    import capo_acm.types.tag_list


class ImportCertificateRequest(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_acm.types.arn.Arn"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an imported certificate to replace. To import a new certificate, omit this field. </p>"""
    certificate: "capo_acm.types.certificate_body_blob.CertificateBodyBlob"
    """<p>The certificate to import.</p>"""
    private_key: "capo_acm.types.private_key_blob.PrivateKeyBlob"
    """<p>The private key that matches the public key in the certificate.</p>"""
    certificate_chain: NotRequired[
        "capo_acm.types.certificate_chain_blob.CertificateChainBlob"
    ]
    """<p>The PEM encoded certificate chain.</p>"""
    tags: NotRequired["capo_acm.types.tag_list.TagList"]
    """<p>One or more resource tags to associate with the imported certificate. </p> <p>Note: You cannot apply tags when reimporting a certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCertificateRequest) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    import capo_acm.types.certificate_body_blob

    out["Certificate"] = capo_acm.types.certificate_body_blob.serialize_aws_json_1_1(
        value["certificate"]
    )
    import capo_acm.types.private_key_blob

    out["PrivateKey"] = capo_acm.types.private_key_blob.serialize_aws_json_1_1(
        value["private_key"]
    )
    if "certificate_chain" in value:
        import capo_acm.types.certificate_chain_blob

        out["CertificateChain"] = (
            capo_acm.types.certificate_chain_blob.serialize_aws_json_1_1(
                value["certificate_chain"]
            )
        )
    if "tags" in value:
        import capo_acm.types.tag_list

        out["Tags"] = capo_acm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCertificateRequest:
    out: ImportCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("Certificate") is not None:
        import capo_acm.types.certificate_body_blob

        out["certificate"] = (
            capo_acm.types.certificate_body_blob.deserialize_aws_json_1_1(
                data["Certificate"]
            )
        )
    else:
        raise DeserializationError("ImportCertificateRequest.certificate required")
    if data.get("PrivateKey") is not None:
        import capo_acm.types.private_key_blob

        out["private_key"] = capo_acm.types.private_key_blob.deserialize_aws_json_1_1(
            data["PrivateKey"]
        )
    else:
        raise DeserializationError("ImportCertificateRequest.private_key required")
    if data.get("CertificateChain") is not None:
        import capo_acm.types.certificate_chain_blob

        out["certificate_chain"] = (
            capo_acm.types.certificate_chain_blob.deserialize_aws_json_1_1(
                data["CertificateChain"]
            )
        )
    if data.get("Tags") is not None:
        import capo_acm.types.tag_list

        out["tags"] = capo_acm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
