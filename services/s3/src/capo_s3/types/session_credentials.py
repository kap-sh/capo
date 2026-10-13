"""Generated from Smithy shape ``com.amazonaws.s3#SessionCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.access_key_id_value
    import capo_s3.types.session_credential_value
    import capo_s3.types.session_expiration


class SessionCredentials(TypedDict, closed=True):
    access_key_id: "capo_s3.types.access_key_id_value.AccessKeyIdValue"
    """<p>A unique identifier that's associated with a secret access key. The access key ID and the secret access key are used together to sign programmatic Amazon Web Services requests cryptographically. </p>"""
    secret_access_key: "capo_s3.types.session_credential_value.SessionCredentialValue"
    """<p>A key that's used with the access key ID to cryptographically sign programmatic Amazon Web Services requests. Signing a request identifies the sender and prevents the request from being altered. </p>"""
    session_token: "capo_s3.types.session_credential_value.SessionCredentialValue"
    """<p>A part of the temporary security credentials. The session token is used to validate the temporary security credentials. </p>"""
    expiration: "capo_s3.types.session_expiration.SessionExpiration"
    """<p>Temporary security credentials expire after a specified interval. After temporary credentials expire, any calls that you make with those credentials will fail. So you must generate a new set of temporary credentials. Temporary credentials cannot be extended or refreshed beyond the original specified interval.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: SessionCredentials, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "AccessKeyId").text = str(value["access_key_id"])
    SubElement(el, "SecretAccessKey").text = str(value["secret_access_key"])
    SubElement(el, "SessionToken").text = str(value["session_token"])
    import capo_s3.types.session_expiration

    capo_s3.types.session_expiration.serialize_xml(
        value["expiration"], el, "Expiration"
    )


def deserialize_xml(el: Element) -> SessionCredentials:
    out: SessionCredentials = {}  # type: ignore[typeddict-item]
    child_access_key_id = el.find("AccessKeyId")
    if child_access_key_id is not None:
        out["access_key_id"] = str(child_access_key_id.text or "")
    else:
        raise DeserializationError("SessionCredentials.access_key_id required")
    child_secret_access_key = el.find("SecretAccessKey")
    if child_secret_access_key is not None:
        out["secret_access_key"] = str(child_secret_access_key.text or "")
    else:
        raise DeserializationError("SessionCredentials.secret_access_key required")
    child_session_token = el.find("SessionToken")
    if child_session_token is not None:
        out["session_token"] = str(child_session_token.text or "")
    else:
        raise DeserializationError("SessionCredentials.session_token required")
    child_expiration = el.find("Expiration")
    if child_expiration is not None:
        import capo_s3.types.session_expiration

        out["expiration"] = capo_s3.types.session_expiration.deserialize_xml(
            child_expiration
        )
    else:
        raise DeserializationError("SessionCredentials.expiration required")
    return out


def redact_sensitive(value: SessionCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_access_key" in value:
        out["secret_access_key"] = "*** Sensitive Data Redacted ***"
    if "session_token" in value:
        out["session_token"] = "*** Sensitive Data Redacted ***"
    return out
