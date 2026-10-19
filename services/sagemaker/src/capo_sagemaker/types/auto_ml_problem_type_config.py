"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLProblemTypeConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.image_classification_job_config
    import capo_sagemaker.types.tabular_job_config
    import capo_sagemaker.types.text_classification_job_config
    import capo_sagemaker.types.text_generation_job_config
    import capo_sagemaker.types.time_series_forecasting_job_config


class _AutoMLProblemTypeConfig_ImageClassificationJobConfig(TypedDict, closed=True):
    ImageClassificationJobConfig: "capo_sagemaker.types.image_classification_job_config.ImageClassificationJobConfig"


class _AutoMLProblemTypeConfig_TextClassificationJobConfig(TypedDict, closed=True):
    TextClassificationJobConfig: "capo_sagemaker.types.text_classification_job_config.TextClassificationJobConfig"


class _AutoMLProblemTypeConfig_TimeSeriesForecastingJobConfig(TypedDict, closed=True):
    TimeSeriesForecastingJobConfig: "capo_sagemaker.types.time_series_forecasting_job_config.TimeSeriesForecastingJobConfig"


class _AutoMLProblemTypeConfig_TabularJobConfig(TypedDict, closed=True):
    TabularJobConfig: "capo_sagemaker.types.tabular_job_config.TabularJobConfig"


class _AutoMLProblemTypeConfig_TextGenerationJobConfig(TypedDict, closed=True):
    TextGenerationJobConfig: (
        "capo_sagemaker.types.text_generation_job_config.TextGenerationJobConfig"
    )


AutoMLProblemTypeConfig: TypeAlias = (
    _AutoMLProblemTypeConfig_ImageClassificationJobConfig
    | _AutoMLProblemTypeConfig_TextClassificationJobConfig
    | _AutoMLProblemTypeConfig_TimeSeriesForecastingJobConfig
    | _AutoMLProblemTypeConfig_TabularJobConfig
    | _AutoMLProblemTypeConfig_TextGenerationJobConfig
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLProblemTypeConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AutoMLProblemTypeConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "ImageClassificationJobConfig" in value:
        import capo_sagemaker.types.image_classification_job_config

        return {
            "ImageClassificationJobConfig": capo_sagemaker.types.image_classification_job_config.serialize_aws_json_1_1(
                value["ImageClassificationJobConfig"]
            )
        }
    elif "TextClassificationJobConfig" in value:
        import capo_sagemaker.types.text_classification_job_config

        return {
            "TextClassificationJobConfig": capo_sagemaker.types.text_classification_job_config.serialize_aws_json_1_1(
                value["TextClassificationJobConfig"]
            )
        }
    elif "TimeSeriesForecastingJobConfig" in value:
        import capo_sagemaker.types.time_series_forecasting_job_config

        return {
            "TimeSeriesForecastingJobConfig": capo_sagemaker.types.time_series_forecasting_job_config.serialize_aws_json_1_1(
                value["TimeSeriesForecastingJobConfig"]
            )
        }
    elif "TabularJobConfig" in value:
        import capo_sagemaker.types.tabular_job_config

        return {
            "TabularJobConfig": capo_sagemaker.types.tabular_job_config.serialize_aws_json_1_1(
                value["TabularJobConfig"]
            )
        }
    elif "TextGenerationJobConfig" in value:
        import capo_sagemaker.types.text_generation_job_config

        return {
            "TextGenerationJobConfig": capo_sagemaker.types.text_generation_job_config.serialize_aws_json_1_1(
                value["TextGenerationJobConfig"]
            )
        }
    else:
        raise SerializationError("AutoMLProblemTypeConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AutoMLProblemTypeConfig:
    if data.get("ImageClassificationJobConfig") is not None:
        import capo_sagemaker.types.image_classification_job_config

        return {
            "ImageClassificationJobConfig": capo_sagemaker.types.image_classification_job_config.deserialize_aws_json_1_1(
                data["ImageClassificationJobConfig"]
            )
        }
    elif data.get("TextClassificationJobConfig") is not None:
        import capo_sagemaker.types.text_classification_job_config

        return {
            "TextClassificationJobConfig": capo_sagemaker.types.text_classification_job_config.deserialize_aws_json_1_1(
                data["TextClassificationJobConfig"]
            )
        }
    elif data.get("TimeSeriesForecastingJobConfig") is not None:
        import capo_sagemaker.types.time_series_forecasting_job_config

        return {
            "TimeSeriesForecastingJobConfig": capo_sagemaker.types.time_series_forecasting_job_config.deserialize_aws_json_1_1(
                data["TimeSeriesForecastingJobConfig"]
            )
        }
    elif data.get("TabularJobConfig") is not None:
        import capo_sagemaker.types.tabular_job_config

        return {
            "TabularJobConfig": capo_sagemaker.types.tabular_job_config.deserialize_aws_json_1_1(
                data["TabularJobConfig"]
            )
        }
    elif data.get("TextGenerationJobConfig") is not None:
        import capo_sagemaker.types.text_generation_job_config

        return {
            "TextGenerationJobConfig": capo_sagemaker.types.text_generation_job_config.deserialize_aws_json_1_1(
                data["TextGenerationJobConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AutoMLProblemTypeConfig: no recognized variant key")
