"""Generated from Smithy shape ``com.amazonaws.iam#AccessKey``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.access_key_id_type
    import capo_iam.types.access_key_secret_type
    import capo_iam.types.date_type
    import capo_iam.types.status_type
    import capo_iam.types.user_name_type


class AccessKey(TypedDict, closed=True):
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the IAM user that the access key is associated with.</p>"""
    access_key_id: "capo_iam.types.access_key_id_type.accessKeyIdType"
    """<p>The ID for this access key.</p>"""
    status: "capo_iam.types.status_type.statusType"
    """<p>The status of the access key. <code>Active</code> means that the key is valid for API calls, while <code>Inactive</code> means it is not. </p>"""
    secret_access_key: "capo_iam.types.access_key_secret_type.accessKeySecretType"
    """<p>The secret key used to sign requests.</p>"""
    create_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date when the access key was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessKey, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}AccessKeyId", str(value["access_key_id"])))
    import capo_iam.types.status_type

    capo_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )
    pairs.append((f"{key_prefix}SecretAccessKey", str(value["secret_access_key"])))
    if "create_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )


def deserialize_query(el: Element) -> AccessKey:
    out: AccessKey = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        out["user_name"] = ""
    child_access_key_id = el.find("AccessKeyId")
    if child_access_key_id is not None:
        out["access_key_id"] = str(child_access_key_id.text or "")
    else:
        out["access_key_id"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        import capo_iam.types.status_type

        out["status"] = capo_iam.types.status_type.deserialize_query(child_status)
    else:
        import typing

        out["status"] = typing.cast("capo_iam.types.status_type.statusType", "")
    child_secret_access_key = el.find("SecretAccessKey")
    if child_secret_access_key is not None:
        out["secret_access_key"] = str(child_secret_access_key.text or "")
    else:
        out["secret_access_key"] = ""
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    return out


def redact_sensitive(value: AccessKey) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_access_key" in value:
        out["secret_access_key"] = "*** Sensitive Data Redacted ***"
    return out
