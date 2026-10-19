"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#SamlConfigOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.open_search_serverless_entity_id
    import capo_opensearchserverless.types.saml_group_attribute
    import capo_opensearchserverless.types.saml_metadata
    import capo_opensearchserverless.types.saml_user_attribute


class SamlConfigOptions(TypedDict, closed=True):
    metadata: "capo_opensearchserverless.types.saml_metadata.samlMetadata"
    """<p>The XML IdP metadata file generated from your identity provider.</p>"""
    user_attribute: NotRequired[
        "capo_opensearchserverless.types.saml_user_attribute.samlUserAttribute"
    ]
    """<p>A user attribute for this SAML integration.</p>"""
    group_attribute: NotRequired[
        "capo_opensearchserverless.types.saml_group_attribute.samlGroupAttribute"
    ]
    """<p>The group attribute for this SAML integration.</p>"""
    open_search_serverless_entity_id: NotRequired[
        "capo_opensearchserverless.types.open_search_serverless_entity_id.openSearchServerlessEntityId"
    ]
    """<p>Custom entity ID attribute to override the default entity ID for this SAML integration.</p>"""
    session_timeout: NotRequired["int"]
    """<p>The session timeout, in minutes. Default is 60 minutes (12 hours).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SamlConfigOptions) -> dict:
    out: dict = {}
    out["metadata"] = value["metadata"]
    if "user_attribute" in value:
        out["userAttribute"] = value["user_attribute"]
    if "group_attribute" in value:
        out["groupAttribute"] = value["group_attribute"]
    if "open_search_serverless_entity_id" in value:
        out["openSearchServerlessEntityId"] = value["open_search_serverless_entity_id"]
    if "session_timeout" in value:
        out["sessionTimeout"] = value["session_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SamlConfigOptions:
    out: SamlConfigOptions = {}  # type: ignore[typeddict-item]
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    else:
        out["metadata"] = ""
    if data.get("userAttribute") is not None:
        out["user_attribute"] = data["userAttribute"]
    if data.get("groupAttribute") is not None:
        out["group_attribute"] = data["groupAttribute"]
    if data.get("openSearchServerlessEntityId") is not None:
        out["open_search_serverless_entity_id"] = data["openSearchServerlessEntityId"]
    if data.get("sessionTimeout") is not None:
        out["session_timeout"] = data["sessionTimeout"]
    return out
