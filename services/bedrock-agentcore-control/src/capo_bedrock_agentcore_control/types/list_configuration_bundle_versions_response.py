"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListConfigurationBundleVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_version_summary_list


class ListConfigurationBundleVersionsResponse(TypedDict, closed=True):
    versions: "capo_bedrock_agentcore_control.types.configuration_bundle_version_summary_list.ConfigurationBundleVersionSummaryList"
    """<p>The list of configuration bundle version summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationBundleVersionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.configuration_bundle_version_summary_list

    out["versions"] = (
        capo_bedrock_agentcore_control.types.configuration_bundle_version_summary_list.serialize_json(
            value["versions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationBundleVersionsResponse:
    out: ListConfigurationBundleVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("versions") is not None:
        import capo_bedrock_agentcore_control.types.configuration_bundle_version_summary_list

        out["versions"] = (
            capo_bedrock_agentcore_control.types.configuration_bundle_version_summary_list.deserialize_json(
                data["versions"]
            )
        )
    else:
        out["versions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
