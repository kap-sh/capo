"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DimensionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dimension_name
    import capo_cloudwatch.types.dimension_value


class DimensionFilter(TypedDict, closed=True):
    name: NotRequired["capo_cloudwatch.types.dimension_name.DimensionName"]
    """<p>The dimension name to be matched.</p>"""
    value: NotRequired["capo_cloudwatch.types.dimension_value.DimensionValue"]
    """<p>The value of the dimension to be matched.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DimensionFilter:
    out: DimensionFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DimensionFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_query(el: Element) -> DimensionFilter:
    out: DimensionFilter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DimensionFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> DimensionFilter:
    out: DimensionFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
