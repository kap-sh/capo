"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.filter_name
    import capo_marketplace_agreement.types.filter_value_list


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_marketplace_agreement.types.filter_name.FilterName"]
    """<p>The name of the filter.</p>"""
    values: NotRequired[
        "capo_marketplace_agreement.types.filter_value_list.FilterValueList"
    ]
    """<p>The filter value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "values" in value:
        import capo_marketplace_agreement.types.filter_value_list

        out["values"] = (
            capo_marketplace_agreement.types.filter_value_list.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("values") is not None:
        import capo_marketplace_agreement.types.filter_value_list

        out["values"] = (
            capo_marketplace_agreement.types.filter_value_list.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "values" in value:
        import capo_marketplace_agreement.types.filter_value_list

        out["values"] = (
            capo_marketplace_agreement.types.filter_value_list.serialize_cbor(
                value["values"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("values") is not None:
        import capo_marketplace_agreement.types.filter_value_list

        out["values"] = (
            capo_marketplace_agreement.types.filter_value_list.deserialize_cbor(
                data["values"]
            )
        )
    return out
