"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListConfigurationBundlesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_summary_list


class ListConfigurationBundlesResponse(TypedDict, closed=True):
    bundles: "capo_bedrock_agentcore_control.types.configuration_bundle_summary_list.ConfigurationBundleSummaryList"
    """<p>The list of configuration bundle summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationBundlesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.configuration_bundle_summary_list

    out["bundles"] = (
        capo_bedrock_agentcore_control.types.configuration_bundle_summary_list.serialize_json(
            value["bundles"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationBundlesResponse:
    out: ListConfigurationBundlesResponse = {}  # type: ignore[typeddict-item]
    if data.get("bundles") is not None:
        import capo_bedrock_agentcore_control.types.configuration_bundle_summary_list

        out["bundles"] = (
            capo_bedrock_agentcore_control.types.configuration_bundle_summary_list.deserialize_json(
                data["bundles"]
            )
        )
    else:
        raise DeserializationError("ListConfigurationBundlesResponse.bundles required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListConfigurationBundlesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bundles" in value:
        import capo_bedrock_agentcore_control.types.configuration_bundle_summary_list

        out["bundles"] = (
            capo_bedrock_agentcore_control.types.configuration_bundle_summary_list.redact_sensitive(
                value["bundles"]
            )
        )
    return out
