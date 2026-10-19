"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CreateApplicationPresignedUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.session_expiration_duration_in_seconds
    import capo_kinesis_analytics_v2.types.url_type


class CreateApplicationPresignedUrlRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the application.</p>"""
    url_type: "capo_kinesis_analytics_v2.types.url_type.UrlType"
    """<p>The type of the extension for which to create and return a URL. Currently, the only valid extension URL type is <code>FLINK_DASHBOARD_URL</code>. </p>"""
    session_expiration_duration_in_seconds: NotRequired[
        "capo_kinesis_analytics_v2.types.session_expiration_duration_in_seconds.SessionExpirationDurationInSeconds"
    ]
    """<p>The duration in seconds for which the returned URL will be valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationPresignedUrlRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    import capo_kinesis_analytics_v2.types.url_type

    out["UrlType"] = capo_kinesis_analytics_v2.types.url_type.serialize_aws_json_1_1(
        value["url_type"]
    )
    if "session_expiration_duration_in_seconds" in value:
        out["SessionExpirationDurationInSeconds"] = value[
            "session_expiration_duration_in_seconds"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationPresignedUrlRequest:
    out: CreateApplicationPresignedUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("UrlType") is not None:
        import capo_kinesis_analytics_v2.types.url_type

        out["url_type"] = (
            capo_kinesis_analytics_v2.types.url_type.deserialize_aws_json_1_1(
                data["UrlType"]
            )
        )
    else:
        import typing

        out["url_type"] = typing.cast(
            "capo_kinesis_analytics_v2.types.url_type.UrlType", ""
        )
    if data.get("SessionExpirationDurationInSeconds") is not None:
        out["session_expiration_duration_in_seconds"] = data[
            "SessionExpirationDurationInSeconds"
        ]
    return out
