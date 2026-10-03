"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateConfigurationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.policy
    import capo_securityhub.types.tag_map


class CreateConfigurationPolicyRequest(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: <code>-, ., !, *, /</code>. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The description of the configuration policy. </p>"""
    configuration_policy: NotRequired["capo_securityhub.types.policy.Policy"]
    """<p> An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls). </p>"""
    tags: NotRequired["capo_securityhub.types.tag_map.TagMap"]
    """<p> User-defined tags associated with a configuration policy. For more information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/tagging-resources.html">Tagging Security Hub CSPM resources</a> in the <i>Security Hub CSPM user guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationPolicyRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "configuration_policy" in value:
        import capo_securityhub.types.policy

        out["ConfigurationPolicy"] = capo_securityhub.types.policy.serialize_json(
            value["configuration_policy"]
        )
    if "tags" in value:
        import capo_securityhub.types.tag_map

        out["Tags"] = capo_securityhub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfigurationPolicyRequest:
    out: CreateConfigurationPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ConfigurationPolicy") is not None:
        import capo_securityhub.types.policy

        out["configuration_policy"] = capo_securityhub.types.policy.deserialize_json(
            data["ConfigurationPolicy"]
        )
    if data.get("Tags") is not None:
        import capo_securityhub.types.tag_map

        out["tags"] = capo_securityhub.types.tag_map.deserialize_json(data["Tags"])
    return out
