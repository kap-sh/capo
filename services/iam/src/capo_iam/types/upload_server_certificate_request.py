"""Generated from Smithy shape ``com.amazonaws.iam#UploadServerCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.certificate_body_type
    import capo_iam.types.certificate_chain_type
    import capo_iam.types.path_type
    import capo_iam.types.private_key_type
    import capo_iam.types.server_certificate_name_type
    import capo_iam.types.tag_list_type


class UploadServerCertificateRequest(TypedDict, closed=True):
    path: NotRequired["capo_iam.types.path_type.pathType"]
    r"""<p>The path for the server certificate. For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</p> <note> <p> If you are uploading a server certificate specifically for use with Amazon CloudFront distributions, you must specify a path using the <code>path</code> parameter. The path must begin with <code>/cloudfront</code> and must include a trailing slash (for example, <code>/cloudfront/test/</code>).</p> </note>"""
    server_certificate_name: (
        "capo_iam.types.server_certificate_name_type.serverCertificateNameType"
    )
    """<p>The name for the server certificate. Do not include the path in this value. The name of the certificate cannot contain any spaces.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    certificate_body: "capo_iam.types.certificate_body_type.certificateBodyType"
    r"""<p>The contents of the public key certificate in PEM-encoded format.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""
    private_key: "capo_iam.types.private_key_type.privateKeyType"
    r"""<p>The contents of the private key in PEM-encoded format.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""
    certificate_chain: NotRequired[
        "capo_iam.types.certificate_chain_type.certificateChainType"
    ]
    r"""<p>The contents of the certificate chain. This is typically a concatenation of the PEM-encoded public key certificates of the chain.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that you want to attach to the new IAM server certificate resource. Each tag consists of a key name and an associated value. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p> <note> <p>If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UploadServerCertificateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    pairs.append(
        (f"{key_prefix}ServerCertificateName", str(value["server_certificate_name"]))
    )
    pairs.append((f"{key_prefix}CertificateBody", str(value["certificate_body"])))
    pairs.append((f"{key_prefix}PrivateKey", str(value["private_key"])))
    if "certificate_chain" in value:
        pairs.append((f"{key_prefix}CertificateChain", str(value["certificate_chain"])))
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> UploadServerCertificateRequest:
    out: UploadServerCertificateRequest = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_server_certificate_name = el.find("ServerCertificateName")
    if child_server_certificate_name is not None:
        out["server_certificate_name"] = str(child_server_certificate_name.text or "")
    else:
        raise DeserializationError(
            "UploadServerCertificateRequest.server_certificate_name required"
        )
    child_certificate_body = el.find("CertificateBody")
    if child_certificate_body is not None:
        out["certificate_body"] = str(child_certificate_body.text or "")
    else:
        raise DeserializationError(
            "UploadServerCertificateRequest.certificate_body required"
        )
    child_private_key = el.find("PrivateKey")
    if child_private_key is not None:
        out["private_key"] = str(child_private_key.text or "")
    else:
        raise DeserializationError(
            "UploadServerCertificateRequest.private_key required"
        )
    child_certificate_chain = el.find("CertificateChain")
    if child_certificate_chain is not None:
        out["certificate_chain"] = str(child_certificate_chain.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
