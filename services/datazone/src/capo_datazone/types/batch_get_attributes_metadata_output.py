"""Generated from Smithy shape ``com.amazonaws.datazone#BatchGetAttributesMetadataOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.attributes_errors
    import capo_datazone.types.batch_get_attribute_items


class BatchGetAttributesMetadataOutput(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_datazone.types.batch_get_attribute_items.BatchGetAttributeItems"
    ]
    """<p>The results of the BatchGetAttributesMetadata action.</p>"""
    errors: "capo_datazone.types.attributes_errors.AttributesErrors"
    """<p>The errors generated when the BatchGetAttributesMetadata action is invoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttributesMetadataOutput) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_datazone.types.batch_get_attribute_items

        out["attributes"] = (
            capo_datazone.types.batch_get_attribute_items.serialize_json(
                value["attributes"]
            )
        )
    import capo_datazone.types.attributes_errors

    out["errors"] = capo_datazone.types.attributes_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetAttributesMetadataOutput:
    out: BatchGetAttributesMetadataOutput = {}  # type: ignore[typeddict-item]
    if data.get("attributes") is not None:
        import capo_datazone.types.batch_get_attribute_items

        out["attributes"] = (
            capo_datazone.types.batch_get_attribute_items.deserialize_json(
                data["attributes"]
            )
        )
    if data.get("errors") is not None:
        import capo_datazone.types.attributes_errors

        out["errors"] = capo_datazone.types.attributes_errors.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError("BatchGetAttributesMetadataOutput.errors required")
    return out


def redact_sensitive(value: BatchGetAttributesMetadataOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attributes" in value:
        import capo_datazone.types.batch_get_attribute_items

        out["attributes"] = (
            capo_datazone.types.batch_get_attribute_items.redact_sensitive(
                value["attributes"]
            )
        )
    return out
