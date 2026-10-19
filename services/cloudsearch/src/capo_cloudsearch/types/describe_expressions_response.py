"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeExpressionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.expression_status_list


class DescribeExpressionsResponse(TypedDict, closed=True):
    expressions: "capo_cloudsearch.types.expression_status_list.ExpressionStatusList"
    """<p>The expressions configured for the domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeExpressionsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_cloudsearch.types.expression_status_list

    capo_cloudsearch.types.expression_status_list.serialize_query(
        value["expressions"], pairs, f"{key_prefix}Expressions"
    )


def deserialize_query(el: Element) -> DescribeExpressionsResponse:
    out: DescribeExpressionsResponse = {}  # type: ignore[typeddict-item]
    child_expressions = el.find("Expressions")
    if child_expressions is not None:
        import capo_cloudsearch.types.expression_status_list

        out["expressions"] = (
            capo_cloudsearch.types.expression_status_list.deserialize_query(
                child_expressions
            )
        )
    else:
        out["expressions"] = []
    return out
