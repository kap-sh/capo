"""Generated from Smithy shape ``com.amazonaws.waf#DeleteSqlInjectionMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id


class DeleteSqlInjectionMatchSetRequest(TypedDict, closed=True):
    sql_injection_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>SqlInjectionMatchSetId</code> of the <a>SqlInjectionMatchSet</a> that you want to delete. <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSqlInjectionMatchSetRequest) -> dict:
    out: dict = {}
    out["SqlInjectionMatchSetId"] = value["sql_injection_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSqlInjectionMatchSetRequest:
    out: DeleteSqlInjectionMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("SqlInjectionMatchSetId") is not None:
        out["sql_injection_match_set_id"] = data["SqlInjectionMatchSetId"]
    else:
        out["sql_injection_match_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out
