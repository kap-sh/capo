"""Generated from Smithy shape ``com.amazonaws.iam#ServerCertificateMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.date_type
    import capo_iam.types.id_type
    import capo_iam.types.path_type
    import capo_iam.types.server_certificate_name_type


class ServerCertificateMetadata(TypedDict, closed=True):
    path: "capo_iam.types.path_type.pathType"
    """<p> The path to the server certificate. For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    server_certificate_name: (
        "capo_iam.types.server_certificate_name_type.serverCertificateNameType"
    )
    """<p>The name that identifies the server certificate.</p>"""
    server_certificate_id: "capo_iam.types.id_type.idType"
    """<p> The stable and unique string identifying the server certificate. For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    arn: "capo_iam.types.arn_type.arnType"
    """<p> The Amazon Resource Name (ARN) specifying the server certificate. For more information about ARNs and how to use them in policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    upload_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date when the server certificate was uploaded.</p>"""
    expiration: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date on which the certificate is set to expire.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerCertificateMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Path", str(value["path"])))
    pairs.append(
        (f"{key_prefix}ServerCertificateName", str(value["server_certificate_name"]))
    )
    pairs.append(
        (f"{key_prefix}ServerCertificateId", str(value["server_certificate_id"]))
    )
    pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "upload_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["upload_date"], pairs, f"{key_prefix}UploadDate"
        )
    if "expiration" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["expiration"], pairs, f"{key_prefix}Expiration"
        )


def deserialize_query(el: Element) -> ServerCertificateMetadata:
    out: ServerCertificateMetadata = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    else:
        raise DeserializationError("ServerCertificateMetadata.path required")
    child_server_certificate_name = el.find("ServerCertificateName")
    if child_server_certificate_name is not None:
        out["server_certificate_name"] = str(child_server_certificate_name.text or "")
    else:
        raise DeserializationError(
            "ServerCertificateMetadata.server_certificate_name required"
        )
    child_server_certificate_id = el.find("ServerCertificateId")
    if child_server_certificate_id is not None:
        out["server_certificate_id"] = str(child_server_certificate_id.text or "")
    else:
        raise DeserializationError(
            "ServerCertificateMetadata.server_certificate_id required"
        )
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("ServerCertificateMetadata.arn required")
    child_upload_date = el.find("UploadDate")
    if child_upload_date is not None:
        import capo_iam.types.date_type

        out["upload_date"] = capo_iam.types.date_type.deserialize_query(
            child_upload_date
        )
    child_expiration = el.find("Expiration")
    if child_expiration is not None:
        import capo_iam.types.date_type

        out["expiration"] = capo_iam.types.date_type.deserialize_query(child_expiration)
    return out
