"""Generated from Smithy shape ``com.amazonaws.forecast#InputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.supplementary_features


class InputDataConfig(TypedDict, closed=True):
    dataset_group_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group.</p>"""
    supplementary_features: NotRequired[
        "capo_forecast.types.supplementary_features.SupplementaryFeatures"
    ]
    """<p>An array of supplementary features. The only supported feature is a holiday calendar.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDataConfig) -> dict:
    out: dict = {}
    out["DatasetGroupArn"] = value["dataset_group_arn"]
    if "supplementary_features" in value:
        import capo_forecast.types.supplementary_features

        out["SupplementaryFeatures"] = (
            capo_forecast.types.supplementary_features.serialize_aws_json_1_1(
                value["supplementary_features"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputDataConfig:
    out: InputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("DatasetGroupArn") is not None:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    else:
        out["dataset_group_arn"] = ""
    if data.get("SupplementaryFeatures") is not None:
        import capo_forecast.types.supplementary_features

        out["supplementary_features"] = (
            capo_forecast.types.supplementary_features.deserialize_aws_json_1_1(
                data["SupplementaryFeatures"]
            )
        )
    return out
