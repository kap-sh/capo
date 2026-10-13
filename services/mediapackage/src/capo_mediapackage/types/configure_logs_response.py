"""Generated from Smithy shape ``com.amazonaws.mediapackage#ConfigureLogsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.egress_access_logs
    import capo_mediapackage.types.hls_ingest
    import capo_mediapackage.types.ingress_access_logs
    import capo_mediapackage.types.tags


class ConfigureLogsResponse(TypedDict, closed=True):
    arn: NotRequired["capo_mediapackage.types.__string.__string"]
    """The Amazon Resource Name (ARN) assigned to the Channel."""
    created_at: NotRequired["capo_mediapackage.types.__string.__string"]
    """The date and time the Channel was created."""
    description: NotRequired["capo_mediapackage.types.__string.__string"]
    """A short text description of the Channel."""
    egress_access_logs: NotRequired[
        "capo_mediapackage.types.egress_access_logs.EgressAccessLogs"
    ]
    hls_ingest: NotRequired["capo_mediapackage.types.hls_ingest.HlsIngest"]
    id: NotRequired["capo_mediapackage.types.__string.__string"]
    """The ID of the Channel."""
    ingress_access_logs: NotRequired[
        "capo_mediapackage.types.ingress_access_logs.IngressAccessLogs"
    ]
    tags: NotRequired["capo_mediapackage.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "description" in value:
        out["description"] = value["description"]
    if "egress_access_logs" in value:
        import capo_mediapackage.types.egress_access_logs

        out["egressAccessLogs"] = (
            capo_mediapackage.types.egress_access_logs.serialize_json(
                value["egress_access_logs"]
            )
        )
    if "hls_ingest" in value:
        import capo_mediapackage.types.hls_ingest

        out["hlsIngest"] = capo_mediapackage.types.hls_ingest.serialize_json(
            value["hls_ingest"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "ingress_access_logs" in value:
        import capo_mediapackage.types.ingress_access_logs

        out["ingressAccessLogs"] = (
            capo_mediapackage.types.ingress_access_logs.serialize_json(
                value["ingress_access_logs"]
            )
        )
    if "tags" in value:
        import capo_mediapackage.types.tags

        out["tags"] = capo_mediapackage.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ConfigureLogsResponse:
    out: ConfigureLogsResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("egressAccessLogs") is not None:
        import capo_mediapackage.types.egress_access_logs

        out["egress_access_logs"] = (
            capo_mediapackage.types.egress_access_logs.deserialize_json(
                data["egressAccessLogs"]
            )
        )
    if data.get("hlsIngest") is not None:
        import capo_mediapackage.types.hls_ingest

        out["hls_ingest"] = capo_mediapackage.types.hls_ingest.deserialize_json(
            data["hlsIngest"]
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("ingressAccessLogs") is not None:
        import capo_mediapackage.types.ingress_access_logs

        out["ingress_access_logs"] = (
            capo_mediapackage.types.ingress_access_logs.deserialize_json(
                data["ingressAccessLogs"]
            )
        )
    if data.get("tags") is not None:
        import capo_mediapackage.types.tags

        out["tags"] = capo_mediapackage.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: ConfigureLogsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "hls_ingest" in value:
        import capo_mediapackage.types.hls_ingest

        out["hls_ingest"] = capo_mediapackage.types.hls_ingest.redact_sensitive(
            value["hls_ingest"]
        )
    return out
