"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PricingPlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.bundle_information
    import capo_iottwinmaker.types.long
    import capo_iottwinmaker.types.pricing_mode
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.update_reason


class PricingPlan(TypedDict, closed=True):
    billable_entity_count: NotRequired["capo_iottwinmaker.types.long.Long"]
    """<p>The billable entity count.</p>"""
    bundle_information: NotRequired[
        "capo_iottwinmaker.types.bundle_information.BundleInformation"
    ]
    """<p>The pricing plan's bundle information.</p>"""
    effective_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The effective date and time of the pricing plan.</p>"""
    pricing_mode: "capo_iottwinmaker.types.pricing_mode.PricingMode"
    """<p>The pricing mode.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The set date and time for updating a pricing plan.</p>"""
    update_reason: "capo_iottwinmaker.types.update_reason.UpdateReason"
    """<p>The update reason for changing a pricing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingPlan) -> dict:
    out: dict = {}
    if "billable_entity_count" in value:
        out["billableEntityCount"] = value["billable_entity_count"]
    if "bundle_information" in value:
        import capo_iottwinmaker.types.bundle_information

        out["bundleInformation"] = (
            capo_iottwinmaker.types.bundle_information.serialize_json(
                value["bundle_information"]
            )
        )
    import capo_iottwinmaker.types.timestamp

    out["effectiveDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["effective_date_time"]
    )
    out["pricingMode"] = value["pricing_mode"]
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    out["updateReason"] = value["update_reason"]
    return out


def deserialize_json(data: dict) -> PricingPlan:
    out: PricingPlan = {}  # type: ignore[typeddict-item]
    if data.get("billableEntityCount") is not None:
        out["billable_entity_count"] = data["billableEntityCount"]
    if data.get("bundleInformation") is not None:
        import capo_iottwinmaker.types.bundle_information

        out["bundle_information"] = (
            capo_iottwinmaker.types.bundle_information.deserialize_json(
                data["bundleInformation"]
            )
        )
    if data.get("effectiveDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["effective_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["effectiveDateTime"]
        )
    else:
        import datetime

        out["effective_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("pricingMode") is not None:
        out["pricing_mode"] = data["pricingMode"]
    else:
        out["pricing_mode"] = ""
    if data.get("updateDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        import datetime

        out["update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateReason") is not None:
        out["update_reason"] = data["updateReason"]
    else:
        out["update_reason"] = ""
    return out
