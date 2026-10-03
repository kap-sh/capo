"""Generated from Smithy shape ``com.amazonaws.iam#TagServerCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.server_certificate_name_type
    import capo_iam.types.tag_list_type


class TagServerCertificateRequest(TypedDict, closed=True):
    server_certificate_name: (
        "capo_iam.types.server_certificate_name_type.serverCertificateNameType"
    )
    """<p>The name of the IAM server certificate to which you want to add tags.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: "capo_iam.types.tag_list_type.tagListType"
    """<p>The list of tags that you want to attach to the IAM server certificate. Each tag consists of a key name and an associated value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagServerCertificateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}ServerCertificateName", str(value["server_certificate_name"]))
    )
    import capo_iam.types.tag_list_type

    capo_iam.types.tag_list_type.serialize_query(
        value["tags"], pairs, f"{key_prefix}Tags"
    )


def deserialize_query(el: Element) -> TagServerCertificateRequest:
    out: TagServerCertificateRequest = {}  # type: ignore[typeddict-item]
    child_server_certificate_name = el.find("ServerCertificateName")
    if child_server_certificate_name is not None:
        out["server_certificate_name"] = str(child_server_certificate_name.text or "")
    else:
        raise DeserializationError(
            "TagServerCertificateRequest.server_certificate_name required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagServerCertificateRequest.tags required")
    return out
