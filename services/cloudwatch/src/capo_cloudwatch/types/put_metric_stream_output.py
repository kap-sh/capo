"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutMetricStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.amazon_resource_name


class PutMetricStreamOutput(TypedDict, closed=True):
    arn: NotRequired["capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"]
    """<p>The ARN of the metric stream.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMetricStreamOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMetricStreamOutput:
    out: PutMetricStreamOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutMetricStreamOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))


def deserialize_query(el: Element) -> PutMetricStreamOutput:
    out: PutMetricStreamOutput = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutMetricStreamOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> PutMetricStreamOutput:
    out: PutMetricStreamOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
