"""Generated from Smithy shape ``com.amazonaws.waf#GetSqlInjectionMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id


class GetSqlInjectionMatchSetRequest(TypedDict, closed=True):
    sql_injection_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>SqlInjectionMatchSetId</code> of the <a>SqlInjectionMatchSet</a> that you want to get. <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSqlInjectionMatchSetRequest) -> dict:
    out: dict = {}
    out["SqlInjectionMatchSetId"] = value["sql_injection_match_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSqlInjectionMatchSetRequest:
    out: GetSqlInjectionMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("SqlInjectionMatchSetId") is not None:
        out["sql_injection_match_set_id"] = data["SqlInjectionMatchSetId"]
    else:
        out["sql_injection_match_set_id"] = ""
    return out
