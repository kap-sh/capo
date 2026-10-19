"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsConfigConnectorArnFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.aws_config_connector_arn
    import capo_inspector2.types.aws_config_connector_arn_comparison


class AwsConfigConnectorArnFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.aws_config_connector_arn_comparison.AwsConfigConnectorArnComparison"
    """<p>The comparison operator for the Amazon Web Services Config connector ARN filter.</p>"""
    value: "capo_inspector2.types.aws_config_connector_arn.AwsConfigConnectorArn"
    """<p>The Amazon Web Services Config connector ARN value to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsConfigConnectorArnFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.aws_config_connector_arn_comparison

    out["comparison"] = (
        capo_inspector2.types.aws_config_connector_arn_comparison.serialize_json(
            value["comparison"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsConfigConnectorArnFilter:
    out: AwsConfigConnectorArnFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.aws_config_connector_arn_comparison

        out["comparison"] = (
            capo_inspector2.types.aws_config_connector_arn_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_inspector2.types.aws_config_connector_arn_comparison.AwsConfigConnectorArnComparison",
            "",
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
