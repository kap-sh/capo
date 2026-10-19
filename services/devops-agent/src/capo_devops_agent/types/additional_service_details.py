"""Generated from Smithy shape ``com.amazonaws.devopsagent#AdditionalServiceDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.registered_azure_dev_ops_service_details
    import capo_devops_agent.types.registered_azure_identity_details
    import capo_devops_agent.types.registered_git_lab_service_details
    import capo_devops_agent.types.registered_github_service_details
    import capo_devops_agent.types.registered_grafana_server_details
    import capo_devops_agent.types.registered_mcp_server_details
    import capo_devops_agent.types.registered_mcp_server_sig_v4_details
    import capo_devops_agent.types.registered_new_relic_details
    import capo_devops_agent.types.registered_pager_duty_details
    import capo_devops_agent.types.registered_remote_agent_details
    import capo_devops_agent.types.registered_remote_agent_sig_v4_details
    import capo_devops_agent.types.registered_service_now_details
    import capo_devops_agent.types.registered_slack_service_details


class _AdditionalServiceDetails_github(TypedDict, closed=True):
    github: "capo_devops_agent.types.registered_github_service_details.RegisteredGithubServiceDetails"


class _AdditionalServiceDetails_slack(TypedDict, closed=True):
    slack: "capo_devops_agent.types.registered_slack_service_details.RegisteredSlackServiceDetails"


class _AdditionalServiceDetails_mcpserverdatadog(TypedDict, closed=True):
    mcpserverdatadog: "capo_devops_agent.types.registered_mcp_server_details.RegisteredMCPServerDetails"


class _AdditionalServiceDetails_mcpserver(TypedDict, closed=True):
    mcpserver: "capo_devops_agent.types.registered_mcp_server_details.RegisteredMCPServerDetails"


class _AdditionalServiceDetails_servicenow(TypedDict, closed=True):
    servicenow: "capo_devops_agent.types.registered_service_now_details.RegisteredServiceNowDetails"


class _AdditionalServiceDetails_gitlab(TypedDict, closed=True):
    gitlab: "capo_devops_agent.types.registered_git_lab_service_details.RegisteredGitLabServiceDetails"


class _AdditionalServiceDetails_mcpserversplunk(TypedDict, closed=True):
    mcpserversplunk: "capo_devops_agent.types.registered_mcp_server_details.RegisteredMCPServerDetails"


class _AdditionalServiceDetails_mcpservernewrelic(TypedDict, closed=True):
    mcpservernewrelic: (
        "capo_devops_agent.types.registered_new_relic_details.RegisteredNewRelicDetails"
    )


class _AdditionalServiceDetails_azuredevops(TypedDict, closed=True):
    azuredevops: "capo_devops_agent.types.registered_azure_dev_ops_service_details.RegisteredAzureDevOpsServiceDetails"


class _AdditionalServiceDetails_azureidentity(TypedDict, closed=True):
    azureidentity: "capo_devops_agent.types.registered_azure_identity_details.RegisteredAzureIdentityDetails"


class _AdditionalServiceDetails_mcpservergrafana(TypedDict, closed=True):
    mcpservergrafana: "capo_devops_agent.types.registered_grafana_server_details.RegisteredGrafanaServerDetails"


class _AdditionalServiceDetails_pagerduty(TypedDict, closed=True):
    pagerduty: "capo_devops_agent.types.registered_pager_duty_details.RegisteredPagerDutyDetails"


class _AdditionalServiceDetails_mcpserversigv4(TypedDict, closed=True):
    mcpserversigv4: "capo_devops_agent.types.registered_mcp_server_sig_v4_details.RegisteredMCPServerSigV4Details"


class _AdditionalServiceDetails_remoteagent(TypedDict, closed=True):
    remoteagent: "capo_devops_agent.types.registered_remote_agent_details.RegisteredRemoteAgentDetails"


class _AdditionalServiceDetails_remoteagentsigv4(TypedDict, closed=True):
    remoteagentsigv4: "capo_devops_agent.types.registered_remote_agent_sig_v4_details.RegisteredRemoteAgentSigV4Details"


AdditionalServiceDetails: TypeAlias = (
    _AdditionalServiceDetails_github
    | _AdditionalServiceDetails_slack
    | _AdditionalServiceDetails_mcpserverdatadog
    | _AdditionalServiceDetails_mcpserver
    | _AdditionalServiceDetails_servicenow
    | _AdditionalServiceDetails_gitlab
    | _AdditionalServiceDetails_mcpserversplunk
    | _AdditionalServiceDetails_mcpservernewrelic
    | _AdditionalServiceDetails_azuredevops
    | _AdditionalServiceDetails_azureidentity
    | _AdditionalServiceDetails_mcpservergrafana
    | _AdditionalServiceDetails_pagerduty
    | _AdditionalServiceDetails_mcpserversigv4
    | _AdditionalServiceDetails_remoteagent
    | _AdditionalServiceDetails_remoteagentsigv4
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalServiceDetails) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AdditionalServiceDetails: cannot serialize unknown variant {value.name!r}"
        )
    elif "github" in value:
        import capo_devops_agent.types.registered_github_service_details

        return {
            "github": capo_devops_agent.types.registered_github_service_details.serialize_json(
                value["github"]
            )
        }
    elif "slack" in value:
        import capo_devops_agent.types.registered_slack_service_details

        return {
            "slack": capo_devops_agent.types.registered_slack_service_details.serialize_json(
                value["slack"]
            )
        }
    elif "mcpserverdatadog" in value:
        import capo_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserverdatadog": capo_devops_agent.types.registered_mcp_server_details.serialize_json(
                value["mcpserverdatadog"]
            )
        }
    elif "mcpserver" in value:
        import capo_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserver": capo_devops_agent.types.registered_mcp_server_details.serialize_json(
                value["mcpserver"]
            )
        }
    elif "servicenow" in value:
        import capo_devops_agent.types.registered_service_now_details

        return {
            "servicenow": capo_devops_agent.types.registered_service_now_details.serialize_json(
                value["servicenow"]
            )
        }
    elif "gitlab" in value:
        import capo_devops_agent.types.registered_git_lab_service_details

        return {
            "gitlab": capo_devops_agent.types.registered_git_lab_service_details.serialize_json(
                value["gitlab"]
            )
        }
    elif "mcpserversplunk" in value:
        import capo_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserversplunk": capo_devops_agent.types.registered_mcp_server_details.serialize_json(
                value["mcpserversplunk"]
            )
        }
    elif "mcpservernewrelic" in value:
        import capo_devops_agent.types.registered_new_relic_details

        return {
            "mcpservernewrelic": capo_devops_agent.types.registered_new_relic_details.serialize_json(
                value["mcpservernewrelic"]
            )
        }
    elif "azuredevops" in value:
        import capo_devops_agent.types.registered_azure_dev_ops_service_details

        return {
            "azuredevops": capo_devops_agent.types.registered_azure_dev_ops_service_details.serialize_json(
                value["azuredevops"]
            )
        }
    elif "azureidentity" in value:
        import capo_devops_agent.types.registered_azure_identity_details

        return {
            "azureidentity": capo_devops_agent.types.registered_azure_identity_details.serialize_json(
                value["azureidentity"]
            )
        }
    elif "mcpservergrafana" in value:
        import capo_devops_agent.types.registered_grafana_server_details

        return {
            "mcpservergrafana": capo_devops_agent.types.registered_grafana_server_details.serialize_json(
                value["mcpservergrafana"]
            )
        }
    elif "pagerduty" in value:
        import capo_devops_agent.types.registered_pager_duty_details

        return {
            "pagerduty": capo_devops_agent.types.registered_pager_duty_details.serialize_json(
                value["pagerduty"]
            )
        }
    elif "mcpserversigv4" in value:
        import capo_devops_agent.types.registered_mcp_server_sig_v4_details

        return {
            "mcpserversigv4": capo_devops_agent.types.registered_mcp_server_sig_v4_details.serialize_json(
                value["mcpserversigv4"]
            )
        }
    elif "remoteagent" in value:
        import capo_devops_agent.types.registered_remote_agent_details

        return {
            "remoteagent": capo_devops_agent.types.registered_remote_agent_details.serialize_json(
                value["remoteagent"]
            )
        }
    elif "remoteagentsigv4" in value:
        import capo_devops_agent.types.registered_remote_agent_sig_v4_details

        return {
            "remoteagentsigv4": capo_devops_agent.types.registered_remote_agent_sig_v4_details.serialize_json(
                value["remoteagentsigv4"]
            )
        }
    else:
        raise SerializationError("AdditionalServiceDetails: no variant present")


def deserialize_json(data: dict) -> AdditionalServiceDetails:
    if data.get("github") is not None:
        import capo_devops_agent.types.registered_github_service_details

        return {
            "github": capo_devops_agent.types.registered_github_service_details.deserialize_json(
                data["github"]
            )
        }
    elif data.get("slack") is not None:
        import capo_devops_agent.types.registered_slack_service_details

        return {
            "slack": capo_devops_agent.types.registered_slack_service_details.deserialize_json(
                data["slack"]
            )
        }
    elif data.get("mcpserverdatadog") is not None:
        import capo_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserverdatadog": capo_devops_agent.types.registered_mcp_server_details.deserialize_json(
                data["mcpserverdatadog"]
            )
        }
    elif data.get("mcpserver") is not None:
        import capo_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserver": capo_devops_agent.types.registered_mcp_server_details.deserialize_json(
                data["mcpserver"]
            )
        }
    elif data.get("servicenow") is not None:
        import capo_devops_agent.types.registered_service_now_details

        return {
            "servicenow": capo_devops_agent.types.registered_service_now_details.deserialize_json(
                data["servicenow"]
            )
        }
    elif data.get("gitlab") is not None:
        import capo_devops_agent.types.registered_git_lab_service_details

        return {
            "gitlab": capo_devops_agent.types.registered_git_lab_service_details.deserialize_json(
                data["gitlab"]
            )
        }
    elif data.get("mcpserversplunk") is not None:
        import capo_devops_agent.types.registered_mcp_server_details

        return {
            "mcpserversplunk": capo_devops_agent.types.registered_mcp_server_details.deserialize_json(
                data["mcpserversplunk"]
            )
        }
    elif data.get("mcpservernewrelic") is not None:
        import capo_devops_agent.types.registered_new_relic_details

        return {
            "mcpservernewrelic": capo_devops_agent.types.registered_new_relic_details.deserialize_json(
                data["mcpservernewrelic"]
            )
        }
    elif data.get("azuredevops") is not None:
        import capo_devops_agent.types.registered_azure_dev_ops_service_details

        return {
            "azuredevops": capo_devops_agent.types.registered_azure_dev_ops_service_details.deserialize_json(
                data["azuredevops"]
            )
        }
    elif data.get("azureidentity") is not None:
        import capo_devops_agent.types.registered_azure_identity_details

        return {
            "azureidentity": capo_devops_agent.types.registered_azure_identity_details.deserialize_json(
                data["azureidentity"]
            )
        }
    elif data.get("mcpservergrafana") is not None:
        import capo_devops_agent.types.registered_grafana_server_details

        return {
            "mcpservergrafana": capo_devops_agent.types.registered_grafana_server_details.deserialize_json(
                data["mcpservergrafana"]
            )
        }
    elif data.get("pagerduty") is not None:
        import capo_devops_agent.types.registered_pager_duty_details

        return {
            "pagerduty": capo_devops_agent.types.registered_pager_duty_details.deserialize_json(
                data["pagerduty"]
            )
        }
    elif data.get("mcpserversigv4") is not None:
        import capo_devops_agent.types.registered_mcp_server_sig_v4_details

        return {
            "mcpserversigv4": capo_devops_agent.types.registered_mcp_server_sig_v4_details.deserialize_json(
                data["mcpserversigv4"]
            )
        }
    elif data.get("remoteagent") is not None:
        import capo_devops_agent.types.registered_remote_agent_details

        return {
            "remoteagent": capo_devops_agent.types.registered_remote_agent_details.deserialize_json(
                data["remoteagent"]
            )
        }
    elif data.get("remoteagentsigv4") is not None:
        import capo_devops_agent.types.registered_remote_agent_sig_v4_details

        return {
            "remoteagentsigv4": capo_devops_agent.types.registered_remote_agent_sig_v4_details.deserialize_json(
                data["remoteagentsigv4"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "AdditionalServiceDetails: no recognized variant key"
        )


def redact_sensitive(
    value: AdditionalServiceDetails,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "mcpserverdatadog" in value:
        import capo_devops_agent.types.registered_mcp_server_details

        out["mcpserverdatadog"] = (
            capo_devops_agent.types.registered_mcp_server_details.redact_sensitive(
                value["mcpserverdatadog"]
            )
        )
    if "mcpserver" in value:
        import capo_devops_agent.types.registered_mcp_server_details

        out["mcpserver"] = (
            capo_devops_agent.types.registered_mcp_server_details.redact_sensitive(
                value["mcpserver"]
            )
        )
    if "mcpserversplunk" in value:
        import capo_devops_agent.types.registered_mcp_server_details

        out["mcpserversplunk"] = (
            capo_devops_agent.types.registered_mcp_server_details.redact_sensitive(
                value["mcpserversplunk"]
            )
        )
    if "mcpservernewrelic" in value:
        import capo_devops_agent.types.registered_new_relic_details

        out["mcpservernewrelic"] = (
            capo_devops_agent.types.registered_new_relic_details.redact_sensitive(
                value["mcpservernewrelic"]
            )
        )
    if "mcpserversigv4" in value:
        import capo_devops_agent.types.registered_mcp_server_sig_v4_details

        out["mcpserversigv4"] = (
            capo_devops_agent.types.registered_mcp_server_sig_v4_details.redact_sensitive(
                value["mcpserversigv4"]
            )
        )
    if "remoteagent" in value:
        import capo_devops_agent.types.registered_remote_agent_details

        out["remoteagent"] = (
            capo_devops_agent.types.registered_remote_agent_details.redact_sensitive(
                value["remoteagent"]
            )
        )
    if "remoteagentsigv4" in value:
        import capo_devops_agent.types.registered_remote_agent_sig_v4_details

        out["remoteagentsigv4"] = (
            capo_devops_agent.types.registered_remote_agent_sig_v4_details.redact_sensitive(
                value["remoteagentsigv4"]
            )
        )
    return out
