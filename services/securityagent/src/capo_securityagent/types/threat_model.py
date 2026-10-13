"""Generated from Smithy shape ``com.amazonaws.securityagent#ThreatModel``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.assets
    import capo_securityagent.types.cloud_watch_log
    import capo_securityagent.types.document_list
    import capo_securityagent.types.report_destination
    import capo_securityagent.types.service_role


class ThreatModel(TypedDict, closed=True):
    threat_model_id: "str"
    """<p>The unique identifier of the threat model.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the threat model.</p>"""
    title: "str"
    """<p>The title of the threat model.</p>"""
    description: NotRequired["str"]
    """<p>A description of the application or system being threat modeled.</p>"""
    assets: "capo_securityagent.types.assets.Assets"
    """<p>The assets included in the threat model.</p>"""
    scope_docs: NotRequired["capo_securityagent.types.document_list.DocumentList"]
    """<p>The scoped documents for the agent to focus on during threat modeling.</p>"""
    service_role: NotRequired["capo_securityagent.types.service_role.ServiceRole"]
    """<p>The IAM service role used for the threat model.</p>"""
    log_config: NotRequired["capo_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The CloudWatch Logs configuration for the threat model.</p>"""
    report_destination: NotRequired[
        "capo_securityagent.types.report_destination.ReportDestination"
    ]
    """<p>The destination for publishing scan reports to an integrated document provider.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat model was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat model was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatModel) -> dict:
    out: dict = {}
    out["threatModelId"] = value["threat_model_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
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
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ThreatModel:
    out: ThreatModel = {}  # type: ignore[typeddict-item]
    if data.get("threatModelId") is not None:
        out["threat_model_id"] = data["threatModelId"]
    else:
        raise DeserializationError("ThreatModel.threat_model_id required")
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("ThreatModel.agent_space_id required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        raise DeserializationError("ThreatModel.title required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("assets") is not None:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.deserialize_json(data["assets"])
    else:
        raise DeserializationError("ThreatModel.assets required")
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
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: ThreatModel) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assets" in value:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.redact_sensitive(
            value["assets"]
        )
    return out
