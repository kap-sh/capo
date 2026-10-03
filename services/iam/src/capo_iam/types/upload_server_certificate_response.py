"""Generated from Smithy shape ``com.amazonaws.iam#UploadServerCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.server_certificate_metadata
    import capo_iam.types.tag_list_type


class UploadServerCertificateResponse(TypedDict, closed=True):
    server_certificate_metadata: NotRequired[
        "capo_iam.types.server_certificate_metadata.ServerCertificateMetadata"
    ]
    """<p>The meta information of the uploaded server certificate without its certificate body, certificate chain, and private key.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that are attached to the new IAM server certificate. The returned list of tags is sorted by tag key. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UploadServerCertificateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "server_certificate_metadata" in value:
        import capo_iam.types.server_certificate_metadata

        capo_iam.types.server_certificate_metadata.serialize_query(
            value["server_certificate_metadata"],
            pairs,
            f"{key_prefix}ServerCertificateMetadata",
        )
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> UploadServerCertificateResponse:
    out: UploadServerCertificateResponse = {}  # type: ignore[typeddict-item]
    child_server_certificate_metadata = el.find("ServerCertificateMetadata")
    if child_server_certificate_metadata is not None:
        import capo_iam.types.server_certificate_metadata

        out["server_certificate_metadata"] = (
            capo_iam.types.server_certificate_metadata.deserialize_query(
                child_server_certificate_metadata
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
