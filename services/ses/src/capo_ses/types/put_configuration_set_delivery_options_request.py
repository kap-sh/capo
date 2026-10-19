"""Generated from Smithy shape ``com.amazonaws.ses#PutConfigurationSetDeliveryOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_name
    import capo_ses.types.delivery_options


class PutConfigurationSetDeliveryOptionsRequest(TypedDict, closed=True):
    configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName"
    """<p>The name of the configuration set.</p>"""
    delivery_options: NotRequired["capo_ses.types.delivery_options.DeliveryOptions"]
    """<p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutConfigurationSetDeliveryOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
    )
    if "delivery_options" in value:
        import capo_ses.types.delivery_options

        capo_ses.types.delivery_options.serialize_query(
            value["delivery_options"], pairs, f"{key_prefix}DeliveryOptions"
        )


def deserialize_query(el: Element) -> PutConfigurationSetDeliveryOptionsRequest:
    out: PutConfigurationSetDeliveryOptionsRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        out["configuration_set_name"] = ""
    child_delivery_options = el.find("DeliveryOptions")
    if child_delivery_options is not None:
        import capo_ses.types.delivery_options

        out["delivery_options"] = capo_ses.types.delivery_options.deserialize_query(
            child_delivery_options
        )
    return out
