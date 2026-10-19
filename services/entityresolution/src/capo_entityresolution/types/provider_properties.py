"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.intermediate_source_configuration
    import capo_entityresolution.types.provider_service_arn


class ProviderProperties(TypedDict, closed=True):
    provider_service_arn: (
        "capo_entityresolution.types.provider_service_arn.ProviderServiceArn"
    )
    """<p>The ARN of the provider service.</p>"""
    provider_configuration: NotRequired["object"]
    """<p>The required configuration fields to use with the provider service.</p>"""
    intermediate_source_configuration: NotRequired[
        "capo_entityresolution.types.intermediate_source_configuration.IntermediateSourceConfiguration"
    ]
    """<p>The Amazon S3 location that temporarily stores your data while it processes. Your information won't be saved permanently.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderProperties) -> dict:
    out: dict = {}
    out["providerServiceArn"] = value["provider_service_arn"]
    if "provider_configuration" in value:
        out["providerConfiguration"] = value["provider_configuration"]
    if "intermediate_source_configuration" in value:
        import capo_entityresolution.types.intermediate_source_configuration

        out["intermediateSourceConfiguration"] = (
            capo_entityresolution.types.intermediate_source_configuration.serialize_json(
                value["intermediate_source_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProviderProperties:
    out: ProviderProperties = {}  # type: ignore[typeddict-item]
    if data.get("providerServiceArn") is not None:
        out["provider_service_arn"] = data["providerServiceArn"]
    else:
        out["provider_service_arn"] = ""
    if data.get("providerConfiguration") is not None:
        out["provider_configuration"] = data["providerConfiguration"]
    if data.get("intermediateSourceConfiguration") is not None:
        import capo_entityresolution.types.intermediate_source_configuration

        out["intermediate_source_configuration"] = (
            capo_entityresolution.types.intermediate_source_configuration.deserialize_json(
                data["intermediateSourceConfiguration"]
            )
        )
    return out
