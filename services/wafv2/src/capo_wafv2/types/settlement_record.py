"""Generated from Smithy shape ``com.amazonaws.wafv2#SettlementRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.currency
    import capo_wafv2.types.filter_string
    import capo_wafv2.types.monetization_amount_value
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.settlement_filter_string
    import capo_wafv2.types.settlement_id_string
    import capo_wafv2.types.settlement_status
    import capo_wafv2.types.timestamp
    import capo_wafv2.types.verified_status


class SettlementRecord(TypedDict, closed=True):
    timestamp: "capo_wafv2.types.timestamp.Timestamp"
    """<p>The timestamp when the settlement was recorded.</p>"""
    payer_address: NotRequired[
        "capo_wafv2.types.settlement_filter_string.SettlementFilterString"
    ]
    """<p>The blockchain wallet address of the paying AI agent.</p>"""
    wallet_address: NotRequired[
        "capo_wafv2.types.settlement_filter_string.SettlementFilterString"
    ]
    """<p>Your receiving wallet address.</p>"""
    status: "capo_wafv2.types.settlement_status.SettlementStatus"
    """<p>The status of the settlement. Possible values:</p> <ul> <li> <p> <code>SETTLED</code> - The payment was successfully settled on the blockchain and the transfer from the payer's wallet to the publisher's wallet is confirmed. The <code>TransactionId</code> field contains the on-chain transaction hash. Content is served to the client.</p> </li> <li> <p> <code>PENDING</code> - The blockchain transaction has been submitted but not yet confirmed on-chain. This is a transient state that automatically resolves to either <code>SETTLED</code> or <code>FAILED</code>. No action is required. While pending, content is not served and the API returns a 402 response. Clients can retry the request.</p> </li> <li> <p> <code>FAILED</code> - The payment settlement was attempted but failed. Possible causes include insufficient funds, an expired payment authorization, or a reverted blockchain transaction. The <code>failureReason</code> field contains a machine-readable error code. Content is not served.</p> </li> <li> <p> <code>SERVICE_ERROR</code> - Settlement could not be completed due to an internal service issue or an issue with the payment network. Content is not served. The client's payment authorization remains valid and the request can be retried.</p> </li> <li> <p> <code>SKIPPED_ORIGIN_ERROR</code> - The origin returned a non-2xx response, so settlement was intentionally skipped. The client is not charged.</p> </li> <li> <p> <code>DUPLICATE</code> - A prior request with the same payment payload has already been settled. This status typically appears when a previous attempt timed out but the payment was ultimately processed. The client is not charged again.</p> </li> </ul>"""
    amount: "capo_wafv2.types.monetization_amount_value.MonetizationAmountValue"
    """<p>The payment amount in the specified currency.</p>"""
    currency: NotRequired["capo_wafv2.types.currency.Currency"]
    """<p>The currency of the payment amount.</p>"""
    network: NotRequired[
        "capo_wafv2.types.settlement_filter_string.SettlementFilterString"
    ]
    """<p>The blockchain network on which the settlement occurred.</p>"""
    transaction_id: NotRequired[
        "capo_wafv2.types.settlement_id_string.SettlementIdString"
    ]
    """<p>The blockchain transaction identifier. You can use this to verify the transaction on a blockchain explorer.</p>"""
    request_id: NotRequired[
        "capo_wafv2.types.settlement_filter_string.SettlementFilterString"
    ]
    """<p>The WAF request ID associated with this settlement.</p>"""
    source_name: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The name of the AI bot that made the payment.</p>"""
    organization: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The organization associated with the AI bot.</p>"""
    source_category: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The category of the AI bot source.</p>"""
    intent: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The declared intent of the AI bot request.</p>"""
    verified: "capo_wafv2.types.verified_status.VerifiedStatus"
    """<p>Whether the AI bot's identity was verified.</p>"""
    content_path: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The content path that was accessed.</p>"""
    web_acl_arn: NotRequired["capo_wafv2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the web ACL that processed the request.</p>"""
    request_timestamp: NotRequired["capo_wafv2.types.timestamp.Timestamp"]
    """<p>The timestamp of the original web request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettlementRecord) -> dict:
    out: dict = {}
    import capo_wafv2.types.timestamp

    out["Timestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
        value["timestamp"]
    )
    if "payer_address" in value:
        out["PayerAddress"] = value["payer_address"]
    if "wallet_address" in value:
        out["WalletAddress"] = value["wallet_address"]
    import capo_wafv2.types.settlement_status

    out["Status"] = capo_wafv2.types.settlement_status.serialize_aws_json_1_1(
        value["status"]
    )
    out["Amount"] = value["amount"]
    if "currency" in value:
        import capo_wafv2.types.currency

        out["Currency"] = capo_wafv2.types.currency.serialize_aws_json_1_1(
            value["currency"]
        )
    if "network" in value:
        out["Network"] = value["network"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    if "organization" in value:
        out["Organization"] = value["organization"]
    if "source_category" in value:
        out["SourceCategory"] = value["source_category"]
    if "intent" in value:
        out["Intent"] = value["intent"]
    out["Verified"] = value.get("verified", False)
    if "content_path" in value:
        out["ContentPath"] = value["content_path"]
    if "web_acl_arn" in value:
        out["WebAclArn"] = value["web_acl_arn"]
    if "request_timestamp" in value:
        import capo_wafv2.types.timestamp

        out["RequestTimestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["request_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SettlementRecord:
    out: SettlementRecord = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_wafv2.types.timestamp

        out["timestamp"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("PayerAddress") is not None:
        out["payer_address"] = data["PayerAddress"]
    if data.get("WalletAddress") is not None:
        out["wallet_address"] = data["WalletAddress"]
    if data.get("Status") is not None:
        import capo_wafv2.types.settlement_status

        out["status"] = capo_wafv2.types.settlement_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_wafv2.types.settlement_status.SettlementStatus", ""
        )
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    else:
        out["amount"] = ""
    if data.get("Currency") is not None:
        import capo_wafv2.types.currency

        out["currency"] = capo_wafv2.types.currency.deserialize_aws_json_1_1(
            data["Currency"]
        )
    if data.get("Network") is not None:
        out["network"] = data["Network"]
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("SourceName") is not None:
        out["source_name"] = data["SourceName"]
    if data.get("Organization") is not None:
        out["organization"] = data["Organization"]
    if data.get("SourceCategory") is not None:
        out["source_category"] = data["SourceCategory"]
    if data.get("Intent") is not None:
        out["intent"] = data["Intent"]
    if data.get("Verified") is not None:
        out["verified"] = data["Verified"]
    else:
        out["verified"] = False
    if data.get("ContentPath") is not None:
        out["content_path"] = data["ContentPath"]
    if data.get("WebAclArn") is not None:
        out["web_acl_arn"] = data["WebAclArn"]
    if data.get("RequestTimestamp") is not None:
        import capo_wafv2.types.timestamp

        out["request_timestamp"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["RequestTimestamp"]
        )
    return out
