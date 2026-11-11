"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DomainFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.domain_list


class DomainFilter(TypedDict, closed=True):
    include: NotRequired["capo_bedrock_agentcore.types.domain_list.DomainList"]
    """<p>The domains to return results from. Results from other domains are not returned.</p>"""
    exclude: NotRequired["capo_bedrock_agentcore.types.domain_list.DomainList"]
    """<p>The domains to never return results from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainFilter) -> dict:
    out: dict = {}
    if "include" in value:
        import capo_bedrock_agentcore.types.domain_list

        out["include"] = capo_bedrock_agentcore.types.domain_list.serialize_json(
            value["include"]
        )
    if "exclude" in value:
        import capo_bedrock_agentcore.types.domain_list

        out["exclude"] = capo_bedrock_agentcore.types.domain_list.serialize_json(
            value["exclude"]
        )
    return out


def deserialize_json(data: dict) -> DomainFilter:
    out: DomainFilter = {}  # type: ignore[typeddict-item]
    if data.get("include") is not None:
        import capo_bedrock_agentcore.types.domain_list

        out["include"] = capo_bedrock_agentcore.types.domain_list.deserialize_json(
            data["include"]
        )
    if data.get("exclude") is not None:
        import capo_bedrock_agentcore.types.domain_list

        out["exclude"] = capo_bedrock_agentcore.types.domain_list.deserialize_json(
            data["exclude"]
        )
    return out
