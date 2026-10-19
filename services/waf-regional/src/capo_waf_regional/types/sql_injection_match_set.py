"""Generated from Smithy shape ``com.amazonaws.wafregional#SqlInjectionMatchSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.resource_name
    import capo_waf_regional.types.sql_injection_match_tuples


class SqlInjectionMatchSet(TypedDict, closed=True):
    sql_injection_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>SqlInjectionMatchSet</code>. You use <code>SqlInjectionMatchSetId</code> to get information about a <code>SqlInjectionMatchSet</code> (see <a>GetSqlInjectionMatchSet</a>), update a <code>SqlInjectionMatchSet</code> (see <a>UpdateSqlInjectionMatchSet</a>), insert a <code>SqlInjectionMatchSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete a <code>SqlInjectionMatchSet</code> from AWS WAF (see <a>DeleteSqlInjectionMatchSet</a>).</p> <p> <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>"""
    name: NotRequired["capo_waf_regional.types.resource_name.ResourceName"]
    """<p>The name, if any, of the <code>SqlInjectionMatchSet</code>.</p>"""
    sql_injection_match_tuples: (
        "capo_waf_regional.types.sql_injection_match_tuples.SqlInjectionMatchTuples"
    )
    """<p>Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlInjectionMatchSet) -> dict:
    out: dict = {}
    out["SqlInjectionMatchSetId"] = value["sql_injection_match_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_waf_regional.types.sql_injection_match_tuples

    out["SqlInjectionMatchTuples"] = (
        capo_waf_regional.types.sql_injection_match_tuples.serialize_aws_json_1_1(
            value["sql_injection_match_tuples"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlInjectionMatchSet:
    out: SqlInjectionMatchSet = {}  # type: ignore[typeddict-item]
    if data.get("SqlInjectionMatchSetId") is not None:
        out["sql_injection_match_set_id"] = data["SqlInjectionMatchSetId"]
    else:
        out["sql_injection_match_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SqlInjectionMatchTuples") is not None:
        import capo_waf_regional.types.sql_injection_match_tuples

        out["sql_injection_match_tuples"] = (
            capo_waf_regional.types.sql_injection_match_tuples.deserialize_aws_json_1_1(
                data["SqlInjectionMatchTuples"]
            )
        )
    else:
        out["sql_injection_match_tuples"] = []
    return out
