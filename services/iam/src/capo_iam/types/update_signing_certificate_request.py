"""Generated from Smithy shape ``com.amazonaws.iam#UpdateSigningCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.certificate_id_type
    import capo_iam.types.existing_user_name_type
    import capo_iam.types.status_type


class UpdateSigningCertificateRequest(TypedDict, closed=True):
    user_name: NotRequired[
        "capo_iam.types.existing_user_name_type.existingUserNameType"
    ]
    """<p>The name of the IAM user the signing certificate belongs to.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    certificate_id: "capo_iam.types.certificate_id_type.certificateIdType"
    """<p>The ID of the signing certificate you want to update.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters that can consist of any upper or lowercased letter or digit.</p>"""
    status: "capo_iam.types.status_type.statusType"
    """<p> The status you want to assign to the certificate. <code>Active</code> means that the certificate can be used for programmatic calls to Amazon Web Services <code>Inactive</code> means that the certificate cannot be used.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateSigningCertificateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}CertificateId", str(value["certificate_id"])))
    import capo_iam.types.status_type

    capo_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )


def deserialize_query(el: Element) -> UpdateSigningCertificateRequest:
    out: UpdateSigningCertificateRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_certificate_id = el.find("CertificateId")
    if child_certificate_id is not None:
        out["certificate_id"] = str(child_certificate_id.text or "")
    else:
        raise DeserializationError(
            "UpdateSigningCertificateRequest.certificate_id required"
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_iam.types.status_type

        out["status"] = capo_iam.types.status_type.deserialize_query(child_status)
    else:
        raise DeserializationError("UpdateSigningCertificateRequest.status required")
    return out
