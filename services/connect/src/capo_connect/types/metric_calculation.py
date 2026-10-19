"""Generated from Smithy shape ``com.amazonaws.connect#MetricCalculation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.calculation_component_list
    import capo_connect.types.calculation_expression


class MetricCalculation(TypedDict, closed=True):
    calculation_components: (
        "capo_connect.types.calculation_component_list.CalculationComponentList"
    )
    """<p>The list of component metrics referenced in the calculation formula. Each component has an alias used in the formula expression.</p>"""
    calculation: "capo_connect.types.calculation_expression.CalculationExpression"
    """<p>The formula expression that defines how the metric is calculated. Uses component aliases (for example, <code>100 * SUM(M1) / SUM(M2)</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricCalculation) -> dict:
    out: dict = {}
    import capo_connect.types.calculation_component_list

    out["CalculationComponents"] = (
        capo_connect.types.calculation_component_list.serialize_json(
            value["calculation_components"]
        )
    )
    out["Calculation"] = value["calculation"]
    return out


def deserialize_json(data: dict) -> MetricCalculation:
    out: MetricCalculation = {}  # type: ignore[typeddict-item]
    if data.get("CalculationComponents") is not None:
        import capo_connect.types.calculation_component_list

        out["calculation_components"] = (
            capo_connect.types.calculation_component_list.deserialize_json(
                data["CalculationComponents"]
            )
        )
    else:
        out["calculation_components"] = []
    if data.get("Calculation") is not None:
        out["calculation"] = data["Calculation"]
    else:
        out["calculation"] = ""
    return out
