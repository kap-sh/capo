"""Generated from Smithy shape ``com.amazonaws.forecast#DataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.additional_datasets
    import capo_forecast.types.arn
    import capo_forecast.types.attribute_configs


class DataConfig(TypedDict, closed=True):
    dataset_group_arn: "capo_forecast.types.arn.Arn"
    """<p>The ARN of the dataset group used to train the predictor.</p>"""
    attribute_configs: NotRequired[
        "capo_forecast.types.attribute_configs.AttributeConfigs"
    ]
    """<p>Aggregation and filling options for attributes in your dataset group.</p>"""
    additional_datasets: NotRequired[
        "capo_forecast.types.additional_datasets.AdditionalDatasets"
    ]
    """<p>Additional built-in datasets like Holidays and the Weather Index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataConfig) -> dict:
    out: dict = {}
    out["DatasetGroupArn"] = value["dataset_group_arn"]
    if "attribute_configs" in value:
        import capo_forecast.types.attribute_configs

        out["AttributeConfigs"] = (
            capo_forecast.types.attribute_configs.serialize_aws_json_1_1(
                value["attribute_configs"]
            )
        )
    if "additional_datasets" in value:
        import capo_forecast.types.additional_datasets

        out["AdditionalDatasets"] = (
            capo_forecast.types.additional_datasets.serialize_aws_json_1_1(
                value["additional_datasets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataConfig:
    out: DataConfig = {}  # type: ignore[typeddict-item]
    if data.get("DatasetGroupArn") is not None:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    else:
        out["dataset_group_arn"] = ""
    if data.get("AttributeConfigs") is not None:
        import capo_forecast.types.attribute_configs

        out["attribute_configs"] = (
            capo_forecast.types.attribute_configs.deserialize_aws_json_1_1(
                data["AttributeConfigs"]
            )
        )
    if data.get("AdditionalDatasets") is not None:
        import capo_forecast.types.additional_datasets

        out["additional_datasets"] = (
            capo_forecast.types.additional_datasets.deserialize_aws_json_1_1(
                data["AdditionalDatasets"]
            )
        )
    return out
