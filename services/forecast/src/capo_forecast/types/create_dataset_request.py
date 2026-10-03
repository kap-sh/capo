"""Generated from Smithy shape ``com.amazonaws.forecast#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.dataset_type
    import capo_forecast.types.domain
    import capo_forecast.types.encryption_config
    import capo_forecast.types.frequency
    import capo_forecast.types.name
    import capo_forecast.types.schema
    import capo_forecast.types.tags


class CreateDatasetRequest(TypedDict, closed=True):
    dataset_name: "capo_forecast.types.name.Name"
    """<p>A name for the dataset.</p>"""
    domain: "capo_forecast.types.domain.Domain"
    """<p>The domain associated with the dataset. When you add a dataset to a dataset group, this value and the value specified for the <code>Domain</code> parameter of the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a> operation must match.</p> <p>The <code>Domain</code> and <code>DatasetType</code> that you choose determine the fields that must be present in the training data that you import to the dataset. For example, if you choose the <code>RETAIL</code> domain and <code>TARGET_TIME_SERIES</code> as the <code>DatasetType</code>, Amazon Forecast requires <code>item_id</code>, <code>timestamp</code>, and <code>demand</code> fields to be present in your data. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html">Importing datasets</a>.</p>"""
    dataset_type: "capo_forecast.types.dataset_type.DatasetType"
    """<p>The dataset type. Valid values depend on the chosen <code>Domain</code>.</p>"""
    data_frequency: NotRequired["capo_forecast.types.frequency.Frequency"]
    """<p>The frequency of data collection. This parameter is required for RELATED_TIME_SERIES datasets.</p> <p>Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example, "1D" indicates every day and "15min" indicates every 15 minutes. You cannot specify a value that would overlap with the next larger frequency. That means, for example, you cannot specify a frequency of 60 minutes, because that is equivalent to 1 hour. The valid values for each frequency are the following:</p> <ul> <li> <p>Minute - 1-59</p> </li> <li> <p>Hour - 1-23</p> </li> <li> <p>Day - 1-6</p> </li> <li> <p>Week - 1-4</p> </li> <li> <p>Month - 1-11</p> </li> <li> <p>Year - 1</p> </li> </ul> <p>Thus, if you want every other week forecasts, specify "2W". Or, if you want quarterly forecasts, you specify "3M".</p>"""
    schema: "capo_forecast.types.schema.Schema"
    """<p>The schema for the dataset. The schema attributes and their order must match the fields in your data. The dataset <code>Domain</code> and <code>DatasetType</code> that you choose determine the minimum required fields in your training data. For information about the required fields for a specific dataset domain and type, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/howitworks-domains-ds-types.html">Dataset Domains and Dataset Types</a>.</p>"""
    encryption_config: NotRequired[
        "capo_forecast.types.encryption_config.EncryptionConfig"
    ]
    """<p>An Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.</p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>The optional metadata that you apply to the dataset to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    import capo_forecast.types.domain

    out["Domain"] = capo_forecast.types.domain.serialize_aws_json_1_1(value["domain"])
    import capo_forecast.types.dataset_type

    out["DatasetType"] = capo_forecast.types.dataset_type.serialize_aws_json_1_1(
        value["dataset_type"]
    )
    if "data_frequency" in value:
        out["DataFrequency"] = value["data_frequency"]
    import capo_forecast.types.schema

    out["Schema"] = capo_forecast.types.schema.serialize_aws_json_1_1(value["schema"])
    if "encryption_config" in value:
        import capo_forecast.types.encryption_config

        out["EncryptionConfig"] = (
            capo_forecast.types.encryption_config.serialize_aws_json_1_1(
                value["encryption_config"]
            )
        )
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_name required")
    if data.get("Domain") is not None:
        import capo_forecast.types.domain

        out["domain"] = capo_forecast.types.domain.deserialize_aws_json_1_1(
            data["Domain"]
        )
    else:
        raise DeserializationError("CreateDatasetRequest.domain required")
    if data.get("DatasetType") is not None:
        import capo_forecast.types.dataset_type

        out["dataset_type"] = capo_forecast.types.dataset_type.deserialize_aws_json_1_1(
            data["DatasetType"]
        )
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_type required")
    if data.get("DataFrequency") is not None:
        out["data_frequency"] = data["DataFrequency"]
    if data.get("Schema") is not None:
        import capo_forecast.types.schema

        out["schema"] = capo_forecast.types.schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    else:
        raise DeserializationError("CreateDatasetRequest.schema required")
    if data.get("EncryptionConfig") is not None:
        import capo_forecast.types.encryption_config

        out["encryption_config"] = (
            capo_forecast.types.encryption_config.deserialize_aws_json_1_1(
                data["EncryptionConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
