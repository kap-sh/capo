"""Generated from Smithy shape ``com.amazonaws.sesv2#DeliveryAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.account_shared_pool_delivery_mode


class DeliveryAttributes(TypedDict, closed=True):
    shared_pool_delivery_mode: NotRequired[
        "capo_sesv2.types.account_shared_pool_delivery_mode.AccountSharedPoolDeliveryMode"
    ]
    """<p>The shared pool delivery mode for your Amazon SES account in the current Amazon Web Services Region. This mode applies to email that you send from shared IP addresses. Can be one of the following:</p> <ul> <li> <p> <code>GLOBAL</code> – Amazon SES delivers from your sending Region first and, when it improves your deliverability, also uses Amazon SES shared IP addresses with established sending history in other Amazon Web Services Regions within the same Amazon Web Services partition.</p> </li> <li> <p> <code>REGIONAL</code> – Amazon SES delivers your email only from shared IP addresses in your sending Region.</p> </li> </ul> <p>Accounts that start sending in a Region on or after the launch of Global Shared Delivery use <code>GLOBAL</code> in that Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeliveryAttributes) -> dict:
    out: dict = {}
    if "shared_pool_delivery_mode" in value:
        import capo_sesv2.types.account_shared_pool_delivery_mode

        out["SharedPoolDeliveryMode"] = (
            capo_sesv2.types.account_shared_pool_delivery_mode.serialize_json(
                value["shared_pool_delivery_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeliveryAttributes:
    out: DeliveryAttributes = {}  # type: ignore[typeddict-item]
    if data.get("SharedPoolDeliveryMode") is not None:
        import capo_sesv2.types.account_shared_pool_delivery_mode

        out["shared_pool_delivery_mode"] = (
            capo_sesv2.types.account_shared_pool_delivery_mode.deserialize_json(
                data["SharedPoolDeliveryMode"]
            )
        )
    return out
