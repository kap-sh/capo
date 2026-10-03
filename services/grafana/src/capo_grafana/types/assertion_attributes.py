"""Generated from Smithy shape ``com.amazonaws.grafana#AssertionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.assertion_attribute


class AssertionAttributes(TypedDict, closed=True):
    name: NotRequired["capo_grafana.types.assertion_attribute.AssertionAttribute"]
    """<p>The name of the attribute within the SAML assertion to use as the user full "friendly" names for SAML users.</p>"""
    login: NotRequired["capo_grafana.types.assertion_attribute.AssertionAttribute"]
    """<p>The name of the attribute within the SAML assertion to use as the login names for SAML users.</p>"""
    email: NotRequired["capo_grafana.types.assertion_attribute.AssertionAttribute"]
    """<p>The name of the attribute within the SAML assertion to use as the email names for SAML users.</p>"""
    groups: NotRequired["capo_grafana.types.assertion_attribute.AssertionAttribute"]
    """<p>The name of the attribute within the SAML assertion to use as the user full "friendly" names for user groups.</p>"""
    role: NotRequired["capo_grafana.types.assertion_attribute.AssertionAttribute"]
    """<p>The name of the attribute within the SAML assertion to use as the user roles.</p>"""
    org: NotRequired["capo_grafana.types.assertion_attribute.AssertionAttribute"]
    """<p>The name of the attribute within the SAML assertion to use as the user full "friendly" names for the users' organizations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssertionAttributes) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "login" in value:
        out["login"] = value["login"]
    if "email" in value:
        out["email"] = value["email"]
    if "groups" in value:
        out["groups"] = value["groups"]
    if "role" in value:
        out["role"] = value["role"]
    if "org" in value:
        out["org"] = value["org"]
    return out


def deserialize_json(data: dict) -> AssertionAttributes:
    out: AssertionAttributes = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("login") is not None:
        out["login"] = data["login"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    if data.get("groups") is not None:
        out["groups"] = data["groups"]
    if data.get("role") is not None:
        out["role"] = data["role"]
    if data.get("org") is not None:
        out["org"] = data["org"]
    return out
