"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EnableInsightRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.batch_failures


class EnableInsightRulesOutput(TypedDict, closed=True):
    failures: NotRequired["capo_cloudwatch.types.batch_failures.BatchFailures"]
    """<p>An array listing the rules that could not be enabled. You cannot disable or enable built-in rules.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnableInsightRulesOutput) -> dict:
    out: dict = {}
    if "failures" in value:
        import capo_cloudwatch.types.batch_failures

        out["Failures"] = capo_cloudwatch.types.batch_failures.serialize_aws_json_1_0(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnableInsightRulesOutput:
    out: EnableInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Failures") is not None:
        import capo_cloudwatch.types.batch_failures

        out["failures"] = capo_cloudwatch.types.batch_failures.deserialize_aws_json_1_0(
            data["Failures"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableInsightRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "failures" in value:
        import capo_cloudwatch.types.batch_failures

        capo_cloudwatch.types.batch_failures.serialize_query(
            value["failures"], pairs, f"{key_prefix}Failures"
        )


def deserialize_query(el: Element) -> EnableInsightRulesOutput:
    out: EnableInsightRulesOutput = {}  # type: ignore[typeddict-item]
    child_failures = el.find("Failures")
    if child_failures is not None:
        import capo_cloudwatch.types.batch_failures

        out["failures"] = capo_cloudwatch.types.batch_failures.deserialize_query(
            child_failures
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableInsightRulesOutput) -> dict:
    out: dict = {}
    if "failures" in value:
        import capo_cloudwatch.types.batch_failures

        out["Failures"] = capo_cloudwatch.types.batch_failures.serialize_cbor(
            value["failures"]
        )
    return out


def deserialize_cbor(data: dict) -> EnableInsightRulesOutput:
    out: EnableInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Failures") is not None:
        import capo_cloudwatch.types.batch_failures

        out["failures"] = capo_cloudwatch.types.batch_failures.deserialize_cbor(
            data["Failures"]
        )
    return out
