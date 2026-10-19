"""Generated from Smithy shape ``com.amazonaws.sts#Credentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.access_key_id_type
    import capo_sts.types.access_key_secret_type
    import capo_sts.types.date_type
    import capo_sts.types.token_type


class Credentials(TypedDict, closed=True):
    access_key_id: "capo_sts.types.access_key_id_type.accessKeyIdType"
    """<p>The access key ID that identifies the temporary security credentials.</p>"""
    secret_access_key: "capo_sts.types.access_key_secret_type.accessKeySecretType"
    """<p>The secret access key that can be used to sign requests.</p>"""
    session_token: "capo_sts.types.token_type.tokenType"
    """<p>The token that users must pass to the service API to use the temporary credentials.</p>"""
    expiration: "capo_sts.types.date_type.dateType"
    """<p>The date on which the current credentials expire.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Credentials, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}AccessKeyId", str(value["access_key_id"])))
    pairs.append((f"{key_prefix}SecretAccessKey", str(value["secret_access_key"])))
    pairs.append((f"{key_prefix}SessionToken", str(value["session_token"])))
    import capo_sts.types.date_type

    capo_sts.types.date_type.serialize_query(
        value["expiration"], pairs, f"{key_prefix}Expiration"
    )


def deserialize_query(el: Element) -> Credentials:
    out: Credentials = {}  # type: ignore[typeddict-item]
    child_access_key_id = el.find("AccessKeyId")
    if child_access_key_id is not None:
        out["access_key_id"] = str(child_access_key_id.text or "")
    else:
        out["access_key_id"] = ""
    child_secret_access_key = el.find("SecretAccessKey")
    if child_secret_access_key is not None:
        out["secret_access_key"] = str(child_secret_access_key.text or "")
    else:
        out["secret_access_key"] = ""
    child_session_token = el.find("SessionToken")
    if child_session_token is not None:
        out["session_token"] = str(child_session_token.text or "")
    else:
        out["session_token"] = ""
    child_expiration = el.find("Expiration")
    if child_expiration is not None:
        import capo_sts.types.date_type

        out["expiration"] = capo_sts.types.date_type.deserialize_query(child_expiration)
    else:
        import datetime

        out["expiration"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: Credentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_access_key" in value:
        out["secret_access_key"] = "*** Sensitive Data Redacted ***"
    return out
