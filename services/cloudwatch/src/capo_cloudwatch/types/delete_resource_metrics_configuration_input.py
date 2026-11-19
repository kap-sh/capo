"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteResourceMetricsConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.resource_arn


class DeleteResourceMetricsConfigurationInput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_cloudwatch.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to delete the resource metrics configuration for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteResourceMetricsConfigurationInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteResourceMetricsConfigurationInput:
    out: DeleteResourceMetricsConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteResourceMetricsConfigurationInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))


def deserialize_query(el: Element) -> DeleteResourceMetricsConfigurationInput:
    out: DeleteResourceMetricsConfigurationInput = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteResourceMetricsConfigurationInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_cbor(data: dict) -> DeleteResourceMetricsConfigurationInput:
    out: DeleteResourceMetricsConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    return out
