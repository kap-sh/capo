"""Generated from Smithy shape ``com.amazonaws.iam#UntagServerCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.server_certificate_name_type
    import capo_iam.types.tag_key_list_type


class UntagServerCertificateRequest(TypedDict, closed=True):
    server_certificate_name: (
        "capo_iam.types.server_certificate_name_type.serverCertificateNameType"
    )
    """<p>The name of the IAM server certificate from which you want to remove tags.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tag_keys: "capo_iam.types.tag_key_list_type.tagKeyListType"
    """<p>A list of key names as a simple array of strings. The tags with matching keys are removed from the specified IAM server certificate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagServerCertificateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}ServerCertificateName", str(value["server_certificate_name"]))
    )
    import capo_iam.types.tag_key_list_type

    capo_iam.types.tag_key_list_type.serialize_query(
        value["tag_keys"], pairs, f"{key_prefix}TagKeys"
    )


def deserialize_query(el: Element) -> UntagServerCertificateRequest:
    out: UntagServerCertificateRequest = {}  # type: ignore[typeddict-item]
    child_server_certificate_name = el.find("ServerCertificateName")
    if child_server_certificate_name is not None:
        out["server_certificate_name"] = str(child_server_certificate_name.text or "")
    else:
        raise DeserializationError(
            "UntagServerCertificateRequest.server_certificate_name required"
        )
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_iam.types.tag_key_list_type

        out["tag_keys"] = capo_iam.types.tag_key_list_type.deserialize_query(
            child_tag_keys
        )
    else:
        raise DeserializationError("UntagServerCertificateRequest.tag_keys required")
    return out
