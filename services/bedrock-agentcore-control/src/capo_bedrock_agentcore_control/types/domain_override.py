"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DomainOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.public_domain_name
    import capo_bedrock_agentcore_control.types.public_domain_name_list


class DomainOverride(TypedDict, closed=True):
    default_domain: (
        "capo_bedrock_agentcore_control.types.public_domain_name.PublicDomainName"
    )
    """<p>The default public domain name for the gateway. The gateway advertises this domain when a request doesn't select a specific domain.</p>"""
    alternate_domains: NotRequired[
        "capo_bedrock_agentcore_control.types.public_domain_name_list.PublicDomainNameList"
    ]
    """<p>Additional public domain names for the gateway, up to 10. Don't repeat the default domain or list a domain more than once. A request can select one of these domains, or the default domain, with the <code>x-amzn-bedrock-agentcore-gateway-domain</code> header. The gateway rejects a request that selects a domain that isn't configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainOverride) -> dict:
    out: dict = {}
    out["default"] = value["default_domain"]
    if "alternate_domains" in value:
        import capo_bedrock_agentcore_control.types.public_domain_name_list

        out["alternateDomains"] = (
            capo_bedrock_agentcore_control.types.public_domain_name_list.serialize_json(
                value["alternate_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainOverride:
    out: DomainOverride = {}  # type: ignore[typeddict-item]
    if data.get("default") is not None:
        out["default_domain"] = data["default"]
    else:
        out["default_domain"] = ""
    if data.get("alternateDomains") is not None:
        import capo_bedrock_agentcore_control.types.public_domain_name_list

        out["alternate_domains"] = (
            capo_bedrock_agentcore_control.types.public_domain_name_list.deserialize_json(
                data["alternateDomains"]
            )
        )
    return out
