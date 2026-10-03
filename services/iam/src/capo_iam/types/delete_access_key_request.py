"""Generated from Smithy shape ``com.amazonaws.iam#DeleteAccessKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.access_key_id_type
    import capo_iam.types.existing_user_name_type


class DeleteAccessKeyRequest(TypedDict, closed=True):
    user_name: NotRequired[
        "capo_iam.types.existing_user_name_type.existingUserNameType"
    ]
    """<p>The name of the user whose access key pair you want to delete.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    access_key_id: "capo_iam.types.access_key_id_type.accessKeyIdType"
    """<p>The access key ID for the access key ID and secret access key you want to delete.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters that can consist of any upper or lowercased letter or digit.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAccessKeyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}AccessKeyId", str(value["access_key_id"])))


def deserialize_query(el: Element) -> DeleteAccessKeyRequest:
    out: DeleteAccessKeyRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_access_key_id = el.find("AccessKeyId")
    if child_access_key_id is not None:
        out["access_key_id"] = str(child_access_key_id.text or "")
    else:
        raise DeserializationError("DeleteAccessKeyRequest.access_key_id required")
    return out
