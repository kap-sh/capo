"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationCodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.code_content
    import capo_kinesis_analytics_v2.types.code_content_type


class ApplicationCodeConfiguration(TypedDict, closed=True):
    code_content: NotRequired[
        "capo_kinesis_analytics_v2.types.code_content.CodeContent"
    ]
    """<p>The location and type of the application code.</p>"""
    code_content_type: (
        "capo_kinesis_analytics_v2.types.code_content_type.CodeContentType"
    )
    """<p>Specifies whether the code content is in text or zip format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationCodeConfiguration) -> dict:
    out: dict = {}
    if "code_content" in value:
        import capo_kinesis_analytics_v2.types.code_content

        out["CodeContent"] = (
            capo_kinesis_analytics_v2.types.code_content.serialize_aws_json_1_1(
                value["code_content"]
            )
        )
    import capo_kinesis_analytics_v2.types.code_content_type

    out["CodeContentType"] = (
        capo_kinesis_analytics_v2.types.code_content_type.serialize_aws_json_1_1(
            value["code_content_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationCodeConfiguration:
    out: ApplicationCodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CodeContent") is not None:
        import capo_kinesis_analytics_v2.types.code_content

        out["code_content"] = (
            capo_kinesis_analytics_v2.types.code_content.deserialize_aws_json_1_1(
                data["CodeContent"]
            )
        )
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
    return out
