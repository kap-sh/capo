"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmPromQLCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.pending_period
    import capo_cloudwatch.types.query
    import capo_cloudwatch.types.recovery_period


class AlarmPromQLCriteria(TypedDict, closed=True):
    query: NotRequired["capo_cloudwatch.types.query.Query"]
    """<p>The PromQL query that the alarm evaluates. The query must return a result of vector type. Each entry in the vector result represents an alarm contributor.</p>"""
    pending_period: NotRequired["capo_cloudwatch.types.pending_period.PendingPeriod"]
    """<p>The duration, in seconds, that a contributor must be continuously breaching before it transitions to the <code>ALARM</code> state.</p>"""
    recovery_period: NotRequired["capo_cloudwatch.types.recovery_period.RecoveryPeriod"]
    """<p>The duration, in seconds, that a contributor must continuously not be breaching before it transitions back to the <code>OK</code> state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmPromQLCriteria) -> dict:
    out: dict = {}
    if "query" in value:
        out["Query"] = value["query"]
    if "pending_period" in value:
        out["PendingPeriod"] = value["pending_period"]
    if "recovery_period" in value:
        out["RecoveryPeriod"] = value["recovery_period"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AlarmPromQLCriteria:
    out: AlarmPromQLCriteria = {}  # type: ignore[typeddict-item]
    if data.get("Query") is not None:
        out["query"] = data["Query"]
    if data.get("PendingPeriod") is not None:
        out["pending_period"] = data["PendingPeriod"]
    if data.get("RecoveryPeriod") is not None:
        out["recovery_period"] = data["RecoveryPeriod"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmPromQLCriteria, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "query" in value:
        pairs.append((f"{key_prefix}Query", str(value["query"])))
    if "pending_period" in value:
        pairs.append((f"{key_prefix}PendingPeriod", str(value["pending_period"])))
    if "recovery_period" in value:
        pairs.append((f"{key_prefix}RecoveryPeriod", str(value["recovery_period"])))


def deserialize_query(el: Element) -> AlarmPromQLCriteria:
    out: AlarmPromQLCriteria = {}  # type: ignore[typeddict-item]
    child_query = el.find("Query")
    if child_query is not None:
        out["query"] = str(child_query.text or "")
    child_pending_period = el.find("PendingPeriod")
    if child_pending_period is not None:
        out["pending_period"] = int(child_pending_period.text or "")
    child_recovery_period = el.find("RecoveryPeriod")
    if child_recovery_period is not None:
        out["recovery_period"] = int(child_recovery_period.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmPromQLCriteria) -> dict:
    out: dict = {}
    if "query" in value:
        out["Query"] = value["query"]
    if "pending_period" in value:
        out["PendingPeriod"] = value["pending_period"]
    if "recovery_period" in value:
        out["RecoveryPeriod"] = value["recovery_period"]
    return out


def deserialize_cbor(data: dict) -> AlarmPromQLCriteria:
    out: AlarmPromQLCriteria = {}  # type: ignore[typeddict-item]
    if data.get("Query") is not None:
        out["query"] = data["Query"]
    if data.get("PendingPeriod") is not None:
        out["pending_period"] = data["PendingPeriod"]
    if data.get("RecoveryPeriod") is not None:
        out["recovery_period"] = data["RecoveryPeriod"]
    return out
