"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#Transformer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.jsonata_configuration
    import capo_eventbridgev2.types.transformer_type


class Transformer(TypedDict, closed=True):
    type: NotRequired["capo_eventbridgev2.types.transformer_type.TransformerType"]
    """Transform type."""
    jsonata_configuration: NotRequired[
        "capo_eventbridgev2.types.jsonata_configuration.JsonataConfiguration"
    ]
    """JSONata expression configuration. Required when Type is JSONATA."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Transformer) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_eventbridgev2.types.transformer_type

        out["Type"] = capo_eventbridgev2.types.transformer_type.serialize_cbor(
            value["type"]
        )
    if "jsonata_configuration" in value:
        import capo_eventbridgev2.types.jsonata_configuration

        out["JsonataConfiguration"] = (
            capo_eventbridgev2.types.jsonata_configuration.serialize_cbor(
                value["jsonata_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Transformer:
    out: Transformer = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_eventbridgev2.types.transformer_type

        out["type"] = capo_eventbridgev2.types.transformer_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("JsonataConfiguration") is not None:
        import capo_eventbridgev2.types.jsonata_configuration

        out["jsonata_configuration"] = (
            capo_eventbridgev2.types.jsonata_configuration.deserialize_cbor(
                data["JsonataConfiguration"]
            )
        )
    return out


def redact_sensitive(value: Transformer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "jsonata_configuration" in value:
        out["jsonata_configuration"] = "*** Sensitive Data Redacted ***"
    return out
