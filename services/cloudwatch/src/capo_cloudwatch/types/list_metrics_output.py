"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListMetricsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metrics
    import capo_cloudwatch.types.next_token
    import capo_cloudwatch.types.owning_accounts


class ListMetricsOutput(TypedDict, closed=True):
    metrics: NotRequired["capo_cloudwatch.types.metrics.Metrics"]
    """<p>The metrics that match your request. </p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results. </p>"""
    owning_accounts: NotRequired["capo_cloudwatch.types.owning_accounts.OwningAccounts"]
    """<p>If you are using this operation in a monitoring account, this array contains the account IDs of the source accounts where the metrics in the returned data are from.</p> <p>This field is a 1:1 mapping between each metric that is returned and the ID of the owning account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMetricsOutput) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_cloudwatch.types.metrics

        out["Metrics"] = capo_cloudwatch.types.metrics.serialize_aws_json_1_0(
            value["metrics"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "owning_accounts" in value:
        import capo_cloudwatch.types.owning_accounts

        out["OwningAccounts"] = (
            capo_cloudwatch.types.owning_accounts.serialize_aws_json_1_0(
                value["owning_accounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMetricsOutput:
    out: ListMetricsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Metrics") is not None:
        import capo_cloudwatch.types.metrics

        out["metrics"] = capo_cloudwatch.types.metrics.deserialize_aws_json_1_0(
            data["Metrics"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("OwningAccounts") is not None:
        import capo_cloudwatch.types.owning_accounts

        out["owning_accounts"] = (
            capo_cloudwatch.types.owning_accounts.deserialize_aws_json_1_0(
                data["OwningAccounts"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListMetricsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metrics" in value:
        import capo_cloudwatch.types.metrics

        capo_cloudwatch.types.metrics.serialize_query(
            value["metrics"], pairs, f"{key_prefix}Metrics"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "owning_accounts" in value:
        import capo_cloudwatch.types.owning_accounts

        capo_cloudwatch.types.owning_accounts.serialize_query(
            value["owning_accounts"], pairs, f"{key_prefix}OwningAccounts"
        )


def deserialize_query(el: Element) -> ListMetricsOutput:
    out: ListMetricsOutput = {}  # type: ignore[typeddict-item]
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import capo_cloudwatch.types.metrics

        out["metrics"] = capo_cloudwatch.types.metrics.deserialize_query(child_metrics)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_owning_accounts = el.find("OwningAccounts")
    if child_owning_accounts is not None:
        import capo_cloudwatch.types.owning_accounts

        out["owning_accounts"] = (
            capo_cloudwatch.types.owning_accounts.deserialize_query(
                child_owning_accounts
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMetricsOutput) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_cloudwatch.types.metrics

        out["Metrics"] = capo_cloudwatch.types.metrics.serialize_cbor(value["metrics"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "owning_accounts" in value:
        import capo_cloudwatch.types.owning_accounts

        out["OwningAccounts"] = capo_cloudwatch.types.owning_accounts.serialize_cbor(
            value["owning_accounts"]
        )
    return out


def deserialize_cbor(data: dict) -> ListMetricsOutput:
    out: ListMetricsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Metrics") is not None:
        import capo_cloudwatch.types.metrics

        out["metrics"] = capo_cloudwatch.types.metrics.deserialize_cbor(data["Metrics"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("OwningAccounts") is not None:
        import capo_cloudwatch.types.owning_accounts

        out["owning_accounts"] = capo_cloudwatch.types.owning_accounts.deserialize_cbor(
            data["OwningAccounts"]
        )
    return out
