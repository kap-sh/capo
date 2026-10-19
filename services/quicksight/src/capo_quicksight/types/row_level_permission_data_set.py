"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionDataSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.namespace
    import capo_quicksight.types.row_level_permission_format_version
    import capo_quicksight.types.row_level_permission_policy
    import capo_quicksight.types.status


class RowLevelPermissionDataSet(TypedDict, closed=True):
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The namespace associated with the dataset that contains permissions for RLS.</p>"""
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset that contains permissions for RLS.</p>"""
    permission_policy: (
        "capo_quicksight.types.row_level_permission_policy.RowLevelPermissionPolicy"
    )
    """<p>The type of permissions to use when interpreting the permissions for RLS. <code>DENY_ACCESS</code> is included for backward compatibility only.</p>"""
    format_version: NotRequired[
        "capo_quicksight.types.row_level_permission_format_version.RowLevelPermissionFormatVersion"
    ]
    """<p>The user or group rules associated with the dataset that contains permissions for RLS.</p> <p>By default, <code>FormatVersion</code> is <code>VERSION_1</code>. When <code>FormatVersion</code> is <code>VERSION_1</code>, <code>UserName</code> and <code>GroupName</code> are required. When <code>FormatVersion</code> is <code>VERSION_2</code>, <code>UserARN</code> and <code>GroupARN</code> are required, and <code>Namespace</code> must not exist.</p>"""
    status: NotRequired["capo_quicksight.types.status.Status"]
    """<p>The status of the row-level security permission dataset. If enabled, the status is <code>ENABLED</code>. If disabled, the status is <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionDataSet) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    out["Arn"] = value["arn"]
    import capo_quicksight.types.row_level_permission_policy

    out["PermissionPolicy"] = (
        capo_quicksight.types.row_level_permission_policy.serialize_json(
            value["permission_policy"]
        )
    )
    if "format_version" in value:
        import capo_quicksight.types.row_level_permission_format_version

        out["FormatVersion"] = (
            capo_quicksight.types.row_level_permission_format_version.serialize_json(
                value["format_version"]
            )
        )
    if "status" in value:
        import capo_quicksight.types.status

        out["Status"] = capo_quicksight.types.status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> RowLevelPermissionDataSet:
    out: RowLevelPermissionDataSet = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("PermissionPolicy") is not None:
        import capo_quicksight.types.row_level_permission_policy

        out["permission_policy"] = (
            capo_quicksight.types.row_level_permission_policy.deserialize_json(
                data["PermissionPolicy"]
            )
        )
    else:
        import typing

        out["permission_policy"] = typing.cast(
            "capo_quicksight.types.row_level_permission_policy.RowLevelPermissionPolicy",
            "",
        )
    if data.get("FormatVersion") is not None:
        import capo_quicksight.types.row_level_permission_format_version

        out["format_version"] = (
            capo_quicksight.types.row_level_permission_format_version.deserialize_json(
                data["FormatVersion"]
            )
        )
    if data.get("Status") is not None:
        import capo_quicksight.types.status

        out["status"] = capo_quicksight.types.status.deserialize_json(data["Status"])
    return out
