"""Generated from Smithy shape ``com.amazonaws.sagemaker#VariantProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.variant_property_type


class VariantProperty(TypedDict, closed=True):
    variant_property_type: NotRequired[
        "capo_sagemaker.types.variant_property_type.VariantPropertyType"
    ]
    """<p>The type of variant property. The supported values are:</p> <ul> <li> <p> <code>DesiredInstanceCount</code>: Overrides the existing variant instance counts using the <code>InitialInstanceCount</code> values in the <code>ProductionVariants</code> of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html">CreateEndpointConfig</a>.</p> </li> <li> <p> <code>DesiredWeight</code>: Overrides the existing variant weights using the <code>InitialVariantWeight</code> values in the <code>ProductionVariants</code> of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html">CreateEndpointConfig</a>.</p> </li> <li> <p> <code>DataCaptureConfig</code>: (Not currently supported.)</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariantProperty) -> dict:
    out: dict = {}
    if "variant_property_type" in value:
        import capo_sagemaker.types.variant_property_type

        out["VariantPropertyType"] = (
            capo_sagemaker.types.variant_property_type.serialize_aws_json_1_1(
                value["variant_property_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VariantProperty:
    out: VariantProperty = {}  # type: ignore[typeddict-item]
    if data.get("VariantPropertyType") is not None:
        import capo_sagemaker.types.variant_property_type

        out["variant_property_type"] = (
            capo_sagemaker.types.variant_property_type.deserialize_aws_json_1_1(
                data["VariantPropertyType"]
            )
        )
    return out
