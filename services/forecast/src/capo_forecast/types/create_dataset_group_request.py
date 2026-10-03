"""Generated from Smithy shape ``com.amazonaws.forecast#CreateDatasetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn_list
    import capo_forecast.types.domain
    import capo_forecast.types.name
    import capo_forecast.types.tags


class CreateDatasetGroupRequest(TypedDict, closed=True):
    dataset_group_name: "capo_forecast.types.name.Name"
    """<p>A name for the dataset group.</p>"""
    domain: "capo_forecast.types.domain.Domain"
    """<p>The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the <code>Domain</code> parameter of the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">CreateDataset</a> operation must match.</p> <p>The <code>Domain</code> and <code>DatasetType</code> that you choose determine the fields that must be present in training data that you import to a dataset. For example, if you choose the <code>RETAIL</code> domain and <code>TARGET_TIME_SERIES</code> as the <code>DatasetType</code>, Amazon Forecast requires that <code>item_id</code>, <code>timestamp</code>, and <code>demand</code> fields are present in your data. For more information, see <a href="https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html">Dataset groups</a>.</p>"""
    dataset_arns: NotRequired["capo_forecast.types.arn_list.ArnList"]
    """<p>An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.</p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>The optional metadata that you apply to the dataset group to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetGroupRequest) -> dict:
    out: dict = {}
    out["DatasetGroupName"] = value["dataset_group_name"]
    import capo_forecast.types.domain

    out["Domain"] = capo_forecast.types.domain.serialize_aws_json_1_1(value["domain"])
    if "dataset_arns" in value:
        import capo_forecast.types.arn_list

        out["DatasetArns"] = capo_forecast.types.arn_list.serialize_aws_json_1_1(
            value["dataset_arns"]
        )
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetGroupRequest:
    out: CreateDatasetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetGroupName") is not None:
        out["dataset_group_name"] = data["DatasetGroupName"]
    else:
        raise DeserializationError(
            "CreateDatasetGroupRequest.dataset_group_name required"
        )
    if data.get("Domain") is not None:
        import capo_forecast.types.domain

        out["domain"] = capo_forecast.types.domain.deserialize_aws_json_1_1(
            data["Domain"]
        )
    else:
        raise DeserializationError("CreateDatasetGroupRequest.domain required")
    if data.get("DatasetArns") is not None:
        import capo_forecast.types.arn_list

        out["dataset_arns"] = capo_forecast.types.arn_list.deserialize_aws_json_1_1(
            data["DatasetArns"]
        )
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
