"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationCodeConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.code_content_description
    import capo_kinesis_analytics_v2.types.code_content_type


class ApplicationCodeConfigurationDescription(TypedDict, closed=True):
    code_content_type: (
        "capo_kinesis_analytics_v2.types.code_content_type.CodeContentType"
    )
    """<p>Specifies whether the code content is in text or zip format.</p>"""
    code_content_description: NotRequired[
        "capo_kinesis_analytics_v2.types.code_content_description.CodeContentDescription"
    ]
    """<p>Describes details about the location and format of the application code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationCodeConfigurationDescription) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.code_content_type

    out["CodeContentType"] = (
        capo_kinesis_analytics_v2.types.code_content_type.serialize_aws_json_1_1(
            value["code_content_type"]
        )
    )
    if "code_content_description" in value:
        import capo_kinesis_analytics_v2.types.code_content_description

        out["CodeContentDescription"] = (
            capo_kinesis_analytics_v2.types.code_content_description.serialize_aws_json_1_1(
                value["code_content_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationCodeConfigurationDescription:
    out: ApplicationCodeConfigurationDescription = {}  # type: ignore[typeddict-item]
    if data.get("CodeContentType") is not None:
        import capo_kinesis_analytics_v2.types.code_content_type

        out["code_content_type"] = (
            capo_kinesis_analytics_v2.types.code_content_type.deserialize_aws_json_1_1(
                data["CodeContentType"]
            )
        )
    else:
        import typing

        out["code_content_type"] = typing.cast(
            "capo_kinesis_analytics_v2.types.code_content_type.CodeContentType", ""
        )
    if data.get("CodeContentDescription") is not None:
        import capo_kinesis_analytics_v2.types.code_content_description

        out["code_content_description"] = (
            capo_kinesis_analytics_v2.types.code_content_description.deserialize_aws_json_1_1(
                data["CodeContentDescription"]
            )
        )
    return out
