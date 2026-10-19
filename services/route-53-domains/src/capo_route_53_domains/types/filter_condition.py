"""Generated from Smithy shape ``com.amazonaws.route53domains#FilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.list_domains_attribute_name
    import capo_route_53_domains.types.operator
    import capo_route_53_domains.types.values


class FilterCondition(TypedDict, closed=True):
    name: "capo_route_53_domains.types.list_domains_attribute_name.ListDomainsAttributeName"
    """<p>Name of the field which should be used for filtering the list of domains.</p>"""
    operator: "capo_route_53_domains.types.operator.Operator"
    """<p>The operator values for filtering domain names. The values can be:</p> <ul> <li> <p> <code>LE</code>: Less than, or equal to</p> </li> <li> <p> <code>GE</code>: Greater than, or equal to</p> </li> <li> <p> <code>BEGINS_WITH</code>: Begins with</p> </li> </ul>"""
    values: "capo_route_53_domains.types.values.Values"
    """<p> An array of strings presenting values to compare. Only 1 item in the list is currently supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterCondition) -> dict:
    out: dict = {}
    import capo_route_53_domains.types.list_domains_attribute_name

    out["Name"] = (
        capo_route_53_domains.types.list_domains_attribute_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import capo_route_53_domains.types.operator

    out["Operator"] = capo_route_53_domains.types.operator.serialize_aws_json_1_1(
        value["operator"]
    )
    import capo_route_53_domains.types.values

    out["Values"] = capo_route_53_domains.types.values.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterCondition:
    out: FilterCondition = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_route_53_domains.types.list_domains_attribute_name

        out["name"] = (
            capo_route_53_domains.types.list_domains_attribute_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_route_53_domains.types.list_domains_attribute_name.ListDomainsAttributeName",
            "",
        )
    if data.get("Operator") is not None:
        import capo_route_53_domains.types.operator

        out["operator"] = capo_route_53_domains.types.operator.deserialize_aws_json_1_1(
            data["Operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_route_53_domains.types.operator.Operator", ""
        )
    if data.get("Values") is not None:
        import capo_route_53_domains.types.values

        out["values"] = capo_route_53_domains.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
