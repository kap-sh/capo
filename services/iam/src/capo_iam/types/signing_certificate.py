"""Generated from Smithy shape ``com.amazonaws.iam#SigningCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.certificate_body_type
    import capo_iam.types.certificate_id_type
    import capo_iam.types.date_type
    import capo_iam.types.status_type
    import capo_iam.types.user_name_type


class SigningCertificate(TypedDict, closed=True):
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the user the signing certificate is associated with.</p>"""
    certificate_id: "capo_iam.types.certificate_id_type.certificateIdType"
    """<p>The ID for the signing certificate.</p>"""
    certificate_body: "capo_iam.types.certificate_body_type.certificateBodyType"
    """<p>The contents of the signing certificate.</p>"""
    status: "capo_iam.types.status_type.statusType"
    """<p>The status of the signing certificate. <code>Active</code> means that the key is valid for API calls, while <code>Inactive</code> means it is not.</p>"""
    upload_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date when the signing certificate was uploaded.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SigningCertificate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}CertificateId", str(value["certificate_id"])))
    pairs.append((f"{key_prefix}CertificateBody", str(value["certificate_body"])))
    import capo_iam.types.status_type

    capo_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )
    if "upload_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["upload_date"], pairs, f"{key_prefix}UploadDate"
        )


def deserialize_query(el: Element) -> SigningCertificate:
    out: SigningCertificate = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        out["user_name"] = ""
    child_certificate_id = el.find("CertificateId")
    if child_certificate_id is not None:
        out["certificate_id"] = str(child_certificate_id.text or "")
    else:
        out["certificate_id"] = ""
    child_certificate_body = el.find("CertificateBody")
    if child_certificate_body is not None:
        out["certificate_body"] = str(child_certificate_body.text or "")
    else:
        out["certificate_body"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        import capo_iam.types.status_type

        out["status"] = capo_iam.types.status_type.deserialize_query(child_status)
    else:
        import typing

        out["status"] = typing.cast("capo_iam.types.status_type.statusType", "")
    child_upload_date = el.find("UploadDate")
    if child_upload_date is not None:
        import capo_iam.types.date_type

        out["upload_date"] = capo_iam.types.date_type.deserialize_query(
            child_upload_date
        )
    return out
