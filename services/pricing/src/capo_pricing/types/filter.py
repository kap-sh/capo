"""Generated from Smithy shape ``com.amazonaws.pricing#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pricing.types.field
    import capo_pricing.types.filter_type
    import capo_pricing.types.value


class Filter(TypedDict, closed=True):
    type: "capo_pricing.types.filter_type.FilterType"
    """<p>The type of filter that you want to use.</p> <p>Valid values are:</p> <ul> <li> <p> <code>TERM_MATCH</code>: Returns only products that match both the given filter field and the given value.</p> </li> <li> <p> <code>EQUALS</code>: Returns products that have a field value exactly matching the provided value.</p> </li> <li> <p> <code>CONTAINS</code>: Returns products where the field value contains the provided value as a substring.</p> </li> <li> <p> <code>ANY_OF</code>: Returns products where the field value is any of the provided values.</p> </li> <li> <p> <code>NONE_OF</code>: Returns products where the field value is not any of the provided values.</p> </li> </ul>"""
    field: "capo_pricing.types.field.Field"
    """<p>The product metadata field that you want to filter on. You can filter by just the service code to see all products for a specific service, filter by just the attribute name to see a specific attribute for multiple services, or use both a service code and an attribute name to retrieve only products that match both fields.</p> <p>Valid values include: <code>ServiceCode</code>, and all attribute names</p> <p>For example, you can filter by the <code>AmazonEC2</code> service code and the <code>volumeType</code> attribute name to get the prices for only Amazon EC2 volumes.</p>"""
    value: "capo_pricing.types.value.Value"
    """<p>The service code or attribute value that you want to filter by. If you're filtering by service code this is the actual service code, such as <code>AmazonEC2</code>. If you're filtering by attribute name, this is the attribute value that you want the returned products to match, such as a <code>Provisioned IOPS</code> volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    import capo_pricing.types.filter_type

    out["Type"] = capo_pricing.types.filter_type.serialize_aws_json_1_1(value["type"])
    out["Field"] = value["field"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_pricing.types.filter_type

        out["type"] = capo_pricing.types.filter_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_pricing.types.filter_type.FilterType", "")
    if data.get("Field") is not None:
        out["field"] = data["Field"]
    else:
        out["field"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
