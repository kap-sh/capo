"""Generated from Smithy shape ``com.amazonaws.wafv2#Statement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.and_statement
    import capo_wafv2.types.asn_match_statement
    import capo_wafv2.types.byte_match_statement
    import capo_wafv2.types.geo_match_statement
    import capo_wafv2.types.ip_set_reference_statement
    import capo_wafv2.types.label_match_statement
    import capo_wafv2.types.managed_rule_group_statement
    import capo_wafv2.types.not_statement
    import capo_wafv2.types.or_statement
    import capo_wafv2.types.rate_based_statement
    import capo_wafv2.types.regex_match_statement
    import capo_wafv2.types.regex_pattern_set_reference_statement
    import capo_wafv2.types.rule_group_reference_statement
    import capo_wafv2.types.size_constraint_statement
    import capo_wafv2.types.sqli_match_statement
    import capo_wafv2.types.xss_match_statement


class Statement(TypedDict, closed=True):
    byte_match_statement: NotRequired[
        "capo_wafv2.types.byte_match_statement.ByteMatchStatement"
    ]
    """<p>A rule statement that defines a string match search for WAF to apply to web requests. The byte match statement provides the bytes to search for, the location in requests that you want WAF to search, and other settings. The bytes to search for are typically a string that corresponds with ASCII characters. In the WAF console and the developer guide, this is called a string match statement.</p>"""
    sqli_match_statement: NotRequired[
        "capo_wafv2.types.sqli_match_statement.SqliMatchStatement"
    ]
    """<p>A rule statement that inspects for malicious SQL code. Attackers insert malicious SQL code into web requests to do things like modify your database or extract data from it. </p>"""
    xss_match_statement: NotRequired[
        "capo_wafv2.types.xss_match_statement.XssMatchStatement"
    ]
    """<p>A rule statement that inspects for cross-site scripting (XSS) attacks. In XSS attacks, the attacker uses vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into other legitimate web browsers. </p>"""
    size_constraint_statement: NotRequired[
        "capo_wafv2.types.size_constraint_statement.SizeConstraintStatement"
    ]
    """<p>A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes. </p> <p>If you configure WAF to inspect the request body, WAF inspects only the number of bytes in the body up to the limit for the web ACL and protected resource type. If you know that the request body for your web requests should never exceed the inspection limit, you can use a size constraint statement to block requests that have a larger request body size. For more information about the inspection limits, see <code>Body</code> and <code>JsonBody</code> settings for the <code>FieldToMatch</code> data type. </p> <p>If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI <code>/logo.jpg</code> is nine characters long.</p>"""
    geo_match_statement: NotRequired[
        "capo_wafv2.types.geo_match_statement.GeoMatchStatement"
    ]
    """<p>A rule statement that labels web requests by country and region and that matches against web requests based on country code. A geo match rule labels every request that it inspects regardless of whether it finds a match.</p> <ul> <li> <p>To manage requests only by country, you can use this statement by itself and specify the countries that you want to match against in the <code>CountryCodes</code> array. </p> </li> <li> <p>Otherwise, configure your geo match rule with Count action so that it only labels requests. Then, add one or more label match rules to run after the geo match rule and configure them to match against the geographic labels and handle the requests as needed. </p> </li> </ul> <p>WAF labels requests using the alpha-2 country and region codes from the International Organization for Standardization (ISO) 3166 standard. WAF determines the codes using either the IP address in the web request origin or, if you specify it, the address in the geo match <code>ForwardedIPConfig</code>. </p> <p>If you use the web request origin, the label formats are <code>awswaf:clientip:geo:region:<ISO country code>-<ISO region code></code> and <code>awswaf:clientip:geo:country:<ISO country code></code>.</p> <p>If you use a forwarded IP address, the label formats are <code>awswaf:forwardedip:geo:region:<ISO country code>-<ISO region code></code> and <code>awswaf:forwardedip:geo:country:<ISO country code></code>.</p> <p>For additional details, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-geo-match.html">Geographic match rule statement</a> in the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">WAF Developer Guide</a>. </p>"""
    rule_group_reference_statement: NotRequired[
        "capo_wafv2.types.rule_group_reference_statement.RuleGroupReferenceStatement"
    ]
    """<p>A rule statement used to run the rules that are defined in a <a>RuleGroup</a>. To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.</p> <p>You cannot nest a <code>RuleGroupReferenceStatement</code>, for example for use inside a <code>NotStatement</code> or <code>OrStatement</code>. You cannot use a rule group reference statement inside another rule group. You can only reference a rule group as a top-level statement within a rule that you define in a web ACL.</p>"""
    ip_set_reference_statement: NotRequired[
        "capo_wafv2.types.ip_set_reference_statement.IPSetReferenceStatement"
    ]
    """<p>A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an <a>IPSet</a> that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see <a>CreateIPSet</a>.</p> <p>Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, WAF automatically updates all rules that reference it.</p>"""
    regex_pattern_set_reference_statement: NotRequired[
        "capo_wafv2.types.regex_pattern_set_reference_statement.RegexPatternSetReferenceStatement"
    ]
    """<p>A rule statement used to search web request components for matches with regular expressions. To use this, create a <a>RegexPatternSet</a> that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see <a>CreateRegexPatternSet</a>.</p> <p>Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, WAF automatically updates all rules that reference it.</p>"""
    rate_based_statement: NotRequired[
        "capo_wafv2.types.rate_based_statement.RateBasedStatement"
    ]
    """<p>A rate-based rule counts incoming requests and rate limits requests when they are coming at too fast a rate. The rule categorizes requests according to your aggregation criteria, collects them into aggregation instances, and counts and rate limits the requests for each instance. </p> <note> <p>If you change any of these settings in a rule that's currently in use, the change resets the rule's rate limiting counts. This can pause the rule's rate limiting activities for up to a minute. </p> </note> <p>You can specify individual aggregation keys, like IP address or HTTP method. You can also specify aggregation key combinations, like IP address and HTTP method, or HTTP method, query argument, and cookie. </p> <p>Each unique set of values for the aggregation keys that you specify is a separate aggregation instance, with the value from each key contributing to the aggregation instance definition. </p> <p>For example, assume the rule evaluates web requests with the following IP address and HTTP method values: </p> <ul> <li> <p>IP address 10.1.1.1, HTTP method POST</p> </li> <li> <p>IP address 10.1.1.1, HTTP method GET</p> </li> <li> <p>IP address 127.0.0.0, HTTP method POST</p> </li> <li> <p>IP address 10.1.1.1, HTTP method GET</p> </li> </ul> <p>The rule would create different aggregation instances according to your aggregation criteria, for example: </p> <ul> <li> <p>If the aggregation criteria is just the IP address, then each individual address is an aggregation instance, and WAF counts requests separately for each. The aggregation instances and request counts for our example would be the following: </p> <ul> <li> <p>IP address 10.1.1.1: count 3</p> </li> <li> <p>IP address 127.0.0.0: count 1</p> </li> </ul> </li> <li> <p>If the aggregation criteria is HTTP method, then each individual HTTP method is an aggregation instance. The aggregation instances and request counts for our example would be the following: </p> <ul> <li> <p>HTTP method POST: count 2</p> </li> <li> <p>HTTP method GET: count 2</p> </li> </ul> </li> <li> <p>If the aggregation criteria is IP address and HTTP method, then each IP address and each HTTP method would contribute to the combined aggregation instance. The aggregation instances and request counts for our example would be the following: </p> <ul> <li> <p>IP address 10.1.1.1, HTTP method POST: count 1</p> </li> <li> <p>IP address 10.1.1.1, HTTP method GET: count 2</p> </li> <li> <p>IP address 127.0.0.0, HTTP method POST: count 1</p> </li> </ul> </li> </ul> <p>For any n-tuple of aggregation keys, each unique combination of values for the keys defines a separate aggregation instance, which WAF counts and rate-limits individually. </p> <p>You can optionally nest another statement inside the rate-based statement, to narrow the scope of the rule so that it only counts and rate limits requests that match the nested statement. You can use this nested scope-down statement in conjunction with your aggregation key specifications or you can just count and rate limit all requests that match the scope-down statement, without additional aggregation. When you choose to just manage all requests that match a scope-down statement, the aggregation instance is singular for the rule. </p> <p>You cannot nest a <code>RateBasedStatement</code> inside another statement, for example inside a <code>NotStatement</code> or <code>OrStatement</code>. You can define a <code>RateBasedStatement</code> inside a web ACL and inside a rule group. </p> <p>For additional information about the options, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-based-rules.html">Rate limiting web requests using rate-based rules</a> in the <i>WAF Developer Guide</i>. </p> <p>If you only aggregate on the individual IP address or forwarded IP address, you can retrieve the list of IP addresses that WAF is currently rate limiting for a rule through the API call <code>GetRateBasedStatementManagedKeys</code>. This option is not available for other aggregation configurations.</p> <p>WAF tracks and manages web requests separately for each instance of a rate-based rule that you use. For example, if you provide the same rate-based rule settings in two web ACLs, each of the two rule statements represents a separate instance of the rate-based rule and gets its own tracking and management by WAF. If you define a rate-based rule inside a rule group, and then use that rule group in multiple places, each use creates a separate instance of the rate-based rule that gets its own tracking and management by WAF. </p>"""
    and_statement: NotRequired["capo_wafv2.types.and_statement.AndStatement"]
    """<p>A logical rule statement used to combine other rule statements with AND logic. You provide more than one <a>Statement</a> within the <code>AndStatement</code>. </p>"""
    or_statement: NotRequired["capo_wafv2.types.or_statement.OrStatement"]
    """<p>A logical rule statement used to combine other rule statements with OR logic. You provide more than one <a>Statement</a> within the <code>OrStatement</code>. </p>"""
    not_statement: NotRequired["capo_wafv2.types.not_statement.NotStatement"]
    """<p>A logical rule statement used to negate the results of another rule statement. You provide one <a>Statement</a> within the <code>NotStatement</code>.</p>"""
    managed_rule_group_statement: NotRequired[
        "capo_wafv2.types.managed_rule_group_statement.ManagedRuleGroupStatement"
    ]
    """<p>A rule statement used to run the rules that are defined in a managed rule group. To use this, provide the vendor name and the name of the rule group in this statement. You can retrieve the required names by calling <a>ListAvailableManagedRuleGroups</a>.</p> <p>You cannot nest a <code>ManagedRuleGroupStatement</code>, for example for use inside a <code>NotStatement</code> or <code>OrStatement</code>. You cannot use a managed rule group inside another rule group. You can only reference a managed rule group as a top-level statement within a rule that you define in a web ACL.</p> <note> <p>You are charged additional fees when you use the WAF Bot Control managed rule group <code>AWSManagedRulesBotControlRuleSet</code>, the WAF Fraud Control account takeover prevention (ATP) managed rule group <code>AWSManagedRulesATPRuleSet</code>, or the WAF Fraud Control account creation fraud prevention (ACFP) managed rule group <code>AWSManagedRulesACFPRuleSet</code>. For more information, see <a href="http://aws.amazon.com/waf/pricing/">WAF Pricing</a>.</p> </note>"""
    label_match_statement: NotRequired[
        "capo_wafv2.types.label_match_statement.LabelMatchStatement"
    ]
    """<p>A rule statement to match against labels that have been added to the web request by rules that have already run in the web ACL. </p> <p>The label match statement provides the label or namespace string to search for. The label string can represent a part or all of the fully qualified label name that had been added to the web request. Fully qualified labels have a prefix, optional namespaces, and label name. The prefix identifies the rule group or web ACL context of the rule that added the label. If you do not provide the fully qualified name in your label match string, WAF performs the search for labels that were added in the same context as the label match statement. </p>"""
    regex_match_statement: NotRequired[
        "capo_wafv2.types.regex_match_statement.RegexMatchStatement"
    ]
    """<p>A rule statement used to search web request components for a match against a single regular expression. </p>"""
    asn_match_statement: NotRequired[
        "capo_wafv2.types.asn_match_statement.AsnMatchStatement"
    ]
    """<p>A rule statement that inspects web traffic based on the Autonomous System Number (ASN) associated with the request's IP address.</p> <p>For additional details, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-asn-match.html">ASN match rule statement</a> in the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">WAF Developer Guide</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Statement) -> dict:
    out: dict = {}
    if "byte_match_statement" in value:
        import capo_wafv2.types.byte_match_statement

        out["ByteMatchStatement"] = (
            capo_wafv2.types.byte_match_statement.serialize_aws_json_1_1(
                value["byte_match_statement"]
            )
        )
    if "sqli_match_statement" in value:
        import capo_wafv2.types.sqli_match_statement

        out["SqliMatchStatement"] = (
            capo_wafv2.types.sqli_match_statement.serialize_aws_json_1_1(
                value["sqli_match_statement"]
            )
        )
    if "xss_match_statement" in value:
        import capo_wafv2.types.xss_match_statement

        out["XssMatchStatement"] = (
            capo_wafv2.types.xss_match_statement.serialize_aws_json_1_1(
                value["xss_match_statement"]
            )
        )
    if "size_constraint_statement" in value:
        import capo_wafv2.types.size_constraint_statement

        out["SizeConstraintStatement"] = (
            capo_wafv2.types.size_constraint_statement.serialize_aws_json_1_1(
                value["size_constraint_statement"]
            )
        )
    if "geo_match_statement" in value:
        import capo_wafv2.types.geo_match_statement

        out["GeoMatchStatement"] = (
            capo_wafv2.types.geo_match_statement.serialize_aws_json_1_1(
                value["geo_match_statement"]
            )
        )
    if "rule_group_reference_statement" in value:
        import capo_wafv2.types.rule_group_reference_statement

        out["RuleGroupReferenceStatement"] = (
            capo_wafv2.types.rule_group_reference_statement.serialize_aws_json_1_1(
                value["rule_group_reference_statement"]
            )
        )
    if "ip_set_reference_statement" in value:
        import capo_wafv2.types.ip_set_reference_statement

        out["IPSetReferenceStatement"] = (
            capo_wafv2.types.ip_set_reference_statement.serialize_aws_json_1_1(
                value["ip_set_reference_statement"]
            )
        )
    if "regex_pattern_set_reference_statement" in value:
        import capo_wafv2.types.regex_pattern_set_reference_statement

        out["RegexPatternSetReferenceStatement"] = (
            capo_wafv2.types.regex_pattern_set_reference_statement.serialize_aws_json_1_1(
                value["regex_pattern_set_reference_statement"]
            )
        )
    if "rate_based_statement" in value:
        import capo_wafv2.types.rate_based_statement

        out["RateBasedStatement"] = (
            capo_wafv2.types.rate_based_statement.serialize_aws_json_1_1(
                value["rate_based_statement"]
            )
        )
    if "and_statement" in value:
        import capo_wafv2.types.and_statement

        out["AndStatement"] = capo_wafv2.types.and_statement.serialize_aws_json_1_1(
            value["and_statement"]
        )
    if "or_statement" in value:
        import capo_wafv2.types.or_statement

        out["OrStatement"] = capo_wafv2.types.or_statement.serialize_aws_json_1_1(
            value["or_statement"]
        )
    if "not_statement" in value:
        import capo_wafv2.types.not_statement

        out["NotStatement"] = capo_wafv2.types.not_statement.serialize_aws_json_1_1(
            value["not_statement"]
        )
    if "managed_rule_group_statement" in value:
        import capo_wafv2.types.managed_rule_group_statement

        out["ManagedRuleGroupStatement"] = (
            capo_wafv2.types.managed_rule_group_statement.serialize_aws_json_1_1(
                value["managed_rule_group_statement"]
            )
        )
    if "label_match_statement" in value:
        import capo_wafv2.types.label_match_statement

        out["LabelMatchStatement"] = (
            capo_wafv2.types.label_match_statement.serialize_aws_json_1_1(
                value["label_match_statement"]
            )
        )
    if "regex_match_statement" in value:
        import capo_wafv2.types.regex_match_statement

        out["RegexMatchStatement"] = (
            capo_wafv2.types.regex_match_statement.serialize_aws_json_1_1(
                value["regex_match_statement"]
            )
        )
    if "asn_match_statement" in value:
        import capo_wafv2.types.asn_match_statement

        out["AsnMatchStatement"] = (
            capo_wafv2.types.asn_match_statement.serialize_aws_json_1_1(
                value["asn_match_statement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Statement:
    out: Statement = {}  # type: ignore[typeddict-item]
    if data.get("ByteMatchStatement") is not None:
        import capo_wafv2.types.byte_match_statement

        out["byte_match_statement"] = (
            capo_wafv2.types.byte_match_statement.deserialize_aws_json_1_1(
                data["ByteMatchStatement"]
            )
        )
    if data.get("SqliMatchStatement") is not None:
        import capo_wafv2.types.sqli_match_statement

        out["sqli_match_statement"] = (
            capo_wafv2.types.sqli_match_statement.deserialize_aws_json_1_1(
                data["SqliMatchStatement"]
            )
        )
    if data.get("XssMatchStatement") is not None:
        import capo_wafv2.types.xss_match_statement

        out["xss_match_statement"] = (
            capo_wafv2.types.xss_match_statement.deserialize_aws_json_1_1(
                data["XssMatchStatement"]
            )
        )
    if data.get("SizeConstraintStatement") is not None:
        import capo_wafv2.types.size_constraint_statement

        out["size_constraint_statement"] = (
            capo_wafv2.types.size_constraint_statement.deserialize_aws_json_1_1(
                data["SizeConstraintStatement"]
            )
        )
    if data.get("GeoMatchStatement") is not None:
        import capo_wafv2.types.geo_match_statement

        out["geo_match_statement"] = (
            capo_wafv2.types.geo_match_statement.deserialize_aws_json_1_1(
                data["GeoMatchStatement"]
            )
        )
    if data.get("RuleGroupReferenceStatement") is not None:
        import capo_wafv2.types.rule_group_reference_statement

        out["rule_group_reference_statement"] = (
            capo_wafv2.types.rule_group_reference_statement.deserialize_aws_json_1_1(
                data["RuleGroupReferenceStatement"]
            )
        )
    if data.get("IPSetReferenceStatement") is not None:
        import capo_wafv2.types.ip_set_reference_statement

        out["ip_set_reference_statement"] = (
            capo_wafv2.types.ip_set_reference_statement.deserialize_aws_json_1_1(
                data["IPSetReferenceStatement"]
            )
        )
    if data.get("RegexPatternSetReferenceStatement") is not None:
        import capo_wafv2.types.regex_pattern_set_reference_statement

        out["regex_pattern_set_reference_statement"] = (
            capo_wafv2.types.regex_pattern_set_reference_statement.deserialize_aws_json_1_1(
                data["RegexPatternSetReferenceStatement"]
            )
        )
    if data.get("RateBasedStatement") is not None:
        import capo_wafv2.types.rate_based_statement

        out["rate_based_statement"] = (
            capo_wafv2.types.rate_based_statement.deserialize_aws_json_1_1(
                data["RateBasedStatement"]
            )
        )
    if data.get("AndStatement") is not None:
        import capo_wafv2.types.and_statement

        out["and_statement"] = capo_wafv2.types.and_statement.deserialize_aws_json_1_1(
            data["AndStatement"]
        )
    if data.get("OrStatement") is not None:
        import capo_wafv2.types.or_statement

        out["or_statement"] = capo_wafv2.types.or_statement.deserialize_aws_json_1_1(
            data["OrStatement"]
        )
    if data.get("NotStatement") is not None:
        import capo_wafv2.types.not_statement

        out["not_statement"] = capo_wafv2.types.not_statement.deserialize_aws_json_1_1(
            data["NotStatement"]
        )
    if data.get("ManagedRuleGroupStatement") is not None:
        import capo_wafv2.types.managed_rule_group_statement

        out["managed_rule_group_statement"] = (
            capo_wafv2.types.managed_rule_group_statement.deserialize_aws_json_1_1(
                data["ManagedRuleGroupStatement"]
            )
        )
    if data.get("LabelMatchStatement") is not None:
        import capo_wafv2.types.label_match_statement

        out["label_match_statement"] = (
            capo_wafv2.types.label_match_statement.deserialize_aws_json_1_1(
                data["LabelMatchStatement"]
            )
        )
    if data.get("RegexMatchStatement") is not None:
        import capo_wafv2.types.regex_match_statement

        out["regex_match_statement"] = (
            capo_wafv2.types.regex_match_statement.deserialize_aws_json_1_1(
                data["RegexMatchStatement"]
            )
        )
    if data.get("AsnMatchStatement") is not None:
        import capo_wafv2.types.asn_match_statement

        out["asn_match_statement"] = (
            capo_wafv2.types.asn_match_statement.deserialize_aws_json_1_1(
                data["AsnMatchStatement"]
            )
        )
    return out
