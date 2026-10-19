"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateEnrichmentJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.enrichment_job_configuration
    import capo_iotsitewise.types.workspace_name


class CreateEnrichmentJobRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the IoT SiteWise workspace containing the video data to analyze.</p>"""
    job_configuration: (
        "capo_iotsitewise.types.enrichment_job_configuration.EnrichmentJobConfiguration"
    )
    """<p>Configuration defining the type of enrichment analysis to perform and which video data to analyze. Currently supports eventDetection for generating embeddings from video data for semantic search.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>Optional unique token that makes the operation idempotent. If you submit the same request with the same token within the idempotency window, the service returns the original job without creating a duplicate. Use a UUID or timestamp-based token for each unique request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnrichmentJobRequest) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.enrichment_job_configuration

    out["jobConfiguration"] = (
        capo_iotsitewise.types.enrichment_job_configuration.serialize_json(
            value["job_configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateEnrichmentJobRequest:
    out: CreateEnrichmentJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobConfiguration") is not None:
        import capo_iotsitewise.types.enrichment_job_configuration

        out["job_configuration"] = (
            capo_iotsitewise.types.enrichment_job_configuration.deserialize_json(
                data["jobConfiguration"]
            )
        )
    else:
        import capo_iotsitewise.types._unknown

        out["job_configuration"] = capo_iotsitewise.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
