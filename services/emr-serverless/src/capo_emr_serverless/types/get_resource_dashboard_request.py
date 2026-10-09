"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetResourceDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.resource_id
    import capo_emr_serverless.types.resource_type


class GetResourceDashboardRequest(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application that the resource belongs to.</p>"""
    resource_id: "capo_emr_serverless.types.resource_id.ResourceId"
    """<p>The ID of the resource.</p>"""
    resource_type: "capo_emr_serverless.types.resource_type.ResourceType"
    """<p>The type of resource to access the dashboard for. Currently, only <code>Session</code> is supported.</p>"""
    access_system_profile_logs: NotRequired["bool"]
    """<p>Allows access to system profile logs for Lake Formation-enabled sessions. Default is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceDashboardRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceDashboardRequest:
    out: GetResourceDashboardRequest = {}  # type: ignore[typeddict-item]
    return out
