"""Generated from Smithy shape ``com.amazonaws.securityagent#Actor``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.authentication
    import capo_securityagent.types.sensitive_email_address
    import capo_securityagent.types.uri_list


class Actor(TypedDict, closed=True):
    identifier: NotRequired["str"]
    """<p>The unique identifier for the actor.</p>"""
    uris: NotRequired["capo_securityagent.types.uri_list.UriList"]
    """<p>The list of URIs that the actor targets during testing.</p>"""
    authentication: NotRequired[
        "capo_securityagent.types.authentication.Authentication"
    ]
    """<p>The authentication configuration for the actor.</p>"""
    description: NotRequired["str"]
    """<p>A description of the actor.</p>"""
    enable_email_mfa: NotRequired["bool"]
    """<p>Whether email-based MFA is enabled for this actor.</p>"""
    mfa_forwarding_address: NotRequired[
        "capo_securityagent.types.sensitive_email_address.SensitiveEmailAddress"
    ]
    """<p>Server-generated email forwarding address for receiving MFA codes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Actor) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "uris" in value:
        import capo_securityagent.types.uri_list

        out["uris"] = capo_securityagent.types.uri_list.serialize_json(value["uris"])
    if "authentication" in value:
        import capo_securityagent.types.authentication

        out["authentication"] = capo_securityagent.types.authentication.serialize_json(
            value["authentication"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "enable_email_mfa" in value:
        out["enableEmailMfa"] = value["enable_email_mfa"]
    if "mfa_forwarding_address" in value:
        out["mfaForwardingAddress"] = value["mfa_forwarding_address"]
    return out


def deserialize_json(data: dict) -> Actor:
    out: Actor = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("uris") is not None:
        import capo_securityagent.types.uri_list

        out["uris"] = capo_securityagent.types.uri_list.deserialize_json(data["uris"])
    if data.get("authentication") is not None:
        import capo_securityagent.types.authentication

        out["authentication"] = (
            capo_securityagent.types.authentication.deserialize_json(
                data["authentication"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("enableEmailMfa") is not None:
        out["enable_email_mfa"] = data["enableEmailMfa"]
    if data.get("mfaForwardingAddress") is not None:
        out["mfa_forwarding_address"] = data["mfaForwardingAddress"]
    return out


def redact_sensitive(value: Actor) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "mfa_forwarding_address" in value:
        out["mfa_forwarding_address"] = "*** Sensitive Data Redacted ***"
    return out
