"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeLogGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.account_ids
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.describe_log_groups_log_group_identifiers
    import capo_cloudwatch_logs.types.include_linked_accounts
    import capo_cloudwatch_logs.types.log_group_class
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.log_group_name_pattern
    import capo_cloudwatch_logs.types.next_token


class DescribeLogGroupsRequest(TypedDict, closed=True):
    account_identifiers: NotRequired[
        "capo_cloudwatch_logs.types.account_ids.AccountIds"
    ]
    """<p>When <code>includeLinkedAccounts</code> is set to <code>true</code>, use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array. </p>"""
    log_group_name_prefix: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The prefix to match.</p> <note> <p> <code>logGroupNamePrefix</code> and <code>logGroupNamePattern</code> are mutually exclusive. Only one of these parameters can be passed. </p> </note>"""
    log_group_name_pattern: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name_pattern.LogGroupNamePattern"
    ]
    """<p>If you specify a string for this parameter, the operation returns only log groups that have names that match the string based on a case-sensitive substring search. For example, if you specify <code>DataLogs</code>, log groups named <code>DataLogs</code>, <code>aws/DataLogs</code>, and <code>GroupDataLogs</code> would match, but <code>datalogs</code>, <code>Data/log/s</code> and <code>Groupdata</code> would not match.</p> <p>If you specify <code>logGroupNamePattern</code> in your request, then only <code>arn</code>, <code>creationTime</code>, and <code>logGroupName</code> are included in the response. </p> <note> <p> <code>logGroupNamePattern</code> and <code>logGroupNamePrefix</code> are mutually exclusive. Only one of these parameters can be passed. </p> </note>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>"""
    include_linked_accounts: NotRequired[
        "capo_cloudwatch_logs.types.include_linked_accounts.IncludeLinkedAccounts"
    ]
    """<p>If you are using a monitoring account, set this to <code>true</code> to have the operation return log groups in the accounts listed in <code>accountIdentifiers</code>.</p> <p>If this parameter is set to <code>true</code> and <code>accountIdentifiers</code> contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account. </p> <p>The default for this parameter is <code>false</code>.</p>"""
    log_group_class: NotRequired[
        "capo_cloudwatch_logs.types.log_group_class.LogGroupClass"
    ]
    """<p>Use this parameter to limit the results to only those log groups in the specified log group class. If you omit this parameter, log groups of all classes can be returned.</p> <p>Specifies the log group class for this log group. There are three classes:</p> <ul> <li> <p>The <code>Standard</code> log class supports all CloudWatch Logs features.</p> </li> <li> <p>The <code>Infrequent Access</code> log class supports a subset of CloudWatch Logs features and incurs lower costs.</p> </li> <li> <p>Use the <code>Delivery</code> log class only for delivering Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesn't offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.</p> </li> </ul> <p>For details about the features supported by each class, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html">Log classes</a> </p>"""
    log_group_identifiers: NotRequired[
        "capo_cloudwatch_logs.types.describe_log_groups_log_group_identifiers.DescribeLogGroupsLogGroupIdentifiers"
    ]
    """<p>Use this array to filter the list of log groups returned. If you specify this parameter, the only other filter that you can choose to specify is <code>includeLinkedAccounts</code>.</p> <p>If you are using this operation in a monitoring account, you can specify the ARNs of log groups in source accounts and in the monitoring account itself. If you are using this operation in an account that is not a cross-account monitoring account, you can specify only log group names in the same account as the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLogGroupsRequest) -> dict:
    out: dict = {}
    if "account_identifiers" in value:
        import capo_cloudwatch_logs.types.account_ids

        out["accountIdentifiers"] = (
            capo_cloudwatch_logs.types.account_ids.serialize_aws_json_1_1(
                value["account_identifiers"]
            )
        )
    if "log_group_name_prefix" in value:
        out["logGroupNamePrefix"] = value["log_group_name_prefix"]
    if "log_group_name_pattern" in value:
        out["logGroupNamePattern"] = value["log_group_name_pattern"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "include_linked_accounts" in value:
        out["includeLinkedAccounts"] = value["include_linked_accounts"]
    if "log_group_class" in value:
        import capo_cloudwatch_logs.types.log_group_class

        out["logGroupClass"] = (
            capo_cloudwatch_logs.types.log_group_class.serialize_aws_json_1_1(
                value["log_group_class"]
            )
        )
    if "log_group_identifiers" in value:
        import capo_cloudwatch_logs.types.describe_log_groups_log_group_identifiers

        out["logGroupIdentifiers"] = (
            capo_cloudwatch_logs.types.describe_log_groups_log_group_identifiers.serialize_aws_json_1_1(
                value["log_group_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLogGroupsRequest:
    out: DescribeLogGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIdentifiers") is not None:
        import capo_cloudwatch_logs.types.account_ids

        out["account_identifiers"] = (
            capo_cloudwatch_logs.types.account_ids.deserialize_aws_json_1_1(
                data["accountIdentifiers"]
            )
        )
    if data.get("logGroupNamePrefix") is not None:
        out["log_group_name_prefix"] = data["logGroupNamePrefix"]
    if data.get("logGroupNamePattern") is not None:
        out["log_group_name_pattern"] = data["logGroupNamePattern"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("includeLinkedAccounts") is not None:
        out["include_linked_accounts"] = data["includeLinkedAccounts"]
    if data.get("logGroupClass") is not None:
        import capo_cloudwatch_logs.types.log_group_class

        out["log_group_class"] = (
            capo_cloudwatch_logs.types.log_group_class.deserialize_aws_json_1_1(
                data["logGroupClass"]
            )
        )
    if data.get("logGroupIdentifiers") is not None:
        import capo_cloudwatch_logs.types.describe_log_groups_log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch_logs.types.describe_log_groups_log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    return out
