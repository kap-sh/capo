"""Generated from Smithy shape ``com.amazonaws.appstream#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.filter_name
    import capo_appstream.types.filter_values


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.filter_name.FilterName"]
    """<p>The name of the filter. Valid filter names depend on the operation being performed.</p>"""
    values: NotRequired["capo_appstream.types.filter_values.FilterValues"]
    """<p>The values for the filter. Multiple values can be specified for a single filter name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import capo_appstream.types.filter_values

        out["Values"] = capo_appstream.types.filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Values") is not None:
        import capo_appstream.types.filter_values

        out["values"] = capo_appstream.types.filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import capo_appstream.types.filter_values

        out["Values"] = capo_appstream.types.filter_values.serialize_cbor(
            value["values"]
        )
    return out


def deserialize_cbor(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Values") is not None:
        import capo_appstream.types.filter_values

        out["values"] = capo_appstream.types.filter_values.deserialize_cbor(
            data["Values"]
        )
    return out
