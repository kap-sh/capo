"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateIngestionStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_stream_detail


class CreateIngestionStreamResponse(TypedDict, closed=True):
    ingestion_stream_detail: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_detail.IngestionStreamDetail"
    ]
    """<p>Details about the created ingestion stream.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIngestionStreamResponse) -> dict:
    out: dict = {}
    if "ingestion_stream_detail" in value:
        import capo_opensearchserverless.types.ingestion_stream_detail

        out["ingestionStreamDetail"] = (
            capo_opensearchserverless.types.ingestion_stream_detail.serialize_aws_json_1_0(
                value["ingestion_stream_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIngestionStreamResponse:
    out: CreateIngestionStreamResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestionStreamDetail") is not None:
        import capo_opensearchserverless.types.ingestion_stream_detail

        out["ingestion_stream_detail"] = (
            capo_opensearchserverless.types.ingestion_stream_detail.deserialize_aws_json_1_0(
                data["ingestionStreamDetail"]
            )
        )
    return out
