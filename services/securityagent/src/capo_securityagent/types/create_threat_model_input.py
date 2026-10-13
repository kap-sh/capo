"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateThreatModelInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.assets
    import capo_securityagent.types.cloud_watch_log
    import capo_securityagent.types.document_list
    import capo_securityagent.types.report_destination
    import capo_securityagent.types.service_role


class CreateThreatModelInput(TypedDict, closed=True):
    title: "str"
    """<p>The title of the threat model.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space to create the threat model in.</p>"""
    description: NotRequired["str"]
    """<p>A description of the application or system being threat modeled.</p>"""
    assets: NotRequired["capo_securityagent.types.assets.Assets"]
    """<p>The assets to include in the threat model.</p>"""
    scope_docs: NotRequired["capo_securityagent.types.document_list.DocumentList"]
    """<p>The scoped documents for the agent to focus on during threat modeling.</p>"""
    service_role: "capo_securityagent.types.service_role.ServiceRole"
    """<p>The IAM service role to use for the threat model.</p>"""
    log_config: NotRequired["capo_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The CloudWatch Logs configuration for the threat model.</p>"""
    report_destination: NotRequired[
        "capo_securityagent.types.report_destination.ReportDestination"
    ]
    """<p>The destination for publishing scan reports to an integrated document provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThreatModelInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["agentSpaceId"] = value["agent_space_id"]
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


def deserialize_json(data: dict) -> CreateThreatModelInput:
    out: CreateThreatModelInput = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CreateThreatModelInput.title required")
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("CreateThreatModelInput.agent_space_id required")
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
    else:
        raise DeserializationError("CreateThreatModelInput.service_role required")
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


def redact_sensitive(value: CreateThreatModelInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assets" in value:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.redact_sensitive(
            value["assets"]
        )
    return out
