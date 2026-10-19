"""Generated from Smithy shape ``com.amazonaws.cloudsearch#Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.expression_value
    import capo_cloudsearch.types.standard_name


class Expression(TypedDict, closed=True):
    expression_name: "capo_cloudsearch.types.standard_name.StandardName"
    expression_value: "capo_cloudsearch.types.expression_value.ExpressionValue"


# --- awsQuery ser/de ---
def serialize_query(
    value: Expression, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ExpressionName", str(value["expression_name"])))
    pairs.append((f"{key_prefix}ExpressionValue", str(value["expression_value"])))


def deserialize_query(el: Element) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    child_expression_name = el.find("ExpressionName")
    if child_expression_name is not None:
        out["expression_name"] = str(child_expression_name.text or "")
    else:
        out["expression_name"] = ""
    child_expression_value = el.find("ExpressionValue")
    if child_expression_value is not None:
        out["expression_value"] = str(child_expression_value.text or "")
    else:
        out["expression_value"] = ""
    return out
