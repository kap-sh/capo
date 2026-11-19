"""Generated from Smithy shape ``com.amazonaws.cloudwatch#CreateResourceMetricsConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.resource_metrics_configuration


class CreateResourceMetricsConfigurationOutput(TypedDict, closed=True):
    resource_metrics_configuration: NotRequired[
        "capo_cloudwatch.types.resource_metrics_configuration.ResourceMetricsConfiguration"
    ]
    """<p>The resource metrics configuration that was created by this operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateResourceMetricsConfigurationOutput) -> dict:
    out: dict = {}
    if "resource_metrics_configuration" in value:
        import capo_cloudwatch.types.resource_metrics_configuration

        out["ResourceMetricsConfiguration"] = (
            capo_cloudwatch.types.resource_metrics_configuration.serialize_aws_json_1_0(
                value["resource_metrics_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateResourceMetricsConfigurationOutput:
    out: CreateResourceMetricsConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceMetricsConfiguration") is not None:
        import capo_cloudwatch.types.resource_metrics_configuration

        out["resource_metrics_configuration"] = (
            capo_cloudwatch.types.resource_metrics_configuration.deserialize_aws_json_1_0(
                data["ResourceMetricsConfiguration"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateResourceMetricsConfigurationOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_metrics_configuration" in value:
        import capo_cloudwatch.types.resource_metrics_configuration

        capo_cloudwatch.types.resource_metrics_configuration.serialize_query(
            value["resource_metrics_configuration"],
            pairs,
            f"{key_prefix}ResourceMetricsConfiguration",
        )


def deserialize_query(el: Element) -> CreateResourceMetricsConfigurationOutput:
    out: CreateResourceMetricsConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_resource_metrics_configuration = el.find("ResourceMetricsConfiguration")
    if child_resource_metrics_configuration is not None:
        import capo_cloudwatch.types.resource_metrics_configuration

        out["resource_metrics_configuration"] = (
            capo_cloudwatch.types.resource_metrics_configuration.deserialize_query(
                child_resource_metrics_configuration
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateResourceMetricsConfigurationOutput) -> dict:
    out: dict = {}
    if "resource_metrics_configuration" in value:
        import capo_cloudwatch.types.resource_metrics_configuration

        out["ResourceMetricsConfiguration"] = (
            capo_cloudwatch.types.resource_metrics_configuration.serialize_cbor(
                value["resource_metrics_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateResourceMetricsConfigurationOutput:
    out: CreateResourceMetricsConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceMetricsConfiguration") is not None:
        import capo_cloudwatch.types.resource_metrics_configuration

        out["resource_metrics_configuration"] = (
            capo_cloudwatch.types.resource_metrics_configuration.deserialize_cbor(
                data["ResourceMetricsConfiguration"]
            )
        )
    return out
