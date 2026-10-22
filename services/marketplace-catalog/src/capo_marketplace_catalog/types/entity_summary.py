"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_product_summary
    import capo_marketplace_catalog.types.arn
    import capo_marketplace_catalog.types.container_product_summary
    import capo_marketplace_catalog.types.data_product_summary
    import capo_marketplace_catalog.types.date_time_iso8601
    import capo_marketplace_catalog.types.entity_name_string
    import capo_marketplace_catalog.types.entity_type
    import capo_marketplace_catalog.types.express_private_offer_configuration_summary
    import capo_marketplace_catalog.types.machine_learning_product_summary
    import capo_marketplace_catalog.types.offer_set_summary
    import capo_marketplace_catalog.types.offer_summary
    import capo_marketplace_catalog.types.resale_authorization_summary
    import capo_marketplace_catalog.types.resource_id
    import capo_marketplace_catalog.types.saa_s_product_summary
    import capo_marketplace_catalog.types.visibility_value


class EntitySummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_marketplace_catalog.types.entity_name_string.EntityNameString"
    ]
    """<p>The name for the entity. This value is not unique. It is defined by the seller.</p>"""
    entity_type: NotRequired["capo_marketplace_catalog.types.entity_type.EntityType"]
    """<p>The type of the entity.</p>"""
    entity_id: NotRequired["capo_marketplace_catalog.types.resource_id.ResourceId"]
    """<p>The unique identifier for the entity.</p>"""
    entity_arn: NotRequired["capo_marketplace_catalog.types.arn.ARN"]
    """<p>The ARN associated with the unique identifier for the entity.</p>"""
    last_modified_date: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The last time the entity was published, using ISO 8601 format (2018-02-27T13:45:22Z).</p>"""
    visibility: NotRequired[
        "capo_marketplace_catalog.types.visibility_value.VisibilityValue"
    ]
    """<p>The visibility status of the entity to buyers. This value can be <code>Public</code> (everyone can view the entity), <code>Limited</code> (the entity is visible to limited accounts only), or <code>Restricted</code> (the entity was published and then unpublished and only existing buyers can view it). </p>"""
    ami_product_summary: NotRequired[
        "capo_marketplace_catalog.types.ami_product_summary.AmiProductSummary"
    ]
    """<p>An object that contains summary information about the AMI product.</p>"""
    container_product_summary: NotRequired[
        "capo_marketplace_catalog.types.container_product_summary.ContainerProductSummary"
    ]
    """<p>An object that contains summary information about the container product.</p>"""
    data_product_summary: NotRequired[
        "capo_marketplace_catalog.types.data_product_summary.DataProductSummary"
    ]
    """<p>An object that contains summary information about the data product.</p>"""
    saa_s_product_summary: NotRequired[
        "capo_marketplace_catalog.types.saa_s_product_summary.SaaSProductSummary"
    ]
    """<p>An object that contains summary information about the SaaS product.</p>"""
    offer_summary: NotRequired[
        "capo_marketplace_catalog.types.offer_summary.OfferSummary"
    ]
    """<p>An object that contains summary information about the offer.</p>"""
    resale_authorization_summary: NotRequired[
        "capo_marketplace_catalog.types.resale_authorization_summary.ResaleAuthorizationSummary"
    ]
    """<p>An object that contains summary information about the Resale Authorization.</p>"""
    machine_learning_product_summary: NotRequired[
        "capo_marketplace_catalog.types.machine_learning_product_summary.MachineLearningProductSummary"
    ]
    offer_set_summary: NotRequired[
        "capo_marketplace_catalog.types.offer_set_summary.OfferSetSummary"
    ]
    """<p>An object that contains summary information about the offer set.</p>"""
    express_private_offer_configuration_summary: NotRequired[
        "capo_marketplace_catalog.types.express_private_offer_configuration_summary.ExpressPrivateOfferConfigurationSummary"
    ]
    """<p>An object that contains summary information about the express private offer configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntitySummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "entity_type" in value:
        out["EntityType"] = value["entity_type"]
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "entity_arn" in value:
        out["EntityArn"] = value["entity_arn"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "visibility" in value:
        out["Visibility"] = value["visibility"]
    if "ami_product_summary" in value:
        import capo_marketplace_catalog.types.ami_product_summary

        out["AmiProductSummary"] = (
            capo_marketplace_catalog.types.ami_product_summary.serialize_json(
                value["ami_product_summary"]
            )
        )
    if "container_product_summary" in value:
        import capo_marketplace_catalog.types.container_product_summary

        out["ContainerProductSummary"] = (
            capo_marketplace_catalog.types.container_product_summary.serialize_json(
                value["container_product_summary"]
            )
        )
    if "data_product_summary" in value:
        import capo_marketplace_catalog.types.data_product_summary

        out["DataProductSummary"] = (
            capo_marketplace_catalog.types.data_product_summary.serialize_json(
                value["data_product_summary"]
            )
        )
    if "saa_s_product_summary" in value:
        import capo_marketplace_catalog.types.saa_s_product_summary

        out["SaaSProductSummary"] = (
            capo_marketplace_catalog.types.saa_s_product_summary.serialize_json(
                value["saa_s_product_summary"]
            )
        )
    if "offer_summary" in value:
        import capo_marketplace_catalog.types.offer_summary

        out["OfferSummary"] = (
            capo_marketplace_catalog.types.offer_summary.serialize_json(
                value["offer_summary"]
            )
        )
    if "resale_authorization_summary" in value:
        import capo_marketplace_catalog.types.resale_authorization_summary

        out["ResaleAuthorizationSummary"] = (
            capo_marketplace_catalog.types.resale_authorization_summary.serialize_json(
                value["resale_authorization_summary"]
            )
        )
    if "machine_learning_product_summary" in value:
        import capo_marketplace_catalog.types.machine_learning_product_summary

        out["MachineLearningProductSummary"] = (
            capo_marketplace_catalog.types.machine_learning_product_summary.serialize_json(
                value["machine_learning_product_summary"]
            )
        )
    if "offer_set_summary" in value:
        import capo_marketplace_catalog.types.offer_set_summary

        out["OfferSetSummary"] = (
            capo_marketplace_catalog.types.offer_set_summary.serialize_json(
                value["offer_set_summary"]
            )
        )
    if "express_private_offer_configuration_summary" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_summary

        out["ExpressPrivateOfferConfigurationSummary"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_summary.serialize_json(
                value["express_private_offer_configuration_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> EntitySummary:
    out: EntitySummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EntityType") is not None:
        out["entity_type"] = data["EntityType"]
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    if data.get("EntityArn") is not None:
        out["entity_arn"] = data["EntityArn"]
    if data.get("LastModifiedDate") is not None:
        out["last_modified_date"] = data["LastModifiedDate"]
    if data.get("Visibility") is not None:
        out["visibility"] = data["Visibility"]
    if data.get("AmiProductSummary") is not None:
        import capo_marketplace_catalog.types.ami_product_summary

        out["ami_product_summary"] = (
            capo_marketplace_catalog.types.ami_product_summary.deserialize_json(
                data["AmiProductSummary"]
            )
        )
    if data.get("ContainerProductSummary") is not None:
        import capo_marketplace_catalog.types.container_product_summary

        out["container_product_summary"] = (
            capo_marketplace_catalog.types.container_product_summary.deserialize_json(
                data["ContainerProductSummary"]
            )
        )
    if data.get("DataProductSummary") is not None:
        import capo_marketplace_catalog.types.data_product_summary

        out["data_product_summary"] = (
            capo_marketplace_catalog.types.data_product_summary.deserialize_json(
                data["DataProductSummary"]
            )
        )
    if data.get("SaaSProductSummary") is not None:
        import capo_marketplace_catalog.types.saa_s_product_summary

        out["saa_s_product_summary"] = (
            capo_marketplace_catalog.types.saa_s_product_summary.deserialize_json(
                data["SaaSProductSummary"]
            )
        )
    if data.get("OfferSummary") is not None:
        import capo_marketplace_catalog.types.offer_summary

        out["offer_summary"] = (
            capo_marketplace_catalog.types.offer_summary.deserialize_json(
                data["OfferSummary"]
            )
        )
    if data.get("ResaleAuthorizationSummary") is not None:
        import capo_marketplace_catalog.types.resale_authorization_summary

        out["resale_authorization_summary"] = (
            capo_marketplace_catalog.types.resale_authorization_summary.deserialize_json(
                data["ResaleAuthorizationSummary"]
            )
        )
    if data.get("MachineLearningProductSummary") is not None:
        import capo_marketplace_catalog.types.machine_learning_product_summary

        out["machine_learning_product_summary"] = (
            capo_marketplace_catalog.types.machine_learning_product_summary.deserialize_json(
                data["MachineLearningProductSummary"]
            )
        )
    if data.get("OfferSetSummary") is not None:
        import capo_marketplace_catalog.types.offer_set_summary

        out["offer_set_summary"] = (
            capo_marketplace_catalog.types.offer_set_summary.deserialize_json(
                data["OfferSetSummary"]
            )
        )
    if data.get("ExpressPrivateOfferConfigurationSummary") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_summary

        out["express_private_offer_configuration_summary"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_summary.deserialize_json(
                data["ExpressPrivateOfferConfigurationSummary"]
            )
        )
    return out
