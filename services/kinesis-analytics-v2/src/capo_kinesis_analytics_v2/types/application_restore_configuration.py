"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationRestoreConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_restore_type
    import capo_kinesis_analytics_v2.types.snapshot_name


class ApplicationRestoreConfiguration(TypedDict, closed=True):
    application_restore_type: "capo_kinesis_analytics_v2.types.application_restore_type.ApplicationRestoreType"
    """<p>Specifies how the application should be restored.</p>"""
    snapshot_name: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_name.SnapshotName"
    ]
    """<p>The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if <code>RESTORE_FROM_CUSTOM_SNAPSHOT</code> is specified for the <code>ApplicationRestoreType</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationRestoreConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.application_restore_type

    out["ApplicationRestoreType"] = (
        capo_kinesis_analytics_v2.types.application_restore_type.serialize_aws_json_1_1(
            value["application_restore_type"]
        )
    )
    if "snapshot_name" in value:
        out["SnapshotName"] = value["snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationRestoreConfiguration:
    out: ApplicationRestoreConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationRestoreType") is not None:
        import capo_kinesis_analytics_v2.types.application_restore_type

        out["application_restore_type"] = (
            capo_kinesis_analytics_v2.types.application_restore_type.deserialize_aws_json_1_1(
                data["ApplicationRestoreType"]
            )
        )
    else:
        import typing

        out["application_restore_type"] = typing.cast(
            "capo_kinesis_analytics_v2.types.application_restore_type.ApplicationRestoreType",
            "",
        )
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    return out
