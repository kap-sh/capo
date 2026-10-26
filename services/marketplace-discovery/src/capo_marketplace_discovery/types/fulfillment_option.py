"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FulfillmentOption``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError, SerializationError
from capo_marketplace_discovery.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.amazon_machine_image_fulfillment_option
    import capo_marketplace_discovery.types.api_fulfillment_option
    import capo_marketplace_discovery.types.cloud_formation_fulfillment_option
    import capo_marketplace_discovery.types.container_fulfillment_option
    import capo_marketplace_discovery.types.data_exchange_fulfillment_option
    import capo_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option
    import capo_marketplace_discovery.types.eks_add_on_fulfillment_option
    import capo_marketplace_discovery.types.helm_fulfillment_option
    import capo_marketplace_discovery.types.professional_services_fulfillment_option
    import capo_marketplace_discovery.types.saas_fulfillment_option
    import capo_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option
    import capo_marketplace_discovery.types.sage_maker_model_fulfillment_option


class _FulfillmentOption_amazonMachineImageFulfillmentOption(TypedDict, closed=True):
    amazonMachineImageFulfillmentOption: "capo_marketplace_discovery.types.amazon_machine_image_fulfillment_option.AmazonMachineImageFulfillmentOption"


class _FulfillmentOption_apiFulfillmentOption(TypedDict, closed=True):
    apiFulfillmentOption: (
        "capo_marketplace_discovery.types.api_fulfillment_option.ApiFulfillmentOption"
    )


class _FulfillmentOption_cloudFormationFulfillmentOption(TypedDict, closed=True):
    cloudFormationFulfillmentOption: "capo_marketplace_discovery.types.cloud_formation_fulfillment_option.CloudFormationFulfillmentOption"


class _FulfillmentOption_containerFulfillmentOption(TypedDict, closed=True):
    containerFulfillmentOption: "capo_marketplace_discovery.types.container_fulfillment_option.ContainerFulfillmentOption"


class _FulfillmentOption_helmFulfillmentOption(TypedDict, closed=True):
    helmFulfillmentOption: (
        "capo_marketplace_discovery.types.helm_fulfillment_option.HelmFulfillmentOption"
    )


class _FulfillmentOption_eksAddOnFulfillmentOption(TypedDict, closed=True):
    eksAddOnFulfillmentOption: "capo_marketplace_discovery.types.eks_add_on_fulfillment_option.EksAddOnFulfillmentOption"


class _FulfillmentOption_ec2ImageBuilderComponentFulfillmentOption(
    TypedDict, closed=True
):
    ec2ImageBuilderComponentFulfillmentOption: "capo_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option.Ec2ImageBuilderComponentFulfillmentOption"


class _FulfillmentOption_dataExchangeFulfillmentOption(TypedDict, closed=True):
    dataExchangeFulfillmentOption: "capo_marketplace_discovery.types.data_exchange_fulfillment_option.DataExchangeFulfillmentOption"


class _FulfillmentOption_professionalServicesFulfillmentOption(TypedDict, closed=True):
    professionalServicesFulfillmentOption: "capo_marketplace_discovery.types.professional_services_fulfillment_option.ProfessionalServicesFulfillmentOption"


class _FulfillmentOption_saasFulfillmentOption(TypedDict, closed=True):
    saasFulfillmentOption: (
        "capo_marketplace_discovery.types.saas_fulfillment_option.SaasFulfillmentOption"
    )


class _FulfillmentOption_sageMakerAlgorithmFulfillmentOption(TypedDict, closed=True):
    sageMakerAlgorithmFulfillmentOption: "capo_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option.SageMakerAlgorithmFulfillmentOption"


class _FulfillmentOption_sageMakerModelFulfillmentOption(TypedDict, closed=True):
    sageMakerModelFulfillmentOption: "capo_marketplace_discovery.types.sage_maker_model_fulfillment_option.SageMakerModelFulfillmentOption"


FulfillmentOption: TypeAlias = (
    _FulfillmentOption_amazonMachineImageFulfillmentOption
    | _FulfillmentOption_apiFulfillmentOption
    | _FulfillmentOption_cloudFormationFulfillmentOption
    | _FulfillmentOption_containerFulfillmentOption
    | _FulfillmentOption_helmFulfillmentOption
    | _FulfillmentOption_eksAddOnFulfillmentOption
    | _FulfillmentOption_ec2ImageBuilderComponentFulfillmentOption
    | _FulfillmentOption_dataExchangeFulfillmentOption
    | _FulfillmentOption_professionalServicesFulfillmentOption
    | _FulfillmentOption_saasFulfillmentOption
    | _FulfillmentOption_sageMakerAlgorithmFulfillmentOption
    | _FulfillmentOption_sageMakerModelFulfillmentOption
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentOption) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FulfillmentOption: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "amazonMachineImageFulfillmentOption" in value:
        import capo_marketplace_discovery.types.amazon_machine_image_fulfillment_option

        return {
            "amazonMachineImageFulfillmentOption": capo_marketplace_discovery.types.amazon_machine_image_fulfillment_option.serialize_json(
                value["amazonMachineImageFulfillmentOption"]
            )
        }
    elif "apiFulfillmentOption" in value:
        import capo_marketplace_discovery.types.api_fulfillment_option

        return {
            "apiFulfillmentOption": capo_marketplace_discovery.types.api_fulfillment_option.serialize_json(
                value["apiFulfillmentOption"]
            )
        }
    elif "cloudFormationFulfillmentOption" in value:
        import capo_marketplace_discovery.types.cloud_formation_fulfillment_option

        return {
            "cloudFormationFulfillmentOption": capo_marketplace_discovery.types.cloud_formation_fulfillment_option.serialize_json(
                value["cloudFormationFulfillmentOption"]
            )
        }
    elif "containerFulfillmentOption" in value:
        import capo_marketplace_discovery.types.container_fulfillment_option

        return {
            "containerFulfillmentOption": capo_marketplace_discovery.types.container_fulfillment_option.serialize_json(
                value["containerFulfillmentOption"]
            )
        }
    elif "helmFulfillmentOption" in value:
        import capo_marketplace_discovery.types.helm_fulfillment_option

        return {
            "helmFulfillmentOption": capo_marketplace_discovery.types.helm_fulfillment_option.serialize_json(
                value["helmFulfillmentOption"]
            )
        }
    elif "eksAddOnFulfillmentOption" in value:
        import capo_marketplace_discovery.types.eks_add_on_fulfillment_option

        return {
            "eksAddOnFulfillmentOption": capo_marketplace_discovery.types.eks_add_on_fulfillment_option.serialize_json(
                value["eksAddOnFulfillmentOption"]
            )
        }
    elif "ec2ImageBuilderComponentFulfillmentOption" in value:
        import capo_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option

        return {
            "ec2ImageBuilderComponentFulfillmentOption": capo_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option.serialize_json(
                value["ec2ImageBuilderComponentFulfillmentOption"]
            )
        }
    elif "dataExchangeFulfillmentOption" in value:
        import capo_marketplace_discovery.types.data_exchange_fulfillment_option

        return {
            "dataExchangeFulfillmentOption": capo_marketplace_discovery.types.data_exchange_fulfillment_option.serialize_json(
                value["dataExchangeFulfillmentOption"]
            )
        }
    elif "professionalServicesFulfillmentOption" in value:
        import capo_marketplace_discovery.types.professional_services_fulfillment_option

        return {
            "professionalServicesFulfillmentOption": capo_marketplace_discovery.types.professional_services_fulfillment_option.serialize_json(
                value["professionalServicesFulfillmentOption"]
            )
        }
    elif "saasFulfillmentOption" in value:
        import capo_marketplace_discovery.types.saas_fulfillment_option

        return {
            "saasFulfillmentOption": capo_marketplace_discovery.types.saas_fulfillment_option.serialize_json(
                value["saasFulfillmentOption"]
            )
        }
    elif "sageMakerAlgorithmFulfillmentOption" in value:
        import capo_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option

        return {
            "sageMakerAlgorithmFulfillmentOption": capo_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option.serialize_json(
                value["sageMakerAlgorithmFulfillmentOption"]
            )
        }
    elif "sageMakerModelFulfillmentOption" in value:
        import capo_marketplace_discovery.types.sage_maker_model_fulfillment_option

        return {
            "sageMakerModelFulfillmentOption": capo_marketplace_discovery.types.sage_maker_model_fulfillment_option.serialize_json(
                value["sageMakerModelFulfillmentOption"]
            )
        }
    else:
        raise SerializationError("FulfillmentOption: no variant present")


def deserialize_json(data: dict) -> FulfillmentOption:
    if data.get("amazonMachineImageFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.amazon_machine_image_fulfillment_option

        return {
            "amazonMachineImageFulfillmentOption": capo_marketplace_discovery.types.amazon_machine_image_fulfillment_option.deserialize_json(
                data["amazonMachineImageFulfillmentOption"]
            )
        }
    elif data.get("apiFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.api_fulfillment_option

        return {
            "apiFulfillmentOption": capo_marketplace_discovery.types.api_fulfillment_option.deserialize_json(
                data["apiFulfillmentOption"]
            )
        }
    elif data.get("cloudFormationFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.cloud_formation_fulfillment_option

        return {
            "cloudFormationFulfillmentOption": capo_marketplace_discovery.types.cloud_formation_fulfillment_option.deserialize_json(
                data["cloudFormationFulfillmentOption"]
            )
        }
    elif data.get("containerFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.container_fulfillment_option

        return {
            "containerFulfillmentOption": capo_marketplace_discovery.types.container_fulfillment_option.deserialize_json(
                data["containerFulfillmentOption"]
            )
        }
    elif data.get("helmFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.helm_fulfillment_option

        return {
            "helmFulfillmentOption": capo_marketplace_discovery.types.helm_fulfillment_option.deserialize_json(
                data["helmFulfillmentOption"]
            )
        }
    elif data.get("eksAddOnFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.eks_add_on_fulfillment_option

        return {
            "eksAddOnFulfillmentOption": capo_marketplace_discovery.types.eks_add_on_fulfillment_option.deserialize_json(
                data["eksAddOnFulfillmentOption"]
            )
        }
    elif data.get("ec2ImageBuilderComponentFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option

        return {
            "ec2ImageBuilderComponentFulfillmentOption": capo_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option.deserialize_json(
                data["ec2ImageBuilderComponentFulfillmentOption"]
            )
        }
    elif data.get("dataExchangeFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.data_exchange_fulfillment_option

        return {
            "dataExchangeFulfillmentOption": capo_marketplace_discovery.types.data_exchange_fulfillment_option.deserialize_json(
                data["dataExchangeFulfillmentOption"]
            )
        }
    elif data.get("professionalServicesFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.professional_services_fulfillment_option

        return {
            "professionalServicesFulfillmentOption": capo_marketplace_discovery.types.professional_services_fulfillment_option.deserialize_json(
                data["professionalServicesFulfillmentOption"]
            )
        }
    elif data.get("saasFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.saas_fulfillment_option

        return {
            "saasFulfillmentOption": capo_marketplace_discovery.types.saas_fulfillment_option.deserialize_json(
                data["saasFulfillmentOption"]
            )
        }
    elif data.get("sageMakerAlgorithmFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option

        return {
            "sageMakerAlgorithmFulfillmentOption": capo_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option.deserialize_json(
                data["sageMakerAlgorithmFulfillmentOption"]
            )
        }
    elif data.get("sageMakerModelFulfillmentOption") is not None:
        import capo_marketplace_discovery.types.sage_maker_model_fulfillment_option

        return {
            "sageMakerModelFulfillmentOption": capo_marketplace_discovery.types.sage_maker_model_fulfillment_option.deserialize_json(
                data["sageMakerModelFulfillmentOption"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FulfillmentOption: no recognized variant key")
