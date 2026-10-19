"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DefineExpressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.expression


class DefineExpressionRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    expression: "capo_cloudsearch.types.expression.Expression"


# --- awsQuery ser/de ---
def serialize_query(
    value: DefineExpressionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    import capo_cloudsearch.types.expression

    capo_cloudsearch.types.expression.serialize_query(
        value["expression"], pairs, f"{key_prefix}Expression"
    )


def deserialize_query(el: Element) -> DefineExpressionRequest:
    out: DefineExpressionRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_expression = el.find("Expression")
    if child_expression is not None:
        import capo_cloudsearch.types.expression

        out["expression"] = capo_cloudsearch.types.expression.deserialize_query(
            child_expression
        )
    else:
        raise DeserializationError("DefineExpressionRequest.expression required")
    return out
