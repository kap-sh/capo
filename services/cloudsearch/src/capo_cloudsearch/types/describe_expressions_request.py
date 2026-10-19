"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeExpressionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.boolean
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.standard_name_list


class DescribeExpressionsRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    """<p>The name of the domain you want to describe.</p>"""
    expression_names: NotRequired[
        "capo_cloudsearch.types.standard_name_list.StandardNameList"
    ]
    """<p>Limits the <code><a>DescribeExpressions</a></code> response to the specified expressions. If not specified, all expressions are shown.</p>"""
    deployed: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeExpressionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    if "expression_names" in value:
        import capo_cloudsearch.types.standard_name_list

        capo_cloudsearch.types.standard_name_list.serialize_query(
            value["expression_names"], pairs, f"{key_prefix}ExpressionNames"
        )
    if "deployed" in value:
        pairs.append(
            (f"{key_prefix}Deployed", "true" if value["deployed"] else "false")
        )


def deserialize_query(el: Element) -> DescribeExpressionsRequest:
    out: DescribeExpressionsRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_expression_names = el.find("ExpressionNames")
    if child_expression_names is not None:
        import capo_cloudsearch.types.standard_name_list

        out["expression_names"] = (
            capo_cloudsearch.types.standard_name_list.deserialize_query(
                child_expression_names
            )
        )
    child_deployed = el.find("Deployed")
    if child_deployed is not None:
        out["deployed"] = (child_deployed.text or "").lower() == "true"
    return out
