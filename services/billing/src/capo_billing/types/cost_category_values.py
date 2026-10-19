"""Generated from Smithy shape ``com.amazonaws.billing#CostCategoryValues``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.cost_category_name
    import capo_billing.types.values


class CostCategoryValues(TypedDict, closed=True):
    key: "capo_billing.types.cost_category_name.CostCategoryName"
    """<p> The unique name of the Cost Category. </p>"""
    values: "capo_billing.types.values.Values"
    """<p> The specific value of the Cost Category. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CostCategoryValues) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_billing.types.values

    out["values"] = capo_billing.types.values.serialize_aws_json_1_0(value["values"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CostCategoryValues:
    out: CostCategoryValues = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("values") is not None:
        import capo_billing.types.values

        out["values"] = capo_billing.types.values.deserialize_aws_json_1_0(
            data["values"]
        )
    else:
        out["values"] = []
    return out
