"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityTypeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_catalog.errors import DeserializationError, SerializationError
from capo_marketplace_catalog.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_product_filters
    import capo_marketplace_catalog.types.container_product_filters
    import capo_marketplace_catalog.types.data_product_filters
    import capo_marketplace_catalog.types.express_private_offer_configuration_filters
    import capo_marketplace_catalog.types.machine_learning_product_filters
    import capo_marketplace_catalog.types.offer_filters
    import capo_marketplace_catalog.types.offer_set_filters
    import capo_marketplace_catalog.types.resale_authorization_filters
    import capo_marketplace_catalog.types.saa_s_product_filters
    import capo_marketplace_catalog.types.subsidiary_authorization_filters


class EntityTypeFiltersDataProductFiltersMember(TypedDict, closed=True):
    DataProductFilters: (
        "capo_marketplace_catalog.types.data_product_filters.DataProductFilters"
    )


class EntityTypeFiltersSaaSProductFiltersMember(TypedDict, closed=True):
    SaaSProductFilters: (
        "capo_marketplace_catalog.types.saa_s_product_filters.SaaSProductFilters"
    )


class EntityTypeFiltersAmiProductFiltersMember(TypedDict, closed=True):
    AmiProductFilters: (
        "capo_marketplace_catalog.types.ami_product_filters.AmiProductFilters"
    )


class EntityTypeFiltersOfferFiltersMember(TypedDict, closed=True):
    OfferFilters: "capo_marketplace_catalog.types.offer_filters.OfferFilters"


class EntityTypeFiltersContainerProductFiltersMember(TypedDict, closed=True):
    ContainerProductFilters: "capo_marketplace_catalog.types.container_product_filters.ContainerProductFilters"


class EntityTypeFiltersResaleAuthorizationFiltersMember(TypedDict, closed=True):
    ResaleAuthorizationFilters: "capo_marketplace_catalog.types.resale_authorization_filters.ResaleAuthorizationFilters"


class EntityTypeFiltersMachineLearningProductFiltersMember(TypedDict, closed=True):
    MachineLearningProductFilters: "capo_marketplace_catalog.types.machine_learning_product_filters.MachineLearningProductFilters"


class EntityTypeFiltersOfferSetFiltersMember(TypedDict, closed=True):
    OfferSetFilters: "capo_marketplace_catalog.types.offer_set_filters.OfferSetFilters"


class EntityTypeFiltersExpressPrivateOfferConfigurationFiltersMember(
    TypedDict, closed=True
):
    ExpressPrivateOfferConfigurationFilters: "capo_marketplace_catalog.types.express_private_offer_configuration_filters.ExpressPrivateOfferConfigurationFilters"


class EntityTypeFiltersSubsidiaryAuthorizationFiltersMember(TypedDict, closed=True):
    SubsidiaryAuthorizationFilters: "capo_marketplace_catalog.types.subsidiary_authorization_filters.SubsidiaryAuthorizationFilters"


EntityTypeFilters: TypeAlias = (
    EntityTypeFiltersDataProductFiltersMember
    | EntityTypeFiltersSaaSProductFiltersMember
    | EntityTypeFiltersAmiProductFiltersMember
    | EntityTypeFiltersOfferFiltersMember
    | EntityTypeFiltersContainerProductFiltersMember
    | EntityTypeFiltersResaleAuthorizationFiltersMember
    | EntityTypeFiltersMachineLearningProductFiltersMember
    | EntityTypeFiltersOfferSetFiltersMember
    | EntityTypeFiltersExpressPrivateOfferConfigurationFiltersMember
    | EntityTypeFiltersSubsidiaryAuthorizationFiltersMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EntityTypeFilters) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EntityTypeFilters: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "DataProductFilters" in value:
        import capo_marketplace_catalog.types.data_product_filters

        return {
            "DataProductFilters": capo_marketplace_catalog.types.data_product_filters.serialize_json(
                value["DataProductFilters"]
            )
        }
    elif "SaaSProductFilters" in value:
        import capo_marketplace_catalog.types.saa_s_product_filters

        return {
            "SaaSProductFilters": capo_marketplace_catalog.types.saa_s_product_filters.serialize_json(
                value["SaaSProductFilters"]
            )
        }
    elif "AmiProductFilters" in value:
        import capo_marketplace_catalog.types.ami_product_filters

        return {
            "AmiProductFilters": capo_marketplace_catalog.types.ami_product_filters.serialize_json(
                value["AmiProductFilters"]
            )
        }
    elif "OfferFilters" in value:
        import capo_marketplace_catalog.types.offer_filters

        return {
            "OfferFilters": capo_marketplace_catalog.types.offer_filters.serialize_json(
                value["OfferFilters"]
            )
        }
    elif "ContainerProductFilters" in value:
        import capo_marketplace_catalog.types.container_product_filters

        return {
            "ContainerProductFilters": capo_marketplace_catalog.types.container_product_filters.serialize_json(
                value["ContainerProductFilters"]
            )
        }
    elif "ResaleAuthorizationFilters" in value:
        import capo_marketplace_catalog.types.resale_authorization_filters

        return {
            "ResaleAuthorizationFilters": capo_marketplace_catalog.types.resale_authorization_filters.serialize_json(
                value["ResaleAuthorizationFilters"]
            )
        }
    elif "MachineLearningProductFilters" in value:
        import capo_marketplace_catalog.types.machine_learning_product_filters

        return {
            "MachineLearningProductFilters": capo_marketplace_catalog.types.machine_learning_product_filters.serialize_json(
                value["MachineLearningProductFilters"]
            )
        }
    elif "OfferSetFilters" in value:
        import capo_marketplace_catalog.types.offer_set_filters

        return {
            "OfferSetFilters": capo_marketplace_catalog.types.offer_set_filters.serialize_json(
                value["OfferSetFilters"]
            )
        }
    elif "ExpressPrivateOfferConfigurationFilters" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_filters

        return {
            "ExpressPrivateOfferConfigurationFilters": capo_marketplace_catalog.types.express_private_offer_configuration_filters.serialize_json(
                value["ExpressPrivateOfferConfigurationFilters"]
            )
        }
    elif "SubsidiaryAuthorizationFilters" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_filters

        return {
            "SubsidiaryAuthorizationFilters": capo_marketplace_catalog.types.subsidiary_authorization_filters.serialize_json(
                value["SubsidiaryAuthorizationFilters"]
            )
        }
    else:
        raise SerializationError("EntityTypeFilters: no variant present")


def deserialize_json(data: dict) -> EntityTypeFilters:
    if data.get("DataProductFilters") is not None:
        import capo_marketplace_catalog.types.data_product_filters

        return {
            "DataProductFilters": capo_marketplace_catalog.types.data_product_filters.deserialize_json(
                data["DataProductFilters"]
            )
        }
    elif data.get("SaaSProductFilters") is not None:
        import capo_marketplace_catalog.types.saa_s_product_filters

        return {
            "SaaSProductFilters": capo_marketplace_catalog.types.saa_s_product_filters.deserialize_json(
                data["SaaSProductFilters"]
            )
        }
    elif data.get("AmiProductFilters") is not None:
        import capo_marketplace_catalog.types.ami_product_filters

        return {
            "AmiProductFilters": capo_marketplace_catalog.types.ami_product_filters.deserialize_json(
                data["AmiProductFilters"]
            )
        }
    elif data.get("OfferFilters") is not None:
        import capo_marketplace_catalog.types.offer_filters

        return {
            "OfferFilters": capo_marketplace_catalog.types.offer_filters.deserialize_json(
                data["OfferFilters"]
            )
        }
    elif data.get("ContainerProductFilters") is not None:
        import capo_marketplace_catalog.types.container_product_filters

        return {
            "ContainerProductFilters": capo_marketplace_catalog.types.container_product_filters.deserialize_json(
                data["ContainerProductFilters"]
            )
        }
    elif data.get("ResaleAuthorizationFilters") is not None:
        import capo_marketplace_catalog.types.resale_authorization_filters

        return {
            "ResaleAuthorizationFilters": capo_marketplace_catalog.types.resale_authorization_filters.deserialize_json(
                data["ResaleAuthorizationFilters"]
            )
        }
    elif data.get("MachineLearningProductFilters") is not None:
        import capo_marketplace_catalog.types.machine_learning_product_filters

        return {
            "MachineLearningProductFilters": capo_marketplace_catalog.types.machine_learning_product_filters.deserialize_json(
                data["MachineLearningProductFilters"]
            )
        }
    elif data.get("OfferSetFilters") is not None:
        import capo_marketplace_catalog.types.offer_set_filters

        return {
            "OfferSetFilters": capo_marketplace_catalog.types.offer_set_filters.deserialize_json(
                data["OfferSetFilters"]
            )
        }
    elif data.get("ExpressPrivateOfferConfigurationFilters") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_filters

        return {
            "ExpressPrivateOfferConfigurationFilters": capo_marketplace_catalog.types.express_private_offer_configuration_filters.deserialize_json(
                data["ExpressPrivateOfferConfigurationFilters"]
            )
        }
    elif data.get("SubsidiaryAuthorizationFilters") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_filters

        return {
            "SubsidiaryAuthorizationFilters": capo_marketplace_catalog.types.subsidiary_authorization_filters.deserialize_json(
                data["SubsidiaryAuthorizationFilters"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EntityTypeFilters: no recognized variant key")
