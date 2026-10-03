"""Generated from Smithy shape ``com.amazonaws.translate#StartTextTranslationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_translate.errors import DeserializationError

if TYPE_CHECKING:
    import capo_translate.types.client_token_string
    import capo_translate.types.iam_role_arn
    import capo_translate.types.input_data_config
    import capo_translate.types.job_name
    import capo_translate.types.language_code_string
    import capo_translate.types.output_data_config
    import capo_translate.types.resource_name_list
    import capo_translate.types.target_language_code_string_list
    import capo_translate.types.translation_settings


class StartTextTranslationJobRequest(TypedDict, closed=True):
    job_name: NotRequired["capo_translate.types.job_name.JobName"]
    """<p>The name of the batch translation job to be performed.</p>"""
    input_data_config: "capo_translate.types.input_data_config.InputDataConfig"
    """<p>Specifies the format and location of the input documents for the translation job.</p>"""
    output_data_config: "capo_translate.types.output_data_config.OutputDataConfig"
    """<p>Specifies the S3 folder to which your job output will be saved. </p>"""
    data_access_role_arn: "capo_translate.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that grants Amazon Translate read access to your input data. For more information, see <a href="https://docs.aws.amazon.com/translate/latest/dg/identity-and-access-management.html">Identity and access management </a>.</p>"""
    source_language_code: "capo_translate.types.language_code_string.LanguageCodeString"
    """<p>The language code of the input language. Specify the language if all input documents share the same language. If you don't know the language of the source files, or your input documents contains different source languages, select <code>auto</code>. Amazon Translate auto detects the source language for each input document. For a list of supported language codes, see <a href="https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html">Supported languages</a>.</p>"""
    target_language_codes: "capo_translate.types.target_language_code_string_list.TargetLanguageCodeStringList"
    """<p>The target languages of the translation job. Enter up to 10 language codes. Each input file is translated into each target language.</p> <p>Each language code is 2 or 5 characters long. For a list of language codes, see <a href="https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html">Supported languages</a>.</p>"""
    terminology_names: NotRequired[
        "capo_translate.types.resource_name_list.ResourceNameList"
    ]
    """<p>The name of a custom terminology resource to add to the translation job. This resource lists examples source terms and the desired translation for each term.</p> <p>This parameter accepts only one custom terminology resource.</p> <p>If you specify multiple target languages for the job, translate uses the designated terminology for each requested target language that has an entry for the source term in the terminology file.</p> <p>For a list of available custom terminology resources, use the <a>ListTerminologies</a> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html">Custom terminology</a>.</p>"""
    parallel_data_names: NotRequired[
        "capo_translate.types.resource_name_list.ResourceNameList"
    ]
    """<p>The name of a parallel data resource to add to the translation job. This resource consists of examples that show how you want segments of text to be translated. If you specify multiple target languages for the job, the parallel data file must include translations for all the target languages.</p> <p>When you add parallel data to a translation job, you create an <i>Active Custom Translation</i> job. </p> <p>This parameter accepts only one parallel data resource.</p> <note> <p>Active Custom Translation jobs are priced at a higher rate than other jobs that don't use parallel data. For more information, see <a href="http://aws.amazon.com/translate/pricing/">Amazon Translate pricing</a>.</p> </note> <p>For a list of available parallel data resources, use the <a>ListParallelData</a> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data.html"> Customizing your translations with parallel data</a>.</p>"""
    client_token: "capo_translate.types.client_token_string.ClientTokenString"
    """<p>A unique identifier for the request. This token is generated for you when using the Amazon Translate SDK.</p>"""
    settings: NotRequired[
        "capo_translate.types.translation_settings.TranslationSettings"
    ]
    """<p>Settings to configure your translation output. You can configure the following options:</p> <ul> <li> <p>Brevity: not supported.</p> </li> <li> <p>Formality: sets the formality level of the output text.</p> </li> <li> <p>Profanity: masks profane words and phrases in your translation output.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTextTranslationJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import capo_translate.types.input_data_config

    out["InputDataConfig"] = (
        capo_translate.types.input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    import capo_translate.types.output_data_config

    out["OutputDataConfig"] = (
        capo_translate.types.output_data_config.serialize_aws_json_1_1(
            value["output_data_config"]
        )
    )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    out["SourceLanguageCode"] = value["source_language_code"]
    import capo_translate.types.target_language_code_string_list

    out["TargetLanguageCodes"] = (
        capo_translate.types.target_language_code_string_list.serialize_aws_json_1_1(
            value["target_language_codes"]
        )
    )
    if "terminology_names" in value:
        import capo_translate.types.resource_name_list

        out["TerminologyNames"] = (
            capo_translate.types.resource_name_list.serialize_aws_json_1_1(
                value["terminology_names"]
            )
        )
    if "parallel_data_names" in value:
        import capo_translate.types.resource_name_list

        out["ParallelDataNames"] = (
            capo_translate.types.resource_name_list.serialize_aws_json_1_1(
                value["parallel_data_names"]
            )
        )
    out["ClientToken"] = value["client_token"]
    if "settings" in value:
        import capo_translate.types.translation_settings

        out["Settings"] = (
            capo_translate.types.translation_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTextTranslationJobRequest:
    out: StartTextTranslationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("InputDataConfig") is not None:
        import capo_translate.types.input_data_config

        out["input_data_config"] = (
            capo_translate.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartTextTranslationJobRequest.input_data_config required"
        )
    if data.get("OutputDataConfig") is not None:
        import capo_translate.types.output_data_config

        out["output_data_config"] = (
            capo_translate.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartTextTranslationJobRequest.output_data_config required"
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartTextTranslationJobRequest.data_access_role_arn required"
        )
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    else:
        raise DeserializationError(
            "StartTextTranslationJobRequest.source_language_code required"
        )
    if data.get("TargetLanguageCodes") is not None:
        import capo_translate.types.target_language_code_string_list

        out["target_language_codes"] = (
            capo_translate.types.target_language_code_string_list.deserialize_aws_json_1_1(
                data["TargetLanguageCodes"]
            )
        )
    else:
        raise DeserializationError(
            "StartTextTranslationJobRequest.target_language_codes required"
        )
    if data.get("TerminologyNames") is not None:
        import capo_translate.types.resource_name_list

        out["terminology_names"] = (
            capo_translate.types.resource_name_list.deserialize_aws_json_1_1(
                data["TerminologyNames"]
            )
        )
    if data.get("ParallelDataNames") is not None:
        import capo_translate.types.resource_name_list

        out["parallel_data_names"] = (
            capo_translate.types.resource_name_list.deserialize_aws_json_1_1(
                data["ParallelDataNames"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "StartTextTranslationJobRequest.client_token required"
        )
    if data.get("Settings") is not None:
        import capo_translate.types.translation_settings

        out["settings"] = (
            capo_translate.types.translation_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out
