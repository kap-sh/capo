"""Generated from Smithy shape ``com.amazonaws.iam#UpdateServiceSpecificCredentialRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.service_specific_credential_id
    import capo_iam.types.status_type
    import capo_iam.types.user_name_type


class UpdateServiceSpecificCredentialRequest(TypedDict, closed=True):
    user_name: NotRequired["capo_iam.types.user_name_type.userNameType"]
    """<p>The name of the IAM user associated with the service-specific credential. If you do not specify this value, then the operation assumes the user whose credentials are used to call the operation.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    service_specific_credential_id: (
        "capo_iam.types.service_specific_credential_id.serviceSpecificCredentialId"
    )
    """<p>The unique identifier of the service-specific credential.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters that can consist of any upper or lowercased letter or digit.</p>"""
    status: "capo_iam.types.status_type.statusType"
    """<p>The status to be assigned to the service-specific credential.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateServiceSpecificCredentialRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append(
        (
            f"{key_prefix}ServiceSpecificCredentialId",
            str(value["service_specific_credential_id"]),
        )
    )
    import capo_iam.types.status_type

    capo_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )


def deserialize_query(el: Element) -> UpdateServiceSpecificCredentialRequest:
    out: UpdateServiceSpecificCredentialRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_service_specific_credential_id = el.find("ServiceSpecificCredentialId")
    if child_service_specific_credential_id is not None:
        out["service_specific_credential_id"] = str(
            child_service_specific_credential_id.text or ""
        )
    else:
        raise DeserializationError(
            "UpdateServiceSpecificCredentialRequest.service_specific_credential_id required"
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_iam.types.status_type

        out["status"] = capo_iam.types.status_type.deserialize_query(child_status)
    else:
        raise DeserializationError(
            "UpdateServiceSpecificCredentialRequest.status required"
        )
    return out
