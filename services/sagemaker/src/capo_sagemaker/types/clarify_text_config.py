"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyTextConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.clarify_text_granularity
    import capo_sagemaker.types.clarify_text_language


class ClarifyTextConfig(TypedDict, closed=True):
    language: NotRequired[
        "capo_sagemaker.types.clarify_text_language.ClarifyTextLanguage"
    ]
    """<p>Specifies the language of the text features in <a href=" https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO 639-1</a> or <a href="https://en.wikipedia.org/wiki/ISO_639-3">ISO 639-3</a> code of a supported language. </p> <note> <p>For a mix of multiple languages, use code <code>'xx'</code>.</p> </note>"""
    granularity: NotRequired[
        "capo_sagemaker.types.clarify_text_granularity.ClarifyTextGranularity"
    ]
    """<p>The unit of granularity for the analysis of text features. For example, if the unit is <code>'token'</code>, then each token (like a word in English) of the text is treated as a feature. SHAP values are computed for each unit/feature.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyTextConfig) -> dict:
    out: dict = {}
    if "language" in value:
        import capo_sagemaker.types.clarify_text_language

        out["Language"] = (
            capo_sagemaker.types.clarify_text_language.serialize_aws_json_1_1(
                value["language"]
            )
        )
    if "granularity" in value:
        import capo_sagemaker.types.clarify_text_granularity

        out["Granularity"] = (
            capo_sagemaker.types.clarify_text_granularity.serialize_aws_json_1_1(
                value["granularity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClarifyTextConfig:
    out: ClarifyTextConfig = {}  # type: ignore[typeddict-item]
    if data.get("Language") is not None:
        import capo_sagemaker.types.clarify_text_language

        out["language"] = (
            capo_sagemaker.types.clarify_text_language.deserialize_aws_json_1_1(
                data["Language"]
            )
        )
    if data.get("Granularity") is not None:
        import capo_sagemaker.types.clarify_text_granularity

        out["granularity"] = (
            capo_sagemaker.types.clarify_text_granularity.deserialize_aws_json_1_1(
                data["Granularity"]
            )
        )
    return out
