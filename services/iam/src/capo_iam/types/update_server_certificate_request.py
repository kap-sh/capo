"""Generated from Smithy shape ``com.amazonaws.iam#UpdateServerCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.path_type
    import capo_iam.types.server_certificate_name_type


class UpdateServerCertificateRequest(TypedDict, closed=True):
    server_certificate_name: (
        "capo_iam.types.server_certificate_name_type.serverCertificateNameType"
    )
    """<p>The name of the server certificate that you want to update.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    new_path: NotRequired["capo_iam.types.path_type.pathType"]
    r"""<p>The new path for the server certificate. Include this only if you are updating the server certificate's path.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</p>"""
    new_server_certificate_name: NotRequired[
        "capo_iam.types.server_certificate_name_type.serverCertificateNameType"
    ]
    """<p>The new name for the server certificate. Include this only if you are updating the server certificate's name. The name of the certificate cannot contain any spaces.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateServerCertificateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}ServerCertificateName", str(value["server_certificate_name"]))
    )
    if "new_path" in value:
        pairs.append((f"{key_prefix}NewPath", str(value["new_path"])))
    if "new_server_certificate_name" in value:
        pairs.append(
            (
                f"{key_prefix}NewServerCertificateName",
                str(value["new_server_certificate_name"]),
            )
        )


def deserialize_query(el: Element) -> UpdateServerCertificateRequest:
    out: UpdateServerCertificateRequest = {}  # type: ignore[typeddict-item]
    child_server_certificate_name = el.find("ServerCertificateName")
    if child_server_certificate_name is not None:
        out["server_certificate_name"] = str(child_server_certificate_name.text or "")
    else:
        raise DeserializationError(
            "UpdateServerCertificateRequest.server_certificate_name required"
        )
    child_new_path = el.find("NewPath")
    if child_new_path is not None:
        out["new_path"] = str(child_new_path.text or "")
    child_new_server_certificate_name = el.find("NewServerCertificateName")
    if child_new_server_certificate_name is not None:
        out["new_server_certificate_name"] = str(
            child_new_server_certificate_name.text or ""
        )
    return out
