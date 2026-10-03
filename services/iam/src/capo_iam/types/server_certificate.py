"""Generated from Smithy shape ``com.amazonaws.iam#ServerCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.certificate_body_type
    import capo_iam.types.certificate_chain_type
    import capo_iam.types.server_certificate_metadata
    import capo_iam.types.tag_list_type


class ServerCertificate(TypedDict, closed=True):
    server_certificate_metadata: (
        "capo_iam.types.server_certificate_metadata.ServerCertificateMetadata"
    )
    """<p>The meta information of the server certificate, such as its name, path, ID, and ARN.</p>"""
    certificate_body: "capo_iam.types.certificate_body_type.certificateBodyType"
    """<p>The contents of the public key certificate.</p>"""
    certificate_chain: NotRequired[
        "capo_iam.types.certificate_chain_type.certificateChainType"
    ]
    """<p>The contents of the public key certificate chain.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that are attached to the server certificate. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerCertificate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.server_certificate_metadata

    capo_iam.types.server_certificate_metadata.serialize_query(
        value["server_certificate_metadata"],
        pairs,
        f"{key_prefix}ServerCertificateMetadata",
    )
    pairs.append((f"{key_prefix}CertificateBody", str(value["certificate_body"])))
    if "certificate_chain" in value:
        pairs.append((f"{key_prefix}CertificateChain", str(value["certificate_chain"])))
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> ServerCertificate:
    out: ServerCertificate = {}  # type: ignore[typeddict-item]
    child_server_certificate_metadata = el.find("ServerCertificateMetadata")
    if child_server_certificate_metadata is not None:
        import capo_iam.types.server_certificate_metadata

        out["server_certificate_metadata"] = (
            capo_iam.types.server_certificate_metadata.deserialize_query(
                child_server_certificate_metadata
            )
        )
    else:
        raise DeserializationError(
            "ServerCertificate.server_certificate_metadata required"
        )
    child_certificate_body = el.find("CertificateBody")
    if child_certificate_body is not None:
        out["certificate_body"] = str(child_certificate_body.text or "")
    else:
        raise DeserializationError("ServerCertificate.certificate_body required")
    child_certificate_chain = el.find("CertificateChain")
    if child_certificate_chain is not None:
        out["certificate_chain"] = str(child_certificate_chain.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
