"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TagOptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.tag_option_key
    import capo_service_catalog.types.tag_option_values


class TagOptionSummary(TypedDict, closed=True):
    key: NotRequired["capo_service_catalog.types.tag_option_key.TagOptionKey"]
    """<p>The TagOption key.</p>"""
    values: NotRequired["capo_service_catalog.types.tag_option_values.TagOptionValues"]
    """<p>The TagOption value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOptionSummary) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import capo_service_catalog.types.tag_option_values

        out["Values"] = (
            capo_service_catalog.types.tag_option_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagOptionSummary:
    out: TagOptionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Values") is not None:
        import capo_service_catalog.types.tag_option_values

        out["values"] = (
            capo_service_catalog.types.tag_option_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagOptionSummary) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import capo_service_catalog.types.tag_option_values

        out["Values"] = capo_service_catalog.types.tag_option_values.serialize_cbor(
            value["values"]
        )
    return out


def deserialize_cbor(data: dict) -> TagOptionSummary:
    out: TagOptionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Values") is not None:
        import capo_service_catalog.types.tag_option_values

        out["values"] = capo_service_catalog.types.tag_option_values.deserialize_cbor(
            data["Values"]
        )
    return out
