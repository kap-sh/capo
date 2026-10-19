"""Generated from Smithy shape ``com.amazonaws.drs#StartRecoveryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.start_recovery_request_source_servers
    import capo_drs.types.tags_map


class StartRecoveryRequest(TypedDict, closed=True):
    source_servers: "capo_drs.types.start_recovery_request_source_servers.StartRecoveryRequestSourceServers"
    """<p>The Source Servers that we want to start a Recovery Job for.</p>"""
    is_drill: NotRequired["bool"]
    """<p>Whether this Source Server Recovery operation is a drill or not.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>The tags to be associated with the Recovery Job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecoveryRequest) -> dict:
    out: dict = {}
    import capo_drs.types.start_recovery_request_source_servers

    out["sourceServers"] = (
        capo_drs.types.start_recovery_request_source_servers.serialize_json(
            value["source_servers"]
        )
    )
    if "is_drill" in value:
        out["isDrill"] = value["is_drill"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartRecoveryRequest:
    out: StartRecoveryRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServers") is not None:
        import capo_drs.types.start_recovery_request_source_servers

        out["source_servers"] = (
            capo_drs.types.start_recovery_request_source_servers.deserialize_json(
                data["sourceServers"]
            )
        )
    else:
        out["source_servers"] = []
    if data.get("isDrill") is not None:
        out["is_drill"] = data["isDrill"]
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: StartRecoveryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
