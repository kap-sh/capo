"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.datasets
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.topic_config_options
    import capo_quicksight.types.topic_user_experience_version


class TopicDetails(TypedDict, closed=True):
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>The name of the topic.</p>"""
    description: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The description of the topic.</p>"""
    user_experience_version: NotRequired[
        "capo_quicksight.types.topic_user_experience_version.TopicUserExperienceVersion"
    ]
    """<p>The user experience version of a topic.</p>"""
    data_sets: NotRequired["capo_quicksight.types.datasets.Datasets"]
    """<p>The data sets that the topic is associated with.</p>"""
    config_options: NotRequired[
        "capo_quicksight.types.topic_config_options.TopicConfigOptions"
    ]
    """<p>Configuration options for a <code>Topic</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "user_experience_version" in value:
        import capo_quicksight.types.topic_user_experience_version

        out["UserExperienceVersion"] = (
            capo_quicksight.types.topic_user_experience_version.serialize_json(
                value["user_experience_version"]
            )
        )
    if "data_sets" in value:
        import capo_quicksight.types.datasets

        out["DataSets"] = capo_quicksight.types.datasets.serialize_json(
            value["data_sets"]
        )
    if "config_options" in value:
        import capo_quicksight.types.topic_config_options

        out["ConfigOptions"] = (
            capo_quicksight.types.topic_config_options.serialize_json(
                value["config_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicDetails:
    out: TopicDetails = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("UserExperienceVersion") is not None:
        import capo_quicksight.types.topic_user_experience_version

        out["user_experience_version"] = (
            capo_quicksight.types.topic_user_experience_version.deserialize_json(
                data["UserExperienceVersion"]
            )
        )
    if data.get("DataSets") is not None:
        import capo_quicksight.types.datasets

        out["data_sets"] = capo_quicksight.types.datasets.deserialize_json(
            data["DataSets"]
        )
    if data.get("ConfigOptions") is not None:
        import capo_quicksight.types.topic_config_options

        out["config_options"] = (
            capo_quicksight.types.topic_config_options.deserialize_json(
                data["ConfigOptions"]
            )
        )
    return out


def redact_sensitive(value: TopicDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_sets" in value:
        import capo_quicksight.types.datasets

        out["data_sets"] = capo_quicksight.types.datasets.redact_sensitive(
            value["data_sets"]
        )
    return out
