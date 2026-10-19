"""Generated from Smithy shape ``com.amazonaws.waf#UpdateSqlInjectionMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id
    import capo_waf.types.sql_injection_match_set_updates


class UpdateSqlInjectionMatchSetRequest(TypedDict, closed=True):
    sql_injection_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>SqlInjectionMatchSetId</code> of the <code>SqlInjectionMatchSet</code> that you want to update. <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: (
        "capo_waf.types.sql_injection_match_set_updates.SqlInjectionMatchSetUpdates"
    )
    """<p>An array of <code>SqlInjectionMatchSetUpdate</code> objects that you want to insert into or delete from a <a>SqlInjectionMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>SqlInjectionMatchSetUpdate</a>: Contains <code>Action</code> and <code>SqlInjectionMatchTuple</code> </p> </li> <li> <p> <a>SqlInjectionMatchTuple</a>: Contains <code>FieldToMatch</code> and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSqlInjectionMatchSetRequest) -> dict:
    out: dict = {}
    out["SqlInjectionMatchSetId"] = value["sql_injection_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    import capo_waf.types.sql_injection_match_set_updates

    out["Updates"] = (
        capo_waf.types.sql_injection_match_set_updates.serialize_aws_json_1_1(
            value["updates"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSqlInjectionMatchSetRequest:
    out: UpdateSqlInjectionMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("SqlInjectionMatchSetId") is not None:
        out["sql_injection_match_set_id"] = data["SqlInjectionMatchSetId"]
    else:
        out["sql_injection_match_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    if data.get("Updates") is not None:
        import capo_waf.types.sql_injection_match_set_updates

        out["updates"] = (
            capo_waf.types.sql_injection_match_set_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        out["updates"] = []
    return out
