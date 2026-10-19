"""Generated from Smithy shape ``com.amazonaws.waf#SqlInjectionMatchSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name


class SqlInjectionMatchSetSummary(TypedDict, closed=True):
    sql_injection_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>SqlInjectionMatchSet</code>. You use <code>SqlInjectionMatchSetId</code> to get information about a <code>SqlInjectionMatchSet</code> (see <a>GetSqlInjectionMatchSet</a>), update a <code>SqlInjectionMatchSet</code> (see <a>UpdateSqlInjectionMatchSet</a>), insert a <code>SqlInjectionMatchSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete a <code>SqlInjectionMatchSet</code> from AWS WAF (see <a>DeleteSqlInjectionMatchSet</a>).</p> <p> <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>"""
    name: "capo_waf.types.resource_name.ResourceName"
    """<p>The name of the <code>SqlInjectionMatchSet</code>, if any, specified by <code>Id</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlInjectionMatchSetSummary) -> dict:
    out: dict = {}
    out["SqlInjectionMatchSetId"] = value["sql_injection_match_set_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlInjectionMatchSetSummary:
    out: SqlInjectionMatchSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("SqlInjectionMatchSetId") is not None:
        out["sql_injection_match_set_id"] = data["SqlInjectionMatchSetId"]
    else:
        out["sql_injection_match_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
