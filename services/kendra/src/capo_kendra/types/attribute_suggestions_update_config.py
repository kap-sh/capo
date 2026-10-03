"""Generated from Smithy shape ``com.amazonaws.kendra#AttributeSuggestionsUpdateConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.attribute_suggestions_mode
    import capo_kendra.types.suggestable_config_list


class AttributeSuggestionsUpdateConfig(TypedDict, closed=True):
    suggestable_config_list: NotRequired[
        "capo_kendra.types.suggestable_config_list.SuggestableConfigList"
    ]
    """<p>The list of fields/attributes that you want to set as suggestible for query suggestions.</p>"""
    attribute_suggestions_mode: NotRequired[
        "capo_kendra.types.attribute_suggestions_mode.AttributeSuggestionsMode"
    ]
    """<p>You can set the mode to <code>ACTIVE</code> or <code>INACTIVE</code>. You must also set <code>SuggestionTypes</code> as either <code>QUERY</code> or <code>DOCUMENT_ATTRIBUTES</code> and then call <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html">GetQuerySuggestions</a>. If <code>Mode</code> to use query history is set to <code>ENABLED</code> when calling <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html">UpdateQuerySuggestionsConfig</a> and <code>AttributeSuggestionsMode</code> to use fields/attributes is set to <code>ACTIVE</code>, and you haven't set your <code>SuggestionTypes</code> preference to <code>DOCUMENT_ATTRIBUTES</code>, then Amazon Kendra uses the query history.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeSuggestionsUpdateConfig) -> dict:
    out: dict = {}
    if "suggestable_config_list" in value:
        import capo_kendra.types.suggestable_config_list

        out["SuggestableConfigList"] = (
            capo_kendra.types.suggestable_config_list.serialize_aws_json_1_1(
                value["suggestable_config_list"]
            )
        )
    if "attribute_suggestions_mode" in value:
        import capo_kendra.types.attribute_suggestions_mode

        out["AttributeSuggestionsMode"] = (
            capo_kendra.types.attribute_suggestions_mode.serialize_aws_json_1_1(
                value["attribute_suggestions_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeSuggestionsUpdateConfig:
    out: AttributeSuggestionsUpdateConfig = {}  # type: ignore[typeddict-item]
    if data.get("SuggestableConfigList") is not None:
        import capo_kendra.types.suggestable_config_list

        out["suggestable_config_list"] = (
            capo_kendra.types.suggestable_config_list.deserialize_aws_json_1_1(
                data["SuggestableConfigList"]
            )
        )
    if data.get("AttributeSuggestionsMode") is not None:
        import capo_kendra.types.attribute_suggestions_mode

        out["attribute_suggestions_mode"] = (
            capo_kendra.types.attribute_suggestions_mode.deserialize_aws_json_1_1(
                data["AttributeSuggestionsMode"]
            )
        )
    return out
