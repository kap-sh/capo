"""Generated from Smithy shape ``com.amazonaws.grafana#WorkspaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_grafana.types.authentication_summary
    import capo_grafana.types.description
    import capo_grafana.types.endpoint
    import capo_grafana.types.grafana_token
    import capo_grafana.types.grafana_version
    import capo_grafana.types.license_type
    import capo_grafana.types.notification_destinations_list
    import capo_grafana.types.tag_map
    import capo_grafana.types.workspace_id
    import capo_grafana.types.workspace_name
    import capo_grafana.types.workspace_status


class WorkspaceSummary(TypedDict, closed=True):
    created: "datetime.datetime"
    """<p>The date that the workspace was created.</p>"""
    description: NotRequired["capo_grafana.types.description.Description"]
    """<p>The customer-entered description of the workspace.</p>"""
    endpoint: "capo_grafana.types.endpoint.Endpoint"
    """<p>The URL endpoint to use to access the Grafana console in the workspace.</p>"""
    grafana_version: "capo_grafana.types.grafana_version.GrafanaVersion"
    """<p>The Grafana version that the workspace is running.</p>"""
    id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The unique ID of the workspace.</p>"""
    modified: "datetime.datetime"
    """<p>The most recent date that the workspace was modified.</p>"""
    name: NotRequired["capo_grafana.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""
    notification_destinations: NotRequired[
        "capo_grafana.types.notification_destinations_list.NotificationDestinationsList"
    ]
    """<p>The Amazon Web Services notification channels that Amazon Managed Grafana can automatically create IAM roles and permissions for, which allows Amazon Managed Grafana to use these channels.</p>"""
    status: "capo_grafana.types.workspace_status.WorkspaceStatus"
    """<p>The current status of the workspace.</p>"""
    authentication: "capo_grafana.types.authentication_summary.AuthenticationSummary"
    """<p>A structure containing information about the authentication methods used in the workspace.</p>"""
    tags: NotRequired["capo_grafana.types.tag_map.TagMap"]
    """<p>The list of tags associated with the workspace.</p>"""
    license_type: NotRequired["capo_grafana.types.license_type.LicenseType"]
    """<p>Specifies whether this workspace has a full Grafana Enterprise license.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>"""
    grafana_token: NotRequired["capo_grafana.types.grafana_token.GrafanaToken"]
    """<p>The token that ties this workspace to a Grafana Labs account. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise">Link your account with Grafana Labs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSummary) -> dict:
    out: dict = {}
    import capo_grafana.types._prelude.timestamp

    out["created"] = capo_grafana.types._prelude.timestamp.serialize_json(
        value["created"]
    )
    if "description" in value:
        out["description"] = value["description"]
    out["endpoint"] = value["endpoint"]
    out["grafanaVersion"] = value["grafana_version"]
    out["id"] = value["id"]
    import capo_grafana.types._prelude.timestamp

    out["modified"] = capo_grafana.types._prelude.timestamp.serialize_json(
        value["modified"]
    )
    if "name" in value:
        out["name"] = value["name"]
    if "notification_destinations" in value:
        import capo_grafana.types.notification_destinations_list

        out["notificationDestinations"] = (
            capo_grafana.types.notification_destinations_list.serialize_json(
                value["notification_destinations"]
            )
        )
    out["status"] = value["status"]
    import capo_grafana.types.authentication_summary

    out["authentication"] = capo_grafana.types.authentication_summary.serialize_json(
        value["authentication"]
    )
    if "tags" in value:
        import capo_grafana.types.tag_map

        out["tags"] = capo_grafana.types.tag_map.serialize_json(value["tags"])
    if "license_type" in value:
        out["licenseType"] = value["license_type"]
    if "grafana_token" in value:
        out["grafanaToken"] = value["grafana_token"]
    return out


def deserialize_json(data: dict) -> WorkspaceSummary:
    out: WorkspaceSummary = {}  # type: ignore[typeddict-item]
    if data.get("created") is not None:
        import capo_grafana.types._prelude.timestamp

        out["created"] = capo_grafana.types._prelude.timestamp.deserialize_json(
            data["created"]
        )
    else:
        raise DeserializationError("WorkspaceSummary.created required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("WorkspaceSummary.endpoint required")
    if data.get("grafanaVersion") is not None:
        out["grafana_version"] = data["grafanaVersion"]
    else:
        raise DeserializationError("WorkspaceSummary.grafana_version required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("WorkspaceSummary.id required")
    if data.get("modified") is not None:
        import capo_grafana.types._prelude.timestamp

        out["modified"] = capo_grafana.types._prelude.timestamp.deserialize_json(
            data["modified"]
        )
    else:
        raise DeserializationError("WorkspaceSummary.modified required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("notificationDestinations") is not None:
        import capo_grafana.types.notification_destinations_list

        out["notification_destinations"] = (
            capo_grafana.types.notification_destinations_list.deserialize_json(
                data["notificationDestinations"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("WorkspaceSummary.status required")
    if data.get("authentication") is not None:
        import capo_grafana.types.authentication_summary

        out["authentication"] = (
            capo_grafana.types.authentication_summary.deserialize_json(
                data["authentication"]
            )
        )
    else:
        raise DeserializationError("WorkspaceSummary.authentication required")
    if data.get("tags") is not None:
        import capo_grafana.types.tag_map

        out["tags"] = capo_grafana.types.tag_map.deserialize_json(data["tags"])
    if data.get("licenseType") is not None:
        out["license_type"] = data["licenseType"]
    if data.get("grafanaToken") is not None:
        out["grafana_token"] = data["grafanaToken"]
    return out
