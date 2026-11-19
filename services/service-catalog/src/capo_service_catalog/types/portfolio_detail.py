"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PortfolioDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.creation_time
    import capo_service_catalog.types.id
    import capo_service_catalog.types.portfolio_description
    import capo_service_catalog.types.portfolio_display_name
    import capo_service_catalog.types.provider_name
    import capo_service_catalog.types.resource_arn


class PortfolioDetail(TypedDict, closed=True):
    id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The portfolio identifier.</p>"""
    arn: NotRequired["capo_service_catalog.types.resource_arn.ResourceARN"]
    """<p>The ARN assigned to the portfolio.</p>"""
    display_name: NotRequired[
        "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
    ]
    """<p>The name to use for display purposes.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.portfolio_description.PortfolioDescription"
    ]
    """<p>The description of the portfolio.</p>"""
    created_time: NotRequired["capo_service_catalog.types.creation_time.CreationTime"]
    """<p>The UTC time stamp of the creation time.</p>"""
    provider_name: NotRequired["capo_service_catalog.types.provider_name.ProviderName"]
    """<p>The name of the portfolio provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortfolioDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_time" in value:
        import capo_service_catalog.types.creation_time

        out["CreatedTime"] = (
            capo_service_catalog.types.creation_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "provider_name" in value:
        out["ProviderName"] = value["provider_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PortfolioDetail:
    out: PortfolioDetail = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.creation_time

        out["created_time"] = (
            capo_service_catalog.types.creation_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if data.get("ProviderName") is not None:
        out["provider_name"] = data["ProviderName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PortfolioDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_time" in value:
        import capo_service_catalog.types.creation_time

        out["CreatedTime"] = capo_service_catalog.types.creation_time.serialize_cbor(
            value["created_time"]
        )
    if "provider_name" in value:
        out["ProviderName"] = value["provider_name"]
    return out


def deserialize_cbor(data: dict) -> PortfolioDetail:
    out: PortfolioDetail = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.creation_time

        out["created_time"] = capo_service_catalog.types.creation_time.deserialize_cbor(
            data["CreatedTime"]
        )
    if data.get("ProviderName") is not None:
        out["provider_name"] = data["ProviderName"]
    return out
