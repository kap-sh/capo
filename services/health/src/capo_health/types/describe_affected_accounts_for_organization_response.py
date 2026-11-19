"""Generated from Smithy shape ``com.amazonaws.health#DescribeAffectedAccountsForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.affected_account_entity_list
    import capo_health.types.affected_accounts_list
    import capo_health.types.event_scope_code
    import capo_health.types.next_token


class DescribeAffectedAccountsForOrganizationResponse(TypedDict, closed=True):
    affected_accounts: NotRequired[
        "capo_health.types.affected_accounts_list.affectedAccountsList"
    ]
    """<p>A JSON set of elements of the affected accounts.</p>"""
    affected_account_entities: NotRequired[
        "capo_health.types.affected_account_entity_list.AffectedAccountEntityList"
    ]
    """<p>The list of affected account entities, including account IDs and their associated tags.</p>"""
    event_scope_code: NotRequired["capo_health.types.event_scope_code.eventScopeCode"]
    """<p>This parameter specifies if the Health event is a public Amazon Web Services service event or an account-specific event.</p> <ul> <li> <p>If the <code>eventScopeCode</code> value is <code>PUBLIC</code>, then the <code>affectedAccounts</code> value is always empty.</p> </li> <li> <p>If the <code>eventScopeCode</code> value is <code>ACCOUNT_SPECIFIC</code>, then the <code>affectedAccounts</code> value lists the affected Amazon Web Services accounts in your organization. For example, if an event affects a service such as Amazon Elastic Compute Cloud and you have Amazon Web Services accounts that use that service, those account IDs appear in the response.</p> </li> <li> <p>If the <code>eventScopeCode</code> value is <code>NONE</code>, then the <code>eventArn</code> that you specified in the request is invalid or doesn't exist.</p> </li> </ul>"""
    next_token: NotRequired["capo_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAffectedAccountsForOrganizationResponse,
) -> dict:
    out: dict = {}
    if "affected_accounts" in value:
        import capo_health.types.affected_accounts_list

        out["affectedAccounts"] = (
            capo_health.types.affected_accounts_list.serialize_aws_json_1_1(
                value["affected_accounts"]
            )
        )
    if "affected_account_entities" in value:
        import capo_health.types.affected_account_entity_list

        out["affectedAccountEntities"] = (
            capo_health.types.affected_account_entity_list.serialize_aws_json_1_1(
                value["affected_account_entities"]
            )
        )
    if "event_scope_code" in value:
        import capo_health.types.event_scope_code

        out["eventScopeCode"] = (
            capo_health.types.event_scope_code.serialize_aws_json_1_1(
                value["event_scope_code"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAffectedAccountsForOrganizationResponse:
    out: DescribeAffectedAccountsForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("affectedAccounts") is not None:
        import capo_health.types.affected_accounts_list

        out["affected_accounts"] = (
            capo_health.types.affected_accounts_list.deserialize_aws_json_1_1(
                data["affectedAccounts"]
            )
        )
    if data.get("affectedAccountEntities") is not None:
        import capo_health.types.affected_account_entity_list

        out["affected_account_entities"] = (
            capo_health.types.affected_account_entity_list.deserialize_aws_json_1_1(
                data["affectedAccountEntities"]
            )
        )
    if data.get("eventScopeCode") is not None:
        import capo_health.types.event_scope_code

        out["event_scope_code"] = (
            capo_health.types.event_scope_code.deserialize_aws_json_1_1(
                data["eventScopeCode"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
