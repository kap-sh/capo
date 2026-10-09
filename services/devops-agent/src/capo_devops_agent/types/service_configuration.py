"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.aws_configuration
    import capo_devops_agent.types.azure_configuration
    import capo_devops_agent.types.azure_dev_ops_configuration
    import capo_devops_agent.types.dynatrace_configuration
    import capo_devops_agent.types.event_channel_configuration
    import capo_devops_agent.types.git_hub_configuration
    import capo_devops_agent.types.git_lab_configuration
    import capo_devops_agent.types.mcp_server_configuration
    import capo_devops_agent.types.mcp_server_datadog_configuration
    import capo_devops_agent.types.mcp_server_grafana_configuration
    import capo_devops_agent.types.mcp_server_new_relic_configuration
    import capo_devops_agent.types.mcp_server_sig_v4_configuration
    import capo_devops_agent.types.mcp_server_splunk_configuration
    import capo_devops_agent.types.pager_duty_configuration
    import capo_devops_agent.types.release_management_configuration
    import capo_devops_agent.types.remote_agent_configuration
    import capo_devops_agent.types.remote_agent_sig_v4_configuration
    import capo_devops_agent.types.service_now_configuration
    import capo_devops_agent.types.slack_configuration
    import capo_devops_agent.types.source_aws_configuration


class _ServiceConfiguration_sourceAws(TypedDict, closed=True):
    sourceAws: "capo_devops_agent.types.source_aws_configuration.SourceAwsConfiguration"


class _ServiceConfiguration_aws(TypedDict, closed=True):
    aws: "capo_devops_agent.types.aws_configuration.AWSConfiguration"


class _ServiceConfiguration_github(TypedDict, closed=True):
    github: "capo_devops_agent.types.git_hub_configuration.GitHubConfiguration"


class _ServiceConfiguration_slack(TypedDict, closed=True):
    slack: "capo_devops_agent.types.slack_configuration.SlackConfiguration"


class _ServiceConfiguration_dynatrace(TypedDict, closed=True):
    dynatrace: "capo_devops_agent.types.dynatrace_configuration.DynatraceConfiguration"


class _ServiceConfiguration_servicenow(TypedDict, closed=True):
    servicenow: (
        "capo_devops_agent.types.service_now_configuration.ServiceNowConfiguration"
    )


class _ServiceConfiguration_mcpservernewrelic(TypedDict, closed=True):
    mcpservernewrelic: "capo_devops_agent.types.mcp_server_new_relic_configuration.MCPServerNewRelicConfiguration"


class _ServiceConfiguration_mcpserverdatadog(TypedDict, closed=True):
    mcpserverdatadog: "capo_devops_agent.types.mcp_server_datadog_configuration.MCPServerDatadogConfiguration"


class _ServiceConfiguration_mcpserver(TypedDict, closed=True):
    mcpserver: "capo_devops_agent.types.mcp_server_configuration.MCPServerConfiguration"


class _ServiceConfiguration_gitlab(TypedDict, closed=True):
    gitlab: "capo_devops_agent.types.git_lab_configuration.GitLabConfiguration"


class _ServiceConfiguration_mcpserversplunk(TypedDict, closed=True):
    mcpserversplunk: "capo_devops_agent.types.mcp_server_splunk_configuration.MCPServerSplunkConfiguration"


class _ServiceConfiguration_eventChannel(TypedDict, closed=True):
    eventChannel: (
        "capo_devops_agent.types.event_channel_configuration.EventChannelConfiguration"
    )


class _ServiceConfiguration_azure(TypedDict, closed=True):
    azure: "capo_devops_agent.types.azure_configuration.AzureConfiguration"


class _ServiceConfiguration_azuredevops(TypedDict, closed=True):
    azuredevops: (
        "capo_devops_agent.types.azure_dev_ops_configuration.AzureDevOpsConfiguration"
    )


class _ServiceConfiguration_mcpservergrafana(TypedDict, closed=True):
    mcpservergrafana: "capo_devops_agent.types.mcp_server_grafana_configuration.MCPServerGrafanaConfiguration"


class _ServiceConfiguration_pagerduty(TypedDict, closed=True):
    pagerduty: "capo_devops_agent.types.pager_duty_configuration.PagerDutyConfiguration"


class _ServiceConfiguration_mcpserversigv4(TypedDict, closed=True):
    mcpserversigv4: "capo_devops_agent.types.mcp_server_sig_v4_configuration.MCPServerSigV4Configuration"


class _ServiceConfiguration_remoteagent(TypedDict, closed=True):
    remoteagent: (
        "capo_devops_agent.types.remote_agent_configuration.RemoteAgentConfiguration"
    )


class _ServiceConfiguration_remoteagentsigv4(TypedDict, closed=True):
    remoteagentsigv4: "capo_devops_agent.types.remote_agent_sig_v4_configuration.RemoteAgentSigV4Configuration"


class _ServiceConfiguration_releaseManagement(TypedDict, closed=True):
    releaseManagement: "capo_devops_agent.types.release_management_configuration.ReleaseManagementConfiguration"


ServiceConfiguration: TypeAlias = (
    _ServiceConfiguration_sourceAws
    | _ServiceConfiguration_aws
    | _ServiceConfiguration_github
    | _ServiceConfiguration_slack
    | _ServiceConfiguration_dynatrace
    | _ServiceConfiguration_servicenow
    | _ServiceConfiguration_mcpservernewrelic
    | _ServiceConfiguration_mcpserverdatadog
    | _ServiceConfiguration_mcpserver
    | _ServiceConfiguration_gitlab
    | _ServiceConfiguration_mcpserversplunk
    | _ServiceConfiguration_eventChannel
    | _ServiceConfiguration_azure
    | _ServiceConfiguration_azuredevops
    | _ServiceConfiguration_mcpservergrafana
    | _ServiceConfiguration_pagerduty
    | _ServiceConfiguration_mcpserversigv4
    | _ServiceConfiguration_remoteagent
    | _ServiceConfiguration_remoteagentsigv4
    | _ServiceConfiguration_releaseManagement
)


# --- restJson1 ser/de ---
def serialize_json(value: ServiceConfiguration) -> dict:
    if "sourceAws" in value:
        import capo_devops_agent.types.source_aws_configuration

        return {
            "sourceAws": capo_devops_agent.types.source_aws_configuration.serialize_json(
                value["sourceAws"]
            )
        }
    elif "aws" in value:
        import capo_devops_agent.types.aws_configuration

        return {
            "aws": capo_devops_agent.types.aws_configuration.serialize_json(
                value["aws"]
            )
        }
    elif "github" in value:
        import capo_devops_agent.types.git_hub_configuration

        return {
            "github": capo_devops_agent.types.git_hub_configuration.serialize_json(
                value["github"]
            )
        }
    elif "slack" in value:
        import capo_devops_agent.types.slack_configuration

        return {
            "slack": capo_devops_agent.types.slack_configuration.serialize_json(
                value["slack"]
            )
        }
    elif "dynatrace" in value:
        import capo_devops_agent.types.dynatrace_configuration

        return {
            "dynatrace": capo_devops_agent.types.dynatrace_configuration.serialize_json(
                value["dynatrace"]
            )
        }
    elif "servicenow" in value:
        import capo_devops_agent.types.service_now_configuration

        return {
            "servicenow": capo_devops_agent.types.service_now_configuration.serialize_json(
                value["servicenow"]
            )
        }
    elif "mcpservernewrelic" in value:
        import capo_devops_agent.types.mcp_server_new_relic_configuration

        return {
            "mcpservernewrelic": capo_devops_agent.types.mcp_server_new_relic_configuration.serialize_json(
                value["mcpservernewrelic"]
            )
        }
    elif "mcpserverdatadog" in value:
        import capo_devops_agent.types.mcp_server_datadog_configuration

        return {
            "mcpserverdatadog": capo_devops_agent.types.mcp_server_datadog_configuration.serialize_json(
                value["mcpserverdatadog"]
            )
        }
    elif "mcpserver" in value:
        import capo_devops_agent.types.mcp_server_configuration

        return {
            "mcpserver": capo_devops_agent.types.mcp_server_configuration.serialize_json(
                value["mcpserver"]
            )
        }
    elif "gitlab" in value:
        import capo_devops_agent.types.git_lab_configuration

        return {
            "gitlab": capo_devops_agent.types.git_lab_configuration.serialize_json(
                value["gitlab"]
            )
        }
    elif "mcpserversplunk" in value:
        import capo_devops_agent.types.mcp_server_splunk_configuration

        return {
            "mcpserversplunk": capo_devops_agent.types.mcp_server_splunk_configuration.serialize_json(
                value["mcpserversplunk"]
            )
        }
    elif "eventChannel" in value:
        import capo_devops_agent.types.event_channel_configuration

        return {
            "eventChannel": capo_devops_agent.types.event_channel_configuration.serialize_json(
                value["eventChannel"]
            )
        }
    elif "azure" in value:
        import capo_devops_agent.types.azure_configuration

        return {
            "azure": capo_devops_agent.types.azure_configuration.serialize_json(
                value["azure"]
            )
        }
    elif "azuredevops" in value:
        import capo_devops_agent.types.azure_dev_ops_configuration

        return {
            "azuredevops": capo_devops_agent.types.azure_dev_ops_configuration.serialize_json(
                value["azuredevops"]
            )
        }
    elif "mcpservergrafana" in value:
        import capo_devops_agent.types.mcp_server_grafana_configuration

        return {
            "mcpservergrafana": capo_devops_agent.types.mcp_server_grafana_configuration.serialize_json(
                value["mcpservergrafana"]
            )
        }
    elif "pagerduty" in value:
        import capo_devops_agent.types.pager_duty_configuration

        return {
            "pagerduty": capo_devops_agent.types.pager_duty_configuration.serialize_json(
                value["pagerduty"]
            )
        }
    elif "mcpserversigv4" in value:
        import capo_devops_agent.types.mcp_server_sig_v4_configuration

        return {
            "mcpserversigv4": capo_devops_agent.types.mcp_server_sig_v4_configuration.serialize_json(
                value["mcpserversigv4"]
            )
        }
    elif "remoteagent" in value:
        import capo_devops_agent.types.remote_agent_configuration

        return {
            "remoteagent": capo_devops_agent.types.remote_agent_configuration.serialize_json(
                value["remoteagent"]
            )
        }
    elif "remoteagentsigv4" in value:
        import capo_devops_agent.types.remote_agent_sig_v4_configuration

        return {
            "remoteagentsigv4": capo_devops_agent.types.remote_agent_sig_v4_configuration.serialize_json(
                value["remoteagentsigv4"]
            )
        }
    elif "releaseManagement" in value:
        import capo_devops_agent.types.release_management_configuration

        return {
            "releaseManagement": capo_devops_agent.types.release_management_configuration.serialize_json(
                value["releaseManagement"]
            )
        }
    else:
        raise SerializationError("ServiceConfiguration: no variant present")


def deserialize_json(data: dict) -> ServiceConfiguration:
    if data.get("sourceAws") is not None:
        import capo_devops_agent.types.source_aws_configuration

        return {
            "sourceAws": capo_devops_agent.types.source_aws_configuration.deserialize_json(
                data["sourceAws"]
            )
        }
    elif data.get("aws") is not None:
        import capo_devops_agent.types.aws_configuration

        return {
            "aws": capo_devops_agent.types.aws_configuration.deserialize_json(
                data["aws"]
            )
        }
    elif data.get("github") is not None:
        import capo_devops_agent.types.git_hub_configuration

        return {
            "github": capo_devops_agent.types.git_hub_configuration.deserialize_json(
                data["github"]
            )
        }
    elif data.get("slack") is not None:
        import capo_devops_agent.types.slack_configuration

        return {
            "slack": capo_devops_agent.types.slack_configuration.deserialize_json(
                data["slack"]
            )
        }
    elif data.get("dynatrace") is not None:
        import capo_devops_agent.types.dynatrace_configuration

        return {
            "dynatrace": capo_devops_agent.types.dynatrace_configuration.deserialize_json(
                data["dynatrace"]
            )
        }
    elif data.get("servicenow") is not None:
        import capo_devops_agent.types.service_now_configuration

        return {
            "servicenow": capo_devops_agent.types.service_now_configuration.deserialize_json(
                data["servicenow"]
            )
        }
    elif data.get("mcpservernewrelic") is not None:
        import capo_devops_agent.types.mcp_server_new_relic_configuration

        return {
            "mcpservernewrelic": capo_devops_agent.types.mcp_server_new_relic_configuration.deserialize_json(
                data["mcpservernewrelic"]
            )
        }
    elif data.get("mcpserverdatadog") is not None:
        import capo_devops_agent.types.mcp_server_datadog_configuration

        return {
            "mcpserverdatadog": capo_devops_agent.types.mcp_server_datadog_configuration.deserialize_json(
                data["mcpserverdatadog"]
            )
        }
    elif data.get("mcpserver") is not None:
        import capo_devops_agent.types.mcp_server_configuration

        return {
            "mcpserver": capo_devops_agent.types.mcp_server_configuration.deserialize_json(
                data["mcpserver"]
            )
        }
    elif data.get("gitlab") is not None:
        import capo_devops_agent.types.git_lab_configuration

        return {
            "gitlab": capo_devops_agent.types.git_lab_configuration.deserialize_json(
                data["gitlab"]
            )
        }
    elif data.get("mcpserversplunk") is not None:
        import capo_devops_agent.types.mcp_server_splunk_configuration

        return {
            "mcpserversplunk": capo_devops_agent.types.mcp_server_splunk_configuration.deserialize_json(
                data["mcpserversplunk"]
            )
        }
    elif data.get("eventChannel") is not None:
        import capo_devops_agent.types.event_channel_configuration

        return {
            "eventChannel": capo_devops_agent.types.event_channel_configuration.deserialize_json(
                data["eventChannel"]
            )
        }
    elif data.get("azure") is not None:
        import capo_devops_agent.types.azure_configuration

        return {
            "azure": capo_devops_agent.types.azure_configuration.deserialize_json(
                data["azure"]
            )
        }
    elif data.get("azuredevops") is not None:
        import capo_devops_agent.types.azure_dev_ops_configuration

        return {
            "azuredevops": capo_devops_agent.types.azure_dev_ops_configuration.deserialize_json(
                data["azuredevops"]
            )
        }
    elif data.get("mcpservergrafana") is not None:
        import capo_devops_agent.types.mcp_server_grafana_configuration

        return {
            "mcpservergrafana": capo_devops_agent.types.mcp_server_grafana_configuration.deserialize_json(
                data["mcpservergrafana"]
            )
        }
    elif data.get("pagerduty") is not None:
        import capo_devops_agent.types.pager_duty_configuration

        return {
            "pagerduty": capo_devops_agent.types.pager_duty_configuration.deserialize_json(
                data["pagerduty"]
            )
        }
    elif data.get("mcpserversigv4") is not None:
        import capo_devops_agent.types.mcp_server_sig_v4_configuration

        return {
            "mcpserversigv4": capo_devops_agent.types.mcp_server_sig_v4_configuration.deserialize_json(
                data["mcpserversigv4"]
            )
        }
    elif data.get("remoteagent") is not None:
        import capo_devops_agent.types.remote_agent_configuration

        return {
            "remoteagent": capo_devops_agent.types.remote_agent_configuration.deserialize_json(
                data["remoteagent"]
            )
        }
    elif data.get("remoteagentsigv4") is not None:
        import capo_devops_agent.types.remote_agent_sig_v4_configuration

        return {
            "remoteagentsigv4": capo_devops_agent.types.remote_agent_sig_v4_configuration.deserialize_json(
                data["remoteagentsigv4"]
            )
        }
    elif data.get("releaseManagement") is not None:
        import capo_devops_agent.types.release_management_configuration

        return {
            "releaseManagement": capo_devops_agent.types.release_management_configuration.deserialize_json(
                data["releaseManagement"]
            )
        }
    else:
        raise DeserializationError("ServiceConfiguration: no recognized variant key")
