"""Generated from Smithy shape ``com.amazonaws.wafv2#MonetizationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.monetization_filter_name
    import capo_wafv2.types.monetization_filter_value_list


class MonetizationFilter(TypedDict, closed=True):
    name: "capo_wafv2.types.monetization_filter_name.MonetizationFilterName"
    r"""<p>The filter name. Format: Key is a string, Value is a list of strings.</p> <p>Enum-restricted (invalid values rejected):</p> <ul> <li> <p> <code>CurrencyMode</code>: <code>REAL</code>, <code>TEST</code> </p> </li> <li> <p> <code>ChainName</code>: <code>BASE</code>, <code>SOLANA</code>, <code>BASE_SEPOLIA</code>, <code>SOLANA_DEVNET</code> </p> </li> <li> <p> <code>SettlementStatus</code>: <code>SETTLED</code>, <code>PENDING</code>, <code>FAILED</code>, <code>SERVICE_ERROR</code>, <code>SKIPPED_ORIGIN_ERROR</code>, <code>DUPLICATE</code> </p> </li> <li> <p> <code>HttpSourceName</code>: <code>CF</code>, <code>ALB</code>, <code>APIGW</code>, <code>APPRUNNER</code>, <code>COGNITO</code>, <code>VERIFIED_ACCESS</code> </p> </li> </ul> <p>ARN-validated:</p> <ul> <li> <p> <code>WebACLArn</code>: valid WAFv2 web ACL ARN</p> </li> </ul> <p>Free-text (any string up to 256 chars):</p> <ul> <li> <p> <code>SourceName</code>: The name of the bot. Populated from Bot Control verified bot labels.</p> </li> <li> <p> <code>SourceCategory</code>: The category classification of the bot. From Bot Control categorization.</p> </li> <li> <p> <code>Intent</code>: The declared intent of the bot request.</p> </li> <li> <p> <code>Organization</code>: The organization operating the bot.</p> </li> <li> <p> <code>UriPathPrefix</code>: The URI path of the request that was monetized.</p> </li> <li> <p> <code>RequestId</code>: The WAF request ID associated with the transaction. Matches the requestId in WAF logs. Pattern: <code>^[a-zA-Z0-9:._\-=+/]+$</code> </p> </li> <li> <p> <code>TransactionId</code>: The blockchain transaction identifier. Pattern: <code>^[a-zA-Z0-9:._\-=+/]+$</code> </p> </li> <li> <p> <code>TerminatingRuleName</code>: The name of the WAF rule that triggered the Monetize action.</p> </li> <li> <p> <code>PayerAddress</code>: The blockchain wallet address of the paying client. Pattern: <code>^[a-zA-Z0-9:._\-=+/]+$</code> </p> </li> <li> <p> <code>HttpSourceId</code>: The identifier of the Amazon Web Services resource associated with the web ACL (for example, CloudFront distribution ID).</p> </li> </ul>"""
    values: (
        "capo_wafv2.types.monetization_filter_value_list.MonetizationFilterValueList"
    )
    """<p>The values to filter on. Specify as a list of strings. Results match any of the specified values (OR logic). Duplicate values are silently deduplicated. Maximum: 20 values per filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonetizationFilter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.monetization_filter_value_list

    out["Values"] = (
        capo_wafv2.types.monetization_filter_value_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonetizationFilter:
    out: MonetizationFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Values") is not None:
        import capo_wafv2.types.monetization_filter_value_list

        out["values"] = (
            capo_wafv2.types.monetization_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
