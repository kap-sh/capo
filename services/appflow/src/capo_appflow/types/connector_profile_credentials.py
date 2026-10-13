"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.amplitude_connector_profile_credentials
    import capo_appflow.types.custom_connector_profile_credentials
    import capo_appflow.types.datadog_connector_profile_credentials
    import capo_appflow.types.dynatrace_connector_profile_credentials
    import capo_appflow.types.google_analytics_connector_profile_credentials
    import capo_appflow.types.honeycode_connector_profile_credentials
    import capo_appflow.types.infor_nexus_connector_profile_credentials
    import capo_appflow.types.marketo_connector_profile_credentials
    import capo_appflow.types.pardot_connector_profile_credentials
    import capo_appflow.types.redshift_connector_profile_credentials
    import capo_appflow.types.salesforce_connector_profile_credentials
    import capo_appflow.types.sapo_data_connector_profile_credentials
    import capo_appflow.types.service_now_connector_profile_credentials
    import capo_appflow.types.singular_connector_profile_credentials
    import capo_appflow.types.slack_connector_profile_credentials
    import capo_appflow.types.snowflake_connector_profile_credentials
    import capo_appflow.types.trendmicro_connector_profile_credentials
    import capo_appflow.types.veeva_connector_profile_credentials
    import capo_appflow.types.zendesk_connector_profile_credentials


class ConnectorProfileCredentials(TypedDict, closed=True):
    amplitude: NotRequired[
        "capo_appflow.types.amplitude_connector_profile_credentials.AmplitudeConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Amplitude. </p>"""
    datadog: NotRequired[
        "capo_appflow.types.datadog_connector_profile_credentials.DatadogConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Datadog. </p>"""
    dynatrace: NotRequired[
        "capo_appflow.types.dynatrace_connector_profile_credentials.DynatraceConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Dynatrace. </p>"""
    google_analytics: NotRequired[
        "capo_appflow.types.google_analytics_connector_profile_credentials.GoogleAnalyticsConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Google Analytics. </p>"""
    honeycode: NotRequired[
        "capo_appflow.types.honeycode_connector_profile_credentials.HoneycodeConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Amazon Honeycode. </p>"""
    infor_nexus: NotRequired[
        "capo_appflow.types.infor_nexus_connector_profile_credentials.InforNexusConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Infor Nexus. </p>"""
    marketo: NotRequired[
        "capo_appflow.types.marketo_connector_profile_credentials.MarketoConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Marketo. </p>"""
    redshift: NotRequired[
        "capo_appflow.types.redshift_connector_profile_credentials.RedshiftConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Amazon Redshift. </p>"""
    salesforce: NotRequired[
        "capo_appflow.types.salesforce_connector_profile_credentials.SalesforceConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Salesforce. </p>"""
    service_now: NotRequired[
        "capo_appflow.types.service_now_connector_profile_credentials.ServiceNowConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using ServiceNow. </p>"""
    singular: NotRequired[
        "capo_appflow.types.singular_connector_profile_credentials.SingularConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Singular. </p>"""
    slack: NotRequired[
        "capo_appflow.types.slack_connector_profile_credentials.SlackConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Slack. </p>"""
    snowflake: NotRequired[
        "capo_appflow.types.snowflake_connector_profile_credentials.SnowflakeConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Snowflake. </p>"""
    trendmicro: NotRequired[
        "capo_appflow.types.trendmicro_connector_profile_credentials.TrendmicroConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Trend Micro. </p>"""
    veeva: NotRequired[
        "capo_appflow.types.veeva_connector_profile_credentials.VeevaConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Veeva. </p>"""
    zendesk: NotRequired[
        "capo_appflow.types.zendesk_connector_profile_credentials.ZendeskConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required when using Zendesk. </p>"""
    sapo_data: NotRequired[
        "capo_appflow.types.sapo_data_connector_profile_credentials.SAPODataConnectorProfileCredentials"
    ]
    custom_connector: NotRequired[
        "capo_appflow.types.custom_connector_profile_credentials.CustomConnectorProfileCredentials"
    ]
    pardot: NotRequired[
        "capo_appflow.types.pardot_connector_profile_credentials.PardotConnectorProfileCredentials"
    ]
    """<p>The connector-specific credentials required when using Salesforce Pardot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfileCredentials) -> dict:
    out: dict = {}
    if "amplitude" in value:
        import capo_appflow.types.amplitude_connector_profile_credentials

        out["Amplitude"] = (
            capo_appflow.types.amplitude_connector_profile_credentials.serialize_json(
                value["amplitude"]
            )
        )
    if "datadog" in value:
        import capo_appflow.types.datadog_connector_profile_credentials

        out["Datadog"] = (
            capo_appflow.types.datadog_connector_profile_credentials.serialize_json(
                value["datadog"]
            )
        )
    if "dynatrace" in value:
        import capo_appflow.types.dynatrace_connector_profile_credentials

        out["Dynatrace"] = (
            capo_appflow.types.dynatrace_connector_profile_credentials.serialize_json(
                value["dynatrace"]
            )
        )
    if "google_analytics" in value:
        import capo_appflow.types.google_analytics_connector_profile_credentials

        out["GoogleAnalytics"] = (
            capo_appflow.types.google_analytics_connector_profile_credentials.serialize_json(
                value["google_analytics"]
            )
        )
    if "honeycode" in value:
        import capo_appflow.types.honeycode_connector_profile_credentials

        out["Honeycode"] = (
            capo_appflow.types.honeycode_connector_profile_credentials.serialize_json(
                value["honeycode"]
            )
        )
    if "infor_nexus" in value:
        import capo_appflow.types.infor_nexus_connector_profile_credentials

        out["InforNexus"] = (
            capo_appflow.types.infor_nexus_connector_profile_credentials.serialize_json(
                value["infor_nexus"]
            )
        )
    if "marketo" in value:
        import capo_appflow.types.marketo_connector_profile_credentials

        out["Marketo"] = (
            capo_appflow.types.marketo_connector_profile_credentials.serialize_json(
                value["marketo"]
            )
        )
    if "redshift" in value:
        import capo_appflow.types.redshift_connector_profile_credentials

        out["Redshift"] = (
            capo_appflow.types.redshift_connector_profile_credentials.serialize_json(
                value["redshift"]
            )
        )
    if "salesforce" in value:
        import capo_appflow.types.salesforce_connector_profile_credentials

        out["Salesforce"] = (
            capo_appflow.types.salesforce_connector_profile_credentials.serialize_json(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import capo_appflow.types.service_now_connector_profile_credentials

        out["ServiceNow"] = (
            capo_appflow.types.service_now_connector_profile_credentials.serialize_json(
                value["service_now"]
            )
        )
    if "singular" in value:
        import capo_appflow.types.singular_connector_profile_credentials

        out["Singular"] = (
            capo_appflow.types.singular_connector_profile_credentials.serialize_json(
                value["singular"]
            )
        )
    if "slack" in value:
        import capo_appflow.types.slack_connector_profile_credentials

        out["Slack"] = (
            capo_appflow.types.slack_connector_profile_credentials.serialize_json(
                value["slack"]
            )
        )
    if "snowflake" in value:
        import capo_appflow.types.snowflake_connector_profile_credentials

        out["Snowflake"] = (
            capo_appflow.types.snowflake_connector_profile_credentials.serialize_json(
                value["snowflake"]
            )
        )
    if "trendmicro" in value:
        import capo_appflow.types.trendmicro_connector_profile_credentials

        out["Trendmicro"] = (
            capo_appflow.types.trendmicro_connector_profile_credentials.serialize_json(
                value["trendmicro"]
            )
        )
    if "veeva" in value:
        import capo_appflow.types.veeva_connector_profile_credentials

        out["Veeva"] = (
            capo_appflow.types.veeva_connector_profile_credentials.serialize_json(
                value["veeva"]
            )
        )
    if "zendesk" in value:
        import capo_appflow.types.zendesk_connector_profile_credentials

        out["Zendesk"] = (
            capo_appflow.types.zendesk_connector_profile_credentials.serialize_json(
                value["zendesk"]
            )
        )
    if "sapo_data" in value:
        import capo_appflow.types.sapo_data_connector_profile_credentials

        out["SAPOData"] = (
            capo_appflow.types.sapo_data_connector_profile_credentials.serialize_json(
                value["sapo_data"]
            )
        )
    if "custom_connector" in value:
        import capo_appflow.types.custom_connector_profile_credentials

        out["CustomConnector"] = (
            capo_appflow.types.custom_connector_profile_credentials.serialize_json(
                value["custom_connector"]
            )
        )
    if "pardot" in value:
        import capo_appflow.types.pardot_connector_profile_credentials

        out["Pardot"] = (
            capo_appflow.types.pardot_connector_profile_credentials.serialize_json(
                value["pardot"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorProfileCredentials:
    out: ConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("Amplitude") is not None:
        import capo_appflow.types.amplitude_connector_profile_credentials

        out["amplitude"] = (
            capo_appflow.types.amplitude_connector_profile_credentials.deserialize_json(
                data["Amplitude"]
            )
        )
    if data.get("Datadog") is not None:
        import capo_appflow.types.datadog_connector_profile_credentials

        out["datadog"] = (
            capo_appflow.types.datadog_connector_profile_credentials.deserialize_json(
                data["Datadog"]
            )
        )
    if data.get("Dynatrace") is not None:
        import capo_appflow.types.dynatrace_connector_profile_credentials

        out["dynatrace"] = (
            capo_appflow.types.dynatrace_connector_profile_credentials.deserialize_json(
                data["Dynatrace"]
            )
        )
    if data.get("GoogleAnalytics") is not None:
        import capo_appflow.types.google_analytics_connector_profile_credentials

        out["google_analytics"] = (
            capo_appflow.types.google_analytics_connector_profile_credentials.deserialize_json(
                data["GoogleAnalytics"]
            )
        )
    if data.get("Honeycode") is not None:
        import capo_appflow.types.honeycode_connector_profile_credentials

        out["honeycode"] = (
            capo_appflow.types.honeycode_connector_profile_credentials.deserialize_json(
                data["Honeycode"]
            )
        )
    if data.get("InforNexus") is not None:
        import capo_appflow.types.infor_nexus_connector_profile_credentials

        out["infor_nexus"] = (
            capo_appflow.types.infor_nexus_connector_profile_credentials.deserialize_json(
                data["InforNexus"]
            )
        )
    if data.get("Marketo") is not None:
        import capo_appflow.types.marketo_connector_profile_credentials

        out["marketo"] = (
            capo_appflow.types.marketo_connector_profile_credentials.deserialize_json(
                data["Marketo"]
            )
        )
    if data.get("Redshift") is not None:
        import capo_appflow.types.redshift_connector_profile_credentials

        out["redshift"] = (
            capo_appflow.types.redshift_connector_profile_credentials.deserialize_json(
                data["Redshift"]
            )
        )
    if data.get("Salesforce") is not None:
        import capo_appflow.types.salesforce_connector_profile_credentials

        out["salesforce"] = (
            capo_appflow.types.salesforce_connector_profile_credentials.deserialize_json(
                data["Salesforce"]
            )
        )
    if data.get("ServiceNow") is not None:
        import capo_appflow.types.service_now_connector_profile_credentials

        out["service_now"] = (
            capo_appflow.types.service_now_connector_profile_credentials.deserialize_json(
                data["ServiceNow"]
            )
        )
    if data.get("Singular") is not None:
        import capo_appflow.types.singular_connector_profile_credentials

        out["singular"] = (
            capo_appflow.types.singular_connector_profile_credentials.deserialize_json(
                data["Singular"]
            )
        )
    if data.get("Slack") is not None:
        import capo_appflow.types.slack_connector_profile_credentials

        out["slack"] = (
            capo_appflow.types.slack_connector_profile_credentials.deserialize_json(
                data["Slack"]
            )
        )
    if data.get("Snowflake") is not None:
        import capo_appflow.types.snowflake_connector_profile_credentials

        out["snowflake"] = (
            capo_appflow.types.snowflake_connector_profile_credentials.deserialize_json(
                data["Snowflake"]
            )
        )
    if data.get("Trendmicro") is not None:
        import capo_appflow.types.trendmicro_connector_profile_credentials

        out["trendmicro"] = (
            capo_appflow.types.trendmicro_connector_profile_credentials.deserialize_json(
                data["Trendmicro"]
            )
        )
    if data.get("Veeva") is not None:
        import capo_appflow.types.veeva_connector_profile_credentials

        out["veeva"] = (
            capo_appflow.types.veeva_connector_profile_credentials.deserialize_json(
                data["Veeva"]
            )
        )
    if data.get("Zendesk") is not None:
        import capo_appflow.types.zendesk_connector_profile_credentials

        out["zendesk"] = (
            capo_appflow.types.zendesk_connector_profile_credentials.deserialize_json(
                data["Zendesk"]
            )
        )
    if data.get("SAPOData") is not None:
        import capo_appflow.types.sapo_data_connector_profile_credentials

        out["sapo_data"] = (
            capo_appflow.types.sapo_data_connector_profile_credentials.deserialize_json(
                data["SAPOData"]
            )
        )
    if data.get("CustomConnector") is not None:
        import capo_appflow.types.custom_connector_profile_credentials

        out["custom_connector"] = (
            capo_appflow.types.custom_connector_profile_credentials.deserialize_json(
                data["CustomConnector"]
            )
        )
    if data.get("Pardot") is not None:
        import capo_appflow.types.pardot_connector_profile_credentials

        out["pardot"] = (
            capo_appflow.types.pardot_connector_profile_credentials.deserialize_json(
                data["Pardot"]
            )
        )
    return out


def redact_sensitive(value: ConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "amplitude" in value:
        import capo_appflow.types.amplitude_connector_profile_credentials

        out["amplitude"] = (
            capo_appflow.types.amplitude_connector_profile_credentials.redact_sensitive(
                value["amplitude"]
            )
        )
    if "datadog" in value:
        import capo_appflow.types.datadog_connector_profile_credentials

        out["datadog"] = (
            capo_appflow.types.datadog_connector_profile_credentials.redact_sensitive(
                value["datadog"]
            )
        )
    if "google_analytics" in value:
        import capo_appflow.types.google_analytics_connector_profile_credentials

        out["google_analytics"] = (
            capo_appflow.types.google_analytics_connector_profile_credentials.redact_sensitive(
                value["google_analytics"]
            )
        )
    if "honeycode" in value:
        import capo_appflow.types.honeycode_connector_profile_credentials

        out["honeycode"] = (
            capo_appflow.types.honeycode_connector_profile_credentials.redact_sensitive(
                value["honeycode"]
            )
        )
    if "infor_nexus" in value:
        import capo_appflow.types.infor_nexus_connector_profile_credentials

        out["infor_nexus"] = (
            capo_appflow.types.infor_nexus_connector_profile_credentials.redact_sensitive(
                value["infor_nexus"]
            )
        )
    if "marketo" in value:
        import capo_appflow.types.marketo_connector_profile_credentials

        out["marketo"] = (
            capo_appflow.types.marketo_connector_profile_credentials.redact_sensitive(
                value["marketo"]
            )
        )
    if "redshift" in value:
        import capo_appflow.types.redshift_connector_profile_credentials

        out["redshift"] = (
            capo_appflow.types.redshift_connector_profile_credentials.redact_sensitive(
                value["redshift"]
            )
        )
    if "salesforce" in value:
        import capo_appflow.types.salesforce_connector_profile_credentials

        out["salesforce"] = (
            capo_appflow.types.salesforce_connector_profile_credentials.redact_sensitive(
                value["salesforce"]
            )
        )
    if "service_now" in value:
        import capo_appflow.types.service_now_connector_profile_credentials

        out["service_now"] = (
            capo_appflow.types.service_now_connector_profile_credentials.redact_sensitive(
                value["service_now"]
            )
        )
    if "singular" in value:
        import capo_appflow.types.singular_connector_profile_credentials

        out["singular"] = (
            capo_appflow.types.singular_connector_profile_credentials.redact_sensitive(
                value["singular"]
            )
        )
    if "slack" in value:
        import capo_appflow.types.slack_connector_profile_credentials

        out["slack"] = (
            capo_appflow.types.slack_connector_profile_credentials.redact_sensitive(
                value["slack"]
            )
        )
    if "snowflake" in value:
        import capo_appflow.types.snowflake_connector_profile_credentials

        out["snowflake"] = (
            capo_appflow.types.snowflake_connector_profile_credentials.redact_sensitive(
                value["snowflake"]
            )
        )
    if "trendmicro" in value:
        import capo_appflow.types.trendmicro_connector_profile_credentials

        out["trendmicro"] = (
            capo_appflow.types.trendmicro_connector_profile_credentials.redact_sensitive(
                value["trendmicro"]
            )
        )
    if "veeva" in value:
        import capo_appflow.types.veeva_connector_profile_credentials

        out["veeva"] = (
            capo_appflow.types.veeva_connector_profile_credentials.redact_sensitive(
                value["veeva"]
            )
        )
    if "zendesk" in value:
        import capo_appflow.types.zendesk_connector_profile_credentials

        out["zendesk"] = (
            capo_appflow.types.zendesk_connector_profile_credentials.redact_sensitive(
                value["zendesk"]
            )
        )
    if "sapo_data" in value:
        import capo_appflow.types.sapo_data_connector_profile_credentials

        out["sapo_data"] = (
            capo_appflow.types.sapo_data_connector_profile_credentials.redact_sensitive(
                value["sapo_data"]
            )
        )
    if "custom_connector" in value:
        import capo_appflow.types.custom_connector_profile_credentials

        out["custom_connector"] = (
            capo_appflow.types.custom_connector_profile_credentials.redact_sensitive(
                value["custom_connector"]
            )
        )
    if "pardot" in value:
        import capo_appflow.types.pardot_connector_profile_credentials

        out["pardot"] = (
            capo_appflow.types.pardot_connector_profile_credentials.redact_sensitive(
                value["pardot"]
            )
        )
    return out
