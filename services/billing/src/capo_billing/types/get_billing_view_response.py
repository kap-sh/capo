"""Generated from Smithy shape ``com.amazonaws.billing#GetBillingViewResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.billing_view_element


class GetBillingViewResponse(TypedDict, closed=True):
    billing_view: "capo_billing.types.billing_view_element.BillingViewElement"
    """<p>The billing view element associated with the specified ARN. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillingViewResponse) -> dict:
    out: dict = {}
    import capo_billing.types.billing_view_element

    out["billingView"] = capo_billing.types.billing_view_element.serialize_aws_json_1_0(
        value["billing_view"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillingViewResponse:
    out: GetBillingViewResponse = {}  # type: ignore[typeddict-item]
    if data.get("billingView") is not None:
        import capo_billing.types.billing_view_element

        out["billing_view"] = (
            capo_billing.types.billing_view_element.deserialize_aws_json_1_0(
                data["billingView"]
            )
        )
    else:
        raise DeserializationError("GetBillingViewResponse.billing_view required")
    return out


def redact_sensitive(value: GetBillingViewResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "billing_view" in value:
        import capo_billing.types.billing_view_element

        out["billing_view"] = capo_billing.types.billing_view_element.redact_sensitive(
            value["billing_view"]
        )
    return out
