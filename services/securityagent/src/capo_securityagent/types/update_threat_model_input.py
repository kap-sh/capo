"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateThreatModelInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.assets
    import capo_securityagent.types.cloud_watch_log
    import capo_securityagent.types.document_list
    import capo_securityagent.types.report_destination
    import capo_securityagent.types.service_role


class UpdateThreatModelInput(TypedDict, closed=True):
    threat_model_id: "str"
    """<p>The unique identifier of the threat model to update.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the threat model.</p>"""
    title: NotRequired["str"]
    """<p>The updated title of the threat model.</p>"""
    description: NotRequired["str"]
    """<p>The updated description of the application or system being threat modeled.</p>"""
    assets: NotRequired["capo_securityagent.types.assets.Assets"]
    """<p>The updated assets for the threat model.</p>"""
    scope_docs: NotRequired["capo_securityagent.types.document_list.DocumentList"]
    """<p>The updated scoped documents for the agent to focus on during threat modeling.</p>"""
    service_role: NotRequired["capo_securityagent.types.service_role.ServiceRole"]
    """<p>The updated IAM service role for the threat model.</p>"""
    log_config: NotRequired["capo_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The updated CloudWatch Logs configuration for the threat model.</p>"""
    report_destination: NotRequired[
        "capo_securityagent.types.report_destination.ReportDestination"
    ]
    """<p>The destination for publishing scan reports to an integrated document provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThreatModelInput) -> dict:
    out: dict = {}
    out["threatModelId"] = value["threat_model_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "assets" in value:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.serialize_json(value["assets"])
    if "scope_docs" in value:
        import capo_securityagent.types.document_list

        out["scopeDocs"] = capo_securityagent.types.document_list.serialize_json(
            value["scope_docs"]
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "log_config" in value:
        import capo_securityagent.types.cloud_watch_log

        out["logConfig"] = capo_securityagent.types.cloud_watch_log.serialize_json(
            value["log_config"]
        )
    if "report_destination" in value:
        import capo_securityagent.types.report_destination

        out["reportDestination"] = (
            capo_securityagent.types.report_destination.serialize_json(
                value["report_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateThreatModelInput:
    out: UpdateThreatModelInput = {}  # type: ignore[typeddict-item]
    if data.get("threatModelId") is not None:
        out["threat_model_id"] = data["threatModelId"]
    else:
        raise DeserializationError("UpdateThreatModelInput.threat_model_id required")
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("UpdateThreatModelInput.agent_space_id required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("assets") is not None:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.deserialize_json(data["assets"])
    if data.get("scopeDocs") is not None:
        import capo_securityagent.types.document_list

        out["scope_docs"] = capo_securityagent.types.document_list.deserialize_json(
            data["scopeDocs"]
        )
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("logConfig") is not None:
        import capo_securityagent.types.cloud_watch_log

        out["log_config"] = capo_securityagent.types.cloud_watch_log.deserialize_json(
            data["logConfig"]
        )
    if data.get("reportDestination") is not None:
        import capo_securityagent.types.report_destination

        out["report_destination"] = (
            capo_securityagent.types.report_destination.deserialize_json(
                data["reportDestination"]
            )
        )
    return out


def redact_sensitive(value: UpdateThreatModelInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assets" in value:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.redact_sensitive(
            value["assets"]
        )
    return out
