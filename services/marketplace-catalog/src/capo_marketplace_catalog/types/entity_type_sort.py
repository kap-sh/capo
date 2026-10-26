"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityTypeSort``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_catalog.errors import DeserializationError, SerializationError
from capo_marketplace_catalog.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_product_sort
    import capo_marketplace_catalog.types.container_product_sort
    import capo_marketplace_catalog.types.data_product_sort
    import capo_marketplace_catalog.types.express_private_offer_configuration_sort
    import capo_marketplace_catalog.types.machine_learning_product_sort
    import capo_marketplace_catalog.types.offer_set_sort
    import capo_marketplace_catalog.types.offer_sort
    import capo_marketplace_catalog.types.resale_authorization_sort
    import capo_marketplace_catalog.types.saa_s_product_sort


class _EntityTypeSort_DataProductSort(TypedDict, closed=True):
    DataProductSort: "capo_marketplace_catalog.types.data_product_sort.DataProductSort"


class _EntityTypeSort_SaaSProductSort(TypedDict, closed=True):
    SaaSProductSort: "capo_marketplace_catalog.types.saa_s_product_sort.SaaSProductSort"


class _EntityTypeSort_AmiProductSort(TypedDict, closed=True):
    AmiProductSort: "capo_marketplace_catalog.types.ami_product_sort.AmiProductSort"


class _EntityTypeSort_OfferSort(TypedDict, closed=True):
    OfferSort: "capo_marketplace_catalog.types.offer_sort.OfferSort"


class _EntityTypeSort_ContainerProductSort(TypedDict, closed=True):
    ContainerProductSort: (
        "capo_marketplace_catalog.types.container_product_sort.ContainerProductSort"
    )


class _EntityTypeSort_ResaleAuthorizationSort(TypedDict, closed=True):
    ResaleAuthorizationSort: "capo_marketplace_catalog.types.resale_authorization_sort.ResaleAuthorizationSort"


class _EntityTypeSort_MachineLearningProductSort(TypedDict, closed=True):
    MachineLearningProductSort: "capo_marketplace_catalog.types.machine_learning_product_sort.MachineLearningProductSort"


class _EntityTypeSort_OfferSetSort(TypedDict, closed=True):
    OfferSetSort: "capo_marketplace_catalog.types.offer_set_sort.OfferSetSort"


class _EntityTypeSort_ExpressPrivateOfferConfigurationSort(TypedDict, closed=True):
    ExpressPrivateOfferConfigurationSort: "capo_marketplace_catalog.types.express_private_offer_configuration_sort.ExpressPrivateOfferConfigurationSort"


EntityTypeSort: TypeAlias = (
    _EntityTypeSort_DataProductSort
    | _EntityTypeSort_SaaSProductSort
    | _EntityTypeSort_AmiProductSort
    | _EntityTypeSort_OfferSort
    | _EntityTypeSort_ContainerProductSort
    | _EntityTypeSort_ResaleAuthorizationSort
    | _EntityTypeSort_MachineLearningProductSort
    | _EntityTypeSort_OfferSetSort
    | _EntityTypeSort_ExpressPrivateOfferConfigurationSort
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EntityTypeSort) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EntityTypeSort: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "DataProductSort" in value:
        import capo_marketplace_catalog.types.data_product_sort

        return {
            "DataProductSort": capo_marketplace_catalog.types.data_product_sort.serialize_json(
                value["DataProductSort"]
            )
        }
    elif "SaaSProductSort" in value:
        import capo_marketplace_catalog.types.saa_s_product_sort

        return {
            "SaaSProductSort": capo_marketplace_catalog.types.saa_s_product_sort.serialize_json(
                value["SaaSProductSort"]
            )
        }
    elif "AmiProductSort" in value:
        import capo_marketplace_catalog.types.ami_product_sort

        return {
            "AmiProductSort": capo_marketplace_catalog.types.ami_product_sort.serialize_json(
                value["AmiProductSort"]
            )
        }
    elif "OfferSort" in value:
        import capo_marketplace_catalog.types.offer_sort

        return {
            "OfferSort": capo_marketplace_catalog.types.offer_sort.serialize_json(
                value["OfferSort"]
            )
        }
    elif "ContainerProductSort" in value:
        import capo_marketplace_catalog.types.container_product_sort

        return {
            "ContainerProductSort": capo_marketplace_catalog.types.container_product_sort.serialize_json(
                value["ContainerProductSort"]
            )
        }
    elif "ResaleAuthorizationSort" in value:
        import capo_marketplace_catalog.types.resale_authorization_sort

        return {
            "ResaleAuthorizationSort": capo_marketplace_catalog.types.resale_authorization_sort.serialize_json(
                value["ResaleAuthorizationSort"]
            )
        }
    elif "MachineLearningProductSort" in value:
        import capo_marketplace_catalog.types.machine_learning_product_sort

        return {
            "MachineLearningProductSort": capo_marketplace_catalog.types.machine_learning_product_sort.serialize_json(
                value["MachineLearningProductSort"]
            )
        }
    elif "OfferSetSort" in value:
        import capo_marketplace_catalog.types.offer_set_sort

        return {
            "OfferSetSort": capo_marketplace_catalog.types.offer_set_sort.serialize_json(
                value["OfferSetSort"]
            )
        }
    elif "ExpressPrivateOfferConfigurationSort" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_sort

        return {
            "ExpressPrivateOfferConfigurationSort": capo_marketplace_catalog.types.express_private_offer_configuration_sort.serialize_json(
                value["ExpressPrivateOfferConfigurationSort"]
            )
        }
    else:
        raise SerializationError("EntityTypeSort: no variant present")


def deserialize_json(data: dict) -> EntityTypeSort:
    if data.get("DataProductSort") is not None:
        import capo_marketplace_catalog.types.data_product_sort

        return {
            "DataProductSort": capo_marketplace_catalog.types.data_product_sort.deserialize_json(
                data["DataProductSort"]
            )
        }
    elif data.get("SaaSProductSort") is not None:
        import capo_marketplace_catalog.types.saa_s_product_sort

        return {
            "SaaSProductSort": capo_marketplace_catalog.types.saa_s_product_sort.deserialize_json(
                data["SaaSProductSort"]
            )
        }
    elif data.get("AmiProductSort") is not None:
        import capo_marketplace_catalog.types.ami_product_sort

        return {
            "AmiProductSort": capo_marketplace_catalog.types.ami_product_sort.deserialize_json(
                data["AmiProductSort"]
            )
        }
    elif data.get("OfferSort") is not None:
        import capo_marketplace_catalog.types.offer_sort

        return {
            "OfferSort": capo_marketplace_catalog.types.offer_sort.deserialize_json(
                data["OfferSort"]
            )
        }
    elif data.get("ContainerProductSort") is not None:
        import capo_marketplace_catalog.types.container_product_sort

        return {
            "ContainerProductSort": capo_marketplace_catalog.types.container_product_sort.deserialize_json(
                data["ContainerProductSort"]
            )
        }
    elif data.get("ResaleAuthorizationSort") is not None:
        import capo_marketplace_catalog.types.resale_authorization_sort

        return {
            "ResaleAuthorizationSort": capo_marketplace_catalog.types.resale_authorization_sort.deserialize_json(
                data["ResaleAuthorizationSort"]
            )
        }
    elif data.get("MachineLearningProductSort") is not None:
        import capo_marketplace_catalog.types.machine_learning_product_sort

        return {
            "MachineLearningProductSort": capo_marketplace_catalog.types.machine_learning_product_sort.deserialize_json(
                data["MachineLearningProductSort"]
            )
        }
    elif data.get("OfferSetSort") is not None:
        import capo_marketplace_catalog.types.offer_set_sort

        return {
            "OfferSetSort": capo_marketplace_catalog.types.offer_set_sort.deserialize_json(
                data["OfferSetSort"]
            )
        }
    elif data.get("ExpressPrivateOfferConfigurationSort") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_sort

        return {
            "ExpressPrivateOfferConfigurationSort": capo_marketplace_catalog.types.express_private_offer_configuration_sort.deserialize_json(
                data["ExpressPrivateOfferConfigurationSort"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EntityTypeSort: no recognized variant key")
