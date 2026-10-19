"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationVersionChangeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_version_id


class ApplicationVersionChangeDetails(TypedDict, closed=True):
    application_version_updated_from: (
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The new version that the application was updated to.</p>"""
    application_version_updated_to: (
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The version that the operation execution applied to the applicartion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationVersionChangeDetails) -> dict:
    out: dict = {}
    out["ApplicationVersionUpdatedFrom"] = value["application_version_updated_from"]
    out["ApplicationVersionUpdatedTo"] = value["application_version_updated_to"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationVersionChangeDetails:
    out: ApplicationVersionChangeDetails = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationVersionUpdatedFrom") is not None:
        out["application_version_updated_from"] = data["ApplicationVersionUpdatedFrom"]
    else:
        out["application_version_updated_from"] = 0
    if data.get("ApplicationVersionUpdatedTo") is not None:
        out["application_version_updated_to"] = data["ApplicationVersionUpdatedTo"]
    else:
        out["application_version_updated_to"] = 0
    return out
