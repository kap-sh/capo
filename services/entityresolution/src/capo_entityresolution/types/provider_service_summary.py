"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderServiceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.provider_service_arn
    import capo_entityresolution.types.provider_service_display_name
    import capo_entityresolution.types.service_type


class ProviderServiceSummary(TypedDict, closed=True):
    provider_service_arn: (
        "capo_entityresolution.types.provider_service_arn.ProviderServiceArn"
    )
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>providerService</code>.</p>"""
    provider_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the provider. This name is typically the company name.</p>"""
    provider_service_display_name: "capo_entityresolution.types.provider_service_display_name.ProviderServiceDisplayName"
    """<p>The display name of the provider service.</p>"""
    provider_service_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the product that the provider service provides.</p>"""
    provider_service_type: "capo_entityresolution.types.service_type.ServiceType"
    """<p>The type of provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderServiceSummary) -> dict:
    out: dict = {}
    out["providerServiceArn"] = value["provider_service_arn"]
    out["providerName"] = value["provider_name"]
    out["providerServiceDisplayName"] = value["provider_service_display_name"]
    out["providerServiceName"] = value["provider_service_name"]
    import capo_entityresolution.types.service_type

    out["providerServiceType"] = (
        capo_entityresolution.types.service_type.serialize_json(
            value["provider_service_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProviderServiceSummary:
    out: ProviderServiceSummary = {}  # type: ignore[typeddict-item]
    if data.get("providerServiceArn") is not None:
        out["provider_service_arn"] = data["providerServiceArn"]
    else:
        out["provider_service_arn"] = ""
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    else:
        out["provider_name"] = ""
    if data.get("providerServiceDisplayName") is not None:
        out["provider_service_display_name"] = data["providerServiceDisplayName"]
    else:
        out["provider_service_display_name"] = ""
    if data.get("providerServiceName") is not None:
        out["provider_service_name"] = data["providerServiceName"]
    else:
        out["provider_service_name"] = ""
    if data.get("providerServiceType") is not None:
        import capo_entityresolution.types.service_type

        out["provider_service_type"] = (
            capo_entityresolution.types.service_type.deserialize_json(
                data["providerServiceType"]
            )
        )
    else:
        import typing

        out["provider_service_type"] = typing.cast(
            "capo_entityresolution.types.service_type.ServiceType", ""
        )
    return out
