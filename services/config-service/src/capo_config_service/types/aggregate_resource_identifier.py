"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateResourceIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region
    import capo_config_service.types.resource_id
    import capo_config_service.types.resource_name
    import capo_config_service.types.resource_type


class AggregateResourceIdentifier(TypedDict, closed=True):
    source_account_id: "capo_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of the source account.</p>"""
    source_region: "capo_config_service.types.aws_region.AwsRegion"
    """<p>The source region where data is aggregated.</p>"""
    resource_id: "capo_config_service.types.resource_id.ResourceId"
    """<p>The ID of the Amazon Web Services resource.</p>"""
    resource_type: "capo_config_service.types.resource_type.ResourceType"
    """<p>The type of the Amazon Web Services resource.</p>"""
    resource_name: NotRequired["capo_config_service.types.resource_name.ResourceName"]
    """<p>The name of the Amazon Web Services resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateResourceIdentifier) -> dict:
    out: dict = {}
    out["SourceAccountId"] = value["source_account_id"]
    out["SourceRegion"] = value["source_region"]
    out["ResourceId"] = value["resource_id"]
    import capo_config_service.types.resource_type

    out["ResourceType"] = (
        capo_config_service.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateResourceIdentifier:
    out: AggregateResourceIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("SourceAccountId") is not None:
        out["source_account_id"] = data["SourceAccountId"]
    else:
        out["source_account_id"] = ""
    if data.get("SourceRegion") is not None:
        out["source_region"] = data["SourceRegion"]
    else:
        out["source_region"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceType") is not None:
        import capo_config_service.types.resource_type

        out["resource_type"] = (
            capo_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_config_service.types.resource_type.ResourceType", ""
        )
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    return out
