"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DisableInsightRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.batch_failures


class DisableInsightRulesOutput(TypedDict, closed=True):
    failures: NotRequired["capo_cloudwatch.types.batch_failures.BatchFailures"]
    """<p>An array listing the rules that could not be disabled. You cannot disable built-in rules.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisableInsightRulesOutput) -> dict:
    out: dict = {}
    if "failures" in value:
        import capo_cloudwatch.types.batch_failures

        out["Failures"] = capo_cloudwatch.types.batch_failures.serialize_aws_json_1_0(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisableInsightRulesOutput:
    out: DisableInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Failures") is not None:
        import capo_cloudwatch.types.batch_failures

        out["failures"] = capo_cloudwatch.types.batch_failures.deserialize_aws_json_1_0(
            data["Failures"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DisableInsightRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "failures" in value:
        import capo_cloudwatch.types.batch_failures

        capo_cloudwatch.types.batch_failures.serialize_query(
            value["failures"], pairs, f"{key_prefix}Failures"
        )


def deserialize_query(el: Element) -> DisableInsightRulesOutput:
    out: DisableInsightRulesOutput = {}  # type: ignore[typeddict-item]
    child_failures = el.find("Failures")
    if child_failures is not None:
        import capo_cloudwatch.types.batch_failures

        out["failures"] = capo_cloudwatch.types.batch_failures.deserialize_query(
            child_failures
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableInsightRulesOutput) -> dict:
    out: dict = {}
    if "failures" in value:
        import capo_cloudwatch.types.batch_failures

        out["Failures"] = capo_cloudwatch.types.batch_failures.serialize_cbor(
            value["failures"]
        )
    return out


def deserialize_cbor(data: dict) -> DisableInsightRulesOutput:
    out: DisableInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Failures") is not None:
        import capo_cloudwatch.types.batch_failures

        out["failures"] = capo_cloudwatch.types.batch_failures.deserialize_cbor(
            data["Failures"]
        )
    return out
