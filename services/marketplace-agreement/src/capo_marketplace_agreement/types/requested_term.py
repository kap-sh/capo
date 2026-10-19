"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RequestedTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.requested_term_configuration
    import capo_marketplace_agreement.types.term_id


class RequestedTerm(TypedDict, closed=True):
    id: "capo_marketplace_agreement.types.term_id.TermId"
    """<p>The unique identifier of the term in the agreement proposal.</p>"""
    configuration: NotRequired[
        "capo_marketplace_agreement.types.requested_term_configuration.RequestedTermConfiguration"
    ]
    """<p>Additional configuration for the requested terms. This configuration is applicable only to the terms that accept a customer-provided configuration, such as <code>ConfigurableUpfrontPricingTerm</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestedTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "configuration" in value:
        import capo_marketplace_agreement.types.requested_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.requested_term_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestedTerm:
    out: RequestedTerm = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("configuration") is not None:
        import capo_marketplace_agreement.types.requested_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.requested_term_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    return out
