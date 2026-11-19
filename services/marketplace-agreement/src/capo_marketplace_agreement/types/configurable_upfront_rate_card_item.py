"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ConfigurableUpfrontRateCardItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.constraints
    import capo_marketplace_agreement.types.rate_card_list
    import capo_marketplace_agreement.types.selector


class ConfigurableUpfrontRateCardItem(TypedDict, closed=True):
    selector: NotRequired["capo_marketplace_agreement.types.selector.Selector"]
    """<p>Differentiates between the mutually exclusive rate cards in the same pricing term to be selected by the buyer.</p>"""
    constraints: NotRequired["capo_marketplace_agreement.types.constraints.Constraints"]
    """<p>Defines limits on how the term can be configured by acceptors.</p>"""
    rate_card: NotRequired[
        "capo_marketplace_agreement.types.rate_card_list.RateCardList"
    ]
    """<p>Defines the per unit rates for product dimensions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurableUpfrontRateCardItem) -> dict:
    out: dict = {}
    if "selector" in value:
        import capo_marketplace_agreement.types.selector

        out["selector"] = (
            capo_marketplace_agreement.types.selector.serialize_aws_json_1_0(
                value["selector"]
            )
        )
    if "constraints" in value:
        import capo_marketplace_agreement.types.constraints

        out["constraints"] = (
            capo_marketplace_agreement.types.constraints.serialize_aws_json_1_0(
                value["constraints"]
            )
        )
    if "rate_card" in value:
        import capo_marketplace_agreement.types.rate_card_list

        out["rateCard"] = (
            capo_marketplace_agreement.types.rate_card_list.serialize_aws_json_1_0(
                value["rate_card"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConfigurableUpfrontRateCardItem:
    out: ConfigurableUpfrontRateCardItem = {}  # type: ignore[typeddict-item]
    if data.get("selector") is not None:
        import capo_marketplace_agreement.types.selector

        out["selector"] = (
            capo_marketplace_agreement.types.selector.deserialize_aws_json_1_0(
                data["selector"]
            )
        )
    if data.get("constraints") is not None:
        import capo_marketplace_agreement.types.constraints

        out["constraints"] = (
            capo_marketplace_agreement.types.constraints.deserialize_aws_json_1_0(
                data["constraints"]
            )
        )
    if data.get("rateCard") is not None:
        import capo_marketplace_agreement.types.rate_card_list

        out["rate_card"] = (
            capo_marketplace_agreement.types.rate_card_list.deserialize_aws_json_1_0(
                data["rateCard"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfigurableUpfrontRateCardItem) -> dict:
    out: dict = {}
    if "selector" in value:
        import capo_marketplace_agreement.types.selector

        out["selector"] = capo_marketplace_agreement.types.selector.serialize_cbor(
            value["selector"]
        )
    if "constraints" in value:
        import capo_marketplace_agreement.types.constraints

        out["constraints"] = (
            capo_marketplace_agreement.types.constraints.serialize_cbor(
                value["constraints"]
            )
        )
    if "rate_card" in value:
        import capo_marketplace_agreement.types.rate_card_list

        out["rateCard"] = (
            capo_marketplace_agreement.types.rate_card_list.serialize_cbor(
                value["rate_card"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ConfigurableUpfrontRateCardItem:
    out: ConfigurableUpfrontRateCardItem = {}  # type: ignore[typeddict-item]
    if data.get("selector") is not None:
        import capo_marketplace_agreement.types.selector

        out["selector"] = capo_marketplace_agreement.types.selector.deserialize_cbor(
            data["selector"]
        )
    if data.get("constraints") is not None:
        import capo_marketplace_agreement.types.constraints

        out["constraints"] = (
            capo_marketplace_agreement.types.constraints.deserialize_cbor(
                data["constraints"]
            )
        )
    if data.get("rateCard") is not None:
        import capo_marketplace_agreement.types.rate_card_list

        out["rate_card"] = (
            capo_marketplace_agreement.types.rate_card_list.deserialize_cbor(
                data["rateCard"]
            )
        )
    return out
