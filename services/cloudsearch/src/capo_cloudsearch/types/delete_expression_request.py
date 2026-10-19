"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DeleteExpressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.standard_name


class DeleteExpressionRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    expression_name: "capo_cloudsearch.types.standard_name.StandardName"
    """<p>The name of the <code><a>Expression</a></code> to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteExpressionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    pairs.append((f"{key_prefix}ExpressionName", str(value["expression_name"])))


def deserialize_query(el: Element) -> DeleteExpressionRequest:
    out: DeleteExpressionRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_expression_name = el.find("ExpressionName")
    if child_expression_name is not None:
        out["expression_name"] = str(child_expression_name.text or "")
    else:
        out["expression_name"] = ""
    return out
