"""Generated from Smithy shape ``com.amazonaws.bedrock#MarketplaceModelEndpointSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.arn
    import capo_bedrock.types.model_source_identifier
    import capo_bedrock.types.status
    import capo_bedrock.types.timestamp


class MarketplaceModelEndpointSummary(TypedDict, closed=True):
    endpoint_arn: "capo_bedrock.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    model_source_identifier: (
        "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier"
    )
    """<p>The ARN of the model from Amazon Bedrock Marketplace that is deployed on this endpoint.</p>"""
    status: NotRequired["capo_bedrock.types.status.Status"]
    """<p>The overall status of the endpoint in Amazon Bedrock Marketplace.</p>"""
    status_message: NotRequired["str"]
    """<p>Additional information about the overall status, if available.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the endpoint was created.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the endpoint was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarketplaceModelEndpointSummary) -> dict:
    out: dict = {}
    out["endpointArn"] = value["endpoint_arn"]
    out["modelSourceIdentifier"] = value["model_source_identifier"]
    if "status" in value:
        import capo_bedrock.types.status

        out["status"] = capo_bedrock.types.status.serialize_json(value["status"])
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> MarketplaceModelEndpointSummary:
    out: MarketplaceModelEndpointSummary = {}  # type: ignore[typeddict-item]
    if data.get("endpointArn") is not None:
        out["endpoint_arn"] = data["endpointArn"]
    else:
        out["endpoint_arn"] = ""
    if data.get("modelSourceIdentifier") is not None:
        out["model_source_identifier"] = data["modelSourceIdentifier"]
    else:
        out["model_source_identifier"] = ""
    if data.get("status") is not None:
        import capo_bedrock.types.status

        out["status"] = capo_bedrock.types.status.deserialize_json(data["status"])
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
